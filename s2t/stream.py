"""Text streams: Shavian words, punctuation, and {{verbatim}} escapes."""

from __future__ import annotations

import re
from typing import List

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
}


def translate_punctuation(text: str) -> List[Item]:
    out: List[Item] = []
    for ch in text:
        if ch in PUNCTUATION:
            base, rule = PUNCTUATION[ch]
            out.append(Cell(base, (), (rule,)))
        else:
            out.append(ch)
    return out


def translate(text: str, strip_escapes: bool = False) -> List[Item]:
    """Translate a text stream to glyph items.

    Shavian words become cells, mapped punctuation becomes cells, and
    everything else (spaces, other punctuation, {{...}} blocks) passes through.
    """
    out: List[Item] = []
    for part in STREAM_RE.split(text):
        if not part:
            continue
        if part.startswith("{{") and part.endswith("}}"):
            out.append(part[2:-2] if strip_escapes else part)
        elif WORD_RE.fullmatch(part):
            out.extend(translate_word(part))
        else:
            out.extend(translate_punctuation(part))
    return out
