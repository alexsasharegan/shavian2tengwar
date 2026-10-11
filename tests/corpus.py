"""Reads corpus/*.md. Shared by the corpus tests.

Three kinds of table are recognised, by their header row:

  | Shavian | English | IPA | Glyphs | Rules |   a case: Shavian must translate to Glyphs
  | A | B | Rules |                                two Shavian spellings that must give the SAME glyphs
  | A | B | Rules |  under a "Distinct" heading     (see below) must give DIFFERENT glyphs

A table counts as "distinct" when the nearest preceding heading contains the word "Distinct".
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = ROOT / "corpus"
RULE_ID = re.compile(r"\b[A-Z]-\d\d\b")


def _cells(line):
    parts = [p.strip() for p in line.strip().strip("|").split("|")]
    return [p.strip("`") if p.startswith("`") and p.endswith("`") else p for p in parts]


def _rules(cell):
    return RULE_ID.findall(cell)


def load(path):
    """Return (cases, identities, distincts); each entry carries its file and line number."""
    cases, identities, distincts = [], [], []
    heading = ""
    kind = None
    for no, line in enumerate(Path(path).read_text(encoding="utf8").split("\n"), 1):
        if line.startswith("#"):
            heading = line
            kind = None
            continue
        if not line.startswith("|"):
            kind = None
            continue
        cells = _cells(line)
        if cells[0] == "Shavian" and "Glyphs" in cells:
            kind = "case"
            continue
        if cells[0] == "A" and cells[1] == "B":
            kind = "distinct" if "distinct" in heading.lower() else "same"
            continue
        if set(line.replace("|", "").strip()) <= set("-: "):
            continue
        where = f"{Path(path).name}:{no}"
        if kind == "case":
            shavian, english, ipa, glyphs, rules = cells[:5]
            cases.append(dict(where=where, shavian=shavian, english=english, ipa=ipa, glyphs=glyphs, rules=_rules(rules)))
        elif kind in ("same", "distinct"):
            row = dict(where=where, a=cells[0], b=cells[1], rules=_rules(cells[2]))
            (identities if kind == "same" else distincts).append(row)
    return cases, identities, distincts


def load_all():
    cases, identities, distincts = [], [], []
    for p in sorted(CORPUS_DIR.glob("*.md")):
        c, i, d = load(p)
        cases += c
        identities += i
        distincts += d
    return cases, identities, distincts


def spec_rules():
    """{rule id: status} for every rule row in spec/mode.md."""
    out = {}
    for line in (ROOT / "spec/mode.md").read_text(encoding="utf8").split("\n"):
        m = re.match(r"^\| ([A-Z]-\d\d) \|", line)
        if m:
            status = "OPEN" if "OPEN" in line else ("PROVISIONAL" if "PROVISIONAL" in line else "ADOPTED")
            out[m.group(1)] = status
    return out
