"""Alcarin Tengwar (Tosche) code points.

Mirrors spec/encodings/alcarin.md; tests/test_encoding.py fails if they drift.
Alcarin's layout is not Everson's and not CSUR.
"""

from . import Encoding

LETTERS = {
    "tinco": "\ue000",
    "parma": "\ue001",
    "calma": "\ue002",
    "quesse": "\ue003",
    "ando": "\ue004",
    "umbar": "\ue005",
    "anga": "\ue006",
    "ungwe": "\ue007",
    "thuule": "\ue008",
    "formen": "\ue009",
    "harma": "\ue00a",
    "hwesta": "\ue00b",
    "anto": "\ue00c",
    "ampa": "\ue00d",
    "anca": "\ue00e",
    "nuumen": "\ue010",
    "malta": "\ue011",
    "nwalme": "\ue013",
    "vala": "\ue015",
    "anna": "\ue016",
    "roomen": "\ue020",
    "lambe": "\ue022",
    "silme": "\ue024",
    "silme-nuquerna": "\ue025",
    "esse": "\ue026",
    "esse-nuquerna": "\ue027",
    "hyarmen": "\ue028",
    "aara": "\ue02c",
    "telco": "\ue02e",
    "the-shorthand": "\ue01c",
    "of-shorthand": "\ue01d",
    "and-shorthand": "\ue004\ue050\ue045",
    "pusta": "\ue060",
    "double-pusta": "\ue061",
    "triple-pusta": "\ue062",
    "section-mark": "\ue068",
    "double-section-mark": "\ue069",
    "exclamation-mark": "\ue065",
    "question-mark": "\ue066",
    "parenthesis-mark": "\ue067",
    "left-quotation-mark": "\ue06a",
    "right-quotation-mark": "\ue06b",
}

MARKS = {
    "triple-dot-above": "\ue040",
    "dot-above": "\ue044",
    "dot-below": "\ue045",
    "acute": "\ue046",
    "right-curl": "\ue04a",
    "left-curl": "\ue04c",
    "bar-above": "\ue050",
    "bar-below": "\ue051",
    "breve": "\ue053",
    "grave": "\ue054",
    "reversed-triple-dot-above": "\ue056",
}

ALCARIN = Encoding("alcarin", LETTERS, MARKS)
