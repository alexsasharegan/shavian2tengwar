# 0004 — Global Docs Workflow and Accept on Merge

> **Status:** Complete (PR #5)
> **Created:** 2026-10-12
> **Branch:** `docs/0004-global-docs-workflow`

## Objective

Make this repo's documentation workflow (projects, append-only logs, ADRs, roadmap) Alex's default in
every repository, and change how decisions are accepted: written as accepted in the PR that implements
them, accepted by merging it.

## Scope & Deliverables

- Outside the repo (not versioned here): the user-level skill `~/.claude/skills/project-docs/` with
  starter templates, and a line in `~/.claude/CLAUDE.md` that loads it in any repo with `docs/projects/`
  or `docs/adr/`.
- ADR-0013, superseding ADR-0001's approval-gate and merge-commit bullets.
- `.agents/skills/documentation/SKILL.md` trimmed to what is specific to this repo, plus a short
  summary for agents that cannot see the user-level skill.
- `AGENTS.md`, `docs/adr/README.md` and `spec/mode.md` §0 and §12 updated to the new statuses.

## Definition of Done

- [x] The user-level skill and `~/.claude/CLAUDE.md` exist
- [x] ADR-0013 written as Active; the repo docs agree with it
- [x] `npm test` and `npm run lint` pass
- [x] README `Complete (PR #5)`, ROADMAP **Done**, final LOG summary
