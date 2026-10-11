# Orthography vs. Phonology: The Philosophy of shavian2tengwar

While the Tengwar community possesses documented conventions for writing English — including resources from [Chad Bornholdt's Tengwar Training Spreadsheet](https://www.texastolkien.com/home/tolkien-resources-helpful-links) and [Tecendil's Tengwar Handbook](https://www.tecendil.com/tengwar-handbook/) — these systems are orthographically biased. They often have an implicit dependency on English spelling, assigning Tengwar characters based on Latin letters rather than raw phonetics.

For standard communication as well as facilitating learning, orthographic modes build upon English literacy. True phonemic transcription is tricky, as it is highly sensitive to dialectal differences. However, analysing the poetry of J.R.R. Tolkien exposes the drawbacks of the orthodox English alphabet and the benefits of Tengwar. As a featural, phonetic script, Tengwar reveals the phonetic mechanics (meter, assonance, alliteration) that orthodox spelling obscures.

To solve this, `shavian2tengwar` completely bypasses English orthography. We use the Shavian alphabet — a strictly phonemic, 40-to-48-character script (8 ligatures) featuring a standardized "Rhotic RP" dialectal base — as a deterministic Intermediate Representation (IR). Because Shavian feeds our engine pure phonemes instead of English spelling, our Tengwar output adheres to strict phonetic rules.

This architectural choice necessitates several deliberate deviations from the community's orthographic norms.

## Deliberate Deviations from Community Norms

### 1. The Schwa as a Breve Above (`U+E053`)

**The Community Norm:** Standard English modes explicitly reserve the under-dot diacritic to represent a silent 'e' on the preceding consonant (e.g., the 'e' in _dade_).

**Our Engine:** Because Shavian maps pure sound, silent letters do not exist in our data stream. We leave the under-dot alone and write the unstressed schwa (`/ə/`) as a breve above the base. English relies heavily on vowel reduction, and a dedicated schwa tehta lets us distinguish fully stressed from reduced vowels with a precision that standard orthographic modes lack. Placing it above keeps every vowel tehta in one position, and avoids repurposing a mark the community already reads as silent 'e'.

### 2. True Phonetic Gemination (The Under-bar `U+E051`)

**The Community Norm:** Orthographic modes use the gemination bar (a horizontal line below the base _tengwa_) to represent doubled spelling letters, such as the _tt_ in _butter_.

**Our Engine:** Shavian never doubles consonants unless they are actually articulated twice across a syllable or morpheme boundary (e.g., _unnamed_ or _midday_). We reserve the gemination bar strictly for true phonetic doubling. This aligns our engine closer to Tolkien’s original linguistic intent for his Elvish languages, where double consonants denote a physically lengthened phonetic hold rather than a spelling quirk.

### 3. Strict Phonetic Diphthongs

**The Community Norm:** Traditional modes map vowel combinations based on their Latin pairings, requiring a complex web of _tengwa/tehta_ combinations (such as _Yanta_ vs. _Anna_ or _Úre_ vs. _Vala_) depending on whether the word is spelled with an 'ai', 'ea', 'ay', or 'ou'.

**Our Engine:** We treat diphthongs purely as phonetic movements, bypassing historical Latin spelling entirely. The offglide is the base and the starting vowel is its tehta: _Anna_ for front-closing `/j/` glides (PRICE `/aɪ/`, FACE `/eɪ/`, CHOICE `/ɔɪ/`) and _Vala_ for back-closing `/w/` glides (MOUTH `/aʊ/`, GOAT `/oʊ/`). A tehta is read before its base, so the glide really is last: `{anna}[acute]` is /e/ then /j/, the same order as the sounds. 𐑾 is written as 𐑦𐑩 and 𐑿 as 𐑘𐑵.

### 4. Rejecting the Terminal S-Hook (`sa-rincë`)

**The Community Norm:** Trailing `-s` appears constantly in written English due to plurals and possessives. Orthographic modes routinely apply the `sa-rincë` terminal hook for brevity, regardless of whether the suffix is pronounced as an unvoiced `/s/` (_cats_) or a voiced `/z/` (_dogs_).

**Our Engine:** ReadLex Rule 2 enforces strict phonetic voicing assimilation for suffixes. To preserve this critical acoustic distinction, we reject the generic `sa-rincë`. Instead, our engine outputs explicit _Silmë_ bases ( or ) for terminal `/s/` and explicit _Essë_ bases ( or ) for terminal `/z/`.

### 5. Logograms and Weak Forms

**The Community Norm:** Specific shorthand logograms are used for common function words, such as _Extended Ando_ (`U+E01C`) for "the" and _Extended Umbar_ (`U+E01D`) for "of". Some community variants append the under-dot to these extended stems to account for a silent 'e'.

**Our Engine:** We adopted the core Appendix E logograms. _the_ and _of_ stay unadorned. _and_ is written _Ando_ + _Nasal Bar Above_ + _Under-dot_ (`U+E004 U+E050 U+E045`). Because the schwa now sits above the base as a breve, the under-dot no longer competes with a vowel tehta and is free to serve as a word-sign here. Shavian has two more word signs, 𐑑 _to_ and 𐑓 _for_, that the Tengwar community has no settled shorthand for. They are written as their weak forms (/tə/, /fər/), which keeps them apart from _too/two_ and _four_ just as the Shavian signs do. This part is provisional; see [ADR-0005](./adr/0005-weak-forms-for-to-and-for.md).

### 6. R Is Always Rómen

**The Community Norm:** The Quenya-based rule writes _Rómen_ before a vowel and _Óre_ otherwise, which records whether an r is pronounced.

**Our Engine:** Our baseline is rhotic, so every r is pronounced and that distinction carries no information. 𐑮 is always _Rómen_ and _Óre_ is never used. The R-vowels (NEAR, SQUARE, START, NORTH, NURSE, lettER) are not separate glyphs: each expands to its vowel followed by 𐑮, so they come out the way the sounds are built.

### 7. Every Vowel Gets Its Own Mark; Length Has Its Own Carrier

**The Community Norm:** Orthographic modes reuse a few tehtar for many vowels and show length by doubling a mark or a spelling convention.

**Our Engine:** Shavian distinguishes eleven monophthongs, so the output does too. STRUT and the schwa each have a mark of their own. Every long vowel (FLEECE, PALM, THOUGHT, GOOSE) always sits on the long carrier, _Ára_, with the same mark as its short partner (KIT, TRAP, LOT, FOOT); Shavian has no short /ɑ/, so PALM shares TRAP's triple dot. A vowel's length is therefore never signalled by doubling a mark, and a short vowel can never be mistaken for a long one.

---

I welcome constructive criticism and correction from fluent Tengwar practitioners, but I hope that my goals are clear: I prioritize zero-Latin dependencies and adherence to Shavian's 40 core phonemes to produce Tengwar output which reads deterministically how it sounds.
