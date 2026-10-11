# 0002 — Documentation and Repository Layout

> **Status:** Complete
> **Created:** 2026-10-11

## Objective

Give the repository an `AGENTS.md`, a `docs/` section for persistent change history (following the
pattern in Alex's alexregan.com repository), and review whether the layout is right.

## Scope & Deliverables

- `docs/adr/` with an index, `docs/projects/`, `docs/ROADMAP.md` ([ADR-0001](../../adr/0001-documentation-and-change-history.md)).
- `DECISIONS.md` consolidated by subject into ADR-0002 to ADR-0010, then removed.
- `spec/mode.md` section 11 (old engine history) moved into project 0001's log.
- `language-guide.md`, `philosophy.md` and their PDFs moved into `docs/`; every reference updated.
- `AGENTS.md`, `CLAUDE.md` (imports it), and the `documentation` skill adapted from alexregan.com.
- Project 0001 bootstrapped after the fact for the engine rewrite.

## Out of scope

- Moving `s2t/`, `spec/`, `corpus/`, `tools/` or `tests/`. They are well placed, and tests and tools
  depend on their paths.
- Rebuilding the PDFs (Alex does this; see ADR-0010).

## Definition of Done

- `npm test` passes.
- No tracked file links to a moved or deleted path.
- `docs/ROADMAP.md` lists both projects.
