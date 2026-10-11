# Execution Log: Documentation and Repository Layout

## 2026-10-11 — Survey and proposal

### Context & Decisions

- Alex asked for an `AGENTS.md`, a review of the repository layout, and a section for persistent
  change history like alexregan.com's `docs/`.
- Findings:
  - The code side (`s2t/`, `spec/`, `corpus/`, `tests/`, `tools/`) is well organised and stays put.
  - History was in four places: `DECISIONS.md`, `spec/mode.md` section 11, the untracked
    `.tmp/audit-2026-10-11.md`, and commit messages.
  - `DECISIONS.md` numbered decisions `D-01` to `D-21`, colliding with the diphthong rules `D-01` to
    `D-05` in the spec.
  - The two guides and their PDFs crowded the root.
- Alex chose: convert `DECISIONS.md` to ADRs, consolidating related decisions; move the guides into
  `docs/`; copy the `documentation` skill, adapted.

### Commands & Operations Executed

```bash
python3 -m unittest discover -s tests -t .   # Ran 62 tests in 0.852s — OK (Python 3.14.8)
```

## 2026-10-11 — Docs tree, ADRs and moves

### Context & Decisions

- The 21 decisions were grouped by subject into nine ADRs (0002 to 0010). D-05 split between the
  engine layout (0002) and dropping CSUR (0003). D-10 split between spec authority (0002) and the
  PDFs (0010). D-20 split between tests and CI (0008) and committed PDFs (0010).
- Each ADR gained **Origin** (the old `D-NN`), **Review** and **Revert** fields, so nothing from
  `DECISIONS.md` was lost. Statuses: `Proposed` for the provisional rules (0005, 0006), `Active` for
  the rest.
- D-11 (commit author) and the "changes made to the old engine" list from spec section 11 went into
  project 0001's log. Section 11 now points there; section numbers are unchanged.
- Project 0001 was bootstrapped after the fact from `git log d729c2c..bd4e50d`, with Alex's review
  items as open tasks.
- `CLAUDE.md` imports `AGENTS.md`, because Claude Code reads `CLAUDE.md`. `.claude/skills/documentation`
  is a symlink to `.agents/skills/documentation`, so Claude Code finds the skill too.
- The untracked `.tmp/` files (the audit and the Nimrodel drafts) were left alone.
- The PDFs were moved, not rebuilt (ADR-0010).

### Commands & Operations Executed

```bash
mkdir -p docs/adr docs/projects .agents/skills/documentation
git mv language-guide.md language-guide.pdf philosophy.md philosophy.pdf docs/
printf '.wip/\n' >> .gitignore
git rm -q DECISIONS.md
printf '@AGENTS.md\n' > CLAUDE.md
ln -s ../../.agents/skills/documentation .claude/skills/documentation
# tools/build_pdfs.py: DEFAULT_DOCS -> docs/language-guide.md, docs/philosophy.md
# docs/language-guide.md: ./spec/mode.md -> ../spec/mode.md
# DECISIONS.md references in spec/mode.md, spec/encodings/alcarin.md and both guides -> ADR links
```

### Verification

```text
python3 -m unittest discover -s tests -t .     OK
relative-link check over 32 Markdown files      0 broken
.venv/bin/python tools/build_pdfs.py --help     OK; both default sources exist
```

### LLM Session Summary

- **Thread purpose:** Add `AGENTS.md`, the `docs/` history section, and tidy the layout.
- **Key findings / Blockers resolved:** `D-NN` decision IDs collided with spec rule IDs; ADR-NNNN
  removes the ambiguity.
- **Context state for next thread:** Complete. The changes are not committed. The PDFs are stale until
  Alex runs `npm run pdf` (a task in project 0001).
