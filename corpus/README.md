# The corpus

The corpus is the test data for the engine and the visual reference for the spec. It is a set of Markdown tables, so you can read it on GitHub, edit it by hand, and see every row rendered in Tengwar in [`review.html`](./review.html).

It currently holds 91 cases, 17 identity pairs and 10 distinct pairs.

## What is in it

| File | Holds |
|---|---|
| `consonants.md` | each consonant, nasals, geminates, silmë and essë |
| `vowels.md` | each vowel, the long carrier, diphthongs, R-vowels, orphan vowels, mark order |
| `contrasts.md` | pairs that must stay different (the vowel contrasts) |
| `identities.md` | pairs that are declared to be written the same (ligatures, diphthongs) |
| `word-signs.md` | *the*, *of*, *and*, and the weak forms of *to* and *for* |
| `marks.md` | punctuation |
| `phrases.md` | whole sentences |
| `review.html` | generated; do not edit |

Every `.md` file is read by `tests/corpus.py`. A file only needs to follow the table formats below; the headings and prose can say anything.

## The three table formats

The parser recognises a table by its header row.

**A case.** The Shavian must translate to exactly the Glyphs.

```markdown
| Shavian | English | IPA | Glyphs | Rules |
|---|---|---|---|---|
| 𐑑𐑬𐑯 | town | /taʊn/ | `{tinco}{vala}[triple-dot-above]{nuumen}` | D-02 |
```

The Glyphs column is the Tecendil-style literal, so it can be pasted into tecendil.com. The Rules column lists spec rule IDs separated by spaces.

**A same pair.** Both spellings must give the same glyphs (a declared identity).

```markdown
| A | B | Rules | Note |
|---|---|---|---|
| 𐑱 | 𐑧𐑘 | I-01 | FACE = DRESS + j |
```

**A distinct pair.** Both spellings must give different glyphs. It is the same header as a same pair, but the nearest heading above it must contain the word "Distinct".

## What the tests check

- `tests/test_corpus.py`: every case produces its stated glyphs. Every rule a row cites must exist in `spec/mode.md` and must actually have fired for that input, so a stale citation fails. Same pairs must match, distinct pairs must differ.
- `tests/test_coverage.py`: every adopted or provisional rule in the spec is cited by at least one row. The exceptions are the constraint rules (P-01 to P-05 and R-02), which have no output of their own.
- `tests/test_identities.py`: independent of the corpus, it enumerates short vowel sequences and fails on any two different Shavian spellings that give the same glyphs, unless the spec declares them identical.
- `tests/test_review_sheet.py`: `review.html` must match what `tools/render_corpus.py` would produce now.

Run them all with `npm test`.

## Adding or changing a row

1. Work out the glyphs from the spec first. Writing the expected Glyphs yourself is the point: the test then checks the engine against the rules. If you copy the engine's output into the table, the row can only ever agree with it.
2. To see what the engine produces, run `python3 shavian2tengwar.py --format literal "𐑞𐑬𐑯"`, or `--inspect WORD` for each step and the rules that fired.
3. Add the row to the right file and cite the rules it exercises.
4. Run `npm test`. If `review.html` is stale, run `python3 tools/render_corpus.py` and commit it with the change.

If the engine and the corpus disagree, one of them is wrong. Decide which by reading the rule in `spec/mode.md`, and change the spec first if the rule itself should change.

## The review sheet

`python3 tools/render_corpus.py` writes `review.html`. It shows each row as Tengwar next to its Shavian, English, IPA, glyph names and rules, and it follows the browser's light or dark setting. It uses the Alcarin Tengwar font if it is installed; otherwise pass `--font path/to/AlcarinTengwar-Regular.ttf`. Open it in a browser to check that marks land where they should, which the text tables cannot show.

## How the first version was made

The first version of these tables was generated once, from a throwaway script that held the Shavian, English, IPA and rule columns and took the Glyphs column from the engine. Every row was then checked by hand against the spec. That script is not part of the repository, so from here on the Markdown files are the source of truth and are edited directly.
