"""Encodings map glyph names to a font's code points."""

from __future__ import annotations

from collections.abc import Iterable

from ..glyphs import Cell, Item


class Encoding:
    def __init__(self, name: str, letters: dict, marks: dict):
        self.name = name
        self.letters = letters
        self.marks = marks

    def encode_cell(self, cell: Cell) -> str:
        try:
            out = self.letters[cell.base]
        except KeyError:
            raise KeyError(f"{self.name}: no code point for glyph {{{cell.base}}}") from None
        for m in cell.marks:
            try:
                out += self.marks[m]
            except KeyError:
                raise KeyError(f"{self.name}: no code point for mark [{m}]") from None
        return out

    def encode(self, items: Iterable[Item]) -> str:
        return "".join(self.encode_cell(i) if isinstance(i, Cell) else i for i in items)


def get_encoding(name: str) -> Encoding:
    if name == "alcarin":
        from .alcarin import ALCARIN

        return ALCARIN
    raise ValueError(f"unknown encoding {name!r} (available: alcarin)")
