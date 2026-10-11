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

- `{triple-pusta}`, `{section-mark}` and `{double-section-mark}` are not found. `{double-pusta}` appears once.
  Tecendil's mode files carry no punctuation table, so these names follow Alcarin's glyph names.
- `{the-shorthand}`, `{of-shorthand}` and `{and-shorthand}` are shorthand names, not glyph names.
  The first two are Tecendil's literals. `{and-shorthand}` is expanded in rule W-03.

**Keyword sets** are John Wells' lexical sets (TRAP, PALM, LOT, THOUGHT, STRUT, FOOT, FLEECE,
GOOSE, NURSE, and so on). They name vowels in rules and anchor the corpus.

**IPA.** Each table gives the sound in IPA, as a fallback for readers who don't know Shavian. It is a
broad transcription of the rhotic RP that Shavian's ReadLex assumes. If an IPA value and a Shavian
letter ever seem to disagree, the Shavian letter is the definition.

## 1. Principles

| ID | Rule | Status |
|---|---|---|
| P-01 | The input is Shavian phonemes. English spelling is never consulted. | ADOPTED |
| P-02 | **Lossless.** Two different Shavian strings give different glyph strings, except the identities declared in sections 6 and 8. A test enforces this. | ADOPTED |
| P-03 | **Every vowel letter is written, including 𐑩 /ə/.** So the absence of a vowel mark between two consonants always means the consonants are adjacent in speech. | ADOPTED |
| P-04 | **Vowel marks sit above the base.** The only marks below are gemination (G-01) and the `and` shorthand (W-03). | ADOPTED |
| P-05 | **Length is written with the long carrier.** It is never written by doubling a mark. | ADOPTED |

## 2. Mark order

| ID | Rule | Status |
|---|---|---|
| K-01 | A consonant's marks follow its base glyph in **reading order**: the vowel mark first, then `[bar-above]` (nasal), then `[bar-below]` (gemination). | ADOPTED |

The order only matters for string identity. A shaping font stacks the marks the same way in any order.
Reading order is the order a reader sounds them: the vowel comes before the consonant, the nasal is
sounded on the way into the consonant, and the gemination holds it last.
Example: 𐑔𐑦𐑙𐑒 *think* /θɪŋk/ is `{thuule}{quesse}[dot-above][bar-above]`, read /θ/, /ɪ/, then /ŋk/.

## 3. Consonants

| ID | Rule | Status |
|---|---|---|
| C-01 | Each consonant letter maps to one fixed glyph, per the table below. | ADOPTED |
| C-02 | The sequence 𐑣𐑢 (aspirated *wh*, /ʍ/) is written as one glyph, `{hwesta}`. | ADOPTED |

| Shavian | IPA | Glyph | Shavian | IPA | Glyph |
|---|---|---|---|---|---|
| 𐑐 | /p/ | `{parma}` | 𐑚 | /b/ | `{umbar}` |
| 𐑑 | /t/ | `{tinco}` | 𐑛 | /d/ | `{ando}` |
| 𐑒 | /k/ | `{quesse}` | 𐑜 | /ɡ/ | `{ungwe}` |
| 𐑗 | /tʃ/ | `{calma}` | 𐑡 | /dʒ/ | `{anga}` |
| 𐑓 | /f/ | `{formen}` | 𐑝 | /v/ | `{ampa}` |
| 𐑔 | /θ/ | `{thuule}` | 𐑞 | /ð/ | `{anto}` |
| 𐑖 | /ʃ/ | `{harma}` | 𐑠 | /ʒ/ | `{anca}` |
| 𐑕 | /s/ | `{silme}` | 𐑟 | /z/ | `{esse}` |
| 𐑥 | /m/ | `{malta}` | 𐑯 | /n/ | `{nuumen}` |
| 𐑙 | /ŋ/ | `{nwalme}` | 𐑤 | /l/ | `{lambe}` |
| 𐑮 | /r/ | `{roomen}` | 𐑢 | /w/ | `{vala}` |
| 𐑘 | /j/ | `{anna}` | 𐑣 | /h/ | `{hyarmen}` |

### 3.1 Silmë and Essë

| ID | Rule | Status |
|---|---|---|
| S-01 | Final /s/ and /z/ use `{silme}` and `{esse}`. The s-hook (*sa-rincë*) is never used, because it hides the /s/ versus /z/ distinction. | ADOPTED |
| S-02 | When any above-mark lands on `{silme}` or `{esse}` (a vowel mark or `[bar-above]`), the nuquerna form is used instead: `{silme-nuquerna}` or `{esse-nuquerna}`. | ADOPTED |

### 3.2 Nasals and gemination

