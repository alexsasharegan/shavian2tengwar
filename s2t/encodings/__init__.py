"""Encodings map glyph names to a font's code points.

Every encoding meets the contract in docs/adr/0012-encoding-contract.md: it encodes every glyph and
mark name the mode emits, says which marks sit below the base, and says in which order the marks
above are written. tests/test_encoding.py checks each registered encoding against its spec table.
"""

from collections.abc import Iterable
from importlib import import_module
from typing import Literal

from ..glyphs import Cell, Item

# How a font wants the marks above a base ordered in the code point stream.
#   "nearest-first": outward from the base, i.e. K-01's top-to-bottom order reversed.
#   "top-first": K-01's order as it is.
type MarkOrder = Literal["nearest-first", "top-first"]


class Encoding:
    def __init__(
        self,
        name: str,
        letters: dict[str, str],
        marks: dict[str, str],
        below: frozenset[str] = frozenset(),
        *,
        families: tuple[str, ...],
        order: MarkOrder = "nearest-first",
    ) -> None:
        self.name = name
        self.letters = letters
        self.marks = marks
        self.below = below  # mark names that sit below the base
        self.families = families  # the font's family names, as CSS and font menus know it; first is canonical
        self.order = order

    def encode_cell(self, cell: Cell) -> str:
        try:
            out = self.letters[cell.base]
        except KeyError:
            raise KeyError(f"{self.name}: no code point for glyph {{{cell.base}}}") from None
        # A cell's marks are in K-01 order, which is top to bottom (vowel, nasal bar, then the
        # marks below). The encoding's order decides how the marks above are written; the marks
        # below always follow them.
        above = [m for m in cell.marks if m not in self.below]
        below = [m for m in cell.marks if m in self.below]
        if self.order == "nearest-first":
            above.reverse()
        for m in above + below:
            try:
                out += self.marks[m]
            except KeyError:
                raise KeyError(f"{self.name}: no code point for mark [{m}]") from None
        return out

    def encode(self, items: Iterable[Item]) -> str:
        return "".join(self.encode_cell(i) if isinstance(i, Cell) else i for i in items)


# Registered encodings: name -> (module, attribute). The first is the default.
_REGISTRY = {
    "alcarin": ("alcarin", "ALCARIN"),
    "freemono": ("freemono", "FREEMONO"),
}
ENCODINGS = tuple(_REGISTRY)
DEFAULT_ENCODING = ENCODINGS[0]


def get_encoding(name: str) -> Encoding:
    try:
        module, attr = _REGISTRY[name]
    except KeyError:
        raise ValueError(f"unknown encoding {name!r} (available: {', '.join(ENCODINGS)})") from None
    return getattr(import_module(f".{module}", __name__), attr)
