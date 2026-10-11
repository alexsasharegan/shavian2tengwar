#!/usr/bin/env python3
"""Vowel-collision guard.

Different Shavian inputs may yield identical Tengwar output. Every such merge
must be listed in ACCEPTED (deliberate). Any new collision fails the test, and
a listed merge that stops colliding fails too, so the list never goes stale.

Run: python3 test_collisions.py
"""
import sys
import unittest

import shavian2tengwar as m

VOWELS = "𐑦𐑧𐑨𐑪𐑷𐑳𐑫𐑩𐑰𐑵𐑭𐑲𐑶𐑱𐑬𐑴𐑾𐑿𐑸𐑹𐑺𐑽𐑻𐑼"
FOLLOWERS = ["", "𐑑", "𐑮", "𐑘", "𐑢"]

# Deliberate merges, each a set of inputs that share one output.
ACCEPTED = [
    # Vowel pairs sharing a tehta (STRUT/FOOT, TRAP/PALM, LOT/THOUGHT).
    # 𐑭 and 𐑷 only merge with 𐑨 and 𐑪 before a consonant: orphaned, they
    # take the long carrier.
    {"𐑳", "𐑫"}, {"𐑳𐑑", "𐑫𐑑"}, {"𐑳𐑢", "𐑫𐑢"}, {"𐑳𐑘", "𐑫𐑘"}, {"𐑑𐑳", "𐑑𐑫"},
    {"𐑨𐑑", "𐑭𐑑"},
    {"𐑪𐑑", "𐑷𐑑"},
    # 𐑿 (Anna + doubled curl) equals 𐑵𐑘; /uːj/ is vanishingly rare.
    {"𐑵𐑘", "𐑿"},
    # R-vowels are ligatures of vowel + 𐑮.
    {"𐑦𐑮", "𐑽"}, {"𐑧𐑮", "𐑺"}, {"𐑩𐑮", "𐑼"},
    {"𐑨𐑮", "𐑭𐑮", "𐑸"}, {"𐑪𐑮", "𐑷𐑮", "𐑹"}, {"𐑳𐑮", "𐑫𐑮", "𐑻"},
    # Diphthongs equal vowel + glide.
    {"𐑦𐑘", "𐑾"}, {"𐑧𐑘", "𐑱"},
    {"𐑨𐑘", "𐑭𐑘", "𐑲"}, {"𐑨𐑢", "𐑭𐑢", "𐑬"},
    {"𐑪𐑘", "𐑷𐑘", "𐑶"}, {"𐑪𐑢", "𐑷𐑢", "𐑴"},
]

# Merges we intend to remove. Reported, but do not fail.
PENDING = []


def collision_groups():
    seen = {}
    for v in VOWELS:
        for f in FOLLOWERS:
            seen.setdefault(m.translate_word(v + f), set()).add(v + f)
        seen.setdefault(m.translate_word("𐑑" + v), set()).add("𐑑" + v)
    return [g for g in seen.values() if len(g) > 1]


class CollisionTest(unittest.TestCase):
    def test_collisions_are_all_accepted(self):
        found = collision_groups()
        allowed = ACCEPTED + PENDING
        new = [g for g in found if g not in allowed]
        stale = [g for g in ACCEPTED if g not in found]
        msg = []
        if new:
            msg.append("New unlisted collisions: " + "; ".join(" = ".join(sorted(g)) for g in new))
        if stale:
            msg.append("Listed merges that no longer collide: " + "; ".join(" = ".join(sorted(g)) for g in stale))
        self.assertFalse(msg, "\n".join(msg))
        for g in PENDING:
            if g in found:
                print("PENDING merge still present: " + " = ".join(sorted(g)), file=sys.stderr)


if __name__ == "__main__":
    unittest.main()
