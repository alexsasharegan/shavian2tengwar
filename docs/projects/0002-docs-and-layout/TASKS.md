# TASKS — Documentation and Repository Layout

## Phase 1: Survey

- [x] Read the code, spec, corpus, tests, tools and `DECISIONS.md`
- [x] Read alexregan.com's `agents.md`, `docs/` and `documentation` skill
- [x] Baseline: `npm test` passes (62 tests, Python 3.14.8)
- [x] Propose layout changes; Alex chose ADR conversion with consolidation, guides into `docs/`, and the skill

## Phase 2: History

- [x] ADR-0001 for the pattern itself
- [x] Consolidate `DECISIONS.md` D-01 to D-21 into ADR-0002 to ADR-0010 by subject; index in `docs/adr/README.md`
- [x] Move D-11 (commit author) and spec section 11 into project 0001's log
- [x] Bootstrap project 0001 (engine rewrite) after the fact
- [x] `docs/ROADMAP.md`
- [x] Remove `DECISIONS.md`; repoint its references in the spec and guides

## Phase 3: Layout and agents

- [x] Move `language-guide.md/.pdf` and `philosophy.md/.pdf` into `docs/`; update `tools/build_pdfs.py` and README
- [x] Ignore `.wip/`
- [x] `AGENTS.md`, `CLAUDE.md`, `.agents/skills/documentation/SKILL.md` (linked from `.claude/skills/`)

## Phase 4: Verify

- [x] `npm test` passes
- [x] No broken relative links in any tracked Markdown file
- [x] `tools/build_pdfs.py` finds both guides at their new paths
- [x] Alex: rebuild the PDFs with `npm run pdf`, since the guides' text changed (`3a135c6`)
