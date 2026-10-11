# Font survey — second encoding

Every value below was read from the font file itself with fontTools 4 (`name`, `OS/2`, `cmap`, `hmtx`
and the table directory), not copied from another table or web page. See `LOG.md` for the commands.

## Summary

| | Tengwar Formal CSUR | FreeMonoTengwar | Tengwar Telcontar |
|---|---|---|---|
| File examined | `TengwarFormalCSUR.ttf`, version 1.1 (installed on Alex's Mac) | not yet obtained | not yet obtained |
| License | SIL OFL 1.1 (font `name` table: copyright and license URL) | GPLv3+ with font exception (per the Free Tengwar page; unverified) | unverified |
| Reserved font names | "Tengwar Formal", "Tengwar Formal A" | — | — |
| Embedding (`OS/2.fsType`) | 0 (installable) | — | — |
| Format | TrueType (`.ttf`) | — | — |
| OpenType GSUB / GPOS | no / no | — | — |
| AAT | `morx` (22 subtables: ligature, non-contextual, insertion, contextual), `feat`; no `kerx`, no `ankr` | — | — |
| Graphite | `Silf`, `Glat`, `Gloc`, `Sill`, `Feat` | — | — |
| PUA code points | 110, `U+E000`–`U+E07D` | — | — |
| Mark positioning method | Zero-width tehtar; `morx` swaps in pre-shifted variants (`tehtaI.shift3`, `tehtaN.narrowlow`, ...), 203 tehta glyphs in all | — | — |

## Tengwar Formal CSUR: PUA cmap

Glyph names are the font's own (`post` table). Advance width in font units (2048/em); 0 is a mark.

| Code point | Glyph name | Advance |
|---|---|---|
| `U+E000` | `tinco` | 1128 |
| `U+E001` | `parma` | 1128 |
| `U+E002` | `calma` | 1128 |
| `U+E003` | `quesse` | 1128 |
| `U+E004` | `ando` | 1724 |
| `U+E005` | `umbar` | 1724 |
| `U+E006` | `anga` | 1724 |
| `U+E007` | `ungwe` | 1724 |
| `U+E008` | `suule` | 1128 |
| `U+E009` | `formen` | 1128 |
| `U+E00A` | `aha` | 1128 |
| `U+E00B` | `hwesta` | 1128 |
| `U+E00C` | `anto` | 1724 |
| `U+E00D` | `ampa` | 1724 |
| `U+E00E` | `anca` | 1724 |
| `U+E00F` | `unque` | 1724 |
| `U+E010` | `nuumen` | 1724 |
| `U+E011` | `malta` | 1724 |
| `U+E012` | `noldo` | 1724 |
| `U+E013` | `nwalme` | 1724 |
| `U+E014` | `oore` | 1128 |
| `U+E015` | `vala` | 1128 |
| `U+E016` | `anna` | 1128 |
| `U+E017` | `vilya` | 1128 |
| `U+E018` | `tincoX` | 1128 |
| `U+E019` | `parmaX` | 1128 |
| `U+E01A` | `calmaX` | 1128 |
| `U+E01B` | `quesseX` | 1128 |
| `U+E01C` | `andoX` | 1724 |
| `U+E01D` | `umbarX` | 1724 |
| `U+E01E` | `angaX` | 1724 |
| `U+E01F` | `ungweX` | 1724 |
| `U+E020` | `roomen` | 1128 |
| `U+E021` | `arda` | 1125 |
| `U+E022` | `lambe` | 1724 |
| `U+E023` | `alda` | 1724 |
| `U+E024` | `silme` | 1128 |
| `U+E025` | `silmeN` | 1128 |
| `U+E026` | `esse` | 1128 |
| `U+E027` | `esseN` | 1128 |
| `U+E028` | `hyarmen` | 1128 |
| `U+E029` | `hwestaS` | 1128 |
| `U+E02A` | `yanta` | 1128 |
| `U+E02B` | `uure` | 1128 |
| `U+E02C` | `longCarrier` | 383 |
| `U+E02D` | `halla` | 383 |
| `U+E02E` | `shortCarrier` | 383 |
| `U+E030` | `osseN` | 1131 |
| `U+E031` | `lambeN` | 1128 |
| `U+E032` | `osse` | 1128 |
| `U+E034` | `carrierX` | 1128 |
| `U+E036` | `annaX` | 1128 |
| `U+E037` | `quesseC` | 1128 |
| `U+E038` | `hwestaC` | 1128 |
| `U+E039` | `roomenN` | 1128 |
| `U+E03A` | `maltaX` | 1724 |
| `U+E03B` | `valaX` | 1128 |
| `U+E03C` | `hallaRoomen` | 840 |
| `U+E03D` | `vaiya` | 1128 |
| `U+E040` | `tehtaA` | 0 |
| `U+E041` | `tehtaAB` | 0 |
| `U+E042` | `tehtaY` | 0 |
| `U+E043` | `tehtaYB` | 0 |
| `U+E044` | `tehtaI` | 0 |
| `U+E045` | `tehtaIB` | 0 |
| `U+E046` | `tehtaE` | 0 |
| `U+E047` | `tehtaEB` | 0 |
| `U+E049` | `tehtaEEB` | 0 |
| `U+E04A` | `tehtaO` | 0 |
| `U+E04B` | `tehtaOB` | 0 |
| `U+E04C` | `tehtaU` | 0 |
| `U+E04D` | `tehtaUB` | 0 |
| `U+E050` | `tehtaN` | 0 |
| `U+E051` | `tehtaB` | 0 |
| `U+E052` | `tehtaW` | 0 |
| `U+E053` | `tehtaBreve` | 0 |
| `U+E054` | `tehtaGrave` | 0 |
| `U+E055` | `tehtaYanta` | 0 |
| `U+E056` | `tehtaAE` | 0 |
| `U+E057` | `tehtaThinnas` | 0 |
| `U+E058` | `tehtaS` | 463 |
| `U+E059` | `tehtaX` | 0 |
| `U+E05A` | `tehtaDotInside` | 0 |
| `U+E060` | `tengwarPusta` | 589 |
| `U+E061` | `tengwarDoublepusta` | 589 |
| `U+E062` | `tengwarTriplepusta` | 722 |
| `U+E063` | `tengwarQuadruplepusta` | 1334 |
| `U+E064` | `tengwarQuintuplepusta` | 1304 |
| `U+E065` | `tengwarExclamation` | 495 |
| `U+E066` | `tengwarQuestion` | 1128 |
| `U+E067` | `tengwarParenthesis` | 897 |
| `U+E068` | `tengwarSection` | 1054 |
| `U+E069` | `tengwarDoublesection` | 1054 |
| `U+E06A` | `tengwarQuoteleft` | 526 |
| `U+E06B` | `tengwarQuoteright` | 526 |
| `U+E06C` | `tengwarExclamationB` | 1174 |
| `U+E070` | `tengwardigit0` | 1131 |
| `U+E071` | `tengwardigit1` | 1128 |
| `U+E072` | `tengwardigit2` | 1645 |
| `U+E073` | `tengwardigit3` | 2161 |
| `U+E074` | `tengwardigit4` | 1160 |
| `U+E075` | `tengwardigit5` | 1418 |
| `U+E076` | `tengwardigit6` | 1934 |
| `U+E077` | `tengwardigit7` | 1075 |
| `U+E078` | `tengwardigit8` | 1797 |
| `U+E079` | `tengwardigit9` | 2394 |
| `U+E07A` | `tengwarduodecimal10` | 1128 |
| `U+E07B` | `tengwarduodecimal11` | 1128 |
| `U+E07C` | `tengwarduodecimal12` | 1128 |
| `U+E07D` | `tengwardigitMark` | 0 |