| ID | Rule | Status |
|---|---|---|
| N-01 | A nasal followed by a homorganic stop is written as the stop plus `[bar-above]`: 𐑯𐑑 /nt/ → `{tinco}[bar-above]`, 𐑯𐑛 /nd/ → `{ando}[bar-above]`, 𐑥𐑐 /mp/ → `{parma}[bar-above]`, 𐑥𐑚 /mb/ → `{umbar}[bar-above]`. | ADOPTED |
| N-02 | 𐑙𐑒 /ŋk/ → `{quesse}[bar-above]` (*think*) and 𐑙𐑜 /ŋɡ/ → `{ungwe}[bar-above]` (*finger*). A lone 𐑙 /ŋ/ (*sing*, *-ing*) is `{nwalme}` (C-01). A /ɡ/ is written only where the Shavian has 𐑜. | ADOPTED |
| G-01 | Two identical adjacent consonant letters are written as the base plus `[bar-below]`. Shavian only doubles a consonant when it is really articulated twice (*unnamed* /ʌnneɪmd/, *midday* /mɪddeɪ/). | ADOPTED |

N-02 follows Tolkien: the nasal bar over a stop means a homorganic nasal came first. Aranoss and
Tecendil write 𐑙𐑒 as `{ungwe}[bar-above]`, which merges *think*'s cluster with *finger*'s; we keep
them apart.

## 4. R

| ID | Rule | Status |
|---|---|---|
| R-01 | 𐑮 /r/ is always `{roomen}`. | ADOPTED |
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

| ID | Shavian | IPA | Keyword | Glyphs | Status |
|---|---|---|---|---|---|
| V-11 | 𐑦 | /ɪ/ | KIT | `[dot-above]` | ADOPTED |
| V-12 | 𐑧 | /ɛ/ | DRESS | `[acute]` | ADOPTED |
| V-13 | 𐑨 | /æ/ | TRAP | `[reversed-triple-dot-above]` | ADOPTED |
| V-14 | 𐑩 | /ə/ | commA | `[breve]` | ADOPTED |
| V-15 | 𐑪 | /ɒ/ | LOT | `[right-curl]` | ADOPTED |
| V-16 | 𐑳 | /ʌ/ | STRUT | `[grave]` | ADOPTED |
| V-17 | 𐑫 | /ʊ/ | FOOT | `[left-curl]` | ADOPTED |
| V-21 | 𐑰 | /iː/ | FLEECE | `{aara}[dot-above]` | ADOPTED |
| V-22 | 𐑭 | /ɑː/ | PALM | `{aara}[triple-dot-above]` | ADOPTED |
| V-23 | 𐑷 | /ɔː/ | THOUGHT | `{aara}[right-curl]` | ADOPTED |
| V-24 | 𐑵 | /uː/ | GOOSE | `{aara}[left-curl]` | ADOPTED |

Notes:
- FLEECE always uses `[dot-above]` (the i-mark), never a doubled e-mark.
- TRAP uses the inverted triple dot (points down) and PALM the upright one (points up).
- The schwa is a breve (V-14), written everywhere it is pronounced (P-03).

## 6. Diphthongs

A diphthong is one glide letter carrying the nucleus mark. No consonant takes the mark.

| ID | Shavian | IPA | Keyword | Glyphs | Status |
|---|---|---|---|---|---|
| D-01 | 𐑲 | /aɪ/ | PRICE | `{anna}[triple-dot-above]` | ADOPTED |
| D-02 | 𐑬 | /aʊ/ | MOUTH | `{vala}[triple-dot-above]` | ADOPTED |
| D-03 | 𐑱 | /eɪ/ | FACE | `{anna}[acute]` | ADOPTED |
| D-04 | 𐑴 | /oʊ/ | GOAT | `{vala}[right-curl]` | ADOPTED |
| D-05 | 𐑶 | /ɔɪ/ | CHOICE | `{anna}[right-curl]` | ADOPTED |

The glide letter is the **last** sound and the mark is the first: `{anna}[acute]` reads /e/ then /j/.
Because every vowel mark is read before its base (V-01), a diphthong is exactly "nucleus, then glide".

𐑾 IAN /ɪə/ is not a diphthong of this kind: it ends in a schwa, not a glide, so it is expanded as a
ligature (L-08).

**Declared identities.** Because a diphthong *is* its nucleus followed by its glide, three of these
letters are written the same as the plain sequence. They are intended, not collisions:

| ID | Letter | IPA | Same as | IPA | Glyphs |
|---|---|---|---|---|---|
| I-01 | 𐑱 FACE | /eɪ/ | 𐑧𐑘 | /ɛj/ | `{anna}[acute]` |
| I-02 | 𐑴 GOAT | /oʊ/ | 𐑪𐑢 | /ɒw/ | `{vala}[right-curl]` |
| I-03 | 𐑶 CHOICE | /ɔɪ/ | 𐑪𐑘 | /ɒj/ | `{anna}[right-curl]` |

