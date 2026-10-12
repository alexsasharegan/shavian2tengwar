# ADR-0011: Second Encoding: Scope and Acceptance Gate

**Status:** Proposed
**Date:** 2026-10-11
**Affected:** s2t/encodings/, spec/encodings/, docs/projects/0003-second-encoding/survey.md
**Origin:** project 0003 (Alex's brief)
**Review:** In PR #3; Alex decided the gate's principle and the font choice on 2026-10-11
**Revert:** `ca18a8e` (with ADR-0012; see there)

## Context

Output only rendered correctly in Alcarin Tengwar (ADR-0003). Alex asked for a second free font, chosen
so that Tengwar written by this tool works for as many readers as possible, and especially on macOS.

Tengwar fonts come in two kinds. ASCII-mapped fonts (Annatar, Parmaite, Eldamar and the like) put
tengwar on Latin code points: the text is unreadable without the font and breaks under any font
fallback. Unicode fonts put tengwar in the Private Use Area (`U+E000`–`U+E07F`). They do not all use
the same PUA layout (Everson 2001, CSUR and FreeTengwar differ), and they place their tehtar in
different ways: OpenType GPOS, AAT `morx`, Graphite, or outlines drawn at fixed offsets.

Tengwar Telcontar had already failed on Alex's Mac: tehtar on dotted circles in Core Text.

## Decision

- **Only PUA fonts.** ASCII-mapped fonts are out.
- **Never copy a code point.** Every code point in an encoding is read from that font's own cmap, as
  `spec/encodings/alcarin.md` was. A shared layout is a finding, never an assumption.
- **The gate.** A font qualifies only if:
  - it is free;
  - it uses PUA code points;
  - it installs on macOS;
  - its tehtar attach to their base, with no dotted circles, in **every place this project's text is
    read**: Core Text (Safari, TextEdit and other word processors), Chrome (the review sheet and the
    PDF build), and the PDFs that Chrome prints.

  Graphite-only fonts are excluded, because macOS has no Graphite.

  The brief first wrote the positioning criterion as "through OpenType GPOS or AAT". Alex ruled
  (2026-10-11) that the principle is robust accessibility across those renderers, not a particular
  font technology. A font that places its marks by outline passes if it renders correctly everywhere.
- **The gate is checked by rendering.** A fixture shows each mark-stacking case in both code point
  orders: a vowel mark, a vowel mark with the nasal bar (on a narrow and a wide base), gemination, a
  vowel with gemination, nuquerna with a vowel, and both carriers. It is rendered in headless Chrome and
  directly through Core Text, and then Alex checks it in Safari and TextEdit. Chromium alone does not
  prove Core Text behaviour.
- **Results** (the full survey is in `docs/projects/0003-second-encoding/survey.md`, with the details in
  its LOG):

  | Font | License | Core Text and Safari | Chrome | Verdict |
  |---|---|---|---|---|
  | FreeMonoTengwar 2013-07-21 | GPLv3+ with font exception | pass | pass | **chosen** |
  | Tengwar Formal CSUR 1.1 | OFL 1.1 | pass (AAT `morx`) | **fail**: Chrome does not apply `morx`; marks are off-centre, and the nasal bar is lost on wide letters | passes Core Text only |
  | Tengwar Telcontar 0.08 | GPLv3+ with font exception | **fail**: dotted circles | **fail** | out (Graphite only) |

- **FreeMonoTengwar is the second encoding** (Alex, 2026-10-11). It renders the same in every engine
  checked, so the review sheet and the PDFs show it correctly.

## Consequences

- Tengwar Formal CSUR stays a candidate. It would become an encoding only together with a review sheet
  and PDF path that shapes AAT, for example by printing through WebKit. Despite its name, it follows
  the FreeTengwar layout, not CSUR (`E018` is `tincoX`, not rómen).
- FreeMonoTengwar is monospaced and does not raise its marks over ascenders. On `{anto}`, `{ampa}`,
  `{formen}`, `{hyarmen}` and `{the-shorthand}`, the marks sit close to the stem and the nasal bar
  crosses it. This is recorded in `spec/encodings/freemono.md` §5.
- **Licensing.** FreeMonoTengwar is GPLv3 or later with a font-embedding exception: a document that
  embeds the font is not itself covered by the GPL. Its FontLog adds that **commercial use of
  Tolkien's tengwar may need permission from the Tolkien Estate**. That applies to the script whatever
  the font, and it applies to Alcarin output too. This project gives no legal advice; anyone publishing
  commercially should ask.
- The gate fixture stays in the project's `.wip/` for now. It is reused by re-running it with a
  font's cmap values.
