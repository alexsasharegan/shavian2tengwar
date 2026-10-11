# The Complete Guide to Shavian, Tengwar, and Featural Transliteration

---

## Part 1: The Shavian Alphabet & ReadLex Specification

The Shavian alphabet is a purely phonemic writing system designed by Kingsley Read to fulfill the bequest of George Bernard Shaw. It replaces traditional non-phonetic English spelling with a 1:1 sound-to-letter mapping.

### 1. Character Taxonomy

Shavian characters fall into four structural categories based on vertical height and composition:

- **Tall (Voiceless Consonants):** Extend above the x-height.
- **Deep (Voiced Consonants):** Extend below the baseline.
- **Short (Vowels, Liquids, Nasals):** Fit entirely within the x-height.
- **Compound (Vocalic Ligatures):** Combine rhotic (/r/) sounds and vowel clusters into single glyphs.

#### Consonant Sound Pairs

Tall and Deep consonants form physical pairs where rotating or flipping a Tall (voiceless) letter generates its Deep (voiced) counterpart.

| Sound Pair      | Tall Glyph (Voiceless) | Deep Glyph (Voiced) | Phonetic Names |
| --------------- | ---------------------- | ------------------- | -------------- |
| **/p/ – /b/**   | **𐑐**                  | **𐑚**               | peep – bib     |
| **/t/ – /d/**   | **𐑑**                  | **𐑛**               | tot – dead     |
| **/k/ – /ɡ/**   | **𐑒**                  | **𐑜**               | kick – gag     |
| **/f/ – /v/**   | **𐑓**                  | **𐑝**               | fee – vow      |
| **/θ/ – /ð/**   | **𐑔**                  | **𐑞**               | thigh – they   |
| **/s/ – /z/**   | **𐑕**                  | **𐑟**               | so – zoo       |
| **/ʃ/ – /ʒ/**   | **𐑖**                  | **𐑠**               | sure – measure |
| **/tʃ/ – /dʒ/** | **𐑗**                  | **𐑡**               | church – judge |
| **/h/ – /w/**   | **𐑣**                  | **𐑢**               | he – woe       |

#### Vowels, Liquids, and Compound Ligatures

| Category               | Characters & Keywords                                                                                                                                 |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Liquids & Nasals**   | **𐑤** (/l/ loll), **𐑥** (/m/ mime), **𐑯** (/n/ nun), **𐑙** (/ŋ/ hung), **𐑮** (/r/ roar), **𐑘** (/j/ yea)                                              |
| **Short Vowels**       | **𐑦** (/ɪ/ if), **𐑧** (/ɛ/ egg), **𐑨** (/æ/ ash), **𐑩** (/ə/ ado), **𐑳** (/ʌ/ up), **𐑪** (/ɒ/ on), **𐑫** (/ʊ/ wool)                                   |
| **Long Vowels**        | **𐑰** (/iː/ eat), **𐑱** (/eɪ/ age), **𐑭** (/ɑː/ ah), **𐑷** (/ɔː/ awe), **𐑴** (/oʊ/ oak), **𐑵** (/uː/ ooze)                                            |
| **Diphthongs**         | **𐑲** (/aɪ/ ice), **𐑶** (/ɔɪ/ oil), **𐑬** (/aʊ/ out)                                                                                                  |
| **Compound Ligatures** | **𐑸** (/ɑːr/ are), **𐑹** (/ɔːr/ or), **𐑺** (/ɛər/ air), **𐑻** (/ɜːr/ err), **𐑼** (/ər/ array), **𐑽** (/ɪər/ ear), **𐑾** (/iə/ Ian), **𐑿** (/juː/ yew) |

---

### 2. The 12 ReadLex Orthographic Rules

1. **Strict Sound-to-Letter Phonetics:** Write strictly by spoken sound, ignoring silent Latin letters (e.g., _write_ = `𐑮𐑲𐑑`).
2. **Phonetic Voicing Assimilation in Suffixes:** Suffixes match spoken voicing (e.g., _cats_ = `𐑒𐑨𐑑𐑕` vs. _dogs_ = `𐑛𐑪𐑜𐑟`; _walked_ = `𐑢𐑷𐑒𐑑` vs. _played_ = `𐑐𐑤𐑱𐑛`).
3. **The Big Five Abbreviations:** Five high-frequency function words are abbreviated as single shorthand letters: _the_ = **𐑞**, _of_ = **𐑝**, _and_ = **𐑯**, _to_ = **𐑑**, _for_ = **𐑓**.
4. **Monosyllabic Invariance:** Single-syllable words maintain their fully stressed spelling regardless of context (e.g., _but_ is always `𐑚𐑳𐑑`).
5. **Monosyllabic Weak Vowel Exception:** Indefinite articles are explicitly written weak using schwa (`𐑩`): _a_ = `𐑩`, _an_ = `𐑩𐑯`.
6. **Stress Distinction in Polysyllabic Words:** Vowel reduction reflects stress shifts (e.g., noun _convict_ = `𐑒𐑪𐑯𐑝𐑦𐑒𐑑` vs. verb _convict_ = `𐑒𐑩𐑯𐑝𐑦𐑒𐑑`).
7. **No Letter Gemination:** Consonants are never doubled unless articulated twice across syllable boundaries (e.g., _annoy_ = `𐑩𐑯𐑶` vs. _unnamed_ = `𐑳𐑯𐑯𐑱𐑥𐑛`).
8. **Syllabic Consonant Formatting:** Insert a schwa (`𐑩`) before terminal liquids or nasals (e.g., _little_ = `𐑤𐑦𐑑𐑩𐑤`, _driven_ = `𐑛𐑮𐑦𐑝𐑩𐑯`).
9. **Verbal Contraction Formatting:** Negative contractions insert `𐑩` before `𐑯𐑑` and omit apostrophes (e.g., _didn't_ = `𐑛𐑦𐑛𐑩𐑯𐑑`).
10. **Proper Noun Marking:** Capital letters are omitted entirely; proper nouns use a middle Namer Dot (`·`) immediately preceding the word (e.g., _London_ = `·𐑤𐑳𐑯𐑛𐑩𐑯`).
11. **Unstressed Terminal Vowels (_happY_ Rule):** Words ending in unstressed _-y_ or _-ie_ use `𐑦` (e.g., _happy_ = `𐑣𐑨𐑐𐑦`). Tense, fully stressed final vowels use `𐑰` (e.g., _trustee_ = `𐑑𐑮𐑳𐑕𐑑𐑰`).
12. **Cross-Dialectal "Rhotic RP" Standard:** Standard spelling uses a broad rhotic Received Pronunciation base so rhotic and non-rhotic speakers share a single format.

---

## Part 2: Tolkien's Tengwar & Alcarin Tengwar Standard

Tengwar is a featural abugida created by J.R.R. Tolkien. Primary consonants (_tengwar_) represent structural articulation features, while vowels (_tehtar_) sit above or below consonant bases as diacritics.

### 1. The Fëanorian Consonant Grid (Appendix E Layout)

In Tolkien's standard layout, primary consonants are organized into **4 Series** (Columns: Place of Articulation) and **6 Grades** (Rows: Manner of Articulation and Voicing):

- **Series I (_Témar 1_):** Dental / Alveolar (/t/, /d/, /θ/, /ð/)
- **Series II (_Témar 2_):** Labial / Bilabial (/p/, /b/, /f/, /v/)
- **Series III (_Témar 3_):** Palatal / Affricate (/ʧ/, /ʤ/, /ʃ/, /ʒ/)
- **Series IV (_Témar 4_):** Velar (/k/, /g/, /ŋ/)

| Grade / Manner                                                    | Series I (Dental)                                | Series II (Labial)                            | Series III (Palatal)                         | Series IV (Velar)                              |
| ----------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------- | -------------------------------------------- | ---------------------------------------------- |
| **Grade 1: Voiceless Stops** _(Stem Down, Single Loop)_<br>       | ****<br> <br>`U+E000`<br> <br>_Tinco_ (/t/)     | ****<br> <br>`U+E001`<br> <br>_Parma_ (/p/)  | ****<br> <br>`U+E002`<br> <br>_Calma_ (/ʧ/) | ****<br> <br>`U+E003`<br> <br>_Quesse_ (/k/)  |
| **Grade 2: Voiced Stops** _(Stem Down, Double Loop)_<br>          | ****<br> <br>`U+E004`<br> <br>_Ando_ (/d/)      | ****<br> <br>`U+E005`<br> <br>_Umbar_ (/b/)  | ****<br> <br>`U+E006`<br> <br>_Anga_ (/ʤ/)  | ****<br> <br>`U+E007`<br> <br>_Ungwe_ (/g/)   |
| **Grade 3: Voiceless Fricatives** _(Stem Up, Single Loop)_<br>    | ****<br> <br>`U+E008`<br> <br>_Thúle_ (/θ/)     | ****<br> <br>`U+E009`<br> <br>_Formen_ (/f/) | ****<br> <br>`U+E00A`<br> <br>_Harma_ (/ʃ/) | ****<br> <br>`U+E00B`<br> <br>_Hwesta_ (/hw/) |
| **Grade 4: Voiced Fricatives** _(Stem Up, Double Loop)_<br>       | ****<br> <br>`U+E00C`<br> <br>_Anta_ (/ð/)      | ****<br> <br>`U+E00D`<br> <br>_Ampa_ (/v/)   | ****<br> <br>`U+E00E`<br> <br>_Anca_ (/ʒ/)  | ****<br> <br>`U+E00F`<br> <br>_Unque_ (/gh/)  |
| **Grade 5: Nasals** _(Short Stem, Double Loop)_<br>               | ****<br> <br>`U+E010`<br> <br>_Númen_ (/n/)     | ****<br> <br>`U+E011`<br> <br>_Malta_ (/m/)  | ****<br> <br>`U+E012`<br> <br>_Noldo_ (/ŋ/) | ****<br> <br>`U+E013`<br> <br>_Nwalme_ (/ŋ/)  |
| **Grade 6: Glides / Semi-vowels** _(Short Stem, Single Loop)_<br> | ****<br> <br>`U+E014`<br> <br>_Óre_ (not used by this mode) | ****<br> <br>`U+E015`<br> <br>_Vala_ (/w/)   | ****<br> <br>`U+E016`<br> <br>_Anna_ (/j/)  | ****<br> <br>`U+E017`<br> <br>_Vilya_<br>     |

---

### 2. Additional & Irregular Tengwar (Alcarin Standard)

Beyond the standard 24-tengwa grid, specialized base characters handle liquids, sibilants, glottal sounds, and silent carriers:

| Tengwa Glyph | Code Point   | Tengwa Name                 | Structural Description / Function                                                        |
| ------------ | ------------ | --------------------------- | ---------------------------------------------------------------------------------------- |
| ****        | `U+E020`     | _Rómen_                     | /r/ in every position (R-01)                                              |
| ****        | `U+E022`     | _Lamba_                     | Upward hooked liquid character (/l/)                                                     |
| ****        | `U+E024`     | _Silme_                     | Upright S-curve sibilant (/s/)                                                           |
| ****        | `U+E025`     | _Silme Nuquerna_            | Inverted S-curve (used when carrying top tehta)                                          |
| ****        | `U+E026`     | _Esse_ / _Aze_              | Z-curve / inverted double loop (/z/)                                                     |
| ****        | `U+E027`     | _Esse Nuquerna_             | Inverted Z-curve (used when carrying top tehta)                                          |
| ****        | `U+E028`     | _Hyarmen_                   | Downward stem with left hook (/h/)                                                       |
| ****        | **`U+E02C`** | **_Ára_ (Long Carrier)**    | Descending vertical stem (dotless 'j', drops below baseline) carrying long orphan vowels |
| ****        | `U+E02D`     | _Halla_ (unused by engine)  | Ascending vertical stem (starts above x-height); not a carrier                           |
| ****        | `U+E02E`     | **_Telco_ (Short Carrier)** | Neutral x-height vertical stem (dotless 'i') carrying short orphan vowels                |

---

### 3. Vowel Tehtar & Diacritic Marks

Vowel marks (*tehtar*) sit above the *following* consonant and are read before it. A long vowel is the same mark as its short partner (KIT/FLEECE, TRAP/PALM, LOT/THOUGHT, FOOT/GOOSE) but written on the long carrier `{aara}` instead of on a consonant. STRUT and the schwa have marks of their own.

| Mark | Code point | Name | Used for | Placement |
| :--: | :--------- | :--- | :------- | :-------- |
|  | `U+E040` | _a-tehta_ | TRAP; PALM; the first half of PRICE and MOUTH | three dots in a triangle above |
|  | `U+E044` | _i-tehta_ | KIT, FLEECE | single dot above |
|  | `U+E046` | _e-tehta_ | DRESS, FACE | single acute stroke above |
|  | `U+E04A` | _o-tehta_ | LOT, THOUGHT, CHOICE, GOAT | right-facing curl above |
|  | `U+E04C` | _u-tehta_ | FOOT, GOOSE | left-facing curl above |
|  | `U+E053` | _schwa-tehta_ | the schwa /ə/ | breve above |
|  | `U+E054` | _grave_ | STRUT | grave stroke above |
|  | `U+E050` | _nasal bar_ | nasal plus stop (𐑯𐑑, 𐑥𐑐 …), 𐑙𐑒, 𐑙𐑜 | bar above the stop |
|  | `U+E051` | _doubler_ | two identical consonants | bar below the consonant |
|  | `U+E045` | _under-dot_ | only inside the *and* shorthand | dot below |

The double acute (`U+E048`), a doubled left curl and the three inverted dots (`U+E056`) are not used. When a mark lands on Silmë or Essë, the nuquerna form is used instead (S-02). Mark order on a base is vowel, then nasal bar, then doubler (K-01).

---

## Part 3: The Shavian-to-Tengwar Transliteration Bridge

By using Shavian as an Intermediate Representation (IR), transliteration bypasses non-phonetic English orthography entirely. Each Shavian word becomes a list of cells (one base glyph plus its marks), which an encoding then turns into code points.

**The rules themselves live in [`spec/mode.md`](./spec/mode.md); this part is a reader's summary.** The tables below were generated from the engine, so they show what the converter actually writes. If they disagree with the spec, the spec wins.

### 1. Consonants

Each consonant letter has one fixed glyph (C-01). The Rules column lists the spec rules that fired.

| Sound | Shavian | Tengwar | Glyph names | Code points | Rules |
| :--- | :--- | :--- | :--- | :--- | :--- |
| /p/ | **𐑐** |  | `{parma}` | `U+E001` | C-01 |
| /b/ | **𐑚** |  | `{umbar}` | `U+E005` | C-01 |
| /t/ | **𐑑** |  | `{tinco}` | `U+E000` | C-01 |
| /d/ | **𐑛** |  | `{ando}` | `U+E004` | C-01 |
| /k/ | **𐑒** |  | `{quesse}` | `U+E003` | C-01 |
| /ɡ/ | **𐑜** |  | `{ungwe}` | `U+E007` | C-01 |
| /tʃ/ | **𐑗** |  | `{calma}` | `U+E002` | C-01 |
| /dʒ/ | **𐑡** |  | `{anga}` | `U+E006` | C-01 |
| /f/ | **𐑓** |  | `{formen}` | `U+E009` | C-01 |
| /v/ | **𐑝** |  | `{ampa}` | `U+E00D` | C-01 |
| /θ/ | **𐑔** |  | `{thuule}` | `U+E008` | C-01 |
| /ð/ | **𐑞** |  | `{anto}` | `U+E00C` | C-01 |
| /ʃ/ | **𐑖** |  | `{harma}` | `U+E00A` | C-01 |
| /ʒ/ | **𐑠** |  | `{anca}` | `U+E00E` | C-01 |
| /s/ | **𐑕** |  | `{silme}` | `U+E024` | C-01 |
| /z/ | **𐑟** |  | `{esse}` | `U+E026` | C-01 |
| /m/ | **𐑥** |  | `{malta}` | `U+E011` | C-01 |
| /n/ | **𐑯** |  | `{nuumen}` | `U+E010` | C-01 |
| /ŋ/ | **𐑙** |  | `{nwalme}` | `U+E013` | C-01 |
| /l/ | **𐑤** |  | `{lambe}` | `U+E022` | C-01 |
| /r/ | **𐑮** |  | `{roomen}` | `U+E020` | C-01 |
| /w/ | **𐑢** |  | `{vala}` | `U+E015` | C-01 |
| /j/ | **𐑘** |  | `{anna}` | `U+E016` | C-01 |
| /h/ | **𐑣** |  | `{hyarmen}` | `U+E028` | C-01 |

Special cases: 𐑣𐑢 is the one glyph `{hwesta}` (C-02). 𐑯𐑑, 𐑯𐑛, 𐑥𐑐, 𐑥𐑚, 𐑙𐑒 and 𐑙𐑜 are the stop plus a nasal bar (N-01, N-02). Two identical consonants take the doubling bar below (G-01). Silmë and Essë flip to their nuquerna forms when a mark lands on them (S-02).

### 2. Vowels

A short vowel is a mark on the *next* consonant, read before it. A short vowel with no consonant after it sits on the short carrier `{telco}`. A long vowel always sits on the long carrier `{aara}` (V-21..V-24). The "alone" forms below show that orphan case.

| Sound | Shavian | Tengwar | Glyph names | Code points | Rules |
| :--- | :--- | :--- | :--- | :--- | :--- |
| /ɪ/ | **𐑦** |  | `{telco}[dot-above]` | `U+E02E U+E044` | V-11, V-02 |
| /ɛ/ | **𐑧** |  | `{telco}[acute]` | `U+E02E U+E046` | V-12, V-02 |
| /æ/ | **𐑨** |  | `{telco}[triple-dot-above]` | `U+E02E U+E040` | V-13, V-02 |
| /ə/ | **𐑩** |  | `{telco}[breve]` | `U+E02E U+E053` | V-14, V-02 |
| /ɒ/ | **𐑪** |  | `{telco}[right-curl]` | `U+E02E U+E04A` | V-15, V-02 |
| /ʌ/ | **𐑳** |  | `{telco}[grave]` | `U+E02E U+E054` | V-16, V-02 |
| /ʊ/ | **𐑫** |  | `{telco}[left-curl]` | `U+E02E U+E04C` | V-17, V-02 |
| /iː/ | **𐑰** |  | `{aara}[dot-above]` | `U+E02C U+E044` | V-21, V-03 |
| /ɑː/ | **𐑭** |  | `{aara}[triple-dot-above]` | `U+E02C U+E040` | V-22, V-03 |
| /ɔː/ | **𐑷** |  | `{aara}[right-curl]` | `U+E02C U+E04A` | V-23, V-03 |
| /uː/ | **𐑵** |  | `{aara}[left-curl]` | `U+E02C U+E04C` | V-24, V-03 |

### 3. Diphthongs and R-vowels

The glide is written last and the vowel mark first. R-vowels are not separate glyphs: they expand to a vowel plus 𐑮 (rómen). 𐑾 is 𐑦𐑩 and 𐑿 is 𐑘𐑵.

| Sound | Shavian | Tengwar | Glyph names | Code points | Rules |
| :--- | :--- | :--- | :--- | :--- | :--- |
| /aɪ/ | **𐑲** |  | `{anna}[triple-dot-above]` | `U+E016 U+E040` | D-01 |
| /aʊ/ | **𐑬** |  | `{vala}[triple-dot-above]` | `U+E015 U+E040` | D-02 |
| /eɪ/ | **𐑱** |  | `{anna}[acute]` | `U+E016 U+E046` | D-03 |
| /oʊ/ | **𐑴** |  | `{vala}[right-curl]` | `U+E015 U+E04A` | D-04 |
| /ɔɪ/ | **𐑶** |  | `{anna}[right-curl]` | `U+E016 U+E04A` | D-05 |
| /juː/ | **𐑿** |  | `{anna}{aara}[left-curl]` | `U+E016 U+E02C U+E04C` | L-07, C-01, V-24, V-03 |
| /ɪə/ | **𐑾** |  | `{telco}[dot-above]{telco}[breve]` | `U+E02E U+E044 U+E02E U+E053` | L-08, V-11, V-02, V-14 |
| /ɑːr/ | **𐑸** |  | `{aara}[triple-dot-above]{roomen}` | `U+E02C U+E040 U+E020` | L-01, V-22, V-03, R-01 |
| /ɔːr/ | **𐑹** |  | `{aara}[right-curl]{roomen}` | `U+E02C U+E04A U+E020` | L-02, V-23, V-03, R-01 |
| /ɛər/ | **𐑺** |  | `{roomen}[acute]` | `U+E020 U+E046` | L-03, R-01, V-12, V-01 |
| /ɪər/ | **𐑽** |  | `{roomen}[dot-above]` | `U+E020 U+E044` | L-04, R-01, V-11, V-01 |
| /ɜːr/ | **𐑻** |  | `{roomen}[grave]` | `U+E020 U+E054` | L-05, R-01, V-16, V-01 |
| /ər/ | **𐑼** |  | `{roomen}[breve]` | `U+E020 U+E053` | L-06, R-01, V-14, V-01 |

### 4. The Big Five: Shorthand Logograms

Shavian writes five very common words as a single letter. *the*, *of* and *and* have Tengwar shorthands. *to* and *for* do not: they are written as their weak forms /tə/ and /fər/, which keeps them distinct from *too/two* and *four*. This replaces an older version of this guide that gave *to* and *for* as the bare letters Tinco and Formen (see `DECISIONS.md`, D-01).

| Target word | Shavian | Tengwar | Glyph names | Code points | Rules |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *the* | **𐑞** |  | `{the-shorthand}` | `U+E01C` | W-01 |
| *of* | **𐑝** |  | `{of-shorthand}` | `U+E01D` | W-02 |
| *and* | **𐑯** |  | `{and-shorthand}` | `U+E004 U+E050 U+E045` | W-03 |
| *to* | **𐑑** |  | `{tinco}{telco}[breve]` | `U+E000 U+E02E U+E053` | W-04, L-09, C-01, V-14, V-02 |
| *for* | **𐑓** |  | `{formen}{roomen}[breve]` | `U+E009 U+E020 U+E053` | W-04, L-10, C-01, L-06, R-01, V-14, V-01 |

### 5. Punctuation

| Input | Glyph names | Code point | Rule |
| :--- | :--- | :--- | :--- |
| `,` | `{pusta}` | `U+E060` | U-01 |
| `.` | `{double-pusta}` | `U+E061` | U-01 |
| `;` | `{double-section-mark}` | `U+E069` | U-02 |
| `:` | `{triple-pusta}` | `U+E062` | U-03 |
| `-` | `{section-mark}` | `U+E068` | U-04 |
| `!` | `{exclamation-mark}` | `U+E065` | U-05 |
| `?` | `{question-mark}` | `U+E066` | U-05 |
| `(` | `{parenthesis-mark}` | `U+E067` | U-05 |
| `)` | `{parenthesis-mark}` | `U+E067` | U-05 |
| `“` | `{left-quotation-mark}` | `U+E06A` | U-05 |
| `”` | `{right-quotation-mark}` | `U+E06B` | U-05 |
| `"` (ASCII) | alternates the two quotation marks | | U-05 |
