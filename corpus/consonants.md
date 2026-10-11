# Corpus: consonants and clusters

Every row is a test: `tests/test_corpus.py` translates the Shavian and compares the glyphs. Rule IDs refer to `spec/mode.md`; each cited rule must actually fire. Glyphs are the Tecendil-style literals, so they can be pasted into tecendil.com.

## Consonant inventory

One word per consonant letter (C-01), plus aspirated *wh* (C-02) and R (R-01).

| Shavian | English | IPA | Glyphs | Rules |
|---|---|---|---|---|
| 𐑐𐑲 | pie | /paɪ/ | `{parma}{anna}[triple-dot-above]` | C-01 |
| 𐑚𐑲 | buy | /baɪ/ | `{umbar}{anna}[triple-dot-above]` | C-01 |
| 𐑑𐑲 | tie | /taɪ/ | `{tinco}{anna}[triple-dot-above]` | C-01 |
| 𐑛𐑲 | dye | /daɪ/ | `{ando}{anna}[triple-dot-above]` | C-01 |
| 𐑒𐑰 | key | /kiː/ | `{quesse}{aara}[dot-above]` | C-01 |
| 𐑜𐑴 | go | /ɡoʊ/ | `{ungwe}{vala}[right-curl]` | C-01 |
| 𐑗𐑦𐑯 | chin | /tʃɪn/ | `{calma}{nuumen}[dot-above]` | C-01 |
| 𐑡𐑦𐑯 | gin | /dʒɪn/ | `{anga}{nuumen}[dot-above]` | C-01 |
| 𐑓𐑰 | fee | /fiː/ | `{formen}{aara}[dot-above]` | C-01 |
| 𐑝𐑨𐑯 | van | /væn/ | `{ampa}{nuumen}[triple-dot-above]` | C-01 |
| 𐑔𐑦𐑯 | thin | /θɪn/ | `{thuule}{nuumen}[dot-above]` | C-01 |
| 𐑞𐑧𐑯 | then | /ðɛn/ | `{anto}{nuumen}[acute]` | C-01 |
| 𐑖𐑲 | shy | /ʃaɪ/ | `{harma}{anna}[triple-dot-above]` | C-01 |
| 𐑥𐑧𐑠𐑼 | measure | /mɛʒər/ | `{malta}{anca}[acute]{roomen}[breve]` | C-01 |
| 𐑥𐑱 | may | /meɪ/ | `{malta}{anna}[acute]` | C-01 |
| 𐑯𐑴 | no | /noʊ/ | `{nuumen}{vala}[right-curl]` | C-01 |
| 𐑕𐑦𐑙 | sing | /sɪŋ/ | `{silme}{nwalme}[dot-above]` | C-01 |
| 𐑤𐑲 | lie | /laɪ/ | `{lambe}{anna}[triple-dot-above]` | C-01 |
| 𐑮𐑲 | rye | /raɪ/ | `{roomen}{anna}[triple-dot-above]` | R-01 |
| 𐑢𐑲 | why | /waɪ/ | `{vala}{anna}[triple-dot-above]` | C-01 |
| 𐑘𐑧𐑕 | yes | /jɛs/ | `{anna}{silme-nuquerna}[acute]` | C-01 |
| 𐑣𐑲 | hi | /haɪ/ | `{hyarmen}{anna}[triple-dot-above]` | C-01 |
| 𐑣𐑢𐑦𐑗 | which | /ʍɪtʃ/ | `{hwesta}{calma}[dot-above]` | C-02 |

## Silmë and Essë

/s/ and /z/ keep their own letters, and flip to the nuquerna form when a mark lands on them (S-01, S-02).

