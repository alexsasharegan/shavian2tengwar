# ADR-0001: Documentation and Change History

**Status:** Active
**Date:** 2026-10-11
**Affected:** docs/, AGENTS.md, .agents/skills/documentation/, .gitignore
**Origin:** Replaces `DECISIONS.md`
**Review:** Approved by Alex, 2026-10-11

## Context

Change history was spread across four places: `DECISIONS.md` (21 unreviewed decisions with revert
pointers), section 11 of `spec/mode.md` (old engine behaviour), an untracked audit in `.tmp/`, and
commit messages. `DECISIONS.md` numbered its entries `D-01` to `D-21`, which collides with the
diphthong rules `D-01` to `D-05` in `spec/mode.md`. The two long-form guides and their PDFs sat at
the repository root next to the code.

The same author keeps another repository (alexregan.com) with a `docs/` tree of ADRs, numbered
projects and a roadmap, and wanted the same pattern here.

## Decision

- `docs/` holds the prose and the history:
  - `docs/language-guide.md`, `docs/philosophy.md` and their PDFs (moved from the root).
  - `docs/adr/NNNN-title.md`: Nygard-style ADRs, indexed in `docs/adr/README.md`.
  - `docs/projects/NNNN-title/` with `README.md` (scope, Definition of Done), `TASKS.md` (checklist)
    and `LOG.md` (append-only, dated execution journal). `.wip/` inside a project is untracked scratch.
  - `docs/ROADMAP.md`: Now / Next / Done.
- `DECISIONS.md` is retired. Its entries were consolidated by subject into ADR-0002 to ADR-0010. Each
  ADR keeps the original `D-NN` number under **Origin**, its review state and its revert pointers.
  The commit-author note (old D-11) is process, not architecture, and lives in project 0001's log.
- ADRs carry two fields that `DECISIONS.md` had and plain Nygard ADRs lack:
  **Review** (whether Alex has approved it) and **Revert** (the commits to back it out).
- Decisions are cited as `ADR-NNNN`, never `D-NN`, so they cannot be mistaken for spec rule IDs.
- `spec/` stays the authority on the rules. An ADR records *why* a rule was chosen; the rule itself
  lives in the spec, and the ADR links to it.
- `AGENTS.md` at the root tells agents about this workflow, and `.agents/skills/documentation/`
  carries the full skill. `CLAUDE.md` imports `AGENTS.md`.

## Consequences

- One place to look for why something is the way it is, and one numbering scheme for it.
- Old commit messages and the PDFs built before the move still say `DECISIONS.md` and `D-NN`. The
  **Origin** line in each ADR maps them.
- Links to `language-guide.pdf` and `philosophy.pdf` at the root on GitHub now 404.
- More ceremony per change: each piece of work gets a project folder and a log.
