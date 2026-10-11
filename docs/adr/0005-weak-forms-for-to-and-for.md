# ADR-0005: Weak Forms for *to* and *for*

**Status:** Proposed
**Date:** 2026-10-11
**Affected:** spec/mode.md (W-04, L-09, L-10, section 12), s2t/mode.py, corpus/word-signs.md, docs/language-guide.md (Part 3)
**Origin:** DECISIONS.md D-01, D-09
**Review:** Unreviewed; open in spec section 12
**Revert:** `6ba78b7` and `510c6f7`; in `spec/mode.md` set W-04, L-09 and L-10 back (the corpus rows citing them also go; `tests/test_coverage.py` names any leftovers)

## Context

Shavian abbreviates five words to one letter: 𐑞 *the*, 𐑝 *of*, 𐑯 *and*, 𐑑 *to* and 𐑓 *for*. The
first three have Tengwar shorthands (W-01 to W-03). The old engine wrote *to* and *for* as a bare
`{tinco}` and a bare `{formen}`; the old language guide documented these as deliberate "unadorned
base" shorthands.

Shavian uses the signs to tell homophones apart: 𐑑 *to* from 𐑑𐑵 *too/two*, 𐑓 *for* from 𐑓𐑹
*four*. ReadLex treats *to* as ending in a schwa. Tengwar precedent is thin: Tecendil's phonemic mode
has `{formen}{roomen}` for *for* (after DTS 39); its classical mode has `{tinco}[right-curl-below]`
for *to*, which breaks P-04 (no vowel marks below); Aranoss writes *to* in full.

## Decision

A bare 𐑑 or 𐑓 is spelled as its weak form, expanded the way ligatures are:

- 𐑑 → 𐑑𐑩 /tə/ → `{tinco}{telco}[breve]` (L-09)
- 𐑓 → 𐑓𐑼 /fər/ → `{formen}{roomen}[breve]` (L-10)

No Tengwar shorthand is adopted for either (W-04). The "Big Five" rows in Part 3 of the language
guide were replaced to match, and its stale tables were regenerated from the engine once.

**Alternatives.**

1. Keep the bare letters. Shortest, but contradicts the guide's own principle that nothing is silent,
   and makes *for* read as just "f".
2. Adopt Tecendil's `{formen}{roomen}` for *for* only. Matches DTS 39 and is the least surprising if
   following Tecendil.
3. Expand *to* as 𐑑𐑵 with the full vowel. Wrong for a weak form.

## Consequences

- *to* stays distinct from *too/two*, and *for* from *four*.
- *for* is less certain than *to*: /fər/ is the usual weak form, but a reader may expect the full vowel.
- The language guide's regenerated tables have no script keeping them in sync with the engine; they
  can drift if the rules change.
- Commit `6ba78b7` calls the old bare letters "an accident of fall-through". That is wrong: the guide
  documented them as deliberate. `spec/mode.md` section 7 (corrected in `4436d55`) is accurate.
