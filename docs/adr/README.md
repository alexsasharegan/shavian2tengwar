# Architecture Decision Records

> Why shavian2tengwar is built the way it is. The rules themselves live in [`spec/`](../../spec); an ADR records why a rule or structure was chosen, and how to back it out.

## Status Legend

| Status | Meaning |
|--------|---------|
| **Proposed** | In an open pull request, waiting for Alex's approval. Never on `main` |
| **Active** | Current, effective decision |
| **Superseded** | Replaced by a later ADR (say which) |
| **Deprecated** | No longer recommended for new work |

## Pattern

```markdown
# ADR-NNNN: Title

**Status:** Proposed | Active | Superseded by ADR-NNNN | Deprecated
**Date:** YYYY-MM-DD
**Affected:** files and spec rules it touches
**Origin:** where it came from (e.g. DECISIONS.md D-12, or a project number)
**Review:** Approved by merging PR #N | Requested by Alex
**Revert:** commits that back it out, and what else must go with them

## Context

What is the issue? What are the constraints?

## Decision

What was decided, and the alternatives considered.

## Consequences

What follows, good and bad. Known risks and things not verified.
```

**The pull request is the approval gate** (ADR-0001). Write new ADRs as `Proposed`. When Alex approves the PR, a final commit sets them to `Active` and records the PR in **Review**; merging is the approval.

Number ADRs sequentially and never reuse a number. Cite them as `ADR-NNNN`, never `D-NN`, which is a spec rule ID (the diphthongs).

## ADR Index

| Ref | Title | Status | Date | Origin |
|-----|-------|--------|------|--------|
| [ADR-0001](./0001-documentation-and-change-history.md) | Documentation and Change History | Active | 2026-10-11 | replaces DECISIONS.md |
| [ADR-0002](./0002-spec-first-engine-and-package-layout.md) | Spec-First Engine and Package Layout | Active | 2026-10-11 | D-05, D-10 |
| [ADR-0003](./0003-alcarin-encoding-and-mark-order.md) | Alcarin Encoding and Mark Order | Active | 2026-10-11 | D-05, D-14 |
| [ADR-0004](./0004-vowel-marks-and-declared-identities.md) | Vowel Marks and Declared Identities | Active | 2026-10-11 | D-04, D-12 |
| [ADR-0005](./0005-weak-forms-for-to-and-for.md) | Weak Forms for *to* and *for* | Active | 2026-10-11 | D-01, D-09 |
| [ADR-0006](./0006-punctuation-mapping.md) | Punctuation Mapping | Active | 2026-10-11 | D-02, D-03 |
| [ADR-0007](./0007-corpus-as-test-suite.md) | The Corpus Is the Test Suite | Active | 2026-10-11 | D-06, D-07, D-08, D-17, D-19 |
| [ADR-0008](./0008-toolchain-and-ci.md) | Toolchain and CI | Active | 2026-10-11 | D-15, D-16, D-20 |
| [ADR-0009](./0009-cli-contract.md) | CLI Contract | Active | 2026-10-11 | D-18 |
| [ADR-0010](./0010-pdf-build-and-committed-pdfs.md) | PDF Build and Committed PDFs | Active | 2026-10-11 | D-10, D-13, D-20, D-21 |
| [ADR-0011](./0011-second-encoding-scope-and-gate.md) | Second Encoding: Scope and Acceptance Gate | Active | 2026-10-11 | project 0003 |
| [ADR-0012](./0012-encoding-contract.md) | The Encoding Contract | Active | 2026-10-11 | project 0003 |

`DECISIONS.md` D-11 (commit author) is recorded in [project 0001's log](../projects/0001-engine-rewrite/LOG.md), not as an ADR.
