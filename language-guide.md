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

## Part 2: Tolkien's Tengwar & CSUR Standard

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
| **Grade 5: Nasals** _(Short Stem, Double Loop)_<br>               | ****<br> <br>`U+E010`<br> <br>_Númen_ (/n/)     | ****<br> <br>`U+E011`<br> <br>_Malta_ (/m/)  | ****<br> <br>`U+E012`<br> <br>_Noldo_ (/ŋ/) | ****<br> <br>`U+E013`<br> <br>_Nwalme_ (/nw/) |
| **Grade 6: Glides / Semi-vowels** _(Short Stem, Single Loop)_<br> | ****<br> <br>`U+E014`<br> <br>_Óre_ (/r/ final) | ****<br> <br>`U+E015`<br> <br>_Vala_ (/w/)   | ****<br> <br>`U+E016`<br> <br>_Anna_ (/j/)  | ****<br> <br>`U+E017`<br> <br>_Vilya_         |

---

### 2. Additional & Irregular Tengwar

Beyond the standard 24-tengwa grid, specialized base characters handle liquids, sibilants, glottal sounds, and silent carriers:

| Tengwa Glyph | Code Point | Tengwa Name             | Structural Description / Function                      |
| ------------ | ---------- | ----------------------- | ------------------------------------------------------ |
| ****        | `U+E018`   | _Rómen_                 | Trilled/vocalic /r/ (used before vowels)               |
| ****        | `U+E01A`   | _Lamba_                 | Upward hooked liquid character (/l/)                   |
| ****        | `U+E024`   | _Silme_                 | Upright S-curve sibilant (/s/)                         |
| ****        | `U+E025`   | _Silme Nuquerna_        | Inverted S-curve (used when carrying top tehta)        |
| ****        | `U+E026`   | _Esse_ / _Aze_          | Z-curve / inverted double loop (/z/)                   |
| ****        | `U+E027`   | _Esse Nuquerna_         | Inverted Z-curve (used when carrying top tehta)        |
| ****        | `U+E020`   | _Hyarmen_               | Downward stem with left hook (/h/)                     |
| ****        | `U+E028`   | _Telco_ (Short Carrier) | Unadorned vertical pillar carrying short orphan vowels |
| ****        | `U+E029`   | _Ára_ (Long Carrier)    | Extended vertical pillar carrying long orphan vowels   |

---

### 3. Vowel Tehtar & Diacritic Marks

In English General Mode, vowel diacritics (_tehtar_) sit directly above or below the following consonant base glyph:

| Tehta Mark | CSUR Hex | Tehta Name     | Phonetic Mapping     | Visual Placement                    |
| ---------- | -------- | -------------- | -------------------- | ----------------------------------- |
| ****      | `U+E040` | _a-tehta_      | /æ/, /ɑː/, /aɪ/      | Three dots in a triangle above base |
| ****      | `U+E044` | _i-tehta_      | /ɪ/, /iː/            | Single dot above base               |
| ****      | `U+E045` | _schwa-tehta_  | /ə/ (schwa)          | Single dot **below** base           |
| ****      | `U+E046` | _e-tehta_      | /ɛ/, /eɪ/            | Single acute stroke above base      |
| ****      | `U+E047` | _long e-tehta_ | /iː/ (FLEECE)        | Double acute stroke above base      |
| ****      | `U+E04A` | _o-tehta_      | /ɒ/, /ɔː/, /oʊ/      | Right-facing curl above base        |
| ****      | `U+E04C` | _u-tehta_      | /ʌ/, /ʊ/, /uː/       | Left-facing curl above base         |
| ****      | `U+E04D` | _long u-tehta_ | /uː/ (GOOSE)         | Double left-facing curl above base  |
| ****      | `U+E04E` | _nasal bar_    | Preconsonantal nasal | Horizontal tilde above base stop    |

---

## Part 3: The Shavian-to-Tengwar Transliteration Bridge

By using Shavian as an Intermediate Representation (IR), transliteration bypasses non-phonetic English orthography entirely, converting text through a 5-pass state machine.

### 1. Direct Phoneme Mapping Matrix

