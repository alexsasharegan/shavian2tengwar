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
- [x] **Alex:** FreeMono and Telcontar in TextEdit (FreeMono pass, Telcontar dotted circles). Formal CSUR's TextEdit section not checked; moot after the choice below
- [x] **Alex:** decide whether FreeMono's outline-positioned tehtar pass the gate: yes, the principle is robust accessibility (Core Text, browsers, PDFs, word processors)
- [x] **Alex:** choose the font for the first encoding: FreeMonoTengwar
- [x] Record the gate verdict per candidate (Telcontar fails; Formal CSUR and FreeMono pass on rendering; see LOG)

## Phase 2: Decisions (only if a candidate passes)

- [x] ADR-0011: second-encoding scope and acceptance gate (Proposed)
- [x] ADR-0012: the encoding contract (Proposed)

## Phase 3: Code (only if a candidate passes)

- [x] Generalise `tests/test_encoding.py` to every registered encoding
- [x] Font family per encoding in `tools/render_corpus.py` and `tools/build_pdfs.py`
- [x] `spec/encodings/freemono.md` with PROVISIONAL rules FE-01 to FE-06, each code point read from the cmap
- [x] `s2t/encodings/freemono.py`, registered; `--encoding freemono` and the review sheet use it
- [x] Render the corpus in it and look at the result (Chrome; tall-letter check in Core Text)
- [ ] **Alex:** decide whether the gate fixture moves from `.wip/` to `tools/` (left in `.wip/` for now)

## Phase 4: Finish

- [x] `npm test` and `npm run lint` on Python 3.14, output in the LOG and the PR
- [x] ADR index, ROADMAP; PR open for Alex (not merged)
- [x] **Alex:** decide whether the FreeMono sheet is committed: yes, every font is rendered and committed (`corpus/review-freemono.html` and `.pdf`)
- [ ] On approval: ADR-0011 and ADR-0012 to Active, FE-01 to FE-06 to ADOPTED, drop "(proposed)" from ADR-0003's last bullet, Review "Approved by merging PR #3", close the project