PRICE and MOUTH have no such twin. Their nucleus is the upright dots, and the plain-sequence forms
(𐑭𐑘, 𐑨𐑘, 𐑭𐑢, 𐑨𐑢) use the long carrier or the inverted dots, so they stay distinct.

## 7. Whole-word shorthands and punctuation

| ID | Rule | Status |
|---|---|---|
| W-01 | The word 𐑞 alone (*the*, /ðə/) is `{the-shorthand}`. | ADOPTED |
| W-02 | The word 𐑝 alone (*of*, /əv/) is `{of-shorthand}`. | ADOPTED |
| W-03 | The word 𐑯 alone (*and*, /ənd/) is `{ando}[bar-above][dot-below]`. It is the only place `[dot-below]` appears, and is exempt from P-04. | ADOPTED |
| W-04 | The words 𐑑 (*to*) and 𐑓 (*for*) have **no** Tengwar shorthand. They are expanded to their weak forms by L-09 and L-10. | PROVISIONAL |
| U-01 | `,` is `{pusta}`. `.` is `{double-pusta}`. | ADOPTED |
| U-02 | `;` is `{double-section-mark}`† (a stronger pause than a comma, distinct from `:`). Aranoss writes it the same way. | PROVISIONAL |
| U-03 | `:` is `{triple-pusta}`†. | PROVISIONAL |
| U-04 | `-` is `{section-mark}`†, because Alcarin has no hyphen glyph. | PROVISIONAL |
| U-05 | `!`, `?`, parentheses and quotation marks. Alcarin has glyphs for them (`E065` to `E067`, `E06A`, `E06B`) but the engine passes the ASCII characters through. | **OPEN** |

Other punctuation passes through unchanged.

**The five Shavian word signs.** Shavian abbreviates five words to one letter: 𐑞 *the*, 𐑝 *of*,
𐑯 *and*, 𐑑 *to* and 𐑓 *for*. ReadLex uses them for standalone words and hyphenated terms, and spells
them out inside longer words. The input arrives pre-normalized, so a bare 𐑑 or 𐑓 is always that word.

Only *the*, *of* and *and* have Tengwar shorthands. Aranoss's *Nimrodel* text uses the same three glyphs
we do, in every place they occur. For *to* and *for* the evidence is thin:

- *for*: Tecendil's phonemic mode has `{formen}{roomen}`, noting that in Tolkien's DTS 39 the o in
  *for* is ignored. Aranoss writes it the same way.
- *to*: only Tecendil's classical mode has a special form, `{tinco}[right-curl-below]`, which puts a
  vowel mark below and breaks P-04. Aranoss writes *to* out in full as `{tinco}{aara}[left-curl]`.

