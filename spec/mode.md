# Phonemic English Tengwar Mode

This document is the font-independent specification of the mode that `shavian2tengwar` implements.
It takes Shavian text as input and produces a sequence of named Tengwar glyphs as output.
It says nothing about code points: `spec/encodings/*.md` maps each glyph name to a font.

Every rule has an ID and a status. Corpus cases in `corpus/` cite rule IDs, and a coverage check
fails if a rule has no case. When this document and the code disagree, the code is wrong.

## 0. Conventions

**Status.** `ADOPTED` is decided and must be enforced. `PROVISIONAL` is the working choice but may
still change. `OPEN` is undecided; the text lists the candidates and current behaviour.

**Glyph names** follow [Tecendil](https://www.tecendil.com/) so that output can be pasted into its
literal-input box.

- `{name}` is a tengwa, carrier, or punctuation glyph.
- `[name]` is a combining mark.
- A **cluster** is one `{base}` followed by its `[marks]`, as in `{tinco}[dot-above]`.

All names below were found in Tecendil's mode files (`modes/*.jsonc`) except those flagged †:

- `{triple-pusta}` and `{section-mark}` are not found. `{double-pusta}` appears once.
- `{the-shorthand}`, `{of-shorthand}` and `{and-shorthand}` are shorthand names, not glyph names.
  The first two are Tecendil's literals. `{and-shorthand}` is expanded in rule W-03.

**Keyword sets** are John Wells' lexical sets (TRAP, PALM, LOT, THOUGHT, STRUT, FOOT, FLEECE,
GOOSE, NURSE, and so on). They name vowels in rules and anchor the corpus.
The base dialect is the rhotic one that Shavian's ReadLex assumes.

## 1. Principles

| ID | Rule | Status |
|---|---|---|
| P-01 | The input is Shavian phonemes. English spelling is never consulted. | ADOPTED |
| P-02 | **Lossless.** Two different Shavian strings give different glyph strings, except the identities declared in section 8. A test enforces this. | ADOPTED |
| P-03 | **Every vowel letter is written, including 𐑩.** So the absence of a vowel mark between two consonants always means the consonants are adjacent in speech. | ADOPTED |
| P-04 | **Vowel marks sit above the base.** The only marks below are gemination (G-01) and the `and` shorthand (W-03). | ADOPTED |
| P-05 | **Length is written with the long carrier.** It is never written by doubling a mark. | ADOPTED |

## 2. Mark order

| ID | Rule | Status |
|---|---|---|
| K-01 | A consonant's marks follow its base glyph in this order: `[bar-below]` (gemination), then `[bar-above]` (nasal), then the vowel mark. | PROVISIONAL |

The order only matters for string identity. A shaping font stacks the marks the same way in any order.

## 3. Consonants

| ID | Rule | Status |
|---|---|---|
| C-01 | Each consonant letter maps to one fixed glyph, per the table below. | ADOPTED |
| C-02 | The sequence 𐑣𐑢 (aspirated *wh*) is written as one glyph, `{hwesta}`. | ADOPTED |

| Shavian | Glyph | Shavian | Glyph | Shavian | Glyph |
|---|---|---|---|---|---|
| 𐑐 | `{parma}` | 𐑚 | `{umbar}` | 𐑑 | `{tinco}` |
| 𐑛 | `{ando}` | 𐑒 | `{quesse}` | 𐑜 | `{ungwe}` |
| 𐑗 | `{calma}` | 𐑡 | `{anga}` | 𐑓 | `{formen}` |
| 𐑝 | `{ampa}` | 𐑔 | `{thuule}` | 𐑞 | `{anto}` |
| 𐑖 | `{harma}` | 𐑠 | `{anca}` | 𐑕 | `{silme}` |
| 𐑟 | `{esse}` | 𐑥 | `{malta}` | 𐑯 | `{nuumen}` |
| 𐑙 | `{nwalme}` | 𐑤 | `{lambe}` | 𐑮 | `{roomen}` |
| 𐑢 | `{vala}` | 𐑘 | `{anna}` | 𐑣 | `{hyarmen}` |

### 3.1 Silmë and Essë

| ID | Rule | Status |
|---|---|---|
| S-01 | Final /s/ and /z/ use `{silme}` and `{esse}`. The s-hook (*sa-rincë*) is never used, because it hides the /s/ versus /z/ distinction. | ADOPTED |
| S-02 | When any above-mark lands on `{silme}` or `{esse}` (a vowel mark or `[bar-above]`), the nuquerna form is used instead: `{silme-nuquerna}` or `{esse-nuquerna}`. | ADOPTED |

### 3.2 Nasals and gemination

