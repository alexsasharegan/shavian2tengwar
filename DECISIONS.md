# Decision log

Decisions made while rewriting the engine overnight, **without your review**. Each entry says what was
decided, why, what the alternatives were, and which commit to revert if you disagree. Decisions you
already approved (the vowel inventory, long carrier, rómen-only R, diphthong order, nasal and gemination
bars, K-01 mark order, silmë/essë flip, the three shorthands, breve for schwa) are in `spec/mode.md`
and not repeated here.

Commits are listed in `git log dev/refactor` after `d729c2c`. Reverting a commit alone may leave the
spec, corpus and engine out of step; the "Revert" lines say what else has to go with it.

| # | Decision | Status | Revert |
|---|---|---|---|
| D-01 | Weak forms for 𐑑 *to* and 𐑓 *for* (L-09, L-10) | provisional | `6ba78b7` |
| D-02 | `;` `:` `-` punctuation glyphs (U-02..U-04) | provisional | `0c27b54` for U-05 only; U-02..U-04 are in `c9f0f33` |
| D-03 | `!` `?` parentheses and quotation marks (U-05) | provisional | `0c27b54` |
| D-04 | Declared-identity edge: 𐑱 𐑴 𐑶 next to the same glide letter | adopted | in `0c27b54` and `f774302` |
| D-05 | Package layout `s2t/`, CLI keeps its name | adopted | `c9f0f33`, `6d1e271` |
| D-06 | Corpus format and the tests around it | adopted | `fe2ee13`, `b5a27f3` |
| D-07 | `corpus/review.html` is committed and guarded by a test | adopted | `2f2dfd7` |
| D-08 | Legacy tests and manifests retired | adopted | `fe59b74` |
| D-09 | Replacing the old guide's "Big Five" rows for *to* and *for* | provisional | with D-01, plus `510c6f7` |
| D-10 | Documentation approach (README, guide, philosophy, PDFs) | adopted | `80aa868`, `510c6f7`, `ae5db0f`, `ec5bc28` |
| D-11 | Commit author | adopted | not revertible; see below |
| D-12 | TRAP uses `[triple-dot-above]`; `E056` retired | **approved by you** | `ca09457` |
| D-13 | Scripted PDF build (`tools/build_pdfs.py`) | adopted | `fdc65e9` |
| D-14 | Alcarin emits marks outward from the base (fixes nasal bar stacking) | fix, at your request | `5eb9596` |
| D-15 | Python 3.14 is the floor; ruff configured in `pyproject.toml` | adopted | `bd91cdb` |
| D-16 | LICENSE holder, narrower `.gitignore`, tracked `.prettierrc`, tidy `package.json` | adopted | `c7f13b4` |
| D-17 | The committed review sheet embeds no font path | adopted | `b8b84a0` |
| D-18 | CLI behaviour: UTF-8 I/O, exit codes, closed pipe | adopted | `e8ca735` |
| D-19 | The corpus parser lives in `tools/`, not `tests/` | adopted | `4e74f64` |
| D-20 | Tests for the CLI, streams and spec tables; GitHub Actions; PDFs stay in git | adopted | `d7b8979`, `324d77d`, and the "Run the tests in CI" commit |

---

## D-01. Weak forms for *to* and *for*

**Decided.** A standalone 𐑑 is written as 𐑑𐑩, `{tinco}{telco}[breve]` (L-09). A standalone 𐑓 is written
as 𐑓𐑼, `{formen}{roomen}[breve]` (L-10). No Tengwar shorthand is adopted for either.

**Why.** You said ReadLex treats *to* as ending in a schwa and that Shavian uses the two signs to
separate homophones. So the output should keep *to* apart from *too/two* (𐑑𐑵) and *for* apart from
*four* (𐑓𐑹). Spelling the weak form does that without needing a community precedent. The Tengwar sources
give little: Tecendil's phonemic mode has `{formen}{roomen}` for *for*; its classical mode has
`{tinco}[right-curl-below]` for *to*, which breaks P-04 (no marks below); Aranoss writes *to* in full.

