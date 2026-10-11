# Execution Log: Engine Rewrite

> This log was reconstructed on 2026-10-11 from `git log d729c2c..bd4e50d`, `DECISIONS.md` and the
> audit notes, when project tracking was introduced (project 0002). Entries after that are written
> as the work happens.

## 2026-10-11 — Engine rewritten to the spec (overnight, unreviewed)

### Context & Decisions

- Starting point: `d729c2c` ("adds IPA to mode; adds alcarin encoding"), Alex's last commit before the
  rewrite. The spec `spec/mode.md` already existed; the code did not follow it.
- Claude rewrote the engine as `s2t/` against the spec, replaced the JSON test manifests with the
  Markdown corpus, and recorded every decision Alex had not reviewed in `DECISIONS.md` with revert
  pointers. Those decisions are now ADR-0002 to ADR-0010.
- Decisions Alex had already approved before the rewrite (vowel inventory, long carrier, rómen-only R,
  diphthong order, nasal and gemination bars, K-01 mark order, silmë/essë flip, the three shorthands,
  breve for schwa) are in `spec/mode.md` and have no ADR.

### What changed from the old engine

Moved here from `spec/mode.md` section 11, for anyone reading old commits:

- CSUR output and `--csur` were dropped.
- FLEECE, PALM, THOUGHT and GOOSE became forced carriers (V-21 to V-24).
- STRUT uses `E054`; the doubled curl and the double acute no longer appear.
- The r-rule and `{oore}` were removed; the R-vowels are ligature expansions (spec section 8).
- The nuquerna trigger list gained the breve and grave (S-02).
- Mark order follows K-01 (vowel, then nasal bar, then gemination bar).
- 𐑾 is 𐑦𐑩 (L-08); whole-word 𐑑 and 𐑓 are weak forms (L-09, L-10).
- `test_collisions.py` became `tests/test_identities.py`, which allows only the declared identities.
- All punctuation in U-01 to U-05 is mapped.

### Commands & Operations Executed

```text
db486b7 Add glyph IR and Alcarin encoding table
c9f0f33 Add phonemic mode engine implementing spec/mode.md
6d1e271 Switch the CLI to the s2t engine and drop CSUR
f774302 Add lossless test: only declared identities may collide
fe2ee13 Add the corpus and its test harness
6ba78b7 Write the Shavian word signs for "to" and "for" as weak forms
0c27b54 Map ! ? parentheses and quotation marks (U-05)
b5a27f3 Add rule-coverage test
2f2dfd7 Add the corpus review sheet
fe59b74 Retire the legacy test manifests and runner
ed529d8 package.json: describe Alcarin output and wire up the test script
80aa868 Rewrite README for the s2t engine and spec
4436d55 spec: correct the to/for history and retire the engine-changes list
510c6f7 language-guide: regenerate the tehta table and Part 3 from the engine
ae5db0f philosophy: update deviations to the current spec
ec5bc28 Add DECISIONS.md: unreviewed decisions with revert pointers
```

### Commit authorship

The rewrite's commits are authored by "Claude <noreply@anthropic.com>" with attribution trailers, not
under Alex's identity, so it is clear at a glance which commits need review. Alex's earlier commits
were not touched. To re-author them as Alex (on a machine where a rebase can delete files):

```bash
git rebase -r d729c2c --exec 'git commit --amend --no-edit --reset-author'
```

Commit `6ba78b7`'s message says the old bare *to*/*for* letters were "an accident of fall-through".
That is wrong (the guide documented them as deliberate), but rewording it needed a rebase that could
not delete files in that environment, so history was left alone. ADR-0005 has the accurate account.

### LLM Session Summary

- **Thread purpose:** Rewrite the engine to the spec without Alex present.
- **Key findings / Blockers resolved:** The old guide contradicted the spec in several places; the
  old tests tested CSUR output the engine no longer produced.
- **Context state for next thread:** Engine, corpus and docs agree. Decisions await review.

## 2026-10-11 — Review fixes: TRAP, mark order, PDF build

### Context & Decisions