| ID | Rule | Status |
|---|---|---|
| N-01 | A nasal followed by a homorganic stop is written as the stop plus `[bar-above]`: 𐑯𐑑 → `{tinco}[bar-above]`, 𐑯𐑛 → `{ando}[bar-above]`, 𐑥𐑐 → `{parma}[bar-above]`, 𐑥𐑚 → `{umbar}[bar-above]`. | ADOPTED |
| N-02 | 𐑙𐑒 and 𐑙𐑜 are written the same way. | **OPEN** |
| G-01 | Two identical adjacent consonant letters are written as the base plus `[bar-below]`. Shavian only doubles a consonant when it is really articulated twice (*unnamed*, *midday*). | ADOPTED |

N-02 candidates:
- **Current:** 𐑙𐑒 → `{quesse}[bar-above]` and 𐑙𐑜 → `{ungwe}[bar-above]`.
- **Alternative:** Aranoss and Tecendil write 𐑙𐑒 as `{ungwe}[bar-above]`. That is the usual convention (the velar nasal is /ŋ/ plus the stop's place), but it merges 𐑙𐑒 with 𐑙𐑜.

## 4. R

| ID | Rule | Status |
|---|---|---|
| R-01 | 𐑮 is always `{roomen}`. | ADOPTED |
| R-02 | `{oore}` is never used. | ADOPTED |

The Quenya rule (rómen before a vowel, óre otherwise) records whether an r is pronounced.
In a rhotic phonemic mode every r is pronounced, so the choice would carry no information.
Tecendil's English phonemic mode and Aranoss's transcription also set the rule aside.
Both keep óre only for the vowel-r of NURSE; we don't, because section 8 builds NURSE out of its parts.

## 5. Vowels

| ID | Rule | Status |
|---|---|---|
| V-01 | A short vowel is written as a mark on the **next** consonant cluster in the word. | ADOPTED |
| V-02 | A short vowel with no consonant after it (word-final, or before another vowel) is written on a short carrier: `{telco}[mark]`. | ADOPTED |
| V-03 | A long vowel is always written as `{aara}[mark]`. It is never placed on a consonant, whatever follows. A short vowel waiting for a consonant is flushed first (V-02). | ADOPTED |

| ID | Shavian | Keyword | Glyphs | Status |
|---|---|---|---|---|
| V-11 | 𐑦 | KIT | `[dot-above]` | ADOPTED |
| V-12 | 𐑧 | DRESS | `[acute]` | ADOPTED |
| V-13 | 𐑨 | TRAP | `[reversed-triple-dot-above]` | ADOPTED |
| V-14 | 𐑩 | commA | `[breve]` | ADOPTED |
| V-15 | 𐑪 | LOT | `[right-curl]` | ADOPTED |
| V-16 | 𐑳 | STRUT | `[grave]` | ADOPTED |
| V-17 | 𐑫 | FOOT | `[left-curl]` | ADOPTED |
| V-21 | 𐑰 | FLEECE | `{aara}[dot-above]` | ADOPTED |
| V-22 | 𐑭 | PALM | `{aara}[triple-dot-above]` | ADOPTED |
| V-23 | 𐑷 | THOUGHT | `{aara}[right-curl]` | ADOPTED |
| V-24 | 𐑵 | GOOSE | `{aara}[left-curl]` | ADOPTED |

Notes:
- FLEECE always uses `[dot-above]` (the i-mark), never a doubled e-mark.
- TRAP uses the inverted triple dot (points down) and PALM the upright one (points up).
- The schwa is a breve (V-14), written everywhere it is pronounced (P-03).

## 6. Diphthongs

A diphthong is one glide letter carrying the nucleus mark. No consonant takes the mark.

| ID | Shavian | Keyword | Glyphs | Status |
|---|---|---|---|---|
| D-01 | 𐑲 | PRICE | `{anna}[triple-dot-above]` | PROVISIONAL |
| D-02 | 𐑬 | MOUTH | `{vala}[triple-dot-above]` | PROVISIONAL |
| D-03 | 𐑱 | FACE | `{anna}[acute]` | PROVISIONAL |
| D-04 | 𐑴 | GOAT | `{vala}[right-curl]` | PROVISIONAL |
| D-05 | 𐑶 | CHOICE | `{anna}[right-curl]` | PROVISIONAL |
| D-06 | 𐑾 | IAN | `{anna}[dot-above]` | **OPEN** |

PRICE and MOUTH use the upright dots because their nucleus is an open vowel. I'll check this
against Aranoss's text before locking it.

**Residual collisions.** FACE, GOAT, CHOICE and IAN still equal a vowel plus glide written with the
same marks: 𐑱 = 𐑧𐑘, 𐑴 = 𐑪𐑢, 𐑶 = 𐑪𐑘 and 𐑾 = 𐑦𐑘. The vowel splits in section 5 removed the others. Options:

1. Accept these four. The sequences are rare in English phonology.
2. Give diphthongs their own glide letters (Tolkien's `{yanta}` and `{uure}`).
3. Write the glide after the nucleus on a carrier.

For 𐑾 there is a further option: expand it to 𐑦𐑩 (section 8), as Unicode's description of the letter suggests.

## 7. Whole-word shorthands and punctuation

| ID | Rule | Status |
|---|---|---|
| W-01 | The word 𐑞 alone is `{the-shorthand}`. | ADOPTED |
| W-02 | The word 𐑝 alone is `{of-shorthand}`. | ADOPTED |
| W-03 | The word 𐑯 alone is `{ando}[bar-above][dot-below]` (*and*). It is the only place `[dot-below]` appears, and is exempt from P-04. | ADOPTED |
| W-04 | Abbreviations for 𐑑 (*to*) and 𐑓 (*for*), as Aranoss uses. Not implemented. | **OPEN** |
| U-01 | `,` is `{pusta}`. `.` is `{double-pusta}`. | ADOPTED |
| U-02 | `;` and `:` are both `{triple-pusta}`†. Aranoss writes `;` as the double section mark. | PROVISIONAL |
| U-03 | `-` is `{section-mark}`†, because Alcarin has no hyphen glyph. | PROVISIONAL |

Other punctuation passes through unchanged.

## 8. Ligatures and declared identities

Shavian's ligature letters are expanded into their components before any other rule applies.
Each pair below is therefore an intended identity: the two spellings give the same glyphs.

| ID | Ligature | Expands to | Result for each |
|---|---|---|---|
| L-01 | 𐑸 START | 𐑭𐑮 | `{aara}[triple-dot-above]{roomen}` |
| L-02 | 𐑹 NORTH | 𐑷𐑮 | `{aara}[right-curl]{roomen}` |
| L-03 | 𐑺 SQUARE | 𐑧𐑮 | `{roomen}[acute]` |
| L-04 | 𐑽 NEAR | 𐑦𐑮 | `{roomen}[dot-above]` |
| L-05 | 𐑻 NURSE | 𐑳𐑮 | `{roomen}[grave]` |
| L-06 | 𐑼 lettER | 𐑩𐑮 | `{roomen}[breve]` |
| L-07 | 𐑿 YEW | 𐑘𐑵 | `{anna}{aara}[left-curl]` |

All of L-01 to L-07 are ADOPTED.

Because the R-vowels are compositional, they follow V-01: the vowel mark sits on `{roomen}`, as the
short vowel before it would.

## 9. Processing order

1. Strip namer dots (`·`).
2. Whole-word shorthands (W-01 to W-03).
3. Ligature expansion (section 8).
4. Left to right: 𐑣𐑢 (C-02), nasal pairs (N-01, N-02), gemination (G-01), then single letters.
5. Vowels (V-01 to V-03) and diphthongs (D-01 to D-06).
6. Nuquerna selection (S-02).

## 10. Worked examples

| Shavian | Word | Glyphs |
|---|---|---|
| 𐑕𐑰 | see | `{silme}{aara}[dot-above]` |
| 𐑓𐑵𐑛 | food | `{formen}{aara}[left-curl]{ando}` |
| 𐑚𐑸𐑛 | bard | `{umbar}{aara}[triple-dot-above]{roomen}{ando}` |
| 𐑣𐑻 | her | `{hyarmen}{roomen}[grave]` |
| 𐑐𐑤𐑲𐑑 | plight | `{parma}{lambe}{anna}[triple-dot-above]{tinco}` |
| 𐑐𐑩𐑤𐑲𐑑 | polite | `{parma}{lambe}[breve]{anna}[triple-dot-above]{tinco}` |
| 𐑦𐑟 | is | `{esse-nuquerna}[dot-above]` |

*plight* and *polite* differ only by the breve. That is P-03 at work.

## 11. Changes needed in the current engine

- Drop CSUR and the `--csur` flag.
- FLEECE, PALM, THOUGHT and GOOSE become forced carriers (V-21 to V-24).
- TRAP uses `E056`, STRUT uses `E054`; the doubled curl and the double acute leave engine output.
- Remove the r-rule and `{oore}`; expand the ligatures (section 8) instead of special-casing the R-vowels.
- `TOP_TEHTAR` (the nuquerna trigger list) is missing the breve `E053` today, so a schwa on silme is never flipped (S-02). It must also gain `E054` and `E056`, and lose `E048` and the doubled curl.
- `test_collisions.py` changes from an accepted-merges list to the identities in section 8, plus whatever remains open in section 6.

## 12. Open questions

| Where | Question |
|---|---|
| N-02 | How to write 𐑙𐑒 and 𐑙𐑜. |
| D-01 to D-06 | Nucleus marks for PRICE and MOUTH; how to separate the four residual collisions. |
| W-04 | Whether to adopt abbreviations for *to* and *for*. |
| U-02 | The semicolon glyph. |
| K-01 | Canonical mark order. |
