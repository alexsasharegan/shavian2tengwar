#!/usr/bin/env python3
"""The font gate (ADR-0011): show the mark-stacking cases in each font, to vet a Tengwar font.

    python3 tools/font_gate.py OUTDIR FONT...

Each FONT is one column:

    alcarin=PATH                  a registered encoding, in its font file
    alcarin                       the same, using the installed font by family name
    alcarin:Label=PATH            a candidate font, tried at the alcarin encoding's code points

Writes OUTDIR/gate.html (fonts embedded, for Safari and Chrome), OUTDIR/gate.rtf (installed fonts, for
TextEdit) and OUTDIR/gate.txt (the code points). Every case with two marks above is shown in both orders,
"nearest first" and "top first", so the page shows which order each font needs. Every code point used
is looked up in the font's own cmap, and a missing one is reported; never trust another font's table.

    --chrome        also screenshot gate.html in Chrome (OUTDIR/chrome.png; needs npm run setup:docs)
    --coretext      also render each font through Core Text (OUTDIR/coretext-LABEL.png; macOS, needs swift)

A font passes when every mark attaches to its base, the vowel mark is on top, the nasal bar sits between
it and the base, the gemination bar is under the base, and no dotted circles appear, in Core Text, in
Chrome, and in Alex's own check in Safari and TextEdit. Core Text renders are not a substitute for that check.
"""

import argparse
import base64
import html
import shutil
import struct
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from s2t import ENCODINGS, get_encoding, parse_literal  # noqa: E402
from s2t.encodings import Encoding  # noqa: E402

# (label, glyph literal in K-01 order). Narrow and wide bases, both marks above, the marks below,
# nuquerna and both carriers.
CASES = [
    ("vowel mark: 𐑦𐑑 it", "{tinco}[dot-above]"),
    ("vowel mark on a wide base: 𐑨𐑛 add", "{ando}[triple-dot-above]"),
    ("vowel + nasal bar: 𐑦𐑯𐑑 int", "{tinco}[dot-above][bar-above]"),
    ("vowel + nasal bar on a wide base: 𐑧𐑯𐑛 end", "{ando}[acute][bar-above]"),
    ("vowel + nasal bar on a tall stem: 𐑦𐑯𐑞", "{anto}[dot-above][bar-above]"),
    ("gemination: 𐑑𐑑", "{tinco}[bar-below]"),
    ("vowel + gemination: 𐑦𐑑𐑑", "{tinco}[dot-above][bar-below]"),
    ("nuquerna + vowel: 𐑦𐑕 iss", "{silme-nuquerna}[dot-above]"),
    ("short carrier: 𐑩", "{telco}[breve]"),
    ("long carrier: 𐑰", "{aara}[dot-above]"),
    ("and: 𐑯", "{and-shorthand}"),
]
ORDERS = ("nearest-first", "top-first")


@dataclass
class Column:
    label: str
    encoding: Encoding
    path: Path | None
    family: str  # the family name CSS and RTF use
    postscript: str  # the name TextEdit resolves


def read_name_table(data: bytes) -> dict[int, str]:
    """Name ID -> string from a TrueType/OpenType font (first font of a collection)."""
    base = struct.unpack_from(">I", data, 12)[0] if data[:4] == b"ttcf" else 0
    tables = {}
    for i in range(struct.unpack_from(">H", data, base + 4)[0]):
        tag, _, offset, length = struct.unpack_from(">4sIII", data, base + 12 + 16 * i)
        tables[tag] = (offset, length)
    names: dict[int, str] = {}
    offset, _ = tables[b"name"]
    _, count, strings = struct.unpack_from(">HHH", data, offset)
    for i in range(count):
        platform, _, language, name_id, length, start = struct.unpack_from(">HHHHHH", data, offset + 6 + 12 * i)
        raw = data[offset + strings + start : offset + strings + start + length]
        if platform == 3 and language == 0x409:
            names[name_id] = raw.decode("utf-16-be")
        elif platform == 1 and name_id not in names:
            names[name_id] = raw.decode("latin-1")
    return names


