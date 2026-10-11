---
name: documentation
description: Manage shavian2tengwar's project documentation and change history - numbered projects (README/TASKS/LOG), Nygard ADRs, the roadmap and the untracked .wip/ scratchpad. Use for every task: bootstrapping work, logging execution in LOG.md, and recording decisions.
---

# Documentation Skill

## Directory Structure

```text
docs/
  adr/                  # Architecture Decision Records
    README.md           # Index of all ADRs, status legend and template
    NNNN-title.md       # One ADR (zero-padded 4-digit, e.g. 0004-vowel-marks-and-declared-identities.md)
  projects/             # One folder per piece of work (git-tracked)
    NNNN-title/
      README.md         # Objective, Scope & Deliverables, Definition of Done (MANDATORY)
      TASKS.md          # Checklist (MANDATORY)
      LOG.md            # Append-only execution journal (MANDATORY)
      .wip/             # UNTRACKED scratchpad
  ROADMAP.md            # Now / Next / Done
  language-guide.md     # Reader's guide to the glyphs (+ .pdf)
  philosophy.md         # Why the mode departs from community norms (+ .pdf)
spec/                   # The rules. NOT history: the authority on what the engine does.
```

`spec/` is where rules live. `docs/` is where the reasons and the history live. Never put a rule only
in an ADR, and never put change history in the spec.

---

## Project Lifecycle

### Phase 1: Bootstrapping

When handed a task, feature, fix or proposal:

1. Create `docs/projects/NNNN-title/` with the next free 4-digit number.
2. Write `README.md`: status, created date, objective, scope & deliverables, Definition of Done.
3. Write `TASKS.md`: a `- [ ]` checklist, grouped in phases.
4. Write `LOG.md` with the header `# Execution Log: <Project Title>` and a first dated entry.
5. Create `.wip/` for scratch notes (git ignores it).
6. Add the project to **Now** or **Next** in `docs/ROADMAP.md`.

A small fix that fits in one commit may be logged as a dated entry in the most relevant open project's
`LOG.md` instead of a new project. Say which you chose.

### Phase 2: Execution and logging

- Tick items in `TASKS.md` as they are done (`- [x]`), with the commit hash when there is one.
- Append to `LOG.md` as you go, not at the end: every significant command, finding, decision and
  dead end.

### Phase 3: Completion

- Set the README status to `Complete`.
- Append a final **LLM Session Summary** to `LOG.md`.
- Move the project to **Done** in `docs/ROADMAP.md`.

---

## LOG.md

`LOG.md` is the audit trail and the bridge between sessions.

````markdown
## YYYY-MM-DD — <Milestone / Operation Title>

### Context & Decisions

- What was being addressed, and what was decided.

### Commands & Operations Executed

```bash
# exact commands, and the commits they produced
```

### LLM Session Summary

- **Thread purpose:** <goal of this session>
- **Key findings / Blockers resolved:** <technical takeaways>
- **Context state for next thread:** <where things stand, what is next>
````

- **Append only.** Add new dated entries; never edit or delete earlier ones. Correct a mistake with a
  new entry that says what was wrong.
- **Concrete.** Real commands, real output, real commit hashes.
- **Say what was not verified** (a tool that could not run, a font that was missing).

---

## ADRs

Nygard-style, in `docs/adr/NNNN-title.md`, using the template in `docs/adr/README.md`. Add every new
ADR to the index there.

Beyond Context / Decision / Consequences, each ADR has:

- **Review:** how it was approved: "Approved by merging PR #N", or "Requested by Alex".
- **Revert:** the commits that back it out, and what else (spec rows, corpus rows) must go with them.

### The pull request is the approval gate

- Write every new ADR as `Proposed`, and every new or changed spec rule as `PROVISIONAL`.
- When Alex says the PR is approved, add a final commit that sets them to `Active` / `ADOPTED`,
  fills in **Review**, updates the ADR index and the project docs, and closes the project.
  Merging the PR is the approval. `main` holds no `Proposed` ADR and no `PROVISIONAL` rule.
- Merge with a merge commit, never squash or rebase: ADRs and logs cite the branch's commit hashes.

### When to write an ADR

- Adding, changing or removing a rule in `spec/` (a new mark, a new identity, a punctuation choice).
- Adding an encoding or a font.
- Changing the package layout, the toolchain, CI, the CLI contract, or how generated files are built.

### When not to

- Bug fixes where the engine disagreed with the spec (the spec already decided).
- A new corpus row for an existing rule.

### Numbering

Cite ADRs as `ADR-NNNN`. Never write `D-NN` for a decision: `D-01` to `D-05` are spec rule IDs (the
diphthongs). Numbers are never reused; a replaced ADR is marked `Superseded by ADR-NNNN`.

---

## `.wip/`

- Scratch notes, raw output and drafts live in `docs/projects/NNNN-title/.wip/`.
- `.wip/` is git-ignored. Promote anything worth keeping into `LOG.md`, an ADR, or `docs/`.
- `.tmp/` at the root is for generated build output (`npm run corpus:view`), not notes.
