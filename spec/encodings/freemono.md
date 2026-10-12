# Encoding: FreeMonoTengwar

Maps the glyph names in `spec/mode.md` to code points in FreeMonoTengwar (Free Tengwar Font Project,
version 2013-07-21, GPLv3 or later with the font-embedding exception). Every code point below was read
from the font's own cmap (`FreeMonoTengwar.ttf`) on 2026-10-11, and the last column is the font's own
glyph name for it (`post` table). None was copied from another table.

**Status:** every rule here is `ADOPTED` (approved by merging PR #3; project 0003, ADR-0011, ADR-0012).

For every glyph the mode uses, FreeMonoTengwar's code points are the same as Alcarin's
(`spec/encodings/alcarin.md`): both fonts follow the FreeTengwar layout. That was found by reading each
font, not assumed. Like Alcarin, it is **not** Everson's 2001 layout and not CSUR: `E018` is
Extended Tinco, not rómen.

FreeMonoTengwar is monospaced. Every glyph is 600 units wide (1000 per em), and every tehta is a
zero-width outline drawn back into the preceding cell at a fixed height. It needs no OpenType or AAT
positioning for the mode's clusters, so it renders the same in Core Text (Safari, TextEdit, Pages) and in
Chrome (the review sheet and the PDFs).

## 1. Letters

| Glyph | Code point(s) | FreeMonoTengwar glyph name |
|---|---|---|
| `{tinco}` | `U+E000` | `tinco` |
| `{parma}` | `U+E001` | `parma` |
| `{calma}` | `U+E002` | `calma` |
| `{quesse}` | `U+E003` | `quesse` |
| `{ando}` | `U+E004` | `ando` |
| `{umbar}` | `U+E005` | `umbar` |
| `{anga}` | `U+E006` | `anga` |
| `{ungwe}` | `U+E007` | `ungwe` |
| `{thuule}` | `U+E008` | `suule` |
| `{formen}` | `U+E009` | `formen` |
| `{harma}` | `U+E00A` | `aha` |
| `{hwesta}` | `U+E00B` | `hwesta` |
| `{anto}` | `U+E00C` | `anto` |
| `{ampa}` | `U+E00D` | `ampa` |
| `{anca}` | `U+E00E` | `anca` |
| `{nuumen}` | `U+E010` | `nuumen` |
| `{malta}` | `U+E011` | `malta` |
| `{nwalme}` | `U+E013` | `nwalme` |
| `{vala}` | `U+E015` | `vala` |
| `{anna}` | `U+E016` | `anna` |
| `{roomen}` | `U+E020` | `roomen` |
| `{lambe}` | `U+E022` | `lambe` |
| `{silme}` | `U+E024` | `silme` |
| `{silme-nuquerna}` | `U+E025` | `silmeN` |
| `{esse}` | `U+E026` | `esse` |
| `{esse-nuquerna}` | `U+E027` | `esseN` |
| `{hyarmen}` | `U+E028` | `hyarmen` |
| `{aara}` | `U+E02C` | `longCarrier` |
| `{telco}` | `U+E02E` | `shortCarrier` |

## 2. Marks

| Glyph | Code point(s) | FreeMonoTengwar glyph name |
|---|---|---|
| `[triple-dot-above]` | `U+E040` | `tehtaA` |
| `[dot-above]` | `U+E044` | `tehtaI` |
| `[dot-below]` | `U+E045` | `tehtaIB` |
| `[acute]` | `U+E046` | `tehtaE` |
| `[right-curl]` | `U+E04A` | `tehtaO` |
| `[left-curl]` | `U+E04C` | `tehtaU` |
| `[bar-above]` | `U+E050` | `tehtaN` |
| `[bar-below]` | `U+E051` | `tehtaB` |
| `[breve]` | `U+E053` | `tehtaBreve` |
| `[grave]` | `U+E054` | `tehtaGrave` |

## 3. Shorthands and punctuation

| Glyph | Code point(s) | FreeMonoTengwar glyph name |
|---|---|---|
| `{the-shorthand}` | `U+E01C` | `andoX` |
| `{of-shorthand}` | `U+E01D` | `umbarX` |
| `{and-shorthand}` | `U+E004 U+E050 U+E045` | `ando`, `tehtaN`, `tehtaIB` |
| `{pusta}` | `U+E060` | `tengwarPusta` |
| `{double-pusta}` | `U+E061` | `tengwarDoublepusta` |
| `{triple-pusta}` | `U+E062` | `tengwarTriplepusta` |
| `{section-mark}` | `U+E068` | `tengwarSection` |
| `{double-section-mark}` | `U+E069` | `tengwarDoublesection` |
| `{exclamation-mark}` | `U+E065` | `tengwarExclamation` |
| `{question-mark}` | `U+E066` | `tengwarQuestion` |
| `{parenthesis-mark}` | `U+E067` | `tengwarParanthesis` |
| `{left-quotation-mark}` | `U+E06A` | `tengwarQuoteleft` |
| `{right-quotation-mark}` | `U+E06B` | `tengwarQuoteright` |

The font has a glyph for each of the mode's punctuation names, so U-01 to U-05 need no substitute.

## 4. Encoding rules

| ID | Rule | Status |
|---|---|---|
| FE-01 | A cluster is its base code point, then its marks above **nearest the base first** (K-01's order reversed), then its marks below. The font draws each mark at a fixed height (every vowel mark starts at y ≥ 528; the nasal bar spans y 490–530), so either order renders the same. Nearest first is chosen so the output is byte-identical to Alcarin's (AE-01), and text moves between the two fonts unchanged. `{tinco}[dot-above][bar-above][bar-below]` is `E000 E050 E044 E051`. | ADOPTED |
| FE-02 | The marks below the base are `[bar-below]` (`tehtaB`, y −110…−70) and `[dot-below]` (`tehtaIB`, y −220…−140). | ADOPTED |
| FE-03 | The mode's nuquerna choice (S-02) is implemented by swapping `E024`/`E026` for `E025`/`E027` (`silmeN`, `esseN`). | ADOPTED |
| FE-04 | The font has Extended Ando (`andoX`, `E01C`) and Extended Umbar (`umbarX`, `E01D`), so W-01 and W-02 need no fallback (ADR-0012). | ADOPTED |
| FE-05 | The mode never emits `U+E014` (`oore`, R-02), `U+E048` (`tehtaEE`, double acute) or `U+E056` (`tehtaAE`). They stay in the font but are reserved, as in AE-04. | ADOPTED |
| FE-06 | Verified on 2026-10-11: Core Text (a direct render, and Alex in Safari and TextEdit) and Chrome 155 show every mark attached, with no dotted circles, in both mark orders. Core Text substitutes one glyph for the mode's clusters: `lambe` + `tehtaB` becomes the ligature `lambe_tehtaB`; Chrome draws the two glyphs. | ADOPTED |

## 5. Known limitations

- **Tall stems.** The marks do not rise over an ascender. On `{anto}`, `{ampa}`, `{formen}` and
  `{the-shorthand}` (stems up to y ≈ 608) a vowel mark sits beside the top of the stem, and the nasal
  bar crosses it. On `{hyarmen}` (apex at y 528) the nasal bar touches the apex. Legible, but cramped.
- **Monospace.** Every letter has the same width, so wide letters such as `{ando}` are narrow, and the
  marks are centred on the cell rather than on the letter's bowl.
