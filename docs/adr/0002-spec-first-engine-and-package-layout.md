# ADR-0002: Spec-First Engine and Package Layout

**Status:** Active
**Date:** 2026-10-11
**Affected:** spec/, s2t/, shavian2tengwar.py, README.md, docs/language-guide.md, docs/philosophy.md
**Origin:** DECISIONS.md D-05, D-10
**Review:** Approved by merging PR #1
**Revert:** `c9f0f33` and `6d1e271` together (engine and CLI); docs in `80aa868`, `510c6f7`, `ae5db0f`

## Context

The original converter was one script that went from Shavian straight to font code points, with
both CSUR and Everson tables. Its rules were documented only in `language-guide.md`, which had
drifted from the code in several places (óre, the doubled curl, the double acute, 𐑾, 𐑿).

## Decision

- **Shavian is the input, and only Shavian.** English spelling is never consulted (spec P-01). The
  reasoning is in [`docs/philosophy.md`](../philosophy.md).
- **The spec is the authority.** `spec/mode.md` gives every rule an ID and a status. When the spec and
  the code disagree, the code is wrong. The guides summarise the spec and link to it.
- **Mode and encoding are separate.** The mode turns a Shavian word into font-independent glyph
  names (the IR, Tecendil's literal notation such as `{tinco}[dot-above]`). An encoding turns names
  into a font's code points. The spec splits the same way: `spec/mode.md` and `spec/encodings/*.md`.
- **Package layout.** The engine is the package `s2t/`: `mode.py`, `stream.py`, `glyphs.py` and
  `encodings/`. The CLI stays `shavian2tengwar.py` at the root and is only a front end.
- To change a rule: edit the spec, then the engine, then the corpus (see ADR-0007).

**Alternatives.** Keep one module. Name the package `shavian2tengwar` (clashes with the script name).

## Consequences

- The mode cannot know code points, so a second font is a new file in `s2t/encodings/` plus a table
  in `spec/encodings/`, with no change to the mode.
- Every cell records which rule IDs produced it, which lets the corpus check its citations and powers
  `--inspect`.
- The old behaviour this replaced is listed in project 0001's log
  ([`docs/projects/0001-engine-rewrite/LOG.md`](../projects/0001-engine-rewrite/LOG.md)).