- Alex approved TRAP sharing PALM's triple dot ([ADR-0004](../../adr/0004-vowel-marks-and-declared-identities.md)).
  All 111,214 ReadLex entries were scanned for 𐑨 before 𐑘, 𐑢 or 𐑿 to justify I-04 and I-05.
- Alex saw the nasal bar stacked above the vowel mark; the encoding now emits marks outward
  ([ADR-0003](../../adr/0003-alcarin-encoding-and-mark-order.md)).
- The PDF build was scripted ([ADR-0010](../../adr/0010-pdf-build-and-committed-pdfs.md)). It was
  tested only in the cloud, without Bernie Sans Beta; Alex rebuilt the PDFs locally (`a106a6e`).

### Commands & Operations Executed

```text
033ddab s2t: use builtin generics and collections.abc (Ruff UP006, UP035)
ca09457 TRAP shares PALM's triple dot; retire the inverted dots (E056)
dac10fb chmod +x shavian2tengwar.py                       (Alex)
fdc65e9 Add a scripted PDF build (tools/build_pdfs.py, npm run pdf)
ef39b68 corpus: add a README and keep it out of the table parser
5eb9596 Alcarin: emit marks outward from the base so the nasal bar sits under the vowel mark
a106a6e gen docs                                         (Alex)
```

### LLM Session Summary

- **Thread purpose:** Act on Alex's first review.
- **Key findings / Blockers resolved:** The spec's claim that mark order did not matter was never
  tested with two marks above. Corrected, and pinned by a test.
- **Context state for next thread:** Ready for a full audit.

## 2026-10-11 — Audit and hardening

### Context & Decisions

- An audit ran the suite under Python 3.14.6 with `-W error -X dev`, read all the Python by hand and
  checked links, hashes and spec-vs-engine tables. It found: `npm test` failing because the committed
  review sheet held a local font path; a placeholder `LICENSE` holder; the CLI garbling non-UTF-8
  input silently; `.gitignore` hiding dotfiles; no declared Python version; untested CLI and spec
  tables; documentation drift; no CI. The audit notes stayed in the untracked `.tmp/`.
- Each finding was fixed in its own commit ([ADR-0007](../../adr/0007-corpus-as-test-suite.md),
  [ADR-0008](../../adr/0008-toolchain-and-ci.md), [ADR-0009](../../adr/0009-cli-contract.md)).
- Ruff and Prettier could not be installed in that environment and have never been run.
- Alex's shell `python3` was Homebrew 3.9.25; the package and tests now stop with a one-line message
  on anything below 3.14.

### Commands & Operations Executed

```text
b8b84a0 Make the review sheet independent of local font paths
c7f13b4 Fix LICENSE holder, narrow .gitignore, track .prettierrc, tidy package.json
bd91cdb Declare Python 3.14 as the floor and adopt its syntax
e8ca735 Harden the command line
4e74f64 Move the corpus parser from tests/ to tools/
d7b8979 Test the CLI, the stream layer and the literal round trip
324d77d Test the engine's tables against spec/mode.md
6ecdd3e Run the tests in CI
30d6156 Fix documentation drift found in the audit
14a1c7b Add the corpus review sheet to the PDF pipeline
dc4c704 Stop with a clear message on Python older than 3.14
0a14dce Install the PDF tools into a virtualenv
bd4e50d doc gen                                          (Alex: built and committed corpus/review.pdf)
```

### LLM Session Summary

- **Thread purpose:** Audit the repository and fix what it found.
- **Key findings / Blockers resolved:** All audit findings are fixed except running ruff and Prettier.
- **Context state for next thread:** 62 tests pass on Python 3.14.8. Remaining work is review, ruff,
  and the merge; see `TASKS.md` Phases 3 and 4.

## 2026-10-11 — Merge readiness check for PR #1

### Context & Decisions

- PR #1 (`dev/refactor` → `main`, 40 commits) is mergeable with state `clean`, and the `unittest`
  check passed on `3a135c6`. Alex committed project 0002 and rebuilt the PDFs in `3a135c6`.
- Ruff ran for the first time (0.17.0, installed into `.venv`). `ruff check` reported only UP036 on
  the two Python-version guards in `s2t/__init__.py` and `tests/__init__.py`. Those guards are
  deliberate (`dc4c704`): ruff assumes `requires-python` is enforced, but this repo is run in place,
  not installed, so nothing else stops an older Python. Marked `# noqa: UP036`. `ruff check` is now clean.
