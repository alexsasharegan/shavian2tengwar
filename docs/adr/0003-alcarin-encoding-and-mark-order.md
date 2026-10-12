# ADR-0003: Alcarin Encoding and Mark Order

**Status:** Active
**Date:** 2026-10-11
**Affected:** s2t/encodings/, spec/encodings/alcarin.md, corpus/review.html
**Origin:** DECISIONS.md D-05 (CSUR dropped), D-14
**Review:** Mark order corrected at Alex's request; approved by merging PR #1
**Revert:** CSUR removal is in `6d1e271`; mark order in `5eb9596` (restores the old order and the review sheet with it)

## Context

The old engine had a CSUR table and a `--csur` flag, and an "Everson" table. Neither matched the font
actually used, Alcarin Tengwar, whose layout derives from FreeTengwar and differs from both at many
code points.

A cluster can carry more than one mark above its base: a vowel mark and the nasal bar. Spec rule K-01
lists a cell's marks top to bottom, which is reading order: vowel mark, nasal bar, base, gemination
bar. The encoding first wrote the marks in that order (`{tinco}[dot-above][bar-above]` as
`E000 E044 E050`), and the font stacked the nasal bar on top of the vowel mark.

## Decision

- **Alcarin is the only encoding.** CSUR and Everson output are dropped. `--encoding` exists so a
  second font can be added later.
- **Marks are emitted outward from the base.** The IR keeps K-01 order. `Encoding.encode_cell` writes
  the marks above the base in reverse (nearest first), then the marks below, because fonts stack
  marks outward in code point order. `{tinco}[dot-above][bar-above]` is now `E000 E050 E044`.
- `tests/test_encoding.py` pins the order.

## Consequences

- Output only renders correctly in a font with Alcarin's layout. The README says so.
- The spec had claimed that mark order did not matter to the font, and AE-03 claimed stacking was
  verified. Neither was checked with two marks above. Both are corrected; the new order was checked
  by rendering it in Chromium.
- Anyone adding an encoding must decide which of its marks sit below (`below=` in `Encoding`).
- ADR-0012 adds a second encoding and makes the mark order a per-encoding setting. This
  ADR's order stays Alcarin's.