| Shavian | English | IPA | Glyphs | Rules |
|---|---|---|---|---|
| 𐑕𐑰 𐑞 𐑕𐑰 | see the sea | /siː ðə siː/ | `{silme}{aara}[dot-above] {the-shorthand} {silme}{aara}[dot-above]` | S-01 |
| 𐑟𐑵 𐑟𐑵𐑟 | zoo zoos | /zuː zuːz/ | `{esse}{aara}[left-curl] {esse}{aara}[left-curl]{esse}` | S-01 |
| 𐑦𐑟 | is | /ɪz/ | `{esse-nuquerna}[dot-above]` | S-02 |
| 𐑳𐑕 | us | /ʌs/ | `{silme-nuquerna}[grave]` | S-02 |
| 𐑨𐑕𐑒 | ask | /æsk/ | `{silme-nuquerna}[triple-dot-above]{quesse}` | S-02 V-01 |
| 𐑕𐑦𐑑 | sit | /sɪt/ | `{silme}{tinco}[dot-above]` | S-01 |

## Nasals before stops

A nasal plus its homorganic stop is the stop with a nasal bar (N-01). 𐑙𐑒 and 𐑙𐑜 are written the same way (N-02). A lone 𐑙 is `{nwalme}`; a /ɡ/ is written only where the Shavian has 𐑜.

| Shavian | English | IPA | Glyphs | Rules |
|---|---|---|---|---|
| 𐑣𐑨𐑯𐑛 | hand | /hænd/ | `{hyarmen}{ando}[triple-dot-above][bar-above]` | N-01 |
| 𐑕𐑧𐑯𐑑 | sent | /sɛnt/ | `{silme}{tinco}[acute][bar-above]` | N-01 |
| 𐑡𐑳𐑥𐑐 | jump | /dʒʌmp/ | `{anga}{parma}[grave][bar-above]` | N-01 |
| 𐑯𐑳𐑥𐑚𐑼 | number | /nʌmbər/ | `{nuumen}{umbar}[grave][bar-above]{roomen}[breve]` | N-01 |
| 𐑔𐑦𐑙𐑒 | think | /θɪŋk/ | `{thuule}{quesse}[dot-above][bar-above]` | N-02 K-01 |
| 𐑓𐑦𐑙𐑜𐑼 | finger | /fɪŋɡər/ | `{formen}{ungwe}[dot-above][bar-above]{roomen}[breve]` | N-02 |
| 𐑕𐑦𐑙𐑦𐑙 | singing | /sɪŋɪŋ/ | `{silme}{nwalme}[dot-above]{nwalme}[dot-above]` | C-01 V-01 |

## Gemination

Shavian only doubles a consonant that is really sounded twice, so the doubling bar is phonetic (G-01).

| Shavian | English | IPA | Glyphs | Rules |
|---|---|---|---|---|
| 𐑥𐑦𐑛𐑛𐑱 | midday | /mɪddeɪ/ | `{malta}{ando}[dot-above][bar-below]{anna}[acute]` | G-01 |
| 𐑳𐑯𐑯𐑱𐑥𐑛 | unnamed | /ʌnneɪmd/ | `{nuumen}[grave][bar-below]{anna}[acute]{malta}{ando}` | G-01 |

## Schwa and clusters

A schwa is always written (P-03), so a consonant cluster and a schwa between consonants never look alike.

| Shavian | English | IPA | Glyphs | Rules |
|---|---|---|---|---|
| 𐑐𐑤𐑲𐑑 | plight | /plaɪt/ | `{parma}{lambe}{anna}[triple-dot-above]{tinco}` | D-01 |
| 𐑐𐑩𐑤𐑲𐑑 | polite | /pəlaɪt/ | `{parma}{lambe}[breve]{anna}[triple-dot-above]{tinco}` | V-14 V-01 |
| 𐑕𐑐𐑹𐑑 | sport | /spɔːrt/ | `{silme}{parma}{aara}[right-curl]{roomen}{tinco}` | L-02 |
| 𐑕𐑩𐑐𐑹𐑑 | support | /səpɔːrt/ | `{silme}{parma}[breve]{aara}[right-curl]{roomen}{tinco}` | V-14 |
