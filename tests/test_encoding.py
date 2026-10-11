"""The Alcarin encoding table must match spec/encodings/alcarin.md, and cover
every glyph name that spec/mode.md uses."""

import re
import unittest
from pathlib import Path

from s2t.encodings.alcarin import LETTERS, MARKS

ROOT = Path(__file__).resolve().parent.parent
ROW = re.compile(r"^\| `([\{\[])([a-z-]+)[\}\]]` \| ((?:`?U\+[0-9A-F]{4}`?\s*)+)\|", re.M)

# Names that appear in mode.md but are not meant to be encoded.
NOT_ENCODED = {
    "{name}", "[name]", "{base}", "[mark]", "[marks]",  # notation placeholders
    "{oore}",  # R-02: never emitted
    "[right-curl-below]",  # rejected candidate for 'to'
}


def spec_table():
    text = (ROOT / "spec/encodings/alcarin.md").read_text(encoding="utf8")
    letters, marks = {}, {}
    for kind, name, cps in ROW.findall(text):
        value = "".join(chr(int(c, 16)) for c in re.findall(r"U\+([0-9A-F]{4})", cps))
        (letters if kind == "{" else marks)[name] = value
    return letters, marks


class MarkOrder(unittest.TestCase):
    """AE-01: marks above the base go in nearest-first, so the nasal bar sits under the vowel mark."""

    def encode(self, literal):
        from s2t import get_encoding, parse_literal

        return get_encoding("alcarin").encode(parse_literal(literal))

    def test_nasal_bar_sits_between_vowel_mark_and_base(self):
        self.assertEqual(self.encode("{tinco}[dot-above][bar-above]"), "\ue000\ue050\ue044")

    def test_marks_below_follow_the_marks_above(self):
        self.assertEqual(
            self.encode("{tinco}[dot-above][bar-above][bar-below]"), "\ue000\ue050\ue044\ue051"
        )

    def test_single_marks_are_unchanged(self):
        self.assertEqual(self.encode("{tinco}[dot-above]"), "\ue000\ue044")
        self.assertEqual(self.encode("{tinco}[bar-below]"), "\ue000\ue051")


class EncodingDrift(unittest.TestCase):
    def test_table_matches_spec(self):
        letters, marks = spec_table()
        self.assertEqual(LETTERS, letters)
        self.assertEqual(MARKS, marks)

    def test_every_mode_name_is_encoded(self):
        mode = (ROOT / "spec/mode.md").read_text(encoding="utf8")
        names = set(re.findall(r"[\{\[][a-z-]+[\}\]]", mode)) - NOT_ENCODED
        missing = sorted(
            n for n in names if (LETTERS if n[0] == "{" else MARKS).get(n[1:-1]) is None
        )
        self.assertEqual(missing, [], "glyph names used in mode.md but not encoded")

    def test_no_reserved_glyphs_in_use_by_accident(self):
        # E014 (oore), E048 (double acute) are reserved (AE-04).
        used = "".join(LETTERS.values()) + "".join(MARKS.values())
        self.assertNotIn("", used)
        self.assertNotIn("", used)


if __name__ == "__main__":
    unittest.main()
