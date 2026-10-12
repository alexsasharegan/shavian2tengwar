# Execution Log: Second Font Encoding

## 2026-10-11 — Bootstrap, survey of Tengwar Formal CSUR, first gate renders

### Context & Decisions

- Brief from Alex: add a second PUA font encoding; tasks 5 (gate) and 6 (survey) first; stop after the
  survey if no candidate passes. ADRs `Proposed`, spec rules `PROVISIONAL`, PR not merged.
- Tools: no Playwright Chromium is installed here (`$PLAYWRIGHT_BROWSERS_PATH` unset, no
  `/opt/pw-browsers`), so the headless renders use the installed Google Chrome 155 through Playwright,
  as `tools/build_pdfs.py` does. fontTools was installed into `.venv` for the survey (not a project
  dependency).
- **Downloads blocked.** SourceForge answers `403` (body "No") from this sandbox for all three zips
  (`FreeMonoTengwar.2013-07-21.zip`, `TengwarFormalCSUR11.zip`, `TengwarTelcontar.008.zip`), including
  the master mirror, which redirects back. Asked Alex for the files instead of lifting the sandbox.
- **Tengwar Formal CSUR is already installed** on Alex's Mac (`~/Library/Fonts/TengwarFormalCSUR.ttf`,
  version 1.1), so it was surveyed and gated first. Findings, all read from the font file:
  - License: SIL OFL 1.1 (copyright notice and license URL in the `name` table). Reserved font names
    "Tengwar Formal" and "Tengwar Formal A". `fsType` 0.
  - Layout: **no GSUB or GPOS.** Graphite (`Silf`, `Glat`, `Gloc`) and AAT `morx` (22 subtables) with
    `feat`; no `kerx` or `ankr`. Tehtar have zero advance width, and `morx` substitutes pre-shifted
    variants per base (`tehtaI.shift3`, `tehtaN.narrowlow`, `tehtaN.widelow`, ...), 203 tehta glyphs.
  - Full PUA cmap in [survey.md](./survey.md): 110 code points, `U+E000`–`U+E07D`.
- **Coverage.** Every glyph and mark name the mode emits (the Alcarin table's keys) was looked up at
  its Alcarin code point in Formal CSUR's cmap. All 42 letters and 10 marks are present, and the font's
  own glyph name matches the intended glyph at every one (e.g. `U+E01C` = `andoX`, `U+E01D` = `umbarX`,
  `U+E025` = `silmeN`, `U+E02C` = `longCarrier`, `U+E045` = `tehtaIB`). For the mode's glyph set, the
  two fonts share a layout.
- **The name "CSUR" is misleading.** The ConScript registry (evertype.com/standards/csur/tengwar.html,
  fetched today) puts `TENGWAR LETTER ROOMEN` at `U+E018` and `TENGWAR SIGN LONG CARRIER BELOW` at
  `U+E056`, which is what `spec/encodings/alcarin.md` says. Tengwar Formal CSUR has `tincoX` at `U+E018`
  and `tehtaAE` at `U+E056`: it follows the FreeTengwar layout, as Alcarin's README says Alcarin does.
  So the spec is right, and this font does not follow the registry its name suggests.
- **Gate fixture** (`.wip/gate_fixture.py`, untracked): tinco with a vowel mark; ando with a vowel mark;
  vowel + nasal bar on tinco and on ando; gemination; vowel + gemination; nuquerna + vowel; short and
  long carriers. Every multi-mark case in both code point orders: "top first" (K-01 order) and "nearest
  first" (Alcarin's AE-01 order). Outputs `gate.html` (fonts embedded, for Safari), `gate.rtf` (installed
  fonts by PostScript name, for TextEdit) and `gate.txt`.

### Results

| Case | Alcarin, Chrome | Alcarin, Core Text | Formal CSUR, Chrome | Formal CSUR, Core Text |
|---|---|---|---|---|
| Vowel mark (tinco, ando) | pass | pass | attached, off-centre (unshifted) | pass (`.shift3`, `.shift4`) |
| Vowel + nasal bar, top first | **fail**: bar above the dot | **fail** (same) | dot over bar | pass (`tehtaN.narrowlow`) |
| Vowel + nasal bar, nearest first | pass | pass | dot over bar | pass |
| Same on wide ando | top first fails, nearest passes | same | **fail**: bar missing | pass, both orders (`tehtaN.widelow`) |
| Gemination, vowel + gemination | pass | pass | pass | pass |
| Nuquerna + vowel, carriers | pass | pass | attached, off-centre | pass |
| Dotted circles | none | none | none | none |

