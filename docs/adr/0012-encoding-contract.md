# ADR-0012: The Encoding Contract

**Status:** Proposed
**Date:** 2026-10-11
**Affected:** s2t/encodings/, spec/encodings/, tests/test_encoding.py, tests/test_review_sheet.py,
tools/render_corpus.py, tools/build_pdfs.py, shavian2tengwar.py
**Origin:** project 0003
**Review:** In PR #3
**Revert:** `ca18a8e` (encodings, spec table, tests), `524c1ee` and `29927b1` (review sheets and
PDF font). Revert them together, and ADR-0011 with them.

## Context

ADR-0003 made Alcarin the only encoding and left `--encoding` "so a second font can be added later".
The encoding layer had grown around one font:

- the mark order (AE-01, nearest the base first) was hard-coded in `Encoding.encode_cell`;
- the review sheet's CSS and the PDF font stack named "Alcarin Tengwar";
- `tests/test_encoding.py` imported Alcarin's tables directly.

## Decision

An encoding is a module in `s2t/encodings/`, registered in `_REGISTRY` in `s2t/encodings/__init__.py`.
`alcarin` is first, and the first is the default (`DEFAULT_ENCODING`). Each encoding has a spec file,
`spec/encodings/<name>.md`, and must provide the following.

1. **Coverage.** A code point sequence for every glyph and mark name the mode emits:
   - every letter in the consonant and ligature tables, `{hwesta}` and `{nwalme}` among them;
   - the nuquerna forms `{silme-nuquerna}` and `{esse-nuquerna}` (S-02);
   - the carriers `{telco}` (short) and `{aara}` (long);
   - the three shorthands `{the-shorthand}`, `{of-shorthand}` and `{and-shorthand}`;
   - the ten punctuation names (U-01 to U-05);
   - all ten marks.

   A value may be several code points, as `{and-shorthand}` is.
2. **The `below` set.** The marks drawn under the base. Under P-04 that is `[bar-below]` and
   `[dot-below]` for every encoding.
3. **Its own mark order** (`order`), either `"nearest-first"` (K-01 reversed, outward from the base)
   or `"top-first"` (K-01 as it is). It is set from the font's behaviour, as checked by the gate
   fixture (ADR-0011), and recorded as a rule in the encoding's spec. AE-01 is Alcarin's. The marks
   below always follow the marks above.
4. **Its font family names** (`families`), first the canonical one. The review sheet and the PDF stack
   use them.
5. **A fallback for missing extended letters.** A font with no Extended Ando or Extended Umbar maps
   `{the-shorthand}` to its `{anto}` code point and `{of-shorthand}` to its `{ampa}` code point. These
   are the letters for 𐑞 and 𐑝 when W-01 and W-02 do not apply. Its spec says so in a `PROVISIONAL`
   rule. No registered font needs this: Alcarin and FreeMonoTengwar both have `E01C` and `E01D`.
6. **No reserved code points.** `U+E014` (óre, R-02), `U+E048` (double acute) and `U+E056` are never
   emitted (AE-04, FE-05).

The mode never changes for a font. Its output, the glyph IR, is the same for every encoding.

`tests/test_encoding.py` enforces the contract for every registered encoding:

- the table matches the spec's table;
- every glyph name in `spec/mode.md` is encoded;
- every corpus row encodes without a missing glyph;
- the `below` set and the families are declared;
- no reserved code point appears.

The mark-order tests are kept for each encoding (AE-01, FE-01), and one test checks `"top-first"`.

The tools follow the encoding:

- **Every encoding gets its own committed review sheet** (Alex, 2026-10-11). `tools/render_corpus.py`
  writes one per encoding, each in its own font: `corpus/review.html` for the default (Alcarin), and
  `corpus/review-NAME.html` for each other one. `--encoding NAME` writes just one. The freshness test
  checks all of them.
- `tools/build_pdfs.py` prints the corpus sheet once per encoding (`corpus/review.pdf`,
  `corpus/review-NAME.pdf`). `--encoding NAME` limits the corpus to that one, and sets the Tengwar font
  in the guides' font stack (Alcarin by default).

**FreeMonoTengwar** (`freemono`) is the second encoding, with rules FE-01 to FE-06 in
`spec/encodings/freemono.md`. For every glyph the mode uses, its code points are the same as
Alcarin's. That was found by reading both cmaps: the two fonts share the FreeTengwar layout. Its marks
are drawn at fixed heights, so both orders render the same. FE-01 chooses nearest first so that the
output is byte-identical to Alcarin's, and text moves between the two fonts unchanged.

Alternatives considered:

- **Reuse Alcarin's table for FreeMono, because the values agree.** Rejected: each table must stand
  on its own font's cmap (ADR-0011), and a future font that differs must not inherit by accident.
- **An order callback per encoding.** Rejected: two named orders cover every font examined.

## Consequences

- This supersedes ADR-0003's "Alcarin is the only encoding". ADR-0003's mark order is unchanged, and is
  now Alcarin's `order`.
- `Encoding(...)` now needs `families=`. `order` defaults to `"nearest-first"`.
- Because the two encodings agree byte for byte, `--encoding freemono` changes no output today. It
  matters for the font the tools use, and for any future font whose layout differs.
- Not verified: renderers other than Core Text and Chrome 155 (for example Word on Windows, or
  LibreOffice).
