# Encoding: Alcarin Tengwar

Maps the glyph names in `spec/mode.md` to code points in
[Alcarin Tengwar](https://github.com/tosche/alcarin-tengwar) (Tosche). Every code point below was
checked against the font's cmap (`AlcarinTengwar-Regular.ttf`) on 2026-10-11.

Alcarin uses its own layout, derived from FreeTengwar. **It is not Everson's 2001 layout and not
CSUR.** The two differ at many code points, so never reuse a table written for either of them.
Examples: here `E018` is Extended Tinco (in CSUR it is rómen), and `E056` is three inverted dots
(in CSUR it is a long carrier below).

The font names its glyphs `uniXXXX`, so the names in the last column come from the font's
[character mapping README](https://github.com/tosche/alcarin-tengwar/blob/main/Character%20mapping/README.md).

## 1. Letters

| Glyph | Code point | Alcarin name |
|---|---|---|
| `{tinco}` | `U+E000` | TINCO |
| `{parma}` | `U+E001` | PARMA |
| `{calma}` | `U+E002` | CALMA |
| `{quesse}` | `U+E003` | QUESSE |
| `{ando}` | `U+E004` | ANDO |
| `{umbar}` | `U+E005` | UMBAR |
| `{anga}` | `U+E006` | ANGA |
| `{ungwe}` | `U+E007` | UNGWE |
| `{thuule}` | `U+E008` | THUULE (SUULE) |
| `{formen}` | `U+E009` | FORMEN |
| `{harma}` | `U+E00A` | HARMA (AHA) |
| `{hwesta}` | `U+E00B` | HWESTA |
| `{anto}` | `U+E00C` | ANTO |
| `{ampa}` | `U+E00D` | AMPA |
| `{anca}` | `U+E00E` | ANCA |
| `{nuumen}` | `U+E010` | NUUMEN |
| `{malta}` | `U+E011` | MALTA |
| `{nwalme}` | `U+E013` | NWALME (NGWALME) |
| `{vala}` | `U+E015` | VALA |
| `{anna}` | `U+E016` | ANNA |
| `{roomen}` | `U+E020` | ROOMEN |
| `{lambe}` | `U+E022` | LAMBE |
| `{silme}` | `U+E024` | SILME |
| `{silme-nuquerna}` | `U+E025` | SILME NUQUERNA |
| `{esse}` | `U+E026` | AARE (AAZE, ESSE) |
| `{esse-nuquerna}` | `U+E027` | AARE NUQUERNA |
| `{hyarmen}` | `U+E028` | HYARMEN |
| `{aara}` | `U+E02C` | LONG CARRIER (a descender, like an undotted *j*) |
| `{telco}` | `U+E02E` | SHORT CARRIER |

## 2. Marks

| Glyph | Code point | Alcarin name |
|---|---|---|
| `[triple-dot-above]` | `U+E040` | THREE DOTS ABOVE |
| `[dot-above]` | `U+E044` | AMATIXE (DOT ABOVE) |
| `[dot-below]` | `U+E045` | UNUTIXE (DOT BELOW) |
| `[acute]` | `U+E046` | ACUTE (ANDAITH, LONG MARK, TECCO) |
| `[right-curl]` | `U+E04A` | RIGHT CURL |
| `[left-curl]` | `U+E04C` | LEFT CURL |
| `[bar-above]` | `U+E050` | NASALIZER |
| `[bar-below]` | `U+E051` | DOUBLER |
| `[breve]` | `U+E053` | BREVE |
| `[grave]` | `U+E054` | GRAVE |

## 3. Shorthands and punctuation

| Glyph | Code point(s) | Alcarin name |
|---|---|---|
| `{the-shorthand}` | `U+E01C` | EXTENDED ANDO |
| `{of-shorthand}` | `U+E01D` | EXTENDED UMBAR |
| `{and-shorthand}` | `U+E004 U+E050 U+E045` | ANDO, NASALIZER, UNUTIXE (three code points) |
| `{pusta}` | `U+E060` | PUSTA |
| `{double-pusta}` | `U+E061` | DOUBLE PUSTA (two stacked dots) |
| `{triple-pusta}` | `U+E062` | TRIPLE PUSTA (three stacked dots) |
| `{section-mark}` | `U+E068` | SECTION MARK (renders as a tilde) |
| `{double-section-mark}` | `U+E069` | DOUBLE SECTION MARK |
| `{exclamation-mark}` | `U+E065` | EXCLAMATION MARK |
| `{question-mark}` | `U+E066` | QUESTION MARK |
| `{parenthesis-mark}` | `U+E067` | PARENTHESIS MARK (one glyph, used for both sides) |
| `{left-quotation-mark}` | `U+E06A` | LEFT QUOTATION MARK (sits high) |
| `{right-quotation-mark}` | `U+E06B` | RIGHT QUOTATION MARK (sits low) |

Alcarin has no hyphen glyph, so `-` uses `{section-mark}` (U-04).

## 4. Encoding rules

| ID | Rule |
|---|---|
| AE-01 | A cluster is written as its base code point followed by its mark code points in K-01 order. The font positions the marks with its own OpenType features. |
| AE-02 | The mode's nuquerna choice (S-02) is implemented by swapping `E024`/`E026` for `E025`/`E027`. |
| AE-03 | Mark stacking was verified with HarfBuzz through Raqm. Other renderers have not been checked. |
| AE-04 | The mode never emits `U+E014` (óre, R-02), `U+E048` (double acute, V-21), a doubled `U+E04C` (V-24), or `U+E056` (three inverted dots, formerly TRAP; see DECISIONS.md D-12). They stay in the font but are reserved. |

## 5. Alcarin glyphs the mode does not use

These are in the font and may matter later: `E00F` unque, `E012` noldo, `E017` vilya, `E021` arda,
`E023` alda, `E029` hwesta sindarinwa, `E02A` yanta, `E02B` uure, `E02D` halla, the extended series
`E018`–`E01F` (other than the two shorthands), and the "below" marks `E047`, `E049`, `E04B`, `E04D`, and `E056` (three inverted dots above).
