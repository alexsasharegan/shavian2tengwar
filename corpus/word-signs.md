# Corpus: Shavian word signs

Every row is a test: `tests/test_corpus.py` translates the Shavian and compares the glyphs. Rule IDs refer to `spec/mode.md`; each cited rule must actually fire. Glyphs are the Tecendil-style literals, so they can be pasted into tecendil.com. Shavian abbreviates *the*, *of*, *and*, *to* and *for* to one letter each. The first three have Tengwar shorthands (W-01 to W-03); *to* and *for* are written as weak forms (W-04, L-09, L-10).

## Shorthands: the, of, and

| Shavian | English | IPA | Glyphs | Rules |
|---|---|---|---|---|
| 𐑞 𐑧𐑯𐑛 𐑝 𐑞 𐑮𐑴𐑛 | the end of the road | /ðə ɛnd əv ðə roʊd/ | `{the-shorthand} {ando}[acute][bar-above] {of-shorthand} {the-shorthand} {roomen}{vala}[right-curl]{ando}` | W-01 W-02 N-01 |
| 𐑚𐑮𐑧𐑛 𐑯 𐑚𐑳𐑑𐑼 | bread and butter | /brɛd ənd bʌtər/ | `{umbar}{roomen}{ando}[acute] {and-shorthand} {umbar}{tinco}[grave]{roomen}[breve]` | W-03 |
| 𐑩 𐑤𐑪𐑑 𐑝 𐑛𐑪𐑑𐑕 | a lot of dots | /ə lɒt əv dɒts/ | `{telco}[breve] {lambe}{tinco}[right-curl] {of-shorthand} {ando}{tinco}[right-curl]{silme}` | W-02 V-15 |

## Weak forms: to, for

Spelled out as /tə/ and /fər/, so they stay distinct from *too*/*two* and *four*.

| Shavian | English | IPA | Glyphs | Rules |
|---|---|---|---|---|
| 𐑓𐑮𐑳𐑥 𐑣𐑽 𐑑 𐑞𐑺 | from here to there | /frʌm hɪr tə ðɛr/ | `{formen}{roomen}{malta}[grave] {hyarmen}{roomen}[dot-above] {tinco}{telco}[breve] {anto}{roomen}[acute]` | W-04 L-09 |
| 𐑓 𐑿 | for you | /fər juː/ | `{formen}{roomen}[breve] {anna}{aara}[left-curl]` | W-04 L-10 |
| 𐑳𐑐-𐑑-𐑛𐑱𐑑 | up-to-date | /ʌp tə deɪt/ | `{parma}[grave]{section-mark}{tinco}{telco}[breve]{section-mark}{ando}{anna}[acute]{tinco}` | W-04 L-09 U-04 |

## Distinct: weak forms and their homophones

The signs exist in Shavian to tell homophones apart, so the Tengwar must too.

| A | B | Rules | Note |
|---|---|---|---|
| 𐑑 | 𐑑𐑵 | W-04 L-09 | to / too, two |
| 𐑓 | 𐑓𐑹 | W-04 L-10 | for / four |

## Weak forms equal their spelled-out sound

The signs expand to the weak-form spelling (L-09, L-10).

| A | B | Rules | Note |
|---|---|---|---|
| 𐑑 | 𐑑𐑩 | W-04 L-09 | to = t + schwa |
| 𐑓 | 𐑓𐑼 | W-04 L-10 | for = f + lettER |
