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

## Part 2: Tolkien's Tengwar & Everson 2001 (Alcarin) Standard

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
| **Grade 6: Glides / Semi-vowels** _(Short Stem, Single Loop)_<br> | ****<br> <br>`U+E014`<br> <br>_Óre_ (/r/ final) | ****<br> <br>`U+E015`<br> <br>_Vala_ (/w/)   | ****<br> <br>`U+E016`<br> <br>_Anna_ (/j/)  | ****<br> <br>`U+E017`<br> <br>_Vilya_<br>     |

---

### 2. Additional & Irregular Tengwar (Everson 2001 / Alcarin Standard)

Beyond the standard 24-tengwa grid, specialized base characters handle liquids, sibilants, glottal sounds, and silent carriers:

| Tengwa Glyph | Code Point   | Tengwa Name                 | Structural Description / Function                                                        |
| ------------ | ------------ | --------------------------- | ---------------------------------------------------------------------------------------- |
| ****        | `U+E020`     | _Rómen_                     | Trilled/prevocalic /r/ (used before vowels)                                              |
| ****        | `U+E022`     | _Lamba_                     | Upward hooked liquid character (/l/)                                                     |
| ****        | `U+E024`     | _Silme_                     | Upright S-curve sibilant (/s/)                                                           |
| ****        | `U+E025`     | _Silme Nuquerna_            | Inverted S-curve (used when carrying top tehta)                                          |
| ****        | `U+E026`     | _Esse_ / _Aze_              | Z-curve / inverted double loop (/z/)                                                     |
| ****        | `U+E027`     | _Esse Nuquerna_             | Inverted Z-curve (used when carrying top tehta)                                          |
| ****        | `U+E028`     | _Hyarmen_                   | Downward stem with left hook (/h/)                                                       |
| ****        | **`U+E02C`** | **_Ára_ (Long Carrier)**    | Descending vertical stem (dotless 'j', drops below baseline) carrying long orphan vowels |
| ****        | `U+E02D`     | _Extended Carrier_          | Ascending vertical stem (starts above x-height)                                          |
| ****        | `U+E02E`     | **_Telco_ (Short Carrier)** | Neutral x-height vertical stem (dotless 'i') carrying short orphan vowels                |

---

### 3. Vowel Tehtar & Diacritic Marks

In English General Mode, vowel diacritics (_tehtar_) sit directly above or below the following consonant base glyph:

| Tehta Mark | Code Point | Tehta Name     | Phonetic Mapping     | Visual Placement                    |
| :--------: | :--------- | :------------- | :------------------- | :---------------------------------- |
|   ****    | `U+E040`   | _a-tehta_      | /æ/, /ɑː/, /aɪ/      | Three dots in a triangle above base |
|   ****    | `U+E044`   | _i-tehta_      | /ɪ/, /iː/            | Single dot above base               |
|   ****    | `U+E045`   | _schwa-tehta_  | /ə/ (schwa)          | Single dot **below** base           |
|   ****    | `U+E046`   | _e-tehta_      | /ɛ/, /eɪ/            | Single acute stroke above base      |
|   ****    | `U+E047`   | _long e-tehta_ | /iː/ (FLEECE)        | Double acute stroke above base      |
|   ****    | `U+E04A`   | _o-tehta_      | /ɒ/, /ɔː/, /oʊ/      | Right-facing curl above base        |
|   ****    | `U+E04C`   | _u-tehta_      | /ʌ/, /ʊ/, /uː/       | Left-facing curl above base         |
|   ****    | `U+E04D`   | _long u-tehta_ | /uː/ (GOOSE)         | Double left-facing curl above base  |
|   ****    | `U+E050`   | _nasal bar_    | Preconsonantal nasal | Horizontal tilde above base stop    |

---

## Part 3: The Shavian-to-Tengwar Transliteration Bridge

By using Shavian as an Intermediate Representation (IR), transliteration bypasses non-phonetic English orthography entirely, converting text through a 5-pass state machine.

### 1. Direct Phoneme Mapping Matrix

