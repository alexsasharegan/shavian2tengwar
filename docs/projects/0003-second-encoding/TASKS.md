# TASKS — Second Font Encoding

## Phase 1: Survey and gate (tasks 5 and 6; first)

- [x] Branch `feat/0003-second-encoding`; project folder
- [x] Mark-stacking fixture: vowel mark, vowel + nasal bar, gemination, plus wide base, nuquerna and carriers; both code point orders (`.wip/gate_fixture.py`)
- [x] Render it in headless Chrome (155) for Alcarin (control) and Tengwar Formal CSUR
- [x] Render it through Core Text directly (`.wip/ctrender.swift`), with the glyphs Core Text chose
- [x] Survey Tengwar Formal CSUR: license, tables, full PUA cmap ([survey.md](./survey.md))
- [x] **Alex:** download `FreeMonoTengwar.2013-07-21.zip` and `TengwarTelcontar.008.zip` (SourceForge returns 403 from Claude's sandbox) into `docs/projects/0003-second-encoding/.wip/fonts/`
- [x] Survey FreeMonoTengwar and Tengwar Telcontar; render both in the fixture
- [x] **Alex:** open `.wip/gate/gate.html` in Safari and `.wip/gate/gate.rtf` in TextEdit (Alcarin and Formal CSUR in Safari; Alcarin in TextEdit)
- [ ] **Alex:** Formal CSUR's section in TextEdit; FreeMono in Safari and TextEdit (install `FreeMonoTengwar.ttf` first)
- [ ] **Alex:** decide whether FreeMono's outline-positioned tehtar pass the gate ("through GPOS or AAT")
- [ ] **Alex:** choose the font for the first encoding (Formal CSUR or FreeMono)
- [x] Record the gate verdict per candidate (Telcontar fails; Formal CSUR and FreeMono pass on rendering; see LOG)

## Phase 2: Decisions (only if a candidate passes)

- [ ] ADR-0011: second-encoding scope and acceptance criteria (Proposed)
- [ ] ADR-0012: the encoding contract (Proposed)

## Phase 3: Code (only if a candidate passes)

- [ ] Generalise `tests/test_encoding.py` to every registered encoding
- [ ] Font family per encoding in `tools/render_corpus.py` and `tools/build_pdfs.py`
- [ ] `spec/encodings/<font>.md` with PROVISIONAL rules, each code point verified against the cmap
- [ ] `s2t/encodings/<font>.py`, registered in `ENCODINGS`; `--encoding` and the review sheet use it
- [ ] Render the corpus in it and look at the result
- [ ] Decide where the gate fixture lives once it is reused (promote from `.wip/` to `tools/`?)

## Phase 4: Finish

- [ ] `npm test` and `npm run lint` on Python 3.14, output in the LOG and the PR
- [ ] ADR index, ROADMAP; PR open for Alex (not merged)