So the Tengwar community has no settled shorthand for *to*, and one Tolkien-based form for *for*. We
adopt none. Their signs exist in Shavian to tell homophones apart (𐑑 *to* from 𐑑𐑵 *too*/*two*, and
𐑓 *for* from 𐑓𐑹 *four*), so the output must still keep them distinct. A bare 𐑑 or 𐑓 is the **weak
form**, which for a rhotic RP baseline ends in a schwa. They are expanded as spellings, as the ligatures
are (L-09, L-10). That needs no community precedent, because it is only the phonemic spelling of the
weak form. The engine had no rule, so today it emits a lone `{tinco}` and a lone `{formen}`.

The ReadLex spelling-principles page confirms the five signs but does not state their vowels. The weak
forms rest on usual English weak forms, and *for* is the less certain of the two.

## 8. Ligatures and declared identities

Shavian's ligature letters, and the weak-form word signs, are expanded into their components before any
other rule applies. Each pair below is therefore an intended identity: the two spellings give the same
glyphs.

| ID | Letter | IPA | Expands to | Result for each |
|---|---|---|---|---|
| L-01 | 𐑸 START | /ɑːr/ | 𐑭𐑮 | `{aara}[triple-dot-above]{roomen}` |
| L-02 | 𐑹 NORTH | /ɔːr/ | 𐑷𐑮 | `{aara}[right-curl]{roomen}` |
| L-03 | 𐑺 SQUARE | /ɛr/ | 𐑧𐑮 | `{roomen}[acute]` |
| L-04 | 𐑽 NEAR | /ɪr/ | 𐑦𐑮 | `{roomen}[dot-above]` |
| L-05 | 𐑻 NURSE | /ɜːr/ | 𐑳𐑮 | `{roomen}[grave]` |
| L-06 | 𐑼 lettER | /ər/ | 𐑩𐑮 | `{roomen}[breve]` |
| L-07 | 𐑿 YEW | /juː/ | 𐑘𐑵 | `{anna}{aara}[left-curl]` |
| L-08 | 𐑾 IAN | /ɪə/ | 𐑦𐑩 | `{telco}[dot-above]` then the schwa: `{telco}[breve]`, or `[breve]` on the next consonant |
| L-09 | 𐑑 (the word *to*) | /tə/ | 𐑑𐑩 | `{tinco}{telco}[breve]` |
| L-10 | 𐑓 (the word *for*) | /fər/ | 𐑓𐑼 (= 𐑓𐑩𐑮) | `{formen}{roomen}[breve]` |

L-01 to L-08 are ADOPTED. L-09 and L-10 are PROVISIONAL, and apply only when the whole word is that one
letter. L-09 stays distinct from *too*/*two* (𐑑𐑵, `{tinco}{aara}[left-curl]`), and L-10 from *four* (𐑓𐑹,
`{formen}{aara}[right-curl]{roomen}`).

𐑾 often spans a syllable break (*media*, *India*), so it is written as two vowels, each with its own
mark. The hiatus stays visible, and the final sound is the schwa, not a glide.

Because the R-vowels are compositional, they follow V-01: the vowel mark sits on `{roomen}`, as the
short vowel before it would. NURSE /ɜːr/ is written as 𐑳𐑮 /ʌr/; in the rhotic baseline the two are the
same sound.

## 9. Processing order

1. Strip namer dots (`·`).
2. Whole-word shorthands (W-01 to W-03).
3. Ligature and weak-form expansion (section 8).
4. Left to right: 𐑣𐑢 (C-02), nasal pairs (N-01, N-02), gemination (G-01), then single letters.
5. Vowels (V-01 to V-03) and diphthongs (D-01 to D-05).
6. Nuquerna selection (S-02).

## 10. Worked examples

| Shavian | Word | IPA | Glyphs |
|---|---|---|---|
| 𐑕𐑰 | see | /siː/ | `{silme}{aara}[dot-above]` |
| 𐑓𐑵𐑛 | food | /fuːd/ | `{formen}{aara}[left-curl]{ando}` |
| 𐑚𐑸𐑛 | bard | /bɑːrd/ | `{umbar}{aara}[triple-dot-above]{roomen}{ando}` |
| 𐑣𐑻 | her | /hɜːr/ | `{hyarmen}{roomen}[grave]` |
| 𐑐𐑤𐑲𐑑 | plight | /plaɪt/ | `{parma}{lambe}{anna}[triple-dot-above]{tinco}` |
| 𐑐𐑩𐑤𐑲𐑑 | polite | /pəlaɪt/ | `{parma}{lambe}[breve]{anna}[triple-dot-above]{tinco}` |
| 𐑦𐑟 | is | /ɪz/ | `{esse-nuquerna}[dot-above]` |
| 𐑔𐑦𐑙𐑒 | think | /θɪŋk/ | `{thuule}{quesse}[dot-above][bar-above]` |
| 𐑾𐑯 | Ian | /ɪən/ | `{telco}[dot-above]{nuumen}[breve]` |
| 𐑥𐑰𐑛𐑾 | media | /miːdɪə/ | `{malta}{aara}[dot-above]{ando}{telco}[dot-above]{telco}[breve]` |
| 𐑑 | to | /tə/ | `{tinco}{telco}[breve]` |

*plight* and *polite* differ only by the breve. That is P-03 at work.

## 11. Changes needed in the current engine

- Drop CSUR and the `--csur` flag.
- FLEECE, PALM, THOUGHT and GOOSE become forced carriers (V-21 to V-24).
- TRAP uses `E056`, STRUT uses `E054`; the doubled curl and the double acute leave engine output.
- Remove the r-rule and `{oore}`; expand the ligatures (section 8) instead of special-casing the R-vowels.
- `TOP_TEHTAR` (the nuquerna trigger list) is missing the breve `E053` today, so a schwa on silme is never flipped (S-02). It must also gain `E054` and `E056`, and lose `E048` and the doubled curl.
- Mark order (K-01) is vowel, then nasal bar, then gemination bar. The engine currently emits the bars before the vowel mark.
- 𐑾 is expanded to 𐑦𐑩 (L-08) instead of being written as Anna plus a dot.
- Whole-word 𐑑 and 𐑓 are expanded (L-09, L-10) instead of falling through as bare letters.
- `test_collisions.py` changes from an accepted-merges list to the identities in section 8 and I-01 to I-03.
- Map the rest of the punctuation (U-02, U-03, U-05).

## 12. Open questions

| Where | Question |
|---|---|
| W-04, L-09, L-10 | Confirm that 𐑑 *to* and 𐑓 *for* are written as weak-form spellings with no shorthand. |
| U-05 | Glyphs for `!`, `?`, parentheses and quotation marks. |
| U-02 to U-04 | Provisional punctuation choices to confirm. |