- Alcarin behaves exactly as ADR-0003 says, which confirms the fixture.
- Formal CSUR in Core Text: every mark attaches and stacks correctly **in either code point order**,
  because `morx` swaps the nasal bar for a lowered variant under a vowel mark.
- Formal CSUR in Chrome: no `morx` shaping, so marks keep their unshifted positions, and the nasal bar
  on a wide base is lost. HarfBuzz itself does apply `morx`: `hb-shape` 14.6.0 gives
  `[tinco|tehtaI.shift3|tehtaN.narrowlow]`, the same glyphs as Core Text. So it is Chrome's build that
  does not shape AAT. Consequence for this project: the review sheet and the PDF pipeline both print
  through Chrome, so they cannot show this font correctly as they are.
- These Core Text renders are machine evidence, not the gate's final word. The brief asks for Alex's
  own check in Safari and TextEdit.

### Commands & Operations Executed

```bash
git checkout -b feat/0003-second-encoding
.venv/bin/pip install -q fonttools
curl -sSL "https://sourceforge.net/projects/freetengwar/files/TengwarFont/<zip>/download"   # 403 "No"
python3 -I fontinfo.py ~/Library/Fonts/TengwarFormalCSUR.ttf      # names, license, tables, PUA range
python3 -I cmapdump.py ~/Library/Fonts/TengwarFormalCSUR.ttf      # -> survey.md
python3 .wip/gate_fixture.py .wip/gate --font "Alcarin Tengwar=…/AlcarinTengwarVF.ttf" \
    --font "Tengwar Formal CSUR=…/TengwarFormalCSUR.ttf"
.venv/bin/python .wip/shoot.py .wip/gate/gate.html .wip/gate/chrome.png      # Chrome 155.0.8059.39
swift .wip/ctrender.swift ~/Library/Fonts/TengwarFormalCSUR.ttf .wip/gate/Tengwar-Formal-CSUR.lines .wip/gate/coretext-formal.png
swift .wip/ctrender.swift ~/Library/Fonts/AlcarinTengwarVF.ttf .wip/gate/Alcarin-Tengwar.lines .wip/gate/coretext-alcarin.png
hb-shape ~/Library/Fonts/TengwarFormalCSUR.ttf --text=$''
curl -sSL https://www.evertype.com/standards/csur/tengwar.html     # registry check
```

### LLM Session Summary

- **Thread purpose:** Start project 0003 with the survey and the gate.
- **Key findings / Blockers resolved:** Formal CSUR passes in a direct Core Text render and covers the
  whole mode at the same code points as Alcarin. Chrome does not shape AAT, which affects the review
  sheet and PDFs.
- **Context state for next thread:** Blocked on Alex for the FreeMonoTengwar and Telcontar files, and
  for the Safari and TextEdit check. No ADR, spec or code yet, by design (tasks 5 and 6 come first).

## 2026-10-11 — FreeMonoTengwar and Telcontar surveyed; Alex's Safari and TextEdit check

### Context & Decisions

- Alex downloaded the three zips into `.wip/fonts/` (untracked). The `TengwarFormalCSUR.ttf` in the zip
  has the same SHA-1 as the installed copy, so the earlier survey stands. Read with `python -I`, scripts
  kept outside the font folders.
- **Tengwar Telcontar fails the gate.** Its only layout tables are Graphite (`Silf`, `Glat`, `Gloc`), and
  its tehtar have a 1125-unit advance. Core Text and Chrome both draw every mark on its own dotted
  circle, beside the base. This matches what Alex saw before. Graphite-only, so it is out by the brief.
