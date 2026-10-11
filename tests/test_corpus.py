"""Every corpus case must translate to its stated glyphs, and the rules it
cites must be real spec rules that actually fired for it."""

import unittest

from s2t import to_literal, translate
from s2t.glyphs import Cell

from .corpus import load_all, spec_rules


def fired(items):
    seen = set()
    for i in items:
        if isinstance(i, Cell):
            seen.update(i.rules)
    return seen


class Corpus(unittest.TestCase):
    def test_cases(self):
        cases, identities, distincts = load_all()
        self.assertTrue(cases, "no corpus cases found")
        known = spec_rules()
        for c in cases:
            with self.subTest(c["where"], shavian=c["shavian"]):
                items = translate(c["shavian"])
                self.assertEqual(to_literal(items), c["glyphs"])
                for rule in c["rules"]:
                    self.assertIn(rule, known, f"{rule} is not a rule in spec/mode.md")
                    self.assertIn(rule, fired(items), f"{rule} is cited but did not fire")

    def test_declared_identities(self):
        _, identities, _ = load_all()
        for row in identities:
            with self.subTest(row["where"]):
                self.assertEqual(to_literal(translate(row["a"])), to_literal(translate(row["b"])))
                for rule in row["rules"]:
                    self.assertIn(rule, spec_rules())

    def test_distinct_pairs(self):
        _, _, distincts = load_all()
        for row in distincts:
            with self.subTest(row["where"]):
                self.assertNotEqual(to_literal(translate(row["a"])), to_literal(translate(row["b"])))


if __name__ == "__main__":
    unittest.main()
