# 0001 — Engine Rewrite

> **Status:** In progress (review)
> **Created:** 2026-10-11 (bootstrapped after the fact; the work started at `d729c2c`)
> **Branch:** `dev/refactor`

## Objective

Replace the single-script converter with an engine that implements a written specification:
Shavian in, font-independent glyph names in the middle, Alcarin Tengwar code points out. Every rule
has an ID, and a Markdown corpus proves each rule fires.

## Scope & Deliverables

- `spec/mode.md` and `spec/encodings/alcarin.md` as the authority ([ADR-0002](../../adr/0002-spec-first-engine-and-package-layout.md)).
- The `s2t/` package and the `shavian2tengwar.py` front end ([ADR-0002](../../adr/0002-spec-first-engine-and-package-layout.md), [ADR-0009](../../adr/0009-cli-contract.md)).
- Alcarin as the only encoding, with marks emitted outward ([ADR-0003](../../adr/0003-alcarin-encoding-and-mark-order.md)).
- The vowel and identity rules ([ADR-0004](../../adr/0004-vowel-marks-and-declared-identities.md)), the weak forms ([ADR-0005](../../adr/0005-weak-forms-for-to-and-for.md)) and punctuation ([ADR-0006](../../adr/0006-punctuation-mapping.md)).
- The corpus, its tests and the review sheet ([ADR-0007](../../adr/0007-corpus-as-test-suite.md)).
- Python 3.14 toolchain and CI ([ADR-0008](../../adr/0008-toolchain-and-ci.md)); scripted PDFs ([ADR-0010](../../adr/0010-pdf-build-and-committed-pdfs.md)).
- README, language guide and philosophy brought in line with the spec.

## Definition of Done

- Alex has reviewed every ADR marked **Unreviewed** and each provisional rule (W-04, L-09, L-10,
  U-02 to U-05) is either ADOPTED or changed.
- `npm test` passes on Python 3.14 and in CI.
- The PDFs match their Markdown.
- `dev/refactor` is merged into `main`.
