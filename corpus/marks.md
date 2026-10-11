# Corpus: question, exclamation, parentheses and quotes

Every row is a test: `tests/test_corpus.py` translates the Shavian and compares the glyphs. Rule IDs refer to `spec/mode.md`; each cited rule must actually fire. Glyphs are the Tecendil-style literals, so they can be pasted into tecendil.com.

## Marks

Alcarin has glyphs for these; the ASCII characters are mapped to them (U-05).

| Shavian | English | IPA | Glyphs | Rules |
|---|---|---|---|---|
| 𐑢𐑪𐑑 𐑩 𐑤𐑳𐑝𐑤𐑦 𐑛𐑱! | What a lovely day! | /wɒt ə lʌvlɪ deɪ/ | `{vala}{tinco}[right-curl] {telco}[breve] {lambe}{ampa}[grave]{lambe}{telco}[dot-above] {ando}{anna}[acute]{exclamation-mark}` | U-05 |
| 𐑦𐑟 𐑦𐑑 𐑜𐑫𐑛? | Is it good? | /ɪz ɪt ɡʊd/ | `{esse-nuquerna}[dot-above] {tinco}[dot-above] {ungwe}{ando}[left-curl]{question-mark}` | U-05 |
| 𐑞 𐑒𐑨𐑑 (𐑞 𐑚𐑤𐑨𐑒 𐑢𐑳𐑯) 𐑕𐑨𐑑. | The cat (the black one) sat. | /ðə kæt ðə blæk wʌn sæt/ | `{the-shorthand} {quesse}{tinco}[reversed-triple-dot-above] {parenthesis-mark}{the-shorthand} {umbar}{lambe}{quesse}[reversed-triple-dot-above] {vala}{nuumen}[grave]{parenthesis-mark} {silme}{tinco}[reversed-triple-dot-above]{double-pusta}` | U-05 U-01 |
| "𐑜𐑴 𐑕𐑤𐑴," 𐑕𐑧𐑛 𐑣𐑰. | "Go slow," said he. | /ɡoʊ sloʊ sɛd hiː/ | `{left-quotation-mark}{ungwe}{vala}[right-curl] {silme}{lambe}{vala}[right-curl]{pusta}{right-quotation-mark} {silme}{ando}[acute] {hyarmen}{aara}[dot-above]{double-pusta}` | U-05 U-01 |
| “𐑜𐑴 𐑕𐑤𐑴,” 𐑕𐑧𐑛 𐑣𐑰. | “Go slow,” said he. | /ɡoʊ sloʊ sɛd hiː/ | `{left-quotation-mark}{ungwe}{vala}[right-curl] {silme}{lambe}{vala}[right-curl]{pusta}{right-quotation-mark} {silme}{ando}[acute] {hyarmen}{aara}[dot-above]{double-pusta}` | U-05 U-01 |
