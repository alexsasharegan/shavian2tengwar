"""shavian2tengwar: Shavian text to Tengwar, via a font-independent glyph IR."""

import sys

if sys.version_info < (3, 14):
    raise RuntimeError(
        f"shavian2tengwar needs Python 3.14 or newer; this is {sys.version.split()[0]} ({sys.executable}). "
        "Install 3.14 and run the commands with it (see README)."
    )

from .encodings import ENCODINGS, get_encoding  # noqa: E402
from .glyphs import Cell, parse_literal, to_literal  # noqa: E402
from .mode import translate_word  # noqa: E402
from .stream import translate  # noqa: E402


def render(text: str, fmt: str = "pua", encoding: str = "alcarin", strip_escapes: bool = False) -> str:
    """Translate text and serialize it: ``fmt`` is "pua" (code points) or "literal" (glyph names)."""
    items = translate(text, strip_escapes=strip_escapes)
    if fmt == "literal":
        return to_literal(items)
    if fmt == "pua":
        return get_encoding(encoding).encode(items)
    raise ValueError(f"unknown format {fmt!r}")


__all__ = ["ENCODINGS", "Cell", "get_encoding", "parse_literal", "render", "to_literal", "translate", "translate_word"]
