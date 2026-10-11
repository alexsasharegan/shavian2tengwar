"""Glyph IR: named glyph clusters, independent of any font.

A *cell* is one base glyph plus its combining marks, written in the literal
notation used by Tecendil: ``{tinco}[dot-above]``. Names are defined in
spec/mode.md; spec/encodings/*.md maps them to code points.
"""

import re
from collections.abc import Iterable
from dataclasses import dataclass, field

CELL_RE = re.compile(r"\{([a-z-]+)\}((?:\[[a-z-]+\])*)")
MARK_RE = re.compile(r"\[([a-z-]+)\]")


@dataclass(frozen=True, slots=True)
class Cell:
    """One base glyph and its marks, in reading order (spec rule K-01)."""

    base: str
    marks: tuple[str, ...] = ()
    # IDs of the spec rules that produced this cell. Not part of equality.
    rules: tuple[str, ...] = field(default=(), compare=False)

    def literal(self) -> str:
        return "{" + self.base + "}" + "".join("[" + m + "]" for m in self.marks)


type Item = Cell | str


def to_literal(items: Iterable[Item]) -> str:
    """Serialize IR items as Tecendil-style literals. Raw text passes through."""
    return "".join(i.literal() if isinstance(i, Cell) else i for i in items)


def parse_literal(text: str) -> list[Item]:
    """Parse literal notation back into cells and raw text."""
    out: list[Item] = []
    pos = 0
    for m in CELL_RE.finditer(text):
        if m.start() > pos:
            out.append(text[pos : m.start()])
        out.append(Cell(m.group(1), tuple(MARK_RE.findall(m.group(2)))))
        pos = m.end()
    if pos < len(text):
        out.append(text[pos:])
    return out
