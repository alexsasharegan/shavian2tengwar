"""FreeMonoTengwar (Free Tengwar Font Project, 2013-07-21) code points.

Mirrors spec/encodings/freemono.md; tests/test_encoding.py fails if they drift.
Every value was read from FreeMonoTengwar.ttf's own cmap, not copied from another table.
"""

from . import Encoding

LETTERS = {
    "tinco": "",
    "parma": "",
    "calma": "",
    "quesse": "",
    "ando": "",
    "umbar": "",
    "anga": "",
    "ungwe": "",
    "thuule": "",
    "formen": "",
    "harma": "",
    "hwesta": "",
    "anto": "",
    "ampa": "",
    "anca": "",
    "nuumen": "",
    "malta": "",
    "nwalme": "",
    "vala": "",
    "anna": "",
    "roomen": "",
    "lambe": "",
    "silme": "",
    "silme-nuquerna": "",
    "esse": "",
    "esse-nuquerna": "",
    "hyarmen": "",
    "aara": "",
    "telco": "",
    "the-shorthand": "",
    "of-shorthand": "",
    "and-shorthand": "",
    "pusta": "",
    "double-pusta": "",
    "triple-pusta": "",
    "section-mark": "",
    "double-section-mark": "",
    "exclamation-mark": "",
    "question-mark": "",
    "parenthesis-mark": "",
    "left-quotation-mark": "",
    "right-quotation-mark": "",
}

MARKS = {
    "triple-dot-above": "",
    "dot-above": "",
    "dot-below": "",
    "acute": "",
    "right-curl": "",
    "left-curl": "",
    "bar-above": "",
    "bar-below": "",
    "breve": "",
    "grave": "",
}

# Marks drawn below the base (FE-02).
BELOW = frozenset({"bar-below", "dot-below"})

# FE-01: the font draws every mark at a fixed height, so either order renders the same. Nearest
# first keeps the output identical to Alcarin's, so text moves between the two fonts unchanged.
FREEMONO = Encoding("freemono", LETTERS, MARKS, BELOW, families=("FreeMonoTengwar",), order="nearest-first")
