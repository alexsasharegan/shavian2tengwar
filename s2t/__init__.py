"""shavian2tengwar: Shavian text to Tengwar, via a font-independent glyph IR."""

from .encodings import get_encoding
from .glyphs import Cell, parse_literal, to_literal
from .mode import translate_word
from .stream import translate


def render(text: str, fmt: str = "pua", encoding: str = "alcarin", strip_escapes: bool = False) -> str:
    """Translate text and serialize it: ``fmt`` is "pua" (code points) or "literal" (glyph names)."""
    items = translate(text, strip_escapes=strip_escapes)
    if fmt == "literal":
        return to_literal(items)
    if fmt == "pua":
        return get_encoding(encoding).encode(items)
    raise ValueError(f"unknown format {fmt!r}")


__all__ = ["Cell", "get_encoding", "parse_literal", "render", "to_literal", "translate", "translate_word"]
