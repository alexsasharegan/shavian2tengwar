# 0003 — Second Font Encoding

> **Status:** In progress (gate: two candidates pass on rendering; waiting on Alex's choice)
> **Created:** 2026-10-11
> **Branch:** `feat/0003-second-encoding`

## Objective

Add a second Tengwar font encoding next to Alcarin, so the mode's glyph names can be written for another
free, Unicode-PUA font that renders correctly on macOS. On the way, make the encoding layer a real
contract that any font has to meet.

## Scope (Alex's decisions)

- Only Unicode Private Use Area fonts. ASCII-mapped fonts (Annatar, Parmaite, Eldamar and the like) are out.
- **Gate.** A candidate qualifies only if it is free, uses PUA code points, installs on macOS, and Core Text
  positions its tehtar through OpenType GPOS or AAT, with no dotted circles. Graphite-only fonts are out.
- Tengwar Telcontar failed on Alex's Mac (tehtar on dotted circles in Core Text). It is evaluated only for
  comparison.
- Candidates: FreeMonoTengwar, Tengwar Formal CSUR, and Tengwar Telcontar for comparison.
- Never copy code points from another table. Every code point is checked against the font's own cmap.

## Deliverables

1. ADR: scope and acceptance criteria (the gate).
2. ADR: the encoding contract (coverage, `below` set, mark order per font, fallback for the shorthands).
3. `tests/test_encoding.py` generalised to every registered encoding.
4. A font family per encoding, used by `tools/render_corpus.py` and `tools/build_pdfs.py`.
5. The gate fixture, rendered per candidate, plus Alex's check in Safari and TextEdit.
6. The survey: license, formats, layout tables and full cmap per candidate ([survey.md](./survey.md)).
7. `spec/encodings/<font>.md` (PROVISIONAL) for the first font that passes.
8. `s2t/encodings/<font>.py`, registered and usable from `--encoding` and the review sheet.

## Stop condition

If no candidate passes the gate, stop after the survey, log the findings, and write no encoding table.

## Definition of Done

- At least one candidate passes the gate on Alex's Mac, or the project stops with the findings logged.
- `npm test` and `npm run lint` pass on Python 3.14.
- The ADRs are `Proposed`, the new spec rules `PROVISIONAL`, and the PR is open for Alex. Not merged.
