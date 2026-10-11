"""Every enforceable spec rule must be exercised by the corpus, and the rules
the corpus cannot show positively (R-02) are checked directly."""

import unittest

from s2t import to_literal, translate

from .corpus import load_all, spec_rules
from .test_identities import sequences

# Principles are cross-cutting; R-02 is a prohibition, tested below.
EXEMPT = {"P-01", "P-02", "P-03", "P-04", "P-05", "R-02"}


class Coverage(unittest.TestCase):
    def test_every_rule_has_a_corpus_case(self):
        cases, identities, distincts = load_all()
        cited = set()
        for row in cases + identities + distincts:
            cited.update(row["rules"])
        missing = sorted(
            rid for rid, status in spec_rules().items()
            if status != "OPEN" and rid not in EXEMPT and rid not in cited
        )
        self.assertEqual(missing, [], "spec rules with no corpus case")

    def test_open_rules_are_listed(self):
        # OPEN rules need no case yet, but they must not be silently implemented as ADOPTED.
        self.assertTrue(all(s in ("ADOPTED", "PROVISIONAL", "OPEN") for s in spec_rules().values()))

    def test_oore_is_never_used(self):  # R-02
        words = sequences() | {"𐑮", "𐑮𐑮", "𐑣𐑻", "𐑓𐑹", "𐑕𐑑𐑸"}
        for w in words:
            self.assertNotIn("{oore}", to_literal(translate(w)))

    def test_no_dot_below(self):  # P-04: [dot-below] only ever appears inside {and-shorthand}
        for w in sequences():
            self.assertNotIn("[dot-below]", to_literal(translate(w)), w)


if __name__ == "__main__":
    unittest.main()
