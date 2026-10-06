# shavian2tengwar

A Unix-style CLI stream converter written in Python that translates UTF-8 Shavian text (`U+10450`–`U+1047F`) into Everson 2001 / Alcarin Tengwar Private Use Area code points (`U+E000`–`U+E07F`).

## Overview

Traditional English orthography is non-phonetic, making direct English-to-Tengwar transliteration complex and context-heavy. `shavian2tengwar` uses the Shavian alphabet's 40–48 character phonemic system as an Intermediate Representation (IR). By first converting English into Shavian (e.g., via tools like _Shave_), orthographic noise is stripped away, allowing a deterministic 5-pass state machine to map phonemes into Tengwar characters and _tehtar_ (vowel diacritics).

### Key Features

- **Zero Dependencies:** Built exclusively using the Python standard library (`sys`, `re`, `argparse`).
- **Stream-Oriented Pipeline:** Reads from `stdin` or CLI arguments and writes to `stdout`.
- **Passthrough & Escape Tokenization:** Non-Shavian tokens (Latin characters, spaces, punctuation, emojis) pass through unmodified. Verbatim blocks inside `{{...}}` can be retained or stripped using `--strip-escapes`.
- **Step-by-Step Inspector:** Interactive debugging flag (`--inspect`) traces state-machine transitions and byte outputs for any word.
- **Dual Encoding Support:** Defaults to Everson 2001 / Alcarin mapping (`U+E000`–`U+E07F`) while providing `--csur` for legacy CSUR mapping compatibility.
- **Language-Agnostic Test Suite:** Includes an extended 26-case test manifest (`test_cases_everson_3.json`) and runner to validate byte parity across implementations.

---

## Repository Structure

```text
.
├── LICENSE
├── shavian2tengwar.py            # Primary Python CLI & translation engine
├── test_cases_everson_3.json     # Extended 26-case test manifest
└── test_runner.py                # Cross-implementation test harness with flag support
```
