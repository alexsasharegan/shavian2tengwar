# ADR-0010: PDF Build and Committed PDFs

**Status:** Active
**Date:** 2026-10-11
**Affected:** tools/build_pdfs.py, tools/requirements-docs.txt, docs/*.pdf, corpus/review.pdf, package.json
**Origin:** DECISIONS.md D-10, D-13, D-20 (PDFs), D-21
**Review:** Corpus PDF proposed by Alex; approved by merging PR #1
**Revert:** build script `fdc65e9`; corpus PDF `14a1c7b`

## Context

The PDFs of the language guide and the philosophy essay were made by pasting into Obsidian and
exporting. They drift from the Markdown whenever a guide is edited. The guides need three fonts at
once: Courier for Latin, Bernie Sans Beta for Shavian and Alcarin Tengwar for Tengwar, and the PDFs
are shared with people who have none of them.

## Decision

- **`tools/build_pdfs.py` builds them**: Markdown to HTML with markdown-it-py, then Chrome's
  print-to-PDF through Playwright (the engine Obsidian prints with). Letter size, font stack Courier,
  Bernie Sans Beta, Alcarin Tengwar, fonts embedded. `npm run pdf`.
- **It also builds `corpus/review.pdf`** from the same HTML as `corpus/review.html`
  (`build_sheet()`), with print CSS: light palette, one corpus file per page, no row split.
- **The PDFs stay committed**, next to their sources.
- **Agents do not regenerate the PDFs.** Alex builds them locally, where all three fonts are installed. Whoever edits a guide says the PDF needs rebuilding.

**Alternatives.** A Node pipeline. `pandoc` and LaTeX, which handle these fonts badly. Building the
PDFs in CI, or not tracking them.

## Consequences

- No test checks the PDFs, so a stale PDF after a guide edit is possible. `test_sheet_is_current`
  guards only the HTML.
- The CSS approximates the old Obsidian output; it is not Obsidian's theme.
- Chrome must be installed to build them.