def read_cmap(data: bytes) -> set[int]:
    """The code points a font maps to a real glyph (formats 4 and 12 of the Unicode cmap)."""
    base = struct.unpack_from(">I", data, 12)[0] if data[:4] == b"ttcf" else 0
    tables = {}
    for i in range(struct.unpack_from(">H", data, base + 4)[0]):
        tag, _, offset, _ = struct.unpack_from(">4sIII", data, base + 12 + 16 * i)
        tables[tag] = offset
    cmap = tables[b"cmap"]
    subtables = {}
    for i in range(struct.unpack_from(">H", data, cmap + 2)[0]):
        platform, encoding, offset = struct.unpack_from(">HHI", data, cmap + 4 + 8 * i)
        subtables[(platform, encoding)] = cmap + offset
    mapped: set[int] = set()
    if (sub := subtables.get((3, 10)) or subtables.get((0, 4))) is not None:
        for i in range(struct.unpack_from(">I", data, sub + 12)[0]):
            start, end, glyph = struct.unpack_from(">III", data, sub + 16 + 12 * i)
            mapped.update(cp for cp in range(start, end + 1) if glyph + cp - start)
        return mapped
    sub = subtables.get((3, 1)) or subtables.get((0, 3))
    if sub is None:
        return mapped
    segs = struct.unpack_from(">H", data, sub + 6)[0] // 2
    ends = struct.unpack_from(f">{segs}H", data, sub + 14)
    starts = struct.unpack_from(f">{segs}H", data, sub + 16 + 2 * segs)
    deltas = struct.unpack_from(f">{segs}h", data, sub + 16 + 4 * segs)
    range_at = sub + 16 + 6 * segs
    ranges = struct.unpack_from(f">{segs}H", data, range_at)
    for i in range(segs):
        for cp in range(starts[i], ends[i] + 1):
            if ranges[i] == 0:
                glyph = (cp + deltas[i]) & 0xFFFF
            else:
                at = range_at + 2 * i + ranges[i] + 2 * (cp - starts[i])
                glyph = struct.unpack_from(">H", data, at)[0]
                glyph = (glyph + deltas[i]) & 0xFFFF if glyph else 0
            if glyph and cp != 0xFFFF:
                mapped.add(cp)
    return mapped


def glyph_names(path: Path) -> dict[int, str]:
    """Code point -> the font's own glyph name, if fontTools is installed (npm run setup:docs)."""
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        return {}
    return TTFont(path, fontNumber=0).getBestCmap()


def parse_column(spec: str) -> Column:
    head, sep, path = spec.partition("=")
    name, _, label = head.partition(":")
    if name not in ENCODINGS:
        sys.exit(f"{spec!r}: {name!r} is not a registered encoding ({', '.join(ENCODINGS)})")
    enc = get_encoding(name)
    if not sep:
        return Column(name, enc, None, enc.families[0], enc.families[0])
    file = Path(path).expanduser()
    if not file.is_file():
        sys.exit(f"{spec!r}: no such font file")
    names = read_name_table(file.read_bytes())
    family = names.get(16) or names.get(1) or file.stem
    return Column(label or name, enc, file, family, names.get(6, family))


def encode(enc: Encoding, literal: str, order: str) -> str:
    variant = Encoding(enc.name, enc.letters, enc.marks, enc.below, families=enc.families, order=order)
    return variant.encode(parse_literal(literal))


def rows(columns: list[Column]):
    """(label, order, {column label: text}) for every case, in both orders where they differ."""
    for label, literal in CASES:
        texts = {o: {c.label: encode(c.encoding, literal, o) for c in columns} for o in ORDERS}
        orders = ORDERS if texts["nearest-first"] != texts["top-first"] else ("nearest-first",)
        for o in orders:
            yield label, o if len(orders) > 1 else "one order", texts[o]


def codepoints(text: str) -> str:
    return " ".join(f"U+{ord(c):04X}" for c in text)


def check_cmaps(columns: list[Column]) -> list[str]:
    """Report each font's glyph at every code point used, and every code point it lacks."""
    report = []
    for c in columns:
        if c.path is None:
            report.append(f"{c.label}: installed font, cmap not checked (pass a file to check it)")
            continue
        mapped = read_cmap(c.path.read_bytes())
        names = glyph_names(c.path)
        used = sorted({ord(ch) for _, literal in CASES for ch in encode(c.encoding, literal, "nearest-first")})
        missing = [cp for cp in used if cp not in mapped]
        report.append(f"{c.label} ({c.family}, {c.path.name}), at {c.encoding.name} code points:")
        for cp in used:
            note = "MISSING" if cp in missing else names.get(cp, "present")
            report.append(f"  U+{cp:04X}  {note}")
    return report


