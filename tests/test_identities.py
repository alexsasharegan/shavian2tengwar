"""P-02: different Shavian must give different glyphs, except for the
identities that spec/mode.md declares (sections 6 and 8)."""

import itertools
import unittest
from collections import defaultdict

from s2t import to_literal, translate

# The declared identities, as rewrites to a canonical spelling.
CANONICAL = {
    "𐑸": "𐑭𐑮", "𐑹": "𐑷𐑮", "𐑺": "𐑧𐑮", "𐑽": "𐑦𐑮", "𐑻": "𐑳𐑮", "𐑼": "𐑩𐑮",  # L-01..L-06
    "𐑿": "𐑘𐑵",  # L-07
    "𐑾": "𐑦𐑩",  # L-08
    "𐑱": "𐑧𐑘", "𐑴": "𐑪𐑢", "𐑶": "𐑪𐑘",  # I-01..I-03
    "𐑲": "𐑨𐑘", "𐑬": "𐑨𐑢",  # I-04, I-05
}


def canonical(s):
    return "".join(CANONICAL.get(c, c) for c in s)


VOWELS = "𐑦𐑧𐑨𐑩𐑪𐑳𐑫𐑰𐑭𐑷𐑵𐑲𐑬𐑱𐑴𐑶𐑾𐑸𐑹𐑺𐑽𐑻𐑼𐑿"
CONTEXT = ["", "𐑑", "𐑮", "𐑘", "𐑢", "𐑕", "𐑯𐑑", "𐑙𐑒"]


def sequences():
    seqs = set()
    for v in VOWELS:
        for c in CONTEXT:
            seqs.add(v + c)
            seqs.add(c + v)
    for a, b in itertools.product(VOWELS, repeat=2):
        seqs.add(a + b)
    # 𐑑 and 𐑓 alone are words, not just letters; keep them out of the enumeration.
    return {s for s in seqs if s not in ("𐑑", "𐑓")}


class Lossless(unittest.TestCase):
    def test_collisions_are_exactly_the_declared_identities(self):
        groups = defaultdict(set)
        for s in sequences():
            groups[to_literal(translate(s))].add(s)
        for glyphs, group in groups.items():
            with self.subTest(glyphs=glyphs):
                self.assertEqual(
                    len({canonical(s) for s in group}), 1, f"undeclared collision: {sorted(group)}"
                )

    def test_declared_identities_hold(self):
        for ch, expansion in CANONICAL.items():
            for ctx in CONTEXT:
                for a, b in ((ch + ctx, expansion + ctx), (ctx + ch, ctx + expansion)):
                    if a in ("𐑑", "𐑓") or b in ("𐑑", "𐑓"):
                        continue
                    # I-01..I-05 note: next to the same glide letter, the plain sequence is a
                    # geminate (𐑪𐑘𐑘), so the identity does not hold. English never has this.
                    if ch in "𐑱𐑴𐑶𐑲𐑬" and (
                        (a == ch + ctx and ctx[:1] == expansion[-1]) or (a == ctx + ch and ctx[-1:] == expansion[0])
                    ):
                        continue
                    with self.subTest(a=a, b=b):
                        self.assertEqual(to_literal(translate(a)), to_literal(translate(b)))


if __name__ == "__main__":
    unittest.main()
