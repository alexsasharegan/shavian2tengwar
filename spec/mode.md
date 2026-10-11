# Phonemic English Tengwar Mode

This document is the font-independent specification of the mode that `shavian2tengwar` implements.
It takes Shavian text as input and produces a sequence of named Tengwar glyphs as output.
It says nothing about code points: `spec/encodings/*.md` maps each glyph name to a font.

Every rule has an ID and a status. Corpus cases in `corpus/` cite rule IDs, and a coverage check
fails if a rule has no case. When this document and the code disagree, the code is wrong.

## 0. Conventions

**Status.** `ADOPTED` is decided and must be enforced. `PROVISIONAL` is proposed in an open pull
request; merging the PR approves it and makes it `ADOPTED`, so `main` has none. `OPEN` is undecided;
the text lists the candidates and current behaviour.

**Glyph names** follow [Tecendil](https://www.tecendil.com/) so that output can be pasted into its
literal-input box.

- `{name}` is a tengwa, carrier, or punctuation glyph.
- `[name]` is a combining mark.
- A **cluster** is one `{base}` followed by its `[marks]`, as in `{tinco}[dot-above]`.

All names below were found in Tecendil's mode files (`modes/*.jsonc`) except those flagged †:

- `{triple-pusta}`, `{section-mark}`, `{double-section-mark}`, `{exclamation-mark}`, `{question-mark}`,
  `{parenthesis-mark}`, `{left-quotation-mark}` and `{right-quotation-mark}` are not found. `{double-pusta}` appears once.
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
| K-01 | A consonant's marks are listed **top to bottom**, which is also reading order: the vowel mark, then `[bar-above]` (nasal), then the base, then `[bar-below]` (gemination). In the glyph notation they follow the base: `{tinco}[dot-above][bar-above][bar-below]`. | ADOPTED |

On the page the vowel mark is highest, the nasal bar sits between it and the base, and the gemination bar
is below the base. This is also reading order: the vowel comes before the consonant, the nasal is
sounded on the way into the consonant, and the gemination holds it last. How the marks are ordered in
a font's code points is an encoding matter (AE-01), because fonts stack marks outward from the base.
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
| V-13 | 𐑨 | /æ/ | TRAP | `[triple-dot-above]` | ADOPTED |
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
- TRAP and PALM share the triple dot, as KIT/FLEECE, LOT/THOUGHT and FOOT/GOOSE share theirs: the short vowel is the mark on a consonant, the long vowel is the same mark on `{aara}` (V-03). Shavian has no short /ɑ/, so the short slot of this mark was free.
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

**Declared identities.** Because a diphthong *is* its nucleus followed by its glide, five of these
letters are written the same as the plain sequence. They are intended, not collisions:

| ID | Letter | IPA | Same as | IPA | Glyphs |
|---|---|---|---|---|---|
| I-01 | 𐑱 FACE | /eɪ/ | 𐑧𐑘 | /ɛj/ | `{anna}[acute]` |
| I-02 | 𐑴 GOAT | /oʊ/ | 𐑪𐑢 | /ɒw/ | `{vala}[right-curl]` |
| I-03 | 𐑶 CHOICE | /ɔɪ/ | 𐑪𐑘 | /ɒj/ | `{anna}[right-curl]` |
| I-04 | 𐑲 PRICE | /aɪ/ | 𐑨𐑘 | /æj/ | `{anna}[triple-dot-above]` |
| I-05 | 𐑬 MOUTH | /aʊ/ | 𐑨𐑢 | /æw/ | `{vala}[triple-dot-above]` |

These identities do not hold next to the same glide letter: 𐑪𐑘𐑘 is a geminate, but 𐑶𐑘 is not. English
never has either sequence.

I-04 and I-05 follow from TRAP sharing PALM's mark (V-13). They are accepted because the sequences 𐑨𐑘 and
𐑨𐑢 are not found in ReadLex's baseline pronunciations: of 111,214 entries, only the TrapBath variant of
*Malawian* (and a one-off name, *iau*) contain them. Should one ever occur, it can be told apart by writing
the TRAP on `{telco}`.

The plain sequences with PALM (𐑭𐑘, 𐑭𐑢) use the long carrier, so they stay distinct from PRICE and MOUTH.

## 7. Whole-word shorthands and punctuation

| ID | Rule | Status |
|---|---|---|
| W-01 | The word 𐑞 alone (*the*, /ðə/) is `{the-shorthand}`. | ADOPTED |
| W-02 | The word 𐑝 alone (*of*, /əv/) is `{of-shorthand}`. | ADOPTED |
| W-03 | The word 𐑯 alone (*and*, /ənd/) is `{ando}[bar-above][dot-below]`. It is the only place `[dot-below]` appears, and is exempt from P-04. | ADOPTED |
| W-04 | The words 𐑑 (*to*) and 𐑓 (*for*) have **no** Tengwar shorthand. They are expanded to their weak forms by L-09 and L-10. | ADOPTED |
| U-01 | `,` is `{pusta}`. `.` is `{double-pusta}`. | ADOPTED |
| U-02 | `;` is `{double-section-mark}`† (a stronger pause than a comma, distinct from `:`). Aranoss writes it the same way. | ADOPTED |
| U-03 | `:` is `{triple-pusta}`†. | ADOPTED |
| U-04 | `-` is `{section-mark}`†, because Alcarin has no hyphen glyph. | ADOPTED |
| U-05 | `!` is `{exclamation-mark}`†, `?` is `{question-mark}`†, and both parentheses are `{parenthesis-mark}`† (Alcarin has one glyph for both sides). Curly double quotes are `{left-quotation-mark}`† and `{right-quotation-mark}`†, and an ASCII `"` alternates between them. Single quotes and apostrophes pass through. | ADOPTED |

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
adopt none. (The earlier `docs/language-guide.md` listed *to* as a bare Tinco and *for* as a bare Formen,
as deliberate "unadorned base" shorthands. This mode replaces them; see `docs/adr/0005-weak-forms-for-to-and-for.md`.) Their signs
exist in Shavian to tell homophones apart (𐑑 *to* from 𐑑𐑵 *too*/*two*, and 𐑓 *for* from 𐑓𐑹 *four*),
so the output must still keep them distinct. A bare 𐑑 or 𐑓 is the **weak form**, which for a rhotic RP
baseline ends in a schwa. They are expanded as spellings, as the ligatures are (L-09, L-10). That needs
no community precedent, because it is only the phonemic spelling of the weak form.

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

L-01 to L-10 are ADOPTED. L-09 and L-10 apply only when the whole word is that one letter. L-09 stays distinct from *too*/*two* (𐑑𐑵, `{tinco}{aara}[left-curl]`), and L-10 from *four* (𐑓𐑹,
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

## 11. History

The engine was rewritten to this spec on the `dev/refactor` branch. What the old engine did
differently, and why each choice was made, is recorded in `docs/`: the change list is in
`docs/projects/0001-engine-rewrite/LOG.md`, and the decisions are in `docs/adr/`.

## 12. Open questions

None. A new question is raised in a pull request, with a `PROVISIONAL` rule and a `Proposed` ADR.