def write_html(columns: list[Column], out: Path) -> None:
    faces = []
    for c in columns:
        if c.path:
            data = base64.b64encode(c.path.read_bytes()).decode("ascii")
            faces.append(f'@font-face {{ font-family: "{c.label} (file)"; src: url("data:font/ttf;base64,{data}"); }}')
    head = "".join(f"<th>{html.escape(c.label)}<br><small>{html.escape(c.family)}</small></th>" for c in columns)
    body = []
    for label, order, texts in rows(columns):
        cells = []
        for c in columns:
            families = f'"{c.label} (file)", "{c.family}"' if c.path else f'"{c.family}"'
            cells.append(
                f"<td><span class=tw style='font-family:{families}, serif'>{html.escape(texts[c.label])}</span></td>"
            )
        first = texts[columns[0].label]
        body.append(
            f"<tr><th>{html.escape(label)}<br><small>{order}: {codepoints(first)}</small></th>{''.join(cells)}</tr>"
        )
    out.write_text(
        f"""<!doctype html><meta charset="utf-8"><title>Tengwar font gate</title>
<style>{"".join(faces)}
body {{ font: 14px -apple-system, system-ui, sans-serif; margin: 24px; background: #fff; color: #111; }}
table {{ border-collapse: collapse; }} th, td {{ border: 1px solid #ccc; padding: 8px 16px; text-align: left; }}
.tw {{ font-size: 64px; line-height: 1.6; }} small {{ color: #666; font-weight: normal; }}
</style>
<h1>Tengwar font gate</h1>
<p>Pass: every mark attaches to its base, the vowel mark is on top, the nasal bar sits between it and the base,
the gemination bar is under the base, and no dotted circles appear. Where a case shows two orders, note which
one stacks correctly in each font. The code points shown are the first column's.</p>
<table><tr><th>case</th>{head}</tr>{"".join(body)}</table>
""",
        encoding="utf-8",
    )


def write_rtf(columns: list[Column], out: Path) -> None:
    def escape(text: str) -> str:
        return "".join(f"\\u{ord(ch) - 0x10000 if ord(ch) > 0x7FFF else ord(ch)}?" for ch in text)

    fonts = "".join(f"{{\\f{i + 1}\\fnil {c.postscript};}}" for i, c in enumerate(columns))
    body = []
    for i, c in enumerate(columns):
        body.append(f"\\f0\\fs28 {c.label} ({c.postscript})\\par")
        for label, order, texts in rows(columns):
            tag = label.split(":")[0]
            body.append(f"\\f0\\fs24 {tag} [{order}]:  \\f{i + 1}\\fs96 {escape(texts[c.label])}\\par")
        body.append("\\par")
    out.write_text(
        "{\\rtf1\\ansi\\deff0{\\fonttbl{\\f0\\fswiss Helvetica;}" + fonts + "}\n" + "\n".join(body) + "\n}",
        encoding="ascii",
    )


def write_txt(columns: list[Column], out: Path) -> None:
    lines = []
    for label, order, texts in rows(columns):
        lines += [f"{c.label:24} {label} [{order}]: {codepoints(texts[c.label])}" for c in columns]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def shoot_chrome(page: Path, png: Path) -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("--chrome needs playwright: npm run setup:docs, then run this with .venv/bin/python")
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        tab = browser.new_page(viewport={"width": 1200, "height": 800})
        tab.goto(page.resolve().as_uri())
        tab.evaluate("document.fonts.ready")
        tab.screenshot(path=str(png), full_page=True)
        print(f"wrote {png} ({browser.version})")
        browser.close()


def render_coretext(columns: list[Column], outdir: Path) -> None:
    if sys.platform != "darwin" or not shutil.which("swift"):
        sys.exit("--coretext needs macOS and swift")
    for c in columns:
        if c.path is None:
            print(f"skipped Core Text for {c.label}: pass its font file")
            continue
        slug = "".join(ch if ch.isalnum() else "-" for ch in c.label)
        lines = outdir / f"coretext-{slug}.lines"
        lines.write_text(
            "".join(f"{label.split(':')[0]} [{order}]\t{texts[c.label]}\n" for label, order, texts in rows(columns)),
            encoding="utf-8",
        )
        png = outdir / f"coretext-{slug}.png"
        run = subprocess.run(
            ["swift", str(ROOT / "tools/ctrender.swift"), str(c.path), str(lines), str(png)],
            capture_output=True,
            text=True,
            check=True,
        )
        print(f"wrote {png}; glyphs Core Text chose:\n{run.stdout}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("outdir", type=Path)
    ap.add_argument("fonts", nargs="+", metavar="FONT", help="ENCODING, ENCODING=PATH or ENCODING:Label=PATH")
    ap.add_argument("--chrome", action="store_true", help="screenshot the page in Chrome")
    ap.add_argument("--coretext", action="store_true", help="render each font file through Core Text")
    args = ap.parse_args(argv)

    columns = [parse_column(spec) for spec in args.fonts]
    if len({c.label for c in columns}) != len(columns):
        sys.exit("two columns have the same label; give candidates a :Label")
    args.outdir.mkdir(parents=True, exist_ok=True)
    write_html(columns, args.outdir / "gate.html")
    write_rtf(columns, args.outdir / "gate.rtf")
    write_txt(columns, args.outdir / "gate.txt")
    print(f"wrote {args.outdir / 'gate.html'}, gate.rtf and gate.txt")
    print("\n".join(check_cmaps(columns)))
    if args.chrome:
        shoot_chrome(args.outdir / "gate.html", args.outdir / "chrome.png")
    if args.coretext:
        render_coretext(columns, args.outdir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
