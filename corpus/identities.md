# Corpus: declared identities

Every row is a test: `tests/test_corpus.py` translates the Shavian and compares the glyphs. Rule IDs refer to `spec/mode.md`; each cited rule must actually fire. Glyphs are the Tecendil-style literals, so they can be pasted into tecendil.com. These spellings are meant to be written the same (P-02).

## Ligatures and expansions

Each ligature is expanded to its components before any other rule runs (section 8 of the spec).

| A | B | Rules | Note |
|---|---|---|---|
| 𐑸 | 𐑭𐑮 | L-01 | START = PALM + r |
| 𐑹 | 𐑷𐑮 | L-02 | NORTH = THOUGHT + r |
| 𐑺 | 𐑧𐑮 | L-03 | SQUARE = DRESS + r |
| 𐑽 | 𐑦𐑮 | L-04 | NEAR = KIT + r |
| 𐑻 | 𐑳𐑮 | L-05 | NURSE = STRUT + r |
| 𐑼 | 𐑩𐑮 | L-06 | lettER = schwa + r |
| 𐑿 | 𐑘𐑵 | L-07 | YEW = y + GOOSE |
| 𐑾 | 𐑦𐑩 | L-08 | IAN = KIT + schwa |
| 𐑣𐑻 | 𐑣𐑳𐑮 | L-05 | her |
| 𐑕𐑑𐑸 | 𐑕𐑑𐑭𐑮 | L-01 | star |

## Diphthongs equal nucleus + glide

A diphthong is its nucleus followed by its glide, so these are the same sounds written the same way (I-01 to I-05).

| A | B | Rules | Note |
|---|---|---|---|
| 𐑱 | 𐑧𐑘 | I-01 | FACE = DRESS + j |
| 𐑴 | 𐑪𐑢 | I-02 | GOAT = LOT + w |
| 𐑶 | 𐑪𐑘 | I-03 | CHOICE = LOT + j |
| 𐑲 | 𐑨𐑘 | I-04 | PRICE = TRAP + j |
| 𐑬 | 𐑨𐑢 | I-05 | MOUTH = TRAP + w |