- Not adopted yet, pending Alex: `ruff format --check` would reformat 11 Python files, and
  `prettier --check` flags 24 files (mostly Markdown tables not column-aligned, plus the CI YAML and
  `package-lock.json`). Both are cosmetic.

### Commands & Operations Executed

```bash
.venv/bin/pip install -q ruff
.venv/bin/ruff check .            # 2 x UP036 -> noqa -> "All checks passed!"
.venv/bin/ruff format --check .   # 11 files would be reformatted
npm ci && npx prettier --check "**/*.{md,json,yml}"   # 24 files
python3 -m unittest discover -s tests -t .           # OK
```

### LLM Session Summary

- **Thread purpose:** Decide whether PR #1 can merge, and close what can be closed.
- **Key findings / Blockers resolved:** Nothing blocks the merge. Lint is clean.
- **Context state for next thread:** Open: Alex's review of the provisional rules and unreviewed
  ADRs, a CI/formatting decision, then the merge.

## 2026-10-11 — Formatting, lint in CI, and approval through PR #1

### Context & Decisions

- Alex wants all Python formatted by the language's standard formatter, churn accepted. `ruff format`
  (Black-compatible, already configured) was run over everything in one mechanical commit, listed in
  `.git-blame-ignore-revs`. Its output is accepted as is; the hand-aligned consonant table in
  `s2t/mode.py` is now one entry per line.
- ruff is pinned in `pyproject.toml` (`[dependency-groups] dev`, `ruff==0.17.0`), with `npm run
  setup:dev`, `fmt` and `lint`. A `lint` CI job runs `ruff check` and `ruff format --check`.
  ADR-0008 updated.
- Alex uses the pull request as the gate from proposed to approved, and said everything in this PR
  follows that. So every ADR is now Active with **Review:** "Approved by merging PR #1", and W-04,
  L-09, L-10 and U-02 to U-05 are ADOPTED. Spec section 12 has no open questions. The rule itself is
  in ADR-0001 and the ADR index.
- Re-authoring Claude's commits was not done: it would change every hash the ADRs cite.
- `docs/philosophy.md` dropped the word "provisional", so `docs/philosophy.pdf` is stale again.
- An auto-mode classifier blocked the matching edits to `AGENTS.md` and the documentation skill
  (agent instruction files). They wait for Alex's go-ahead.

### Commands & Operations Executed

```bash
.venv/bin/ruff format .                    # 11 files reformatted -> 1a43c0c
.venv/bin/pip install -q --group dev
npm run lint                               # All checks passed! / 54 files already formatted -> 6886431
npm test                                   # OK
npm run corpus                             # review.html unchanged
```

### LLM Session Summary

- **Thread purpose:** Format the Python, enforce lint in CI, and approve the PR's proposals.
- **Key findings / Blockers resolved:** Nothing blocks the merge.
- **Context state for next thread:** Merge PR #1 with a merge commit, then mark the project Complete
  and move it to Done in the roadmap. Rebuild `docs/philosophy.pdf`.

## 2026-10-11 — Merged

### Context & Decisions

- Alex rebuilt the PDFs (`5c08c26`) and merged PR #1 with a merge commit, `193cca5`, so the branch
  hashes cited by the ADRs survive on `main`. `dev/refactor` was deleted.
- The regenerated `corpus/review.pdf` was compared with the copy Alex had already shared: all 21
  pages render identically and the extracted text matches; only the PDF creation date differs. It
  did not need resharing.

### Commands & Operations Executed

```bash
pdftoppm -r 60 -png <shared copy> old/p && pdftoppm -r 60 -png corpus/review.pdf new/p
# md5 of every page image: identical. pdftotext -layout of both: identical.
gh pr view 1 --json state,mergeCommit    # MERGED 193cca5
```

### LLM Session Summary

- **Thread purpose:** Close the project after the merge.
- **Key findings / Blockers resolved:** None outstanding.
- **Context state for next thread:** Complete. Moved to Done in the roadmap.
