# Font survey — second encoding

Every value below was read from the font file itself with fontTools 4 (`name`, `OS/2`, `cmap`, `hmtx`
and the table directory), not copied from another table or web page. See `LOG.md` for the commands.

## Summary

| | Tengwar Formal CSUR | FreeMonoTengwar | Tengwar Telcontar |
|---|---|---|---|
| File examined | `TengwarFormalCSUR.ttf` 1.1 (`TengwarFormalCSUR11.zip`; same SHA-1 as the copy installed on Alex's Mac) | `FreeMonoTengwar.ttf`, version 2013-07-21 (`FreeMonoTengwar.2013-07-21.zip`) | `tengtelc.ttf` (and `tengtelcb.ttf`, bold), version 0.08 (`TengwarTelcontar.008.zip`) |
| License | SIL OFL 1.1 (`name` table, `OFL.txt`) | GPLv3 or later, with the font-embedding exception (`name` table, `FontLog.txt`, `GPL.txt`) | GPLv3 or later, with the font-embedding exception (`README.txt`, `COPYING.txt`) |
| Reserved font names | "Tengwar Formal", "Tengwar Formal A" | none | none |
| Tolkien Estate note | none | `FontLog.txt`: commercial use of the tengwar "may need permission from the Tolkien Estate" | none in the zip (same project as FreeMono) |
| Embedding (`OS/2.fsType`) | 0 (installable) | 0 | 0 |
| Format | TrueType (`.ttf`), 2048/em | TrueType (`.ttf`), 1000/em; also `FreeMonoTengwar-embedding.ttf`, a subset | TrueType (`.ttf`), 2048/em |
| Spacing | proportional | **monospaced**: every glyph 600 units, marks 0 | proportional |
| OpenType GSUB / GPOS | no / no | GSUB `liga` only (one ligature lookup) / GPOS present but **empty** (no features, no lookups) | no / no |
| AAT | `morx` (22 subtables), `feat`; no `kerx`, no `ankr` | `morx` (14 subtables), `feat`; no `kerx`, no `ankr` | none |
| Graphite | `Silf`, `Glat`, `Gloc`, `Sill`, `Feat` | `Silf`, `Glat`, `Gloc`, `Sill`, `Feat` | `Silf`, `Glat`, `Gloc`, `Sill`, `Feat` (**Graphite only**) |
| PUA code points | 110, `U+E000`–`U+E07D` | 114, `U+E000`–`U+E07D` | 110, `U+E000`–`U+E07D`, plus `U+F8FF` |
| Glyph names | descriptive (`tinco`, `tehtaI`) | descriptive, the same as Formal CSUR's | `uniXXXX` only |
| Mark positioning method | Zero-width tehtar; `morx` swaps in pre-shifted variants (`tehtaI.shift3`, `tehtaN.narrowlow`, ...), 203 tehta glyphs in all | Zero-width tehtar drawn at fixed offsets into the preceding 600-unit cell (e.g. `tehtaI` x −340…−260, y 563…643; `tehtaN` y 490…530). The dot is always above the bar, in either order. No table is needed, and Core Text substitutes nothing | Tehtar have a 1125-unit advance; only Graphite places them |
| Mode coverage at Alcarin's code points | all 42 letters and 10 marks, matching glyph names | all 42 letters and 10 marks, matching glyph names | a glyph at every code point, but the names cannot confirm which |
| Gate (Core Text, Chrome) | Core Text pass; Chrome fails (no `morx`) | **pass in both** | **fail in both: dotted circles**, every mark on its own |

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

## FreeMonoTengwar: PUA cmap

Glyph names are the font's own (`post` table). Advance width in font units (1000/em); 0 is a mark.

| Code point | Glyph name | Advance |
|---|---|---|
| `U+E000` | `tinco` | 600 |
| `U+E001` | `parma` | 600 |
| `U+E002` | `calma` | 600 |
| `U+E003` | `quesse` | 600 |
| `U+E004` | `ando` | 600 |
| `U+E005` | `umbar` | 600 |
| `U+E006` | `anga` | 600 |
| `U+E007` | `ungwe` | 600 |
| `U+E008` | `suule` | 600 |
| `U+E009` | `formen` | 600 |
| `U+E00A` | `aha` | 600 |
| `U+E00B` | `hwesta` | 600 |
| `U+E00C` | `anto` | 600 |
| `U+E00D` | `ampa` | 600 |
| `U+E00E` | `anca` | 600 |
| `U+E00F` | `unque` | 600 |
| `U+E010` | `nuumen` | 600 |
| `U+E011` | `malta` | 600 |
| `U+E012` | `noldo` | 600 |
| `U+E013` | `nwalme` | 600 |
| `U+E014` | `oore` | 600 |
| `U+E015` | `vala` | 600 |
| `U+E016` | `anna` | 600 |
| `U+E017` | `vilya` | 600 |
| `U+E018` | `tincoX` | 600 |
| `U+E019` | `parmaX` | 600 |
| `U+E01A` | `calmaX` | 600 |
| `U+E01B` | `quesseX` | 600 |
| `U+E01C` | `andoX` | 600 |
| `U+E01D` | `umbarX` | 600 |
| `U+E01E` | `angaX` | 600 |
| `U+E01F` | `ungweX` | 600 |
| `U+E020` | `roomen` | 600 |
| `U+E021` | `arda` | 600 |
| `U+E022` | `lambe` | 600 |
| `U+E023` | `alda` | 600 |
| `U+E024` | `silme` | 600 |
| `U+E025` | `silmeN` | 600 |
| `U+E026` | `esse` | 600 |
| `U+E027` | `esseN` | 600 |
| `U+E028` | `hyarmen` | 599 |
| `U+E029` | `hwestaS` | 600 |
| `U+E02A` | `yanta` | 600 |
| `U+E02B` | `uure` | 600 |
| `U+E02C` | `longCarrier` | 600 |
| `U+E02D` | `halla` | 600 |
| `U+E02E` | `shortCarrier` | 600 |
| `U+E030` | `osseN` | 600 |
| `U+E031` | `lambeN` | 600 |
| `U+E032` | `osse` | 600 |
| `U+E034` | `carrierX` | 600 |
| `U+E035` | `annaS` | 600 |
| `U+E036` | `annaX` | 600 |
| `U+E037` | `quesseC` | 600 |
| `U+E038` | `hwestaC` | 600 |
| `U+E039` | `roomenN` | 600 |
| `U+E03A` | `maltaX` | 600 |
| `U+E03B` | `valaX` | 600 |
| `U+E03C` | `hallaRoomen` | 600 |
| `U+E03D` | `vaiya` | 600 |
| `U+E040` | `tehtaA` | 0 |
| `U+E041` | `tehtaAB` | 0 |
| `U+E042` | `tehtaY` | 0 |
| `U+E043` | `tehtaYB` | 0 |
| `U+E044` | `tehtaI` | 0 |
| `U+E045` | `tehtaIB` | 0 |
| `U+E046` | `tehtaE` | 0 |
| `U+E047` | `tehtaEB` | 0 |
| `U+E048` | `tehtaEE` | 0 |
| `U+E049` | `tehtaEEB` | 0 |
| `U+E04A` | `tehtaO` | 0 |
| `U+E04B` | `tehtaOB` | 0 |
| `U+E04C` | `tehtaU` | 0 |
| `U+E04D` | `tehtaUB` | 0 |
| `U+E04E` | `tehtaOO` | 0 |
| `U+E04F` | `tehtaUU` | 0 |
| `U+E050` | `tehtaN` | 0 |
| `U+E051` | `tehtaB` | 0 |
| `U+E052` | `tehtaW` | 0 |
| `U+E053` | `tehtaBreve` | 0 |
| `U+E054` | `tehtaGrave` | 0 |
| `U+E055` | `tehtaYanta` | 0 |
| `U+E056` | `tehtaAE` | 0 |
| `U+E057` | `tehtaThinnas` | 0 |
| `U+E058` | `tehtaS` | 600 |
| `U+E059` | `tehtaX` | 0 |
| `U+E05A` | `tehtaDotInside` | 0 |
| `U+E060` | `tengwarPusta` | 600 |
| `U+E061` | `tengwarDoublepusta` | 600 |
| `U+E062` | `tengwarTriplepusta` | 600 |
| `U+E063` | `tengwarQuadruplepusta` | 600 |
| `U+E064` | `tengwarQuintuplepusta` | 600 |
| `U+E065` | `tengwarExclamation` | 600 |
| `U+E066` | `tengwarQuestion` | 600 |
| `U+E067` | `tengwarParanthesis` | 600 |
| `U+E068` | `tengwarSection` | 600 |
| `U+E069` | `tengwarDoublesection` | 600 |
| `U+E06A` | `tengwarQuoteleft` | 600 |
| `U+E06B` | `tengwarQuoteright` | 600 |
| `U+E06C` | `tengwarExclamationB` | 600 |
| `U+E070` | `tengwardigit0` | 600 |
| `U+E071` | `tengwardigit1` | 600 |
| `U+E072` | `tengwardigit2` | 600 |
| `U+E073` | `tengwardigit3` | 600 |
| `U+E074` | `tengwardigit4` | 600 |
| `U+E075` | `tengwardigit5` | 600 |
| `U+E076` | `tengwardigit6` | 600 |
| `U+E077` | `tengwardigit7` | 600 |
| `U+E078` | `tengwardigit8` | 600 |
| `U+E079` | `tengwardigit9` | 600 |
| `U+E07A` | `tengwarduodecimal10` | 600 |
| `U+E07B` | `tengwarduodecimal11` | 600 |
| `U+E07C` | `tengwarduodecimal12` | 600 |
| `U+E07D` | `tengwardigitMark` | 0 |

## Tengwar Telcontar: PUA cmap

Glyph names are the font's own (`post` table), which are only `uniXXXX`. Advance width in font units (2048/em). The tehtar are not zero-width.

| Code point | Glyph name | Advance |
|---|---|---|
| `U+E000` | `uniE000` | 1388 |
| `U+E001` | `uniE001` | 1366 |
| `U+E002` | `uniE002` | 1307 |
| `U+E003` | `uniE003` | 1312 |
| `U+E004` | `uniE004` | 2032 |
| `U+E005` | `uniE005` | 2011 |
| `U+E006` | `uniE006` | 1952 |
| `U+E007` | `uniE007` | 1957 |
| `U+E008` | `uniE008` | 1342 |
| `U+E009` | `uniE009` | 1321 |
| `U+E00A` | `uniE00A` | 1338 |
| `U+E00B` | `uniE00B` | 1347 |
| `U+E00C` | `uniE00C` | 1986 |
| `U+E00D` | `uniE00D` | 1966 |
| `U+E00E` | `uniE00E` | 1982 |
| `U+E00F` | `uniE00F` | 1992 |
| `U+E010` | `uniE010` | 2033 |
| `U+E011` | `uniE011` | 2011 |
| `U+E012` | `uniE012` | 1956 |
| `U+E013` | `uniE013` | 1957 |
| `U+E014` | `uniE014` | 1390 |
| `U+E015` | `uniE015` | 1365 |
| `U+E016` | `uniE016` | 1312 |
| `U+E017` | `uniE017` | 1312 |
| `U+E018` | `uniE018` | 1340 |
| `U+E019` | `uniE019` | 1313 |
| `U+E01A` | `uniE01A` | 1340 |
| `U+E01B` | `uniE01B` | 1346 |
| `U+E01C` | `uniE01C` | 1983 |
| `U+E01D` | `uniE01D` | 1958 |
| `U+E01E` | `uniE01E` | 1983 |
| `U+E01F` | `uniE01F` | 1991 |
| `U+E020` | `uniE020` | 1165 |
| `U+E021` | `uniE021` | 1165 |
| `U+E022` | `uniE022` | 1618 |
| `U+E023` | `uniE023` | 1618 |
| `U+E024` | `uniE024` | 1165 |
| `U+E025` | `uniE025` | 1165 |
| `U+E026` | `uniE026` | 1177 |
| `U+E027` | `uniE027` | 1177 |
| `U+E028` | `uniE028` | 1216 |
| `U+E029` | `uniE029` | 1440 |
| `U+E02A` | `uniE02A` | 1216 |
| `U+E02B` | `uniE02B` | 1125 |
| `U+E02C` | `uniE02C` | 615 |
| `U+E02D` | `uniE02D` | 615 |
| `U+E02E` | `uniE02E` | 615 |
| `U+E030` | `uniE030` | 1086 |
| `U+E031` | `uniE031` | 1077 |
| `U+E032` | `uniE032` | 1026 |
| `U+E034` | `uniE034` | 846 |
| `U+E036` | `uniE036` | 1211 |
| `U+E037` | `uniE037` | 1248 |
| `U+E039` | `uniE039` | 1152 |
| `U+E03A` | `uniE03A` | 2011 |
| `U+E03B` | `uniE03B` | 1365 |
| `U+E03C` | `uniE03C` | 1106 |
| `U+E03D` | `uniE03D` | 1358 |
| `U+E040` | `uniE040` | 1125 |
| `U+E041` | `uniE041` | 1125 |
| `U+E042` | `uniE042` | 1125 |
| `U+E043` | `uniE043` | 1125 |
| `U+E044` | `uniE044` | 1125 |
| `U+E045` | `uniE045` | 1125 |
| `U+E046` | `uniE046` | 1125 |
| `U+E047` | `uniE047` | 1125 |
| `U+E049` | `uniE049` | 1125 |
| `U+E04A` | `uniE04A` | 1125 |
| `U+E04B` | `uniE04B` | 1125 |
| `U+E04C` | `uniE04C` | 1125 |
| `U+E04D` | `uniE04D` | 1125 |
| `U+E050` | `uniE050` | 1125 |
| `U+E051` | `uniE051` | 1125 |
| `U+E052` | `uniE052` | 1125 |
| `U+E053` | `uniE053` | 1125 |
| `U+E054` | `uniE054` | 1125 |
| `U+E055` | `uniE055` | 1125 |
| `U+E056` | `uniE056` | 1125 |
| `U+E057` | `uniE057` | 1125 |
| `U+E058` | `uniE058` | 1092 |
| `U+E059` | `uniE059` | 1125 |
| `U+E05A` | `uniE05A` | 1125 |
| `U+E060` | `uniE060` | 530 |
| `U+E061` | `uniE061` | 530 |
| `U+E062` | `uniE062` | 530 |
| `U+E063` | `uniE063` | 1236 |
| `U+E064` | `uniE064` | 1412 |
| `U+E065` | `uniE065` | 617 |
| `U+E066` | `uniE066` | 962 |
| `U+E067` | `uniE067` | 767 |
| `U+E068` | `uniE068` | 1641 |
| `U+E069` | `uniE069` | 1641 |
| `U+E06A` | `uniE06A` | 793 |
| `U+E06B` | `uniE06B` | 793 |
| `U+E06C` | `uniE06C` | 2098 |
| `U+E070` | `uniE070` | 1228 |
| `U+E071` | `uniE071` | 1228 |
| `U+E072` | `uniE072` | 1228 |
| `U+E073` | `uniE073` | 1228 |
| `U+E074` | `uniE074` | 1228 |
| `U+E075` | `uniE075` | 1228 |
| `U+E076` | `uniE076` | 1228 |
| `U+E077` | `uniE077` | 1228 |
| `U+E078` | `uniE078` | 1228 |
| `U+E079` | `uniE079` | 1228 |
| `U+E07A` | `uniE07A` | 1228 |
| `U+E07B` | `uniE07B` | 1228 |
| `U+E07C` | `uniE07C` | 1228 |
| `U+E07D` | `uniE07D` | 0 |
| `U+F8FF` | `uniF8FF` | 2318 |
