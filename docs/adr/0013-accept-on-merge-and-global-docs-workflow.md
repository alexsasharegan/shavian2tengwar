# ADR-0013: Accept on Merge, Squash Merges, and the Global Docs Workflow

**Status:** Active
**Date:** 2026-10-12
**Affected:** AGENTS.md, .agents/skills/documentation/SKILL.md, docs/adr/README.md, spec/mode.md §0
and §12, ADR-0001
**Origin:** project 0004 (Alex, 2026-10-12)
**Review:** Accepted by merging PR #5. Alex decided the rules on 2026-10-12: squash merges are
preferred; ADRs are drafted as accepted when the work implements them; Proposed is for spikes and
roadmap plans.
**Revert:** the squash commit of PR #5. The user-level `project-docs` skill lives outside the repo and
is not reverted by it.

## Context

ADR-0001 made the pull request the approval gate this way: a PR's decisions were `Proposed` (its rules
`PROVISIONAL`) while it was open, and only after Alex approved it did a last commit set them to `Active`
and `ADOPTED`. It also required merge commits, because ADRs cited branch commit hashes.

In practice both projects that went through it needed a follow-up PR after the merge: #2 to close
project 0001, and #4 to close project 0003 and flip its statuses, because #3 was merged before the
approval commit. So `main` briefly held proposed decisions. PR #3 and #4 were squash-merged, so
the branch hashes that ADR-0011 and ADR-0012 cited were not on `main`.

Alex wants the same documentation workflow in every repository, not just this one.

## Decision

- **Accept on merge.** An ADR is written as `Active`, and its rules as `ADOPTED`, in the PR that
  implements them. Review happens in the PR; merging it accepts them. There is no flip commit.
- **Proposed is for work not yet settled.** `Proposed` ADRs and `PROVISIONAL` rules are for spikes and
  roadmap plans, and may be merged that way. A `PROVISIONAL` rule is still implemented and must still
  fire in the corpus. The PR that settles it promotes it.
- **The PR closes its project.** Its last commits set the project README to `Complete (PR #N)`, move it
  to **Done** in the roadmap and write the final LOG summary.
- **Squash merges are preferred.** ADRs cite the PR, and **Revert** names the PR's squash commit.
- **The general workflow is a user-level skill**, `project-docs` in `~/.claude/skills/`, loaded through
  `~/.claude/CLAUDE.md` in any repo with `docs/projects/` or `docs/adr/`. This repo's
  `.agents/skills/documentation/` keeps only what is specific here (spec authority, rule IDs, ADR
  triggers, status words) and a short summary for agents that cannot see the user-level skill.
- This repo keeps `Active` as its word for an accepted ADR.

Alternatives considered:

- **Keep the flip commit, with merge commits.** Rejected: it twice needed a follow-up PR, and the
  squash merges Alex prefers break the hash citations it relied on.
- **Vendor the whole skill into every repo.** Rejected: copies drift. A short summary is kept here
  only so that other agents are not left without it.

## Consequences

- This supersedes ADR-0001's approval-gate and merge-commit bullets. The rest of ADR-0001 stands.
- Fewer PRs and no window where `main` holds a decision waiting for a flip.
- A PR that is closed unmerged accepted nothing; its ADR numbers are not reused.
- ADRs written before this one still cite branch hashes (ADR-0003) or squash commits (ADR-0011,
  ADR-0012). Both remain valid.
- The user-level skill is outside version control here. It is Alex's to keep or put in a repo of its
  own.
