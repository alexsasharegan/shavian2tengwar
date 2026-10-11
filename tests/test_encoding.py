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
