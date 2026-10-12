---
name: documentation
description: shavian2tengwar's additions to the project-docs workflow - spec/ as the authority, rule IDs, ADR triggers, and the ADR and spec statuses this repo uses. Use for every task, together with the user-level project-docs skill.
---

# Documentation Skill (shavian2tengwar)

The general workflow is Alex's user-level **`project-docs`** skill (`~/.claude/skills/project-docs/`):
numbered projects with `README.md`, `TASKS.md` and an append-only `LOG.md`; Nygard ADRs; the roadmap;
the untracked `.wip/`. Load it first. This file adds what is specific to this repo, and wins where the
two differ (ADR-0013).

If `project-docs` is not available (another agent, another machine), the essentials are:

- Every piece of work gets `docs/projects/NNNN-title/` (README, TASKS, LOG) and a line in
  `docs/ROADMAP.md`. A one-commit fix can be a dated entry in an open project's `LOG.md` instead.
- `LOG.md` is append-only and written as you go: dated entries with context and decisions, the exact
  commands and their output, and an **LLM Session Summary**. Say what was not verified.
- The pull request closes the project: its last commits set the README to `Complete (PR #N)`, move the
  project to **Done**, and write the final LOG summary. Never merge it yourself.
- Scratch goes in the project's `.wip/` (git-ignored); build output goes in `.tmp/`.

## Layout

```text
docs/
  adr/                  # ADRs; README.md has the legend, template and index
  projects/NNNN-title/  # README.md, TASKS.md, LOG.md, .wip/
  ROADMAP.md
  language-guide.md     # reader's guide to the glyphs (+ .pdf)
  philosophy.md         # why the mode departs from community norms (+ .pdf)
spec/                   # the rules: the authority on what the engine does, not history
```

`spec/` is where rules live. `docs/` is where the reasons and the history live. Never put a rule only
in an ADR, and never put change history in the spec.

## Statuses

| Thing | Implemented in the PR | On trial (a spike) or planned | Undecided |
|---|---|---|---|
| ADR | `Active` (this repo's word for Accepted) | `Proposed` | - |
| Spec rule | `ADOPTED` | `PROVISIONAL` | `OPEN` |

- Write an ADR as `Active`, and its rules as `ADOPTED`, in the PR that implements them. Merging the PR
  accepts them. There is no flip commit after approval.
- `Proposed` / `PROVISIONAL` are for spike work and roadmap plans. A `PROVISIONAL` rule is still
  implemented and tested (`tests/test_coverage.py`); it is just expected to be revisited. The PR that
  settles it sets it to `ADOPTED` and its ADR to `Active`.
- Never promote a `Proposed` ADR or a `PROVISIONAL` rule on your own judgment. Alex decides.

## ADRs here

Use the template in `docs/adr/README.md`, and add each ADR to its index.

- **Review:** `Accepted by merging PR #N`, plus the decisions Alex made along the way, with dates.
- **Revert:** `the squash commit of PR #N`, and the spec rows and corpus rows that must go with it.
  PRs are squash-merged, so branch commit hashes are not on `main`; don't cite them as the revert.

Write an ADR for:

- adding, changing or removing a rule in `spec/` (a new mark, a new identity, a punctuation choice);
- adding an encoding or a font;
- changing the package layout, the toolchain, CI, the CLI contract, or how generated files are built.

Not for: bug fixes where the engine disagreed with the spec (the spec already decided), or a new
corpus row for an existing rule.

Cite ADRs as `ADR-NNNN`. Never write `D-NN` for a decision: `D-01` to `D-05` are spec rule IDs (the
diphthongs). Numbers are never reused; a replaced ADR is marked `Superseded by ADR-NNNN`.
