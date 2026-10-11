# TASKS — Engine Rewrite

## Phase 1: Engine and spec

- [x] Glyph IR and Alcarin encoding table (`db486b7`)
- [x] Phonemic mode engine implementing `spec/mode.md` (`c9f0f33`)
- [x] Switch the CLI to `s2t` and drop CSUR (`6d1e271`)
- [x] Weak forms for *to* and *for* (`6ba78b7`)
- [x] Punctuation U-05 (`0c27b54`)
- [x] TRAP shares PALM's triple dot; retire `E056` (`ca09457`)
- [x] Emit Alcarin marks outward from the base (`5eb9596`)

## Phase 2: Tests and tooling

- [x] Lossless test: only declared identities collide (`f774302`)
- [x] Corpus and its harness; rule-coverage test (`fe2ee13`, `b5a27f3`)
- [x] Review sheet and its freshness test (`2f2dfd7`, `b8b84a0`)
- [x] Retire the legacy manifests and runner (`fe59b74`)
- [x] Python 3.14 floor and ruff config (`bd91cdb`)
- [x] Harden the CLI (`e8ca735`)
- [x] Tests for the CLI, stream layer and spec tables (`d7b8979`, `324d77d`)
- [x] GitHub Actions (`6ecdd3e`)
- [x] Scripted PDF build, including the corpus sheet (`fdc65e9`, `14a1c7b`, `0a14dce`)
- [x] Build and commit `corpus/review.pdf` on Alex's machine (`bd4e50d`)

## Phase 3: Review (Alex, through PR #1)

- [x] Confirm or change the weak forms W-04, L-09, L-10 ([ADR-0005](../../adr/0005-weak-forms-for-to-and-for.md))
- [x] Confirm or change punctuation U-02 to U-05 ([ADR-0006](../../adr/0006-punctuation-mapping.md))
- [x] Decide on `"` alternation across the stream, and whether `...` needs an ellipsis rule ([ADR-0006](../../adr/0006-punctuation-mapping.md))
- [x] Review the unreviewed ADRs (0002 to 0010): approved by merging PR #1, with the provisional rules ADOPTED
- [ ] ~~Optional: re-author Claude's commits as yourself~~ Not done: it rewrites every hash the ADRs cite

## Phase 4: Finish

- [x] Run ruff once and fix or record what it reports (ruff 0.17.0: two intentional UP036 guards, marked `noqa`)
- [x] `ruff format` the Python (`1a43c0c`) and run `ruff check` and `ruff format --check` in CI (`6886431`)
- [x] Rebuild the PDFs (`npm run pdf`): the guides changed in project 0002 (`3a135c6`)
- [ ] Rebuild `docs/philosophy.pdf` (`npm run pdf`): its text changed with the approval
- [ ] Merge PR #1 (`dev/refactor` into `main`) with a merge commit, not squash or rebase
