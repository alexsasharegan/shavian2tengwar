"""Every registered encoding must meet the encoding contract (ADR-0012): its table matches
spec/encodings/<name>.md, it encodes every glyph name spec/mode.md uses and every cell the engine
emits for the corpus, and it writes the marks in its own order."""

import re
import unittest
from pathlib import Path

from s2t import ENCODINGS, get_encoding, parse_literal, translate
from s2t.encodings import Encoding
from tools.corpus import corpus_files, load

ROOT = Path(__file__).resolve().parent.parent
ROW = re.compile(r"^\| `([\{\[])([a-z-]+)[\}\]]` \| ((?:`?U\+[0-9A-F]{4}`?\s*)+)\|", re.M)

# Names that appear in mode.md but are not meant to be encoded.
NOT_ENCODED = {
    "{name}",
    "[name]",
    "{base}",
    "[mark]",
    "[marks]",  # notation placeholders
    "{oore}",  # R-02: never emitted
    "[right-curl-below]",  # rejected candidate for 'to'
}

# Code points no encoding may emit: óre (R-02), the double acute, and three inverted dots
# (AE-04, FE-05). Every registered font so far has these at the same code points.
RESERVED = {"", "", ""}


def spec_table(name):
    text = (ROOT / f"spec/encodings/{name}.md").read_text(encoding="utf8")
    letters, marks = {}, {}
    for kind, glyph, cps in ROW.findall(text):
        value = "".join(chr(int(c, 16)) for c in re.findall(r"U\+([0-9A-F]{4})", cps))
        (letters if kind == "{" else marks)[glyph] = value
    return letters, marks


def mode_names():
    mode = (ROOT / "spec/mode.md").read_text(encoding="utf8")
    return set(re.findall(r"[\{\[][a-z-]+[\}\]]", mode)) - NOT_ENCODED


class Contract(unittest.TestCase):
    def test_more_than_one_encoding_is_registered(self):
        self.assertEqual(ENCODINGS[0], "alcarin")
        self.assertIn("freemono", ENCODINGS)

    def test_table_matches_spec(self):
        for name in ENCODINGS:
            with self.subTest(name):
                enc = get_encoding(name)
                letters, marks = spec_table(name)
                self.assertEqual(enc.letters, letters)
                self.assertEqual(enc.marks, marks)

    def test_every_mode_name_is_encoded(self):
        names = mode_names()
        for name in ENCODINGS:
            with self.subTest(name):
                enc = get_encoding(name)
                missing = sorted(n for n in names if (enc.letters if n[0] == "{" else enc.marks).get(n[1:-1]) is None)
                self.assertEqual(missing, [], "glyph names used in mode.md but not encoded")

    def test_every_corpus_row_encodes(self):
        texts = []
        for path in corpus_files():
            cases, identities, distincts = load(path)
            texts += [r["shavian"] for r in cases] + [r[k] for r in identities + distincts for k in ("a", "b")]
        self.assertGreater(len(texts), 50)
        for name in ENCODINGS:
            enc = get_encoding(name)
            for text in texts:
                with self.subTest(encoding=name, text=text):
                    enc.encode(translate(text))  # raises KeyError on a missing glyph or mark

    def test_marks_below_are_declared(self):
        # P-04: the only marks below are gemination and the 'and' shorthand's dot.
        for name in ENCODINGS:
            with self.subTest(name):
                enc = get_encoding(name)
                self.assertEqual(enc.below, {"bar-below", "dot-below"})
                self.assertLessEqual(enc.below, enc.marks.keys())

    def test_every_encoding_names_its_font_family(self):
        for name in ENCODINGS:
            with self.subTest(name):
                enc = get_encoding(name)
                self.assertTrue(enc.families and all(enc.families))
                self.assertIn(enc.order, ("nearest-first", "top-first"))

    def test_no_reserved_glyphs_in_use_by_accident(self):
        for name in ENCODINGS:
            with self.subTest(name):
                enc = get_encoding(name)
                used = set("".join(enc.letters.values()) + "".join(enc.marks.values()))
                self.assertEqual(used & RESERVED, set())


class MarkOrder(unittest.TestCase):
    """Each encoding writes the marks above in its own order; the marks below always follow."""

    def encode(self, encoding, literal):
        return get_encoding(encoding).encode(parse_literal(literal))

    def test_alcarin_nasal_bar_sits_between_vowel_mark_and_base(self):
        # AE-01
        self.assertEqual(self.encode("alcarin", "{tinco}[dot-above][bar-above]"), "")

    def test_alcarin_marks_below_follow_the_marks_above(self):
        self.assertEqual(self.encode("alcarin", "{tinco}[dot-above][bar-above][bar-below]"), "")

    def test_single_marks_are_unchanged(self):
        for name in ENCODINGS:
            with self.subTest(name):
                self.assertEqual(self.encode(name, "{tinco}[dot-above]"), "")
                self.assertEqual(self.encode(name, "{tinco}[bar-below]"), "")

    def test_freemono_is_nearest_first_like_alcarin(self):
        # FE-01
        self.assertEqual(self.encode("freemono", "{tinco}[dot-above][bar-above][bar-below]"), "")
        self.assertEqual(self.encode("freemono", "{ando}[acute][bar-above]"), "")

    def test_top_first_keeps_k01_order(self):
        enc = Encoding(
            "test",
            {"tinco": "T"},
            {"dot-above": "d", "bar-above": "b", "bar-below": "g"},
            frozenset({"bar-below"}),
            families=("Test",),
            order="top-first",
        )
        self.assertEqual(enc.encode(parse_literal("{tinco}[dot-above][bar-above][bar-below]")), "Tdbg")


if __name__ == "__main__":
    unittest.main()
