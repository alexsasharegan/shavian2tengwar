"""The tables in the engine must match the tables in spec/mode.md.

Vowels and diphthongs are covered by the corpus (every row is checked against the
spec's rule IDs). These tests cover the rest: consonants, ligatures, weak forms,
word signs and punctuation.
"""

import re
import unittest
from pathlib import Path

from s2t import render
from s2t.encodings.alcarin import LETTERS
from s2t.mode import CONSONANTS, LIGATURES, SHORTHANDS, WEAK_FORMS
from s2t.stream import PUNCTUATION

SPEC = (Path(__file__).resolve().parent.parent / "spec/mode.md").read_text(encoding="utf8")


def rows(rule_prefix):
    """Table rows whose first cell is a rule ID starting with ``rule_prefix`` (e.g. ``"L-"``)."""
    return [line for line in SPEC.splitlines() if re.match(rf"\| {re.escape(rule_prefix)}\d\d \|", line)]


class Consonants(unittest.TestCase):
    def test_c01_table_matches_engine(self):
        section = SPEC.split("## 3. Consonants")[1].split("### 3.1")[0]
        spec = dict(re.findall(r"\| (\S) \| /[^|]+/ \| `\{([a-z]+)\}`", section))
        spec.update(dict(re.findall(r"\| \S \| /[^|]+/ \| `\{[a-z]+\}` \| (\S) \| /[^|]+/ \| `\{([a-z]+)\}`", section)))
        self.assertEqual(len(spec), 24)
        self.assertEqual(spec, CONSONANTS)

    def test_every_consonant_glyph_is_encoded(self):
        for letter, name in CONSONANTS.items():
            with self.subTest(letter):
                self.assertIn(name, LETTERS)


class Ligatures(unittest.TestCase):
    def test_l01_to_l08_match_engine(self):
        spec = {}
        for line in rows("L-"):
            m = re.match(r"\| (L-0[1-8]) \| (\S) \S+ \| [^|]+ \| (\S+) \|", line)
            if m:
                spec[m[2]] = (m[3], m[1])
        self.assertEqual(len(spec), 8)
        self.assertEqual(spec, LIGATURES)

    def test_weak_forms_match_engine(self):
        spec = {}
        for line in rows("L-"):
            m = re.match(r"\| (L-09|L-10) \| (\S) \(the word [^)]*\) \| [^|]+ \| (\S+)", line)
            if m:
                spec[m[2]] = (m[3], m[1])
        self.assertEqual(spec, WEAK_FORMS)


class WordSigns(unittest.TestCase):
    def test_w01_w02_match_engine(self):
        spec = {}
        for line in rows("W-"):
            m = re.match(r"\| (W-0[12]) \| The word (\S) alone .* is `\{([a-z-]+)\}`", line)
            if m:
                spec[m[2]] = (m[3], m[1])
        self.assertEqual(spec, {k: v for k, v in SHORTHANDS.items() if v[1] in ("W-01", "W-02")})

    def test_w03_and_is_ando_with_nasal_bar_and_under_dot(self):
        self.assertEqual(SHORTHANDS["𐑯"], ("and-shorthand", "W-03"))
        self.assertIn("`{ando}[bar-above][dot-below]`", [r for r in rows("W-") if r.startswith("| W-03")][0])
        # The encoded shorthand is exactly those three code points.
        self.assertEqual(LETTERS["and-shorthand"], "")

    def test_a_shorthand_is_only_the_whole_word(self):
        self.assertEqual(render("𐑞", "literal"), "{the-shorthand}")
        self.assertNotIn("shorthand", render("𐑞𐑞", "literal"))
        self.assertNotIn("shorthand", render("𐑞𐑩", "literal"))


class Punctuation(unittest.TestCase):
    def test_single_character_marks_match_engine(self):
        spec = {}
        for line in rows("U-"):
            for char, name in re.findall(r"`(.)` is `\{([a-z-]+)\}`", line):
                spec[char] = name
        # U-05 also lists both parentheses and the curly quotes in prose; check those by name.
        u05 = [line for line in rows("U-") if line.startswith("| U-05")][0]
        for name in ("parenthesis-mark", "left-quotation-mark", "right-quotation-mark"):
            self.assertIn("{" + name + "}", u05)
        engine = {c: n for c, (n, _) in PUNCTUATION.items() if c in spec}
        self.assertEqual(spec, engine)
        self.assertEqual(set(spec), set(",.;:-!?"))

    def test_every_glyph_name_the_spec_uses_for_punctuation_is_the_one_the_engine_emits(self):
        spec_names = set(re.findall(r"`\{([a-z-]+)\}`", "\n".join(rows("U-"))))
        self.assertEqual(spec_names, {n for n, _ in PUNCTUATION.values()})

    def test_every_punctuation_glyph_is_encoded(self):
        for char, (name, _) in PUNCTUATION.items():
            with self.subTest(char):
                self.assertIn(name, LETTERS)


if __name__ == "__main__":
    unittest.main()