**Alternatives.**
1. Keep the old behaviour: a lone `{tinco}` and a lone `{formen}` (the language guide called these
   "unadorned base" shorthands). Shortest, but it conflicts with the guide's own principle that nothing
   is silent, and it makes *for* read as just "f".
2. Adopt Tecendil's `{formen}{roomen}` for *for* only. Matches DTS 39, but then *for* and *four*
   (𐑓𐑹 = `{formen}{aara}[right-curl]{roomen}`) are distinct anyway. It is the least-surprising option
   if you want to follow Tecendil.
3. Make *to* a ligature-style expansion of 𐑑𐑵 (full vowel). Wrong for a weak form.

**Uncertainty.** *for* is less certain than *to*: /fər/ is the usual weak form, but a reader might expect
the full vowel. Section 12 of the spec still lists this as open.

**Note on history.** The commit message of `6ba78b7` says the old bare letters were an accident of
fall-through. That is imprecise: the language guide documented them as deliberate. `spec/mode.md` section
7 (corrected in `4436d55`) has the accurate account. I tried to reword that commit but the rebase cannot
delete files in this environment, so I left history alone.

**Revert.** `6ba78b7`, and in `spec/mode.md` set W-04, L-09 and L-10 back (the corpus rows citing them
also go; `tests/test_coverage.py` will name any leftovers).

## D-02. Punctuation: `;` `:` `-`

**Decided.**

| Input | Glyph | Code point | Rule |
|---|---|---|---|
| `;` | `{double-section-mark}` | `U+E069` | U-02 |
| `:` | `{triple-pusta}` | `U+E062` | U-03 |
| `-` | `{section-mark}` | `U+E068` | U-04 |

You had no opinion on `;`, so I went by what the glyphs look like and by Aranoss's text, which writes the
semicolon the same way. A semicolon is a pause between a comma and a full stop; the double section mark
reads as a heavier pause than the comma's single dot and is not confused with `:`. The colon takes the
three stacked dots because it introduces something and the stack of dots is the visually closest to the
Latin colon. Alcarin has no hyphen glyph; the section mark (a tilde) is the nearest short horizontal
stroke.

**Alternatives.**
- `;` as `{pusta}` + `{double-pusta}` composed from existing glyphs. Reads as two marks.
- `-` passed through as ASCII. Mixes a Latin glyph into Tengwar text and may fall back to another font.
- `-` as nothing (join the words). Loses compound boundaries.

**Revert.** These rules came in with the engine (`c9f0f33`), so reverting that commit would remove the
engine. Instead edit `PUNCTUATION` in `s2t/stream.py`, then U-02..U-04 in `spec/mode.md` and the
matching rows in `corpus/marks.md`.

## D-03. Punctuation: `!` `?` parentheses and quotes (U-05)

**Decided.**
- `!` is `{exclamation-mark}` (`U+E065`) and `?` is `{question-mark}` (`U+E066`).
- Both `(` and `)` are `{parenthesis-mark}` (`U+E067`). Alcarin has one glyph for both sides, so I did
  not invent a second.
- Curly double quotes are `{left-quotation-mark}` (`U+E06A`) and `{right-quotation-mark}` (`U+E06B`).
  An ASCII `"` alternates open and close, tracked across the whole stream, and resets nowhere.
- Single quotes and apostrophes pass through unchanged, because Shavian apostrophes are rare and a
  single quote is ambiguous with an apostrophe.

**Why.** These are the font's own punctuation glyphs; leaving them unused would send Latin punctuation
into a Tengwar line.

**Risks.** The alternating `"` goes wrong if the text has an odd number of quotes: a stray quote flips
every later one, because the state runs across the whole stream. Square brackets, braces and `/` pass
through. Each `.` maps on its own, so `...` is three `{double-pusta}` marks; there is no ellipsis rule.
Say if you want one.

