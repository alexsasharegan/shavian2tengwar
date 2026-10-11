"""Encodings map glyph names to a font's code points."""

from collections.abc import Iterable

from ..glyphs import Cell, Item


class Encoding:
    def __init__(
        self, name: str, letters: dict[str, str], marks: dict[str, str], below: frozenset[str] = frozenset()
    ) -> None:
        self.name = name
        self.letters = letters
        self.marks = marks
        self.below = below  # mark names that sit below the base

    def encode_cell(self, cell: Cell) -> str:
        try:
            out = self.letters[cell.base]
        except KeyError:
            raise KeyError(f"{self.name}: no code point for glyph {{{cell.base}}}") from None
        # A cell's marks are in K-01 order, which is top to bottom (vowel, nasal bar, then
        # the marks below). A font stacks marks outward from the base in code point order,
        # so the marks above go in reversed: the one nearest the base comes first.
        above = [m for m in cell.marks if m not in self.below]
        below = [m for m in cell.marks if m in self.below]
        for m in above[::-1] + below:
            try:
                out += self.marks[m]
            except KeyError:
                raise KeyError(f"{self.name}: no code point for mark [{m}]") from None
        return out

    def encode(self, items: Iterable[Item]) -> str:
        return "".join(self.encode_cell(i) if isinstance(i, Cell) else i for i in items)


ENCODINGS = ("alcarin",)


def get_encoding(name: str) -> Encoding:
    if name == "alcarin":
        from .alcarin import ALCARIN

        return ALCARIN
    raise ValueError(f"unknown encoding {name!r} (available: {', '.join(ENCODINGS)})")
