# Corpus: vowels

Every row is a test: `tests/test_corpus.py` translates the Shavian and compares the glyphs. Rule IDs refer to `spec/mode.md`; each cited rule must actually fire. Glyphs are the Tecendil-style literals, so they can be pasted into tecendil.com. Vowels are named by their Wells keyword sets.

## Short vowels

Each short vowel sits on the next consonant (V-01). A short vowel with no consonant after it falls back to `{telco}` (V-02).

| Shavian | English | IPA | Glyphs | Rules |
|---|---|---|---|---|
| 𐑩 𐑚𐑦𐑜 𐑓𐑦𐑖 | a big fish | /ə bɪɡ fɪʃ/ | `{telco}[breve] {umbar}{ungwe}[dot-above] {formen}{harma}[dot-above]` | V-11 V-14 V-01 V-02 |
| 𐑜𐑧𐑑 𐑢𐑧𐑤 | get well | /ɡɛt wɛl/ | `{ungwe}{tinco}[acute] {vala}{lambe}[acute]` | V-12 V-01 |
| 𐑞 𐑚𐑤𐑨𐑒 𐑒𐑨𐑑 | the black cat | /ðə blæk kæt/ | `{the-shorthand} {umbar}{lambe}{quesse}[triple-dot-above] {quesse}{tinco}[triple-dot-above]` | V-13 V-01 W-01 |
| 𐑣𐑪𐑑 𐑐𐑪𐑑 | hot pot | /hɒt pɒt/ | `{hyarmen}{tinco}[right-curl] {parma}{tinco}[right-curl]` | V-15 V-01 |
| 𐑥𐑳𐑗 𐑓𐑳𐑯 | much fun | /mʌtʃ fʌn/ | `{malta}{calma}[grave] {formen}{nuumen}[grave]` | V-16 V-01 |
| 𐑜𐑫𐑛 𐑚𐑫𐑒 | good book | /ɡʊd bʊk/ | `{ungwe}{ando}[left-curl] {umbar}{quesse}[left-curl]` | V-17 V-01 |
| 𐑩𐑚𐑬𐑑 | about | /əbaʊt/ | `{umbar}[breve]{vala}[triple-dot-above]{tinco}` | V-14 V-01 D-02 |
| 𐑕𐑦𐑑𐑦 | city | /sɪtɪ/ | `{silme}{tinco}[dot-above]{telco}[dot-above]` | V-11 V-02 |

## Long vowels

A long vowel always takes the long carrier `{aara}`, whatever follows it (V-03). It never sits on a consonant.

| Shavian | English | IPA | Glyphs | Rules |
|---|---|---|---|---|
| 𐑕𐑰 𐑞 𐑕𐑰 | see the sea | /siː ðə siː/ | `{silme}{aara}[dot-above] {the-shorthand} {silme}{aara}[dot-above]` | V-21 V-03 W-01 |
| 𐑩 𐑒𐑭𐑥 𐑕𐑐𐑭 | a calm spa | /ə kɑːm spɑː/ | `{telco}[breve] {quesse}{aara}[triple-dot-above]{malta} {silme}{parma}{aara}[triple-dot-above]` | V-22 V-03 |
| 𐑷𐑤 𐑑𐑷𐑒 | all talk | /ɔːl tɔːk/ | `{aara}[right-curl]{lambe} {tinco}{aara}[right-curl]{quesse}` | V-23 V-03 |
| 𐑑𐑵 𐑒𐑵𐑤 | too cool | /tuː kuːl/ | `{tinco}{aara}[left-curl] {quesse}{aara}[left-curl]{lambe}` | V-24 V-03 |
| 𐑓𐑰𐑤 𐑓𐑮𐑰 | feel free | /fiːl friː/ | `{formen}{aara}[dot-above]{lambe} {formen}{roomen}{aara}[dot-above]` | V-21 R-01 |
| 𐑚𐑤𐑵 𐑥𐑵𐑯 | blue moon | /bluː muːn/ | `{umbar}{lambe}{aara}[left-curl] {malta}{aara}[left-curl]{nuumen}` | V-24 |

## R-coloured vowels

These ligatures are expanded to vowel + 𐑮 (L-01 to L-06), so the vowel mark sits on `{roomen}` and `{oore}` is never used.