**Revert.** `0c27b54`. The pass-through behaviour from before returns.

## D-04. Declared-identity edge case

**Decided.** The spec declares 𐑱 = 𐑧𐑘, 𐑴 = 𐑪𐑢 and 𐑶 = 𐑪𐑘 as identical spellings (I-01..I-03). Those
identities do **not** hold when the next letter is the same glide, e.g. 𐑪𐑘𐑘, because the doubled glide is
a geminate and gets the doubler. `tests/test_identities.py` skips that edge, and the spec says so.

**Why.** The alternative is to deny the declared identity everywhere. It is simpler to state an
exception once.

**Revert.** The test change is in `f774302`; the spec note in `0c27b54`.

## D-05. Package layout

**Decided.** The engine is the package `s2t/` (`mode`, `stream`, `glyphs`, `encodings/`). The CLI is still
`shavian2tengwar.py` and is only a front end. The CSUR code and flag were removed (they never matched
Alcarin's layout).

**Why.** The mode must not know code points, and the spec splits mode from encoding, so the code does too.

**Alternatives.** Keep one module; name the package `shavian2tengwar` (clashes with the script).

**Revert.** `c9f0f33` (engine) and `6d1e271` (CLI). They go together.

## D-06. Corpus format

**Decided.** `corpus/*.md` are Markdown tables: `case` (input, expected glyph literal, cited rule IDs),
`same` and `distinct` (pairs that must or must not collide). The tests parse them; the engine fills in
the Glyphs column when I generate them, and I audited each row by hand against the rules. A row fails if
a cited rule does not exist or does not fire. `tests/test_coverage.py` demands every adopted or
provisional rule appear in some row (exempt: P-01..P-05 and R-02, which are constraints, not outputs).

**Why.** The corpus is both documentation and test, so it is readable on GitHub and gives you the pairs to
review without running anything.

**Alternatives.** JSON manifests (the old way), which can't be read well in review.

**Revert.** `fe2ee13` and `b5a27f3`.

## D-07. Committed review sheet

**Decided.** `corpus/review.html` is the whole corpus rendered in Tengwar for you to look at. It is
generated by `tools/render_corpus.py` and committed, and `tests/test_review_sheet.py` fails if it is
stale. It needs the Alcarin font installed to show glyphs.

**Why.** A visual check is the only way to judge a mark that lands wrong, and committing it lets you
open it from a checkout.

**Cost.** A diff in the HTML every time the corpus changes. If that bothers you, drop the file and the
test and generate on demand.

**Revert.** `2f2dfd7`.

## D-08. Legacy tests retired

**Decided.** `test_cases.json`, `test_cases_everson.json`, `test_runner.py` and `test_collisions.py` were
removed. They tested CSUR/Everson output the engine no longer produces; `tests/test_identities.py`
replaces the collisions test with the stricter rule that only declared identities may collide.

**Revert.** `fe59b74`. The restored files will fail against the new engine.

## D-09. The old guide's "Big Five" rows

**Decided.** `language-guide.md` Part 3 listed *to* as a bare Tinco and *for* as a bare Formen. Those rows
are replaced by D-01's weak forms. The stale tables in that part (the letter matrix, the tehta table)
were regenerated from the engine's output as a one-off; there is no script in the repo that keeps
them in sync, so they can drift if the rules change.

**Why.** Part 3 contradicted the spec in several places (óre, doubled curl, double acute, 𐑾, 𐑿).

**Revert.** `510c6f7`; the bare-letter rows return.

## D-10. Documentation

**Decided.** README rewritten; `language-guide.md` (Part 2 text, tehta table, all of Part 3) and `philosophy.md`
(diphthong order, word signs, and new sections on R and on the vowel marks) updated to the spec;
`spec/` is the authority and the guides point to it. I did not regenerate the PDFs, per your standing
instruction; you rebuilt them with `npm run pdf` (`a106a6e`), and they now match the Markdown. The
README previously still said they were older; that sentence is gone. Whoever edits either guide
rebuilds its PDF (D-20).

**Revert.** `80aa868` (README), `510c6f7` (guide), `ae5db0f` (philosophy), `ec5bc28` (this log).

## D-11. Commit author

**Decided.** The commits are authored by "Claude <noreply@anthropic.com>" with the attribution trailers,
not under your identity, so you can tell at a glance which commits to review. The rewrite did not touch
your earlier commits. To re-author them as yourself: `git rebase -r d729c2c --exec 'git commit
--amend --no-edit --reset-author'`. Run this on a machine where the rebase can delete files.

## D-12. TRAP shares PALM's triple dot

**Decided (approved by you, 2026-10-11).** 𐑨 TRAP is `[triple-dot-above]` on a consonant, and 𐑭 PALM stays
`{aara}[triple-dot-above]`. `[reversed-triple-dot-above]` (`U+E056`) is removed from the mode and the
Alcarin table, and listed as reserved.

**Why.** Shavian has no short /ɑ/, so the short slot of the triple dot was empty, and TRAP's separate mark
broke the pattern that a long vowel is its short partner's mark on the long carrier.

**Consequence.** 𐑲 PRICE = 𐑨𐑘 and 𐑬 MOUTH = 𐑨𐑢 become declared identities (I-04, I-05), because a
diphthong is its nucleus plus its glide. I scanned all 111,214 ReadLex entries: only the TrapBath variant of
*Malawian* (32 occurrences by frequency) and a one-off name, *iau*, contain 𐑨 followed by 𐑘, 𐑢 or 𐑿 (𐑿
expands to 𐑘𐑵). You said *Malawian* is fine as it comes out.

**Revert.** `ca09457`. It also reverts I-04 and I-05 and restores `E056`.

## D-13. Scripted PDF build

**Decided.** `tools/build_pdfs.py` builds both PDFs from the Markdown: markdown-it-py to HTML, then Chrome
print-to-PDF through Playwright, Letter size, Courier / Bernie Sans Beta / Alcarin Tengwar as the font
stack. Run it with `npm run pdf`. By default it writes over the PDFs next to the sources.

**Why.** It replaces copy-pasting into Obsidian. Obsidian prints with Chromium too, so the look is close
(the CSS is my approximation of the old output, not Obsidian's theme).

**Not verified.** I could test the pipeline only in the cloud, with Alcarin loaded from a file and without
Bernie Sans Beta, so the Shavian letters came out in a fallback font there. I did not run it over the
committed PDFs. The first run on your machine is the real check on fonts and page breaks.

**Alternatives.** A Node pipeline (the repo already has `package.json`), which I could not install from the
cloud; or `pandoc` plus LaTeX, which handles these fonts badly.

**Revert.** `fdc65e9`. Nothing else depends on it.

## D-14. Mark stacking in the Alcarin encoding

**Decided (your correction).** On the page, top to bottom, a cluster is: vowel mark, nasal bar, base,
gemination bar. The IR keeps that order (K-01). The Alcarin encoding now writes the marks above the
base nearest-first, so the nasalizer's code point comes before the vowel mark's: `{tinco}[dot-above][bar-above]`
is `E000 E050 E044`. Before, it was `E000 E044 E050`, which the font stacks with the bar on top.

**My error.** The spec said a font stacks marks the same way in any order, and AE-03 said stacking was
verified. I had not checked orders with more than one mark above. Both statements are corrected, and
`tests/test_encoding.py` now pins the order. I checked the new order by rendering it in Chromium.

**Revert.** `5eb9596` restores the old order, and the review sheet with it.

## D-15. Python 3.14 is the floor

**Decided.** You moved to Python 3.14, so `pyproject.toml` says `requires-python = ">=3.14"` and
`.python-version` pins `3.14`. The code uses what 3.14 offers: lazy annotations (no
`from __future__ import annotations`), `X | None`, `type` aliases (`Item`, `Letter`, `Trace`), a slotted frozen
`Cell`, and parameterized `list`/`dict`/`tuple`/`frozenset` annotations. `pyproject.toml` also configures ruff
(target py314, line length 120, rules E4/E7/E9/F plus `UP`).

**Not verified.** I could not install ruff, so the ruff settings have never run. I ran the tests on Python
3.14.6 with warnings as errors. The Python I had on your machine is 3.10, which can no longer import the
package, so run `npm test` there yourself. I did not make the tests support 3.10.

**Alternatives.** Keep 3.10 compatibility (what the README said); that costs the `type` aliases and slots
and buys nothing for a repo only you run. `pyproject.toml` has no `[build-system]` and no dependencies: this
is run in place, not installed, and the PDF tools' dependencies stay in `tools/requirements-docs.txt`.

**Revert.** `bd91cdb`.

## D-16. Repository housekeeping

**Decided.** `LICENSE` names "Alex Regan" as holder (your name from your email address; change it if you
want an organization). `.gitignore` no longer ignores every dotfile (`.*`): it lists `.DS_Store`, `.tmp/`,
`__pycache__/` and `node_modules/`, so `.prettierrc` is tracked and a future `.github/` is not hidden.
`package.json` loses the unused `main` and `type` fields, gets `author`, and is indented with tabs to match
`.prettierrc`. I did not run Prettier, so other files may still differ from it.

**Revert.** `c7f13b4`.

## D-17. The review sheet embeds no font path

**Decided.** `npm run corpus` regenerates `corpus/review.html` with no font file, which keeps the committed
sheet identical on every machine and keeps `test_sheet_is_current` passing. It uses the installed "Alcarin
Tengwar" font. If the browser shows boxes, `npm run corpus:view` writes `.tmp/review.html` with the font file
from `package.json` embedded; edit that path for your machine.

**Why.** The committed sheet had your local font path in it, so the freshness test failed everywhere else.
I could not find out why the installed font was not picked up by name on your machine (the family name in
the variable font is "Alcarin Tengwar", which the CSS lists first).

**Revert.** `b8b84a0`.

## D-18. CLI behaviour

**Decided.** The script forces UTF-8 on stdin and stdout, since the output is Private Use code points and
a non-UTF-8 locale used to garble it without any error. `--encoding` is checked by argparse (exit 2).
Invalid UTF-8 input prints a one-line error and exits 1. A closed pipe (`| head`) exits 1 without a
traceback. An empty-string argument is treated as the text, not as "read stdin". `main()` takes `argv` and
returns the exit code.

**Revert.** `e8ca735`.

## D-19. Corpus parser in `tools/`

**Decided.** The corpus table parser moved from `tests/corpus.py` to `tools/corpus.py`, because
`tools/render_corpus.py` imported from `tests/`. `tools/` is now a package.

**Revert.** `4e74f64`.

## D-20. New tests, CI, and committed PDFs

**Decided.** Added tests for the CLI, the stream layer, the literal round trip, and the spec's consonant,
ligature, weak-form, word-sign and punctuation tables (`d7b8979`, `324d77d`). Added a GitHub Actions
workflow that runs the suite on Python 3.14. It does not run ruff, because I could not run it myself to
confirm it passes. The two PDFs stay committed: they are built from the Markdown by hand, the tests do not
check them, and a stale PDF is possible after a guide edit. Say so if you would rather build them in CI or
stop tracking them.

**Revert.** The test commits above; the workflow is the "Run the tests in CI" commit.

---

## Still open

- W-04, L-09, L-10: confirm the weak forms (D-01).
- U-02..U-05: confirm the punctuation (D-02, D-03), or tell me what to change.
- The `"` alternation and ellipsis (D-03).