| IPA Phoneme | Shavian Glyph | Tengwa          | Target Tengwa / Tehta           | Code Point Stream      | State Machine Transformation Rule                               |
| ----------- | ------------- | --------------- | ------------------------------- | ---------------------- | --------------------------------------------------------------- |
| /p/         | **𐑐**         | ****           | _Parma_                         | `U+E001`               | Direct 1:1 Consonant Base                                       |
| /b/         | **𐑚**         | ****           | _Umbar_                         | `U+E005`               | Direct 1:1 Consonant Base                                       |
| /t/         | **𐑑**         | ****           | _Tinco_                         | `U+E000`               | Direct 1:1 Consonant Base                                       |
| /d/         | **𐑛**         | ****           | _Ando_                          | `U+E004`               | Direct 1:1 Consonant Base                                       |
| /k/         | **𐑒**         | ****           | _Quesse_                        | `U+E003`               | Direct 1:1 Consonant Base                                       |
| /ɡ/         | **𐑜**         | ****           | _Ungwe_                         | `U+E007`               | Direct 1:1 Consonant Base                                       |
| /f/         | **𐑓**         | ****           | _Formen_                        | `U+E009`               | Direct 1:1 Consonant Base                                       |
| /v/         | **𐑝**         | ****           | _Ampa_                          | `U+E00D`               | Direct 1:1 Consonant Base                                       |
| /θ/         | **𐑔**         | ****           | _Thúle_                         | `U+E008`               | Direct 1:1 Consonant Base                                       |
| /ð/         | **𐑞**         | ****           | _Anta_                          | `U+E00C`               | Direct 1:1 Consonant Base                                       |
| /s/         | **𐑕**         | ****           | _Silme_ / _Nuquerna_            | `U+E024` / `U+E025`    | Flips to _Silme Nuquerna_ (`U+E025`) if top tehta present       |
| /z/         | **𐑟**         | ****           | _Esse_ / _Nuquerna_             | `U+E026` / `U+E027`    | Flips to _Esse Nuquerna_ (`U+E027`) if top tehta present        |
| /ʃ/         | **𐑖**         | ****           | _Harma_                         | `U+E00A`               | Direct 1:1 Consonant Base                                       |
| /ʒ/         | **𐑠**         | ****           | _Anca_                          | `U+E00E`               | Direct 1:1 Consonant Base                                       |
| /tʃ/        | **𐑗**         | ****           | _Calma_                         | `U+E002`               | Direct 1:1 Consonant Base                                       |
| /dʒ/        | **𐑡**         | ****           | _Anga_                          | `U+E006`               | Direct 1:1 Consonant Base                                       |
| /j/         | **𐑘**         | ****           | _Anna_                          | `U+E016`               | Direct 1:1 Consonant Base                                       |
| /w/         | **𐑢**         | ****           | _Vala_                          | `U+E015`               | Direct 1:1 Consonant Base                                       |
| /hw/        | **𐑣𐑢**        | ****           | _Hwesta_                        | `U+E00B`               | Lookahead intercept: Aspirated Wh cluster to _Hwesta_           |
| /ŋ/         | **𐑙**         | ****           | _Nwalme_                        | `U+E013`               | Direct 1:1 Consonant Base                                       |
| /h/         | **𐑣**         | ****           | _Hyarmen_                       | `U+E028`               | Direct 1:1 Consonant Base                                       |
| /l/         | **𐑤**         | ****           | _Lamba_                         | `U+E022`               | Direct 1:1 Consonant Base                                       |
| /m/         | **𐑥**         | ****           | _Malta_                         | `U+E011`               | Direct 1:1 Consonant Base                                       |
| /n/         | **𐑯**         | ****           | _Númen_                         | `U+E010`               | Direct 1:1 Consonant Base                                       |
| /r/         | **𐑮**         | **** / ****   | _Rómen_ / _Óre_                 | `U+E020` / `U+E014`    | Contextual: _Rómen_ before vowels; _Óre_ word-final/consonantal |
| /ɪ/         | **𐑦**         | ****          | _i-tehta_                       | `U+E044`               | Attach dot above next available consonant                       |
| /iː/        | **𐑰**         | ****          | _Ára_ + _i-tehta_               | `U+E02D U+E044`        | FLEECE vowel: Attach to Long Carrier or double acute on base    |
| /ɛ/         | **𐑧**         | ****          | _e-tehta_                       | `U+E046`               | Attach acute stroke above next available consonant              |
| /eɪ/        | **𐑱**         | ****          | _Anna_ + _e-tehta_              | `U+E016 U+E046`        | FACE diphthong: Offglide _Anna_ base + _e-tehta_                |
| /æ/         | **𐑨**         | ****          | _a-tehta_                       | `U+E040`               | Attach three dots above next available consonant                |
| /aɪ/        | **𐑲**         | ****          | _Anna_ + _a-tehta_              | `U+E016 U+E040`        | PRICE diphthong: Offglide _Anna_ base + _a-tehta_               |
| /ə/         | **𐑩**         | ****          | _schwa-tehta_                   | `U+E045`               | Attach single dot **below** next available consonant            |
| /ʌ/         | **𐑳**         | ****          | _u-tehta_                       | `U+E04C`               | STRUT vowel: Attach left curl above next available consonant    |
| /ɒ/         | **𐑪**         | ****          | _o-tehta_                       | `U+E04A`               | LOT vowel: Attach right curl above next available consonant     |
| /oʊ/        | **𐑴**         | ****          | _Vala_ + _o-tehta_              | `U+E015 U+E04A`        | GOAT diphthong: Offglide _Vala_ base + _o-tehta_                |
| /ʊ/         | **𐑫**         | ****          | _foot-tehta_                    | `U+E04C`               | FOOT vowel: Attach left curl above next available consonant     |
| /uː/        | **𐑵**         | ****          | _Ára_ + _u-tehta_               | `U+E02D U+E04C`        | GOOSE vowel: Attach to Long Carrier or double curl on base      |
| /aʊ/        | **𐑬**         | ****          | _Vala_ + _a-tehta_              | `U+E015 U+E040`        | MOUTH diphthong: Offglide _Vala_ base + _a-tehta_               |
| /ɔɪ/        | **𐑶**         | ****          | _Anna_ + _o-tehta_              | `U+E016 U+E04A`        | CHOICE diphthong: Offglide _Anna_ base + _o-tehta_              |
| /ɑː/        | **𐑭**         | ****          | _a-tehta_                       | `U+E040`               | PALM vowel: Attach three dots above next available consonant    |
| /ɔː/        | **𐑷**         | ****          | _awe-tehta_                     | `U+E04A`               | THOUGHT vowel: Attach right curl above next available consonant |
| /iə/        | **𐑾**         | ****          | _Anna_ + _i-tehta_              | `U+E016 U+E044`        | IAN ligature: Offglide _Anna_ base + _i-tehta_                  |
| /juː/       | **𐑿**         | ****          | _Anna_ + _u-tehta_              | `U+E016 U+E04C`        | YEW ligature: Offglide _Anna_ base + _u-tehta_                  |
| /ɑːr/       | **𐑸**         | **** / **** | _Rómen_ / _Óre_ + _a-tehta_     | `U+E020/U+E014 U+E040` | START vowel: Decomposes into R-base + _a-tehta_                 |
| /ɔːr/       | **𐑹**         | **** / **** | _Rómen_ / _Óre_ + _o-tehta_     | `U+E020/U+E014 U+E04A` | NORTH vowel: Decomposes into R-base + _o-tehta_                 |
| /ər/        | **𐑼**         | **** / **** | _Rómen_ / _Óre_ + _schwa-tehta_ | `U+E020/U+E014 U+E045` | lettER vowel: Decomposes into R-base + _schwa-tehta_            |
| /ɪər/       | **𐑽**         | **** / **** | _Rómen_ / _Óre_ + _i-tehta_     | `U+E020/U+E014 U+E044` | NEAR vowel: Decomposes into R-base + _i-tehta_                  |
| /ɛər/       | **𐑺**         | **** / **** | _Rómen_ / _Óre_ + _e-tehta_     | `U+E020/U+E014 U+E046` | SQUARE vowel: Decomposes into R-base + _e-tehta_                |
| /ɜːr/       | **𐑻**         | **** / **** | _Rómen_ / _Óre_ + _u-tehta_     | `U+E020/U+E014 U+E04C` | NURSE vowel: Decomposes into R-base + _u-tehta_                 |

