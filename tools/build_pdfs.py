#!/usr/bin/env python3
"""Build the PDF editions of the Markdown documents.

    python3 tools/build_pdfs.py                    # language-guide.pdf and philosophy.pdf
    python3 tools/build_pdfs.py README.md          # any other Markdown file
    python3 tools/build_pdfs.py --out-dir build/   # write somewhere else

Pipeline: Markdown -> HTML (markdown-it-py) -> PDF (Chrome's print-to-PDF, through
Playwright). Obsidian prints through the same engine, so the result is close to what
exporting from Obsidian gave.

Fonts are looked up by name from the system, in this order (CSS falls back one glyph at a
time, so Latin text uses Courier, Shavian letters use Bernie Sans Beta, and Tengwar
code points use Alcarin Tengwar):

    Courier, Bernie Sans Beta, Alcarin Tengwar

If a font is not installed, pass its file with --font, for example
    --font "Alcarin Tengwar=/path/to/AlcarinTengwar-Regular.otf"

Setup (once):
    pip install -r tools/requirements-docs.txt
Chrome must be installed; use --browser PATH to point at a different executable.
Python 3.14; nothing else from this repo is imported.
"""

import argparse
import base64
import html
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DOCS = ["language-guide.md", "philosophy.md"]
FONT_STACK = ["Courier", "Bernie Sans Beta", "Alcarin Tengwar"]

CSS = """
@page { size: Letter; margin: 0.75in; }
html { font-family: %(stack)s, monospace; font-size: 10pt; line-height: 1.5; color: #222; }
body { margin: 0; }
h1, h2, h3, h4 { line-height: 1.25; margin: 1.4em 0 0.5em; break-after: avoid; }
h1 { font-size: 1.7em; margin-top: 0; }
h2 { font-size: 1.35em; }
h3 { font-size: 1.15em; }
h4 { font-size: 1.0em; }
p, ul, ol { margin: 0.6em 0; }
li { margin: 0.2em 0; }
hr { border: 0; border-top: 1px solid #ddd; margin: 1.6em 0; }
a { color: inherit; text-decoration: underline; }
code { font-family: %(stack)s, monospace; background: #f3f3f3; padding: 0 0.25em; border-radius: 3px; font-size: 0.95em; }
pre { background: #f3f3f3; padding: 0.7em 0.9em; border-radius: 4px; white-space: pre-wrap;
      overflow-wrap: anywhere; break-inside: avoid; }
pre code { background: none; padding: 0; }
blockquote { margin: 0.8em 0; padding-left: 1em; border-left: 3px solid #ccc; color: #444; }
table { border-collapse: collapse; width: 100%%; margin: 0.9em 0; font-size: 8.5pt; }
th, td { border: 1px solid #d8d8d8; padding: 0.3em 0.55em; vertical-align: top; text-align: left; }
th { background: #f6f6f6; font-weight: bold; }
td code { overflow-wrap: anywhere; }
tr { break-inside: avoid; }
img { max-width: 100%%; }
"""

FONT_PROBE = """
([family, sample]) => {
  const width = (font) => {
    const s = document.createElement('span');
    s.style.cssText = 'position:absolute;visibility:hidden;white-space:nowrap;font-size:48px;font:48px ' + font;
    s.textContent = sample;
    document.body.appendChild(s);
    const w = s.getBoundingClientRect().width;
    s.remove();
    return w;
  };
  return ['monospace', 'serif', 'sans-serif'].some(
    (generic) => width('"' + family + '",' + generic) !== width(generic));
}
"""

# Characters each font is expected to cover; used only to warn about missing fonts.
FONT_SAMPLES = {
    "Courier": "Abc",
    "Bernie Sans Beta": "\U00010450\U00010451\U00010452",
    "Alcarin Tengwar": "",
}


def render_html(markdown_text: str, title: str, font_faces: list[tuple[str, Path]]) -> str:
    try:
        from markdown_it import MarkdownIt
    except ImportError:
        sys.exit("markdown-it-py is missing: pip install -r tools/requirements-docs.txt")
    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    body = md.render(markdown_text)
    # Data URIs: a page set from a string cannot load file:// URLs.
    formats = {".otf": "opentype", ".ttf": "truetype", ".woff": "woff", ".woff2": "woff2"}
    faces = "\n".join(
        '@font-face {{ font-family: "{}"; src: url("data:font/{};base64,{}") format("{}"); }}'.format(
            name,
            path.suffix.lstrip(".").lower(),
            base64.b64encode(path.read_bytes()).decode("ascii"),
            formats.get(path.suffix.lower(), "opentype"),
        )
        for name, path in font_faces
    )
    stack = ", ".join(f'"{f}"' for f in FONT_STACK)
    return (
        "<!doctype html><html><head><meta charset='utf-8'>"
        f"<title>{html.escape(title)}</title><style>{faces}\n{CSS % {'stack': stack}}</style>"
        f"</head><body>{body}</body></html>"
    )


def first_heading(markdown_text: str, fallback: str) -> str:
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def parse_fonts(specs: list[str]) -> list[tuple[str, Path]]:
    out = []
    for spec in specs:
        name, sep, path = spec.partition("=")
        if not sep or not Path(path).is_file():
            sys.exit(f'--font expects "Family Name=/path/to/font" with an existing file: {spec!r}')
        out.append((name.strip(), Path(path)))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docs", nargs="*", help="Markdown files (default: language-guide.md and philosophy.md)")
    ap.add_argument("--out-dir", type=Path, help="where to write the PDFs (default: next to each source)")
    ap.add_argument("--font", action="append", default=[], metavar="NAME=PATH", help="load a font file")
    ap.add_argument("--browser", metavar="PATH", help="Chrome/Chromium executable (default: installed Google Chrome)")
    ap.add_argument("--strict", action="store_true", help="fail if a font in the stack is not available")
    args = ap.parse_args(argv)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("playwright is missing: pip install -r tools/requirements-docs.txt")

    sources = [Path(d) if Path(d).is_absolute() else ROOT / d for d in (args.docs or DEFAULT_DOCS)]
    for src in sources:
        if not src.is_file():
            sys.exit(f"not found: {src}")
    font_faces = parse_fonts(args.font)
    missing_any = False

    with sync_playwright() as p:
        launch = {"executable_path": args.browser} if args.browser else {"channel": "chrome"}
        try:
            browser = p.chromium.launch(**launch)
        except Exception as exc:  # noqa: BLE001 - surface Playwright's own message
            sys.exit(f"could not start the browser ({exc}). Install Chrome or pass --browser PATH.")
        page = browser.new_page()
        for src in sources:
            text = src.read_text(encoding="utf-8")
            doc = render_html(text, first_heading(text, src.stem), font_faces)
            page.set_content(doc, wait_until="load")
            for name, _ in font_faces:  # @font-face files load lazily; force them
                page.evaluate("([n, s]) => document.fonts.load('16px \"' + n + '\"', s)", [name, FONT_SAMPLES.get(name, "A")])
            page.evaluate("document.fonts.ready")
            for family, sample in FONT_SAMPLES.items():
                if not page.evaluate(FONT_PROBE, [family, sample]):
                    missing_any = True
                    print(f'warning: font "{family}" does not seem to be available (use --font)', file=sys.stderr)
            out = (args.out_dir or src.parent) / (src.stem + ".pdf")
            out.parent.mkdir(parents=True, exist_ok=True)
            page.pdf(path=str(out), prefer_css_page_size=True, print_background=True)
            print(f"wrote {out}")
        browser.close()
    return 1 if (missing_any and args.strict) else 0


if __name__ == "__main__":
    raise SystemExit(main())
