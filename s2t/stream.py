"""Text streams: Shavian words, punctuation, and {{verbatim}} escapes."""

import re

from .glyphs import Cell, Item
from .mode import translate_word

# Shavian letters are U+10450..U+1047F; the namer dot is part of a word.
WORD_RE = re.compile(r"[·\U00010450-\U0001047F]+")
STREAM_RE = re.compile(r"(\{\{.*?\}\}|[·\U00010450-\U0001047F]+)", re.DOTALL)

# U-01..U-04
PUNCTUATION = {
    ",": ("pusta", "U-01"),
    ".": ("double-pusta", "U-01"),
    ";": ("double-section-mark", "U-02"),
    ":": ("triple-pusta", "U-03"),
    "-": ("section-mark", "U-04"),
    # U-05
    "!": ("exclamation-mark", "U-05"),
    "?": ("question-mark", "U-05"),
    "(": ("parenthesis-mark", "U-05"),
    ")": ("parenthesis-mark", "U-05"),
    "\u201c": ("left-quotation-mark", "U-05"),
    "\u201d": ("right-quotation-mark", "U-05"),
}


def translate_punctuation(text: str, quote_state: list[bool]) -> list[Item]:
    """Map punctuation. ``quote_state`` is a one-item list holding whether the next
    ASCII double quote opens (False) or closes (True) a quotation."""
    out: list[Item] = []
    for ch in text:
        if ch == '"':
            base = "right-quotation-mark" if quote_state[0] else "left-quotation-mark"
            quote_state[0] = not quote_state[0]
            out.append(Cell(base, (), ("U-05",)))
        elif ch in PUNCTUATION:
            base, rule = PUNCTUATION[ch]
            out.append(Cell(base, (), (rule,)))
        else:
            out.append(ch)
    return out


def translate(text: str, strip_escapes: bool = False) -> list[Item]:
    """Translate a text stream to glyph items.

    Shavian words become cells, mapped punctuation becomes cells, and
    everything else (spaces, other punctuation, {{...}} blocks) passes through.
    """
    out: list[Item] = []
    quote_state = [False]
    for part in STREAM_RE.split(text):
        if not part:
            continue
        if part.startswith("{{") and part.endswith("}}"):
            out.append(part[2:-2] if strip_escapes else part)
        elif WORD_RE.fullmatch(part):
            out.extend(translate_word(part))
        else:
            out.extend(translate_punctuation(part, quote_state))
    return out
