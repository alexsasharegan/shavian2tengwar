# Execution Log: Global Docs Workflow and Accept on Merge

## 2026-10-12: User-level skill and accept on merge

### Context & Decisions

- After project 0003 closed, Alex asked how to use this documentation workflow in every repo instead
  of per repo. Options given: a user-level skill in `~/.claude/skills/`, a pointer in
  `~/.claude/CLAUDE.md`, a thin per-repo layer, and optionally a plugin for other machines.
- Alex's decisions: squash merges are allowed and preferred; ADRs are drafted as accepted when the work
  implements the decision, and merging the PR accepts them; Proposed stages are for spike work and
  roadmap plans.
- The old rule (ADR-0001) had needed a follow-up PR after both earlier projects (#2, #4), and squash
  merges left ADR-0011 and ADR-0012 citing branch hashes that are not on `main`. ADR-0013 replaces it.
- The global skill is named `project-docs`, not `documentation`, so it does not clash with this repo's
  skill of that name. It uses Nygard's `Accepted`, and allows a repo its own word: this repo keeps
  `Active`. It adds `Rejected`, for spikes that decide against something.
- Spec statuses here: `PROVISIONAL` now means implemented and enforced but on trial, since
  `tests/test_coverage.py` requires every provisional rule to fire. No code change was needed.
- This repo's skill keeps a short summary of the general workflow, because agents other than Claude
  Code cannot read `~/.claude/`.
- The user-level files are outside the repo and not versioned. A plugin repo would version them; not
  done, as only one machine is in use.

### Commands & Operations Executed

```bash
git switch -c docs/0004-global-docs-workflow
# wrote ~/.claude/skills/project-docs/{SKILL.md,templates/...} and ~/.claude/CLAUDE.md
npm test && npm run lint
```

```
Ran 72 tests in 0.943s

OK
All checks passed!
68 files already formatted
```

### LLM Session Summary

- **Thread purpose:** make the docs workflow global, and accept decisions on merge.
- **Key findings / Blockers resolved:** the flip commit was the source of the follow-up PRs; with
  accept-on-merge the PR closes its own project.
- **Context state for next thread:** complete when PR #5 merges. Nothing else is in progress.
