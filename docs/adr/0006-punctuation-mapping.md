# ADR-0006: Punctuation Mapping

**Status:** Active
**Date:** 2026-10-11
**Affected:** spec/mode.md (U-02 to U-05), s2t/stream.py (`PUNCTUATION`), corpus/marks.md
**Origin:** DECISIONS.md D-02, D-03
**Review:** Approved by merging PR #1
**Revert:** U-05 is `0c27b54`. U-02 to U-04 came in with the engine (`c9f0f33`), so edit `PUNCTUATION` in `s2t/stream.py`, U-02 to U-04 in `spec/mode.md` and the rows in `corpus/marks.md` instead

## Context

Only `,` and `.` had settled Tengwar forms (U-01). Other punctuation passed through as Latin
characters, which puts Latin glyphs into a Tengwar line and may fall back to another font. Alcarin has
its own punctuation glyphs, and Tecendil's mode files have no punctuation table, so the names follow
Alcarin's.

## Decision

| Input | Glyph | Code point | Rule |
|---|---|---|---|
| `;` | `{double-section-mark}` | `U+E069` | U-02 |
| `:` | `{triple-pusta}` | `U+E062` | U-03 |
| `-` | `{section-mark}` | `U+E068` | U-04 |
| `!` | `{exclamation-mark}` | `U+E065` | U-05 |
| `?` | `{question-mark}` | `U+E066` | U-05 |
| `(` and `)` | `{parenthesis-mark}` | `U+E067` | U-05 |
| `“` | `{left-quotation-mark}` | `U+E06A` | U-05 |
| `”` | `{right-quotation-mark}` | `U+E06B` | U-05 |

- `;` reads as a heavier pause than the comma's single dot and is not confused with `:`; Aranoss's text
  writes it the same way. `:` takes the stacked dots, the nearest to the Latin colon. Alcarin has no
  hyphen, and the section mark is the nearest short horizontal stroke.
- Alcarin has one parenthesis glyph for both sides; no second one is invented.
- An ASCII `"` alternates open and close, tracked across the whole stream.
- Single quotes and apostrophes pass through, because a single quote is ambiguous with an apostrophe.
  Square brackets, braces and `/` pass through.

**Alternatives.** `;` as `{pusta}` + `{double-pusta}` (reads as two marks). `-` passed through as ASCII,
or dropped (loses compound boundaries).

## Consequences

- An odd number of `"` in the input flips every later quote, because the state never resets.
- `...` is three `{double-pusta}`; there is no ellipsis rule.
- Both were accepted as is in PR #1. An ellipsis rule, or resetting the quote state per paragraph,
  would be a new ADR.
