# ADR-0008: Toolchain and CI

**Status:** Active
**Date:** 2026-10-11
**Affected:** pyproject.toml, .python-version, package.json, .prettierrc, .gitignore, LICENSE, .github/workflows/test.yml, tests/
**Origin:** DECISIONS.md D-15, D-16, D-20 (tests and CI)
**Review:** Python 3.14 requested by Alex; the rest unreviewed
**Revert:** Python floor `bd91cdb`; housekeeping `c7f13b4`; tests `d7b8979`, `324d77d`; CI `6ecdd3e`; formatting `1a43c0c` and the "lint and format-check in CI" commit

## Context

The README claimed Python 3.10, `build_pdfs.py` said 3.9, and Alex had moved to 3.14. There was no
`pyproject.toml`, no CI, and no tests for the CLI, the stream layer, or the spec's tables.
`.gitignore` ignored every dotfile (`.*`), which hid `.prettierrc` and would have hidden `.github/`.

## Decision

- **Python 3.14 is the floor**, standard library only. `pyproject.toml` has `requires-python = ">=3.14"`
  and no `[build-system]`: the repo is run in place, not installed. `.python-version` pins `3.14`.
  The code uses 3.14 freely: lazy annotations, `X | None`, `type` aliases, a slotted frozen `Cell`.
  `s2t/__init__.py` and `tests/__init__.py` stop with a one-line message on older Pythons.
- **Ruff is the Python formatter and linter** (target py314, line length 120, rules E4, E7, E9, F and UP).
  `ruff format` is the canonical formatter: it is Black-compatible, so the code reads like any other
  formatted Python, and one tool does both jobs. Its output is accepted as is, with no `# fmt: skip`
  for hand-aligned tables. Ruff is pinned in `pyproject.toml` under `[dependency-groups] dev`
  (`npm run setup:dev`, `npm run fmt`, `npm run lint`). Pure reformatting commits are listed in
  `.git-blame-ignore-revs`.
- **npm is the task runner** (`npm test`, `npm run corpus`, `npm run pdf`), and Prettier is its only
  dependency (`.prettierrc`: tabs, width 120). The PDF tools' Python dependencies live in
  `tools/requirements-docs.txt`, installed into `.venv` by `npm run setup:docs`.
- **Tests cover** the CLI, the stream layer, the literal round trip, and the spec's consonant,
  ligature, weak-form, word-sign and punctuation tables (`tests/test_spec_tables.py`).
- **GitHub Actions** runs the unittest suite, `ruff check` and `ruff format --check` on Python 3.14
  on every push and pull request.
- **Housekeeping:** `LICENSE` names Alex Regan; `.gitignore` lists what it ignores; `package.json`
  lost unused fields and is tab-indented.

**Alternatives.** Keep 3.10 compatibility. That costs the `type` aliases and slots, and buys nothing
for a repository only its author runs. Black plus a separate linter, instead of ruff for both.

## Consequences

- Homebrew's `python3` on macOS may be older; the README says how to get 3.14.
- The formatter breaks hand-aligned tables (the consonant pairs in `s2t/mode.py`) into one entry per
  line. Accepted: the spec's tables are the readable version.
- The two Python-version guards carry `# noqa: UP036`, because ruff assumes `requires-python` is
  enforced, and here nothing installs the package.
- Prettier is configured (`.prettierrc`) for Markdown, JSON and YAML but not enforced; 24 files do not
  match it.