---

### 2. The Big Five: Shorthand Logograms

| Target Word | Shavian IR | Tengwar Output | Glyph Name           | Code Point Stream | State Machine Rule                 |
| :---------- | :--------- | :------------- | :------------------- | :---------------- | :--------------------------------- |
| _the_       | **𐑞**      | ****          | _Extended Anta_      | `U+E01C`          | Standalone logogram for "the"      |
| _of_        | **𐑝**      | ****          | _Extended Ampa_      | `U+E01D`          | Standalone logogram for "of"       |
| _and_       | **𐑯**      | ****         | _Ando_ + _Nasal Bar_ | `U+E004 U+E050`   | Standalone shorthand for "and"     |
| _to_        | **𐑑**      | ****          | _Tinco_ Base         | `U+E000`          | Unadorned base shorthand for "to"  |
| _for_       | **𐑓**      | ****          | _Formen_ Base        | `U+E009`          | Unadorned base shorthand for "for" |

---

### 3. Verified Test Cases & Output Comparison

To verify visual output in Obsidian or PDF export, install **[Alcarin Tengwar](https://github.com/Tosche/Alcarin-Tengwar)**. The table below lists the exact Shavian input, rendered Tengwar output, Everson hex bytes, and feature rules applied:

| Word      | Shavian Input | Tengwar Output | Everson 2001 Hex Stream                            | Applied Rule / Logic                                                                                        |
| :-------- | :------------ | :------------- | :------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| _winter_  | `𐑢𐑦𐑯𐑑𐑼`       | ****     | `U+E015 U+E000 U+E050 U+E044 U+E014 U+E045`        | Universal Nasal Bar over _Tinco_ (``); _i-tehta_ attaches above bar; ends in _Óre_ + _schwa-tehta_.        |
| _chamber_ | `𐑗𐑱𐑥𐑚𐑼`       | ****    | `U+E002 U+E016 U+E046 U+E005 U+E050 U+E014 U+E045` | Preconsonantal nasal pair `𐑥𐑚` emits _Umbar_ + _Nasal Bar Above_ (`U+E050`); ends in _Óre_ + _schwa-tehta_. |
| _the_     | `𐑞`           | ****          | `U+E01C`                                           | Big Five abbreviation: Standalone character maps directly to _Extended Anta_ logogram.                      |
| _of_      | `𐑝`           | ****          | `U+E01D`                                           | Big Five abbreviation: Standalone character maps directly to _Extended Ampa_ logogram.                      |
| _and_     | `𐑯`           | ****         | `U+E004 U+E050`                                    | Big Five abbreviation: Standalone character maps directly to _Ando_ + _Nasal Bar Above_.                    |
| _to_      | `𐑑`           | ****          | `U+E000`                                           | Big Five abbreviation: Standalone character maps directly to _Tinco_ base.                                  |
| _for_     | `𐑓`           | ****          | `U+E009`                                           | Big Five abbreviation: Standalone character maps directly to _Formen_ base.                                 |
| _land_    | `𐑤𐑨𐑯𐑛`        | ****       | `U+E022 U+E004 U+E050 U+E040`                      | _Lamba_ (`U+E022`); Universal Nasal Bar over _Ando_ (``) with top _a-tehta_.                               |
| _wind_    | `𐑢𐑦𐑯𐑛`        | ****       | `U+E015 U+E004 U+E050 U+E044`                      | _Vala_ (`U+E015`); Universal Nasal Bar over _Ando_ (``) with top _i-tehta_.                                |