| Shavian Glyph | IPA Phoneme | Target Tengwa / Tehta | CSUR Hex Stream     | State Machine Transformation Rule                         |
| ------------- | ----------- | --------------------- | ------------------- | --------------------------------------------------------- |
| **𐑐**         | /p/         | _Parma_               | `U+E001`            | Direct 1:1 Consonant Base                                 |
| **𐑚**         | /b/         | _Umbar_               | `U+E005`            | Direct 1:1 Consonant Base                                 |
| **𐑑**         | /t/         | _Tinco_               | `U+E000`            | Direct 1:1 Consonant Base                                 |
| **𐑛**         | /d/         | _Ando_                | `U+E004`            | Direct 1:1 Consonant Base                                 |
| **𐑒**         | /k/         | _Quesse_              | `U+E003`            | Direct 1:1 Consonant Base                                 |
| **𐑜**         | /ɡ/         | _Ungwe_               | `U+E007`            | Direct 1:1 Consonant Base                                 |
| **𐑓**         | /f/         | _Formen_              | `U+E009`            | Direct 1:1 Consonant Base                                 |
| **𐑝**         | /v/         | _Ampa_                | `U+E00D`            | Direct 1:1 Consonant Base                                 |
| **𐑔**         | /θ/         | _Thúle_               | `U+E008`            | Direct 1:1 Consonant Base                                 |
| **𐑞**         | /ð/         | _Anta_                | `U+E00C`            | Direct 1:1 Consonant Base                                 |
| **𐑕**         | /s/         | _Silme_ / _Nuquerna_  | `U+E01C` / `U+E01D` | Flips to _Silme Nuquerna_ (`U+E01D`) if top tehta present |
| **𐑟**         | /z/         | _Esse_ / _Nuquerna_   | `U+E01E` / `U+E01F` | Flips to _Esse Nuquerna_ (`U+E01F`) if top tehta present  |
| **𐑦**         | /ɪ/         | _i-tehta_             | `U+E044`            | Attach dot above next available consonant                 |
| **𐑧**         | /ɛ/         | _e-tehta_             | `U+E046`            | Attach acute stroke above next available consonant        |
| **𐑨**         | /æ/         | _a-tehta_             | `U+E040`            | Attach three dots above next available consonant          |
| **𐑩**         | /ə/         | _schwa-tehta_         | `U+E045`            | Attach single dot **below** next available consonant      |
| **𐑻**         | /ɜːr/       | _Rómen_ + _u-tehta_   | `U+E018 U+E04C`     | NURSE vowel: Decomposes into _Rómen_ + _u-tehta_<br>      |
| **𐑺**         | /ɛər/       | _Rómen_ + _e-tehta_   | `U+E018 U+E046`     | SQUARE vowel: Decomposes into _Rómen_ + _e-tehta_<br>     |
| **𐑼**         | /ər/        | _Óre_                 | `U+E014`            | lettER vowel: Decomposes into unadorned _Óre_<br>         |
| **𐑲**         | /aɪ/        | _Anna_ + _a-tehta_    | `U+E016 U+E040`     | PRICE diphthong: Offglide _Anna_ base + _a-tehta_<br>     |
| **𐑴**         | /oʊ/        | _Vala_ + _o-tehta_    | `U+E015 U+E04A`     | GOAT diphthong: Offglide _Vala_ base + _o-tehta_<br>      |

---

### 2. Verified Test Cases & Output Comparison

To verify visual output in Obsidian or PDF export, install **[Alcarin Tengwar](https://github.com/Tosche/Alcarin-Tengwar)**. The table below lists the exact Shavian input, rendered Tengwar output, CSUR hex bytes, and feature rules applied:

| Word          | Shavian Input | CSUR Tengwar Output | CSUR Hex Stream                                           | Applied Rule / Logic                                                          |
| ------------- | ------------- | ------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- |
| _winter_<br>  | `𐑢𐑦𐑯𐑑𐑼`       | ****           | `U+E015 U+E010 U+E044 U+E000 U+E014`                      | _i-tehta_ attaches to _Númen_; _Tinco_ follows; ends in _Óre_.                |
| _chamber_<br> | `𐑗𐑱𐑥𐑚𐑼`       | ****          | `U+E002 U+E016 U+E046 U+E005 U+E04E U+E014`               | Nasal pair `𐑥𐑚` lacks vowel, emitting _Umbar_ + _Nasal Bar Above_ (`U+E04E`). |
| _third_<br>   | `𐑔𐑻𐑛`         | ****            | `U+E008 U+E018 U+E04C U+E004`                             | NURSE vowel `𐑻` decomposes into _Rómen_ + _u-tehta_ (`U+E04C`).               |
| _hair_        | `𐑣𐑺`          | ****             | `U+E020 U+E018 U+E046`                                    | SQUARE vowel `𐑺` decomposes into _Rómen_ + _e-tehta_ (`U+E046`).              |
| _bruised_<br> | `𐑚𐑮𐑵𐑟𐑛`       | ****           | `U+E005 U+E018 U+E01F U+E04D U+E004`                      | Carrying _double u-curl_ forces _Esse_ to flip to _Esse Nuquerna_ (`U+E01F`). |
| _merry_<br>   | `𐑥𐑧𐑮𐑦`        | ****           | `U+E011 U+E018 U+E046 U+E028 U+E044`                      | Word-final short vowel attaches to _Short Carrier_ (_Telco_, `U+E028`).       |
| _he_<br>      | `𐑣𐑰`          | ****             | `U+E020 U+E029 U+E044`                                    | Word-final long vowel attaches to _Long Carrier_ (_Ára_, `U+E029`).           |
| _lady's_<br>  | `𐑤𐑱𐑛𐑦’𐑟`      | **’**        | `U+E01A U+E016 U+E046 U+E004 U+E028 U+E044 U+2019 U+E01E` | Contraction apostrophe splits token; trailing _Esse_ is unadorned.            |
