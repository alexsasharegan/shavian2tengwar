# Orthography vs. Phonology: The Philosophy of shavian2tengwar

While the Tengwar community possesses documented conventions for writing English — including resources from [Chad Bornholdt's Tengwar Training Spreadsheet](https://www.texastolkien.com/home/tolkien-resources-helpful-links) and [Tecendil's Tengwar Handbook](https://www.tecendil.com/tengwar-handbook/) — these systems are orthographically biased. They often have an implicit dependency on English spelling, assigning Tengwar characters based on Latin letters rather than raw phonetics.

For standard communication as well as facilitating learning, orthographic modes build upon English literacy. True phonemic transcription is tricky, as it is highly sensitive to dialectal differences. However, analysing the poetry of J.R.R. Tolkien exposes the drawbacks of the orthodox English alphabet and the benefits of Tengwar. As a featural, phonetic script, Tengwar reveals the phonetic mechanics (meter, assonance, alliteration) that orthodox spelling obscures.

To solve this, `shavian2tengwar` completely bypasses English orthography. We use the Shavian alphabet — a strictly phonemic, 40-to-48-character script (8 ligatures) featuring a standardized "Rhotic RP" dialectal base — as a deterministic Intermediate Representation (IR). Because Shavian feeds our engine pure phonemes instead of English spelling, our Tengwar output adheres to strict phonetic rules.

This architectural choice necessitates several deliberate deviations from the community's orthographic norms.

## Deliberate Deviations from Community Norms

### 1. Repurposing the Under-dot (`unutixë`) for the Schwa

**The Community Norm:** Standard English modes explicitly reserve the under-dot diacritic to represent a silent 'e' on the preceding consonant (e.g., the 'e' in _dade_).
**Our Engine:** Because Shavian maps pure sound, silent letters do not exist in our data stream. Rather than discarding the diacritic, we repurposed the under-dot to represent the unstressed schwa (`/ə/`). English relies heavily on vowel reduction; deploying the under-dot exclusively for the schwa allows us to distinguish between fully stressed and reduced vowels with a precision that standard orthographic modes lack.

### 2. True Phonetic Gemination (The Under-bar `U+E051`)

**The Community Norm:** Orthographic modes use the gemination bar (a horizontal line below the base _tengwa_) to represent doubled spelling letters, such as the _tt_ in _butter_.
**Our Engine:** Shavian never doubles consonants unless they are actually articulated twice across a syllable or morpheme boundary (e.g., _unnamed_ or _midday_). We reserve the gemination bar strictly for true phonetic doubling. This aligns our engine closer to Tolkien’s original linguistic intent for his Elvish languages, where double consonants denote a physically lengthened phonetic hold rather than a spelling quirk.

### 3. Strict Phonetic Diphthongs

**The Community Norm:** Traditional modes map vowel combinations based on their Latin pairings, requiring a complex web of _tengwa/tehta_ combinations (such as _Yanta_ vs. _Anna_ or _Úre_ vs. _Vala_) depending on whether the word is spelled with an 'ai', 'ea', 'ay', or 'ou'.
**Our Engine:** We treat diphthongs purely as phonetic movements, bypassing historical Latin spelling entirely. We map them uniformly by placing the primary vowel _tehta_ directly onto the appropriate phonetic offglide carrier: _Anna_ for front-closing `/j/` glides (e.g., PRICE `/aɪ/`, FACE `/eɪ/`) and _Vala_ for back-closing `/w/` glides (e.g., MOUTH `/aʊ/`, GOAT `/oʊ/`).

### 4. Rejecting the Terminal S-Hook (`sa-rince`)

**The Community Norm:** Trailing `-s` appears constantly in written English due to plurals and possessives. Orthographic modes routinely apply the `sa-rince` terminal hook for brevity, regardless of whether the suffix is pronounced as an unvoiced `/s/` (_cats_) or a voiced `/z/` (_dogs_).
**Our Engine:** ReadLex Rule 2 enforces strict phonetic voicing assimilation for suffixes. To preserve this critical acoustic distinction, we reject the generic `sa-rince`. Instead, our engine outputs explicit _Silmë_ bases (`` or ``) for terminal `/s/` and explicit _Essë_ bases (`` or ``) for terminal `/z/`.

### 5. Unadorned Logograms

**The Community Norm:** Specific shorthand logograms are used for common function words, such as _Extended Anta_ (``, `U+E01C`) for "the" and _Extended Ampa_ (``, `U+E01D`) for "of". Some community variants append the under-dot to these extended stems to account for a silent 'e'.
**Our Engine:** We adopted the core Appendix E logograms but strictly avoid adorning them. Because our engine fiercely protects the under-dot as the schwa, placing it under an extended carrier as a static word-sign would introduce visual and mechanical confusion. Our logograms remain unadorned to preserve the semantic integrity of the vowel diacritics.

---

I welcome constructive criticism and correction from fluent Tengwar practitioners, but I hope that my goals are clear: I prioritize zero-Latin dependencies and adherence to Shavian's 40 core phonemes to produce Tengwar output which reads deterministically how it sounds.
