# ADR-0004: Vowel Marks and Declared Identities

**Status:** Active
**Date:** 2026-10-11
**Affected:** spec/mode.md (V-13, section 6), spec/encodings/alcarin.md (AE-04), s2t/mode.py, s2t/encodings/alcarin.py, tests/test_identities.py, corpus/
**Origin:** DECISIONS.md D-12, D-04
**Review:** TRAP mark approved by Alex, 2026-10-11; approved by merging PR #1
**Revert:** `ca09457` (also reverts I-04 and I-05 and restores `E056`); the edge case is in `f774302` and `0c27b54`

## Context

Spec principle P-02 says the output is lossless: two different Shavian strings never give the same
glyphs, except identities the spec declares. `tests/test_identities.py` enforces it by enumerating
short vowel sequences.

Short and long vowels pair up by mark: KIT/FLEECE, LOT/THOUGHT and FOOT/GOOSE share a mark, with the
long vowel on the long carrier `{aara}`. TRAP had its own mark, three inverted dots (`U+E056`), while
PALM used the triple dot. Shavian has no short /ɑ/, so the short slot of the triple dot was empty.

## Decision

- **TRAP shares PALM's triple dot.** 𐑨 is `[triple-dot-above]` on a consonant; 𐑭 stays
  `{aara}[triple-dot-above]` (V-13, V-22). `U+E056` is removed from the mode and the Alcarin table
  and listed as reserved (AE-04).
- **A diphthong is its nucleus plus its glide**, so five letters are declared identical to the plain
  sequence (spec section 6): 𐑱 = 𐑧𐑘, 𐑴 = 𐑪𐑢, 𐑶 = 𐑪𐑘 (I-01 to I-03), and, following from the
  TRAP change, 𐑲 = 𐑨𐑘 and 𐑬 = 𐑨𐑢 (I-04, I-05).
- **The identities do not hold next to the same glide letter.** 𐑪𐑘𐑘 is a geminate and takes the
  gemination bar; 𐑶𐑘 does not. The test skips that edge and the spec states it once, rather than
  denying the identity everywhere.

## Consequences

- One rule covers every long vowel: the short partner's mark on `{aara}`.
- I-04 and I-05 were accepted after scanning all 111,214 ReadLex entries: only the TrapBath variant of
  *Malawian* (32 occurrences by frequency) and the one-off name *iau* contain 𐑨 followed by 𐑘, 𐑢 or
  𐑿. Alex said *Malawian* is fine as it comes out. Should a real case appear, TRAP can be written on
  `{telco}` to keep it apart.
- English has neither 𐑪𐑘𐑘 nor 𐑶𐑘, so the glide edge case has no known word.