- **FreeMonoTengwar passes in Core Text and in Chrome.** It is monospaced: every glyph is 600 units and
  the tehtar are zero-width outlines drawn into the preceding cell at fixed heights (`tehtaI` y 563…643,
  `tehtaN` y 490…530). The vowel mark always lands above the nasal bar, so **both code point orders give
  the same picture**. Core Text substitutes nothing for any fixture case (its glyph names stay `tinco
  tehtaI tehtaN`). The font has `morx` (14 subtables), an empty `GPOS` and a `liga`-only `GSUB`, but the
  gate cases need none of them.
  - Open point for Alex: the gate says "Core Text positions its tehtar through OpenType GPOS or AAT".
    FreeMono positions them by their outlines, not by a table. It meets the gate's purpose (marks attach,
    no dotted circles, no Graphite needed) but not its letter. Alex decides whether that passes.
  - License: GPLv3 or later with the font-embedding exception. `FontLog.txt` says commercial use of the
    tengwar "may need permission from the Tolkien Estate" (for ADR-0011).
  - Coverage: all 42 letters and 10 marks at Alcarin's code points, with the same glyph names as Formal
    CSUR (one spelling differs: `tengwarParanthesis`).
- **Alex's check (screenshots, Safari and TextEdit).** Alex reported "several nasal bars stacked over the
  tehta". In the screenshots those are the **Alcarin "top first"** rows, in both apps: the bar sits above
  the dot, and above the acute on ando. Alcarin's "nearest first" rows are correct. That is ADR-0003's
  finding again. The fixture shows the failing order on purpose, and the engine emits nearest first for
  Alcarin (`Encoding.encode_cell`), so the converter's output is not affected.
  - Tengwar Formal CSUR in Safari: dot over bar and acute over bar in **both** orders; every mark
    attached; no dotted circles. Pass, the same as the direct Core Text render.
  - TextEdit: the screenshot shows only the Alcarin section. Formal CSUR's section still to be seen.
- The fixture now has four columns (FreeMono and Telcontar added, code points read from each cmap) and
  was regenerated. FreeMono must be installed for the TextEdit file to show it.

### Results

| Case | FreeMono, Chrome | FreeMono, Core Text | Telcontar, Chrome | Telcontar, Core Text |
|---|---|---|---|---|
| Vowel mark (tinco, ando) | pass | pass | **fail**: dotted circle | **fail** (same) |
| Vowel + nasal bar, either order | pass | pass | **fail** | **fail** |
| Same on ando | pass (ando is narrow in this font) | pass | **fail** | **fail** |
| Gemination, vowel + gemination | pass | pass | **fail** | **fail** |
| Nuquerna + vowel, carriers | pass | pass | **fail** | **fail** |

Alex, Safari (Formal CSUR): pass, both orders. Alex, Safari and TextEdit (Alcarin): top first fails,
nearest first passes.

### Commands & Operations Executed

```bash
python -I fontinfo.py .wip/fonts/FreeMonoTengwar.2013-07-21/FreeMonoTengwar.ttf   # and -embedding, tengtelc, tengtelcb
python -I coverage.py <repo> <Formal CSUR> <FreeMono> <tengtelc>     # mode names at Alcarin's code points
python -I cmapdump.py <font>                                          # -> survey.md
shasum .wip/fonts/TengwarFormalCSUR11/TengwarFormalCSUR.ttf ~/Library/Fonts/TengwarFormalCSUR.ttf
python3 .wip/gate_fixture.py .wip/gate --font ... (four fonts)
swift .wip/ctrender.swift <FreeMono> .wip/gate/FreeMonoTengwar.lines .wip/gate/coretext-freemono.png
swift .wip/ctrender.swift <tengtelc> .wip/gate/Tengwar-Telcontar.lines .wip/gate/coretext-telcontar.png
.venv/bin/python .wip/shoot.py .wip/gate/gate.html .wip/gate/chrome.png
```

### LLM Session Summary

- **Thread purpose:** Finish tasks 5 and 6: survey the downloaded fonts and record Alex's check.
- **Key findings / Blockers resolved:** Two candidates pass on rendering. Formal CSUR passes in Core Text
  and Safari but not Chrome. FreeMono passes everywhere but positions marks by outline, not by GPOS or
  AAT. Telcontar fails. The stacked bars Alex saw are Alcarin's top-first control rows.
- **Context state for next thread:** Waiting on Alex for: (1) whether FreeMono's outline positioning
  passes the gate; (2) which font gets the first encoding; (3) Formal CSUR's section in TextEdit, and
  FreeMono in Safari and TextEdit once installed. No ADR, spec or code yet.