| Shavian | English | IPA | Glyphs | Rules |
|---|---|---|---|---|
| 𐑩 𐑣𐑸𐑛 𐑒𐑸 | a hard car | /ə hɑːrd kɑːr/ | `{telco}[breve] {hyarmen}{aara}[triple-dot-above]{roomen}{ando} {quesse}{aara}[triple-dot-above]{roomen}` | L-01 R-01 |
| 𐑯𐑴 𐑥𐑹 | no more | /noʊ mɔːr/ | `{nuumen}{vala}[right-curl] {malta}{aara}[right-curl]{roomen}` | L-02 D-04 |
| 𐑓𐑺 𐑖𐑺 | fair share | /fɛr ʃɛr/ | `{formen}{roomen}[acute] {harma}{roomen}[acute]` | L-03 |
| 𐑩 𐑒𐑤𐑽 𐑘𐑽 | a clear year | /ə klɪr jɪr/ | `{telco}[breve] {quesse}{lambe}{roomen}[dot-above] {anna}{roomen}[dot-above]` | L-04 |
| 𐑣𐑻 𐑓𐑻𐑕𐑑 𐑢𐑻𐑛 | her first word | /hɜːr fɜːrst wɜːrd/ | `{hyarmen}{roomen}[grave] {formen}{roomen}[grave]{silme}{tinco} {vala}{roomen}[grave]{ando}` | L-05 |
| 𐑩 𐑚𐑧𐑑𐑼 𐑤𐑧𐑑𐑼 | a better letter | /ə bɛtər lɛtər/ | `{telco}[breve] {umbar}{tinco}[acute]{roomen}[breve] {lambe}{tinco}[acute]{roomen}[breve]` | L-06 |
| 𐑣𐑻𐑦 | hurry | /hɜːrɪ/ | `{hyarmen}{roomen}[grave]{telco}[dot-above]` | L-05 V-02 |

## Diphthongs

The glide letter is the last sound and carries the nucleus mark (D-01 to D-05). 𐑿 and 𐑾 are ligatures, not diphthongs (L-07, L-08).

| Shavian | English | IPA | Glyphs | Rules |
|---|---|---|---|---|
| 𐑩 𐑜𐑮𐑱𐑑 𐑛𐑱 | a great day | /ə ɡreɪt deɪ/ | `{telco}[breve] {ungwe}{roomen}{anna}[acute]{tinco} {ando}{anna}[acute]` | D-03 |
| 𐑩 𐑕𐑤𐑴 𐑚𐑴𐑑 | a slow boat | /ə sloʊ boʊt/ | `{telco}[breve] {silme}{lambe}{vala}[right-curl] {umbar}{vala}[right-curl]{tinco}` | D-04 |
| 𐑩 𐑚𐑮𐑲𐑑 𐑤𐑲𐑑 | a bright light | /ə braɪt laɪt/ | `{telco}[breve] {umbar}{roomen}{anna}[triple-dot-above]{tinco} {lambe}{anna}[triple-dot-above]{tinco}` | D-01 |
| 𐑩 𐑚𐑶𐑟 𐑑𐑶 | a boy's toy | /ə bɔɪz tɔɪ/ | `{telco}[breve] {umbar}{anna}[right-curl]{esse} {tinco}{anna}[right-curl]` | D-05 |
| 𐑩 𐑤𐑬𐑛 𐑒𐑮𐑬𐑛 | a loud crowd | /ə laʊd kraʊd/ | `{telco}[breve] {lambe}{vala}[triple-dot-above]{ando} {quesse}{roomen}{vala}[triple-dot-above]{ando}` | D-02 |
| 𐑩 𐑓𐑿 𐑝𐑿𐑟 | a few views | /ə fjuː vjuːz/ | `{telco}[breve] {formen}{anna}{aara}[left-curl] {ampa}{anna}{aara}[left-curl]{esse}` | L-07 |
| 𐑥𐑰𐑛𐑾 | media | /miːdɪə/ | `{malta}{aara}[dot-above]{ando}{telco}[dot-above]{telco}[breve]` | L-08 V-02 |
| ·𐑾𐑯 | Ian | /ɪən/ | `{telco}[dot-above]{nuumen}[breve]` | L-08 V-01 |
