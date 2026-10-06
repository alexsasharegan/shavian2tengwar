# shave2tengwar

A Unix-style CLI stream converter written in Python that translates UTF-8 Shavian text (`U+10450`–`U+1047F`) into ConScript Unicode Registry (CSUR) Tengwar Private Use Area code points (`U+E000`–`U+E07F`).

## Overview

Traditional English orthography is non-phonetic, making direct English-to-Tengwar transliteration complex and context-heavy. `shave2tengwar` uses the Shavian alphabet's 40–48 character phonemic system as an Intermediate Representation (IR). By first converting English into Shavian (e.g., via tools like *Shave*), orthographic noise is stripped away, allowing a deterministic 5-pass state machine to map phonemes into Tengwar characters and *tehtar* (vowel diacritics).

### Key Features

* **Zero Dependencies:** Built exclusively using the Python standard library (`sys`, `re`, `argparse`).
* **Stream-Oriented Pipeline:** Reads from `stdin` or CLI arguments and writes to `stdout`.
* **Passthrough Tokenization:** Non-Shavian tokens (Latin characters, spaces, punctuation, emojis) pass through completely unmodified.
* **Step-by-Step Inspector:** Interactive debugging flag (`--inspect`) traces state-machine transitions and byte outputs for any word.
* **Language-Agnostic Test Suite:** Includes a harness to validate byte parity across Python, Go, Rust, or C++ ports.

---

## Repository Structure

```text
.
├── LICENSE
├── main.py            # Primary Python CLI & translation engine
├── test_cases.json    # Language-agnostic test case manifest
└── test_runner.py     # Universal cross-implementation test harness
```

---

## Translation Engine Architecture

The engine executes a 5-pass state machine on word-boundary isolated tokens (`TOKEN_SHAVIAN_WORD`) in **Following Consonant Mode** (vowel *tehtar* attach to the *next* consonant in the word):

```text
[ Input Stream ] ──► [ Tokenizer ] ──► TOKEN_PASSTHROUGH ───────────────┐
                          │                                             │
                          ▼                                             ▼
                 TOKEN_SHAVIAN_WORD ──► [ 5-Pass State Machine ] ──► [ Output Stream ]
```

1. **Pass 1: Normalization & Namer Dot Strip:** Strips Shavian namer dots (`·`, `U+00B7`) to ensure plain-text portability.
2. **Pass 2: Preconsonantal Nasals:** Handles homorganic nasal-stop pairs (`𐑯𐑑`, `𐑯𐑛`, `𐑥𐑐`, `𐑥𐑚`, `𐑙𐑒`, `𐑙𐑜`).
	* If a vowel *tehta* is active on the pair, the engine emits a full nasal base character (*Númen* `U+E010` / *Malta* `U+E011`) to carry the mark.
	* If no vowel *tehta* is active, the cluster collapses into a single stop base character carrying a *Nasal Bar Above* (`U+E04E`).
3. **Pass 3: Contextual Consonant Selection (`𐑮` /r/):**
	* Emits *Rómen* (`U+E018`) when followed by a Shavian vowel in the word.
	* Emits *Óre* (`U+E014`) when word-final or followed by a consonant.
4. **Pass 4: Vowel Attachment & Carrier Resolution:**
	* **Short Vowels:** Attach to the following consonant base glyph.
	* **R-Colored Vowels (`𐑸`, `𐑹`, `𐑻`, `𐑺`, `𐑽`):** Decompose into `[Tehta]` + *Rómen* (`U+E018`). Unadorned `𐑼` maps directly to *Óre* (`U+E014`).
	* **Diphthongs (`𐑲`, `𐑶`, `𐑱`, `𐑬`, `𐑴`):** Emit offglide carriers (*Anna* `U+E016` or *Vala* `U+E015`) carrying the primary *tehta*.
	* **Orphan / Word-Final Vowels:** Flush to a *Short Carrier* (*Telco*, `U+E028`) or *Long Carrier* (*Ára*, `U+E029`).
5. **Pass 5: Positional Inversions (*Nuquerna* Flips):** Automatically converts upright *Silme* (`U+E01C`) and *Esse* (`U+E01E`) to *Silme Nuquerna* (`U+E01D`) and *Esse Nuquerna* (`U+E01F`) whenever carrying any top-placed *tehta* or nasal bar.

---

## Font & Rendering Requirements

Because CSUR code points reside in the Unicode Private Use Area (`U+E000`–`U+E07F`), displaying transformed text requires a CSUR-compatible Tengwar font.

* **Recommended Font:** **[Alcarin Tengwar](https://github.com/Tosche/Alcarin-Tengwar)** (by Toshi Omagari / Tosche).
	* **macOS & Modern IDE Users:** Download and install *Alcarin Tengwar* for clean visual rendering in macOS apps, VS Code, and browser text editors. *Alcarin* is built with native OpenType `mark` / `mkmk` GPOS positioning tables, allowing standard Chromium/HarfBuzz text shapers to anchor diacritics directly over consonant bases without fallback errors.
* **Important Note on *Tengwar Telcontar*:**
	* While *Tengwar Telcontar* is a popular CSUR font, it relies on the **SIL Graphite** layout engine to calculate mark positioning.
	* Most modern text editors, terminals, and OS text views (including VS Code and macOS native UI components) do not execute SIL Graphite tables for Private Use Area characters. In these environments, *Tengwar Telcontar* will fail to anchor diacritics and will render orphan **dotted circles** (`◌`) underneath every vowel *tehta*. Always use an OpenType-native font like *Alcarin Tengwar* when editing in VS Code or viewing text on macOS.

---

## Usage

### Stream Processing (Pipes & Redirection)

```bash
# Process string via pipe
echo "𐑢𐑦𐑯𐑑𐑼" | python3 main.py

# Process input file to output file
python3 main.py < in.md > out.md
```

### Direct Argument Processing

```bash
python3 main.py "𐑦𐑯 𐑩 𐑣𐑴𐑤 𐑦𐑯 𐑞 𐑜𐑮𐑬𐑯𐑛 𐑞𐑺 𐑤𐑦𐑝𐑛 𐑩 𐑣𐑪𐑚𐑦𐑑"
```

### Interactive Word Inspector (`--inspect`)

Trace individual character state transitions, carrier flushes, and final CSUR hex outputs:

```bash
python3 main.py --inspect "𐑢𐑦𐑯𐑑𐑼"
```

**Output:**

```text
=== INSPECTING WORD: '𐑢𐑦𐑯𐑑𐑼' ===
Pass 1 (Namer Dot Strip): '𐑢𐑦𐑯𐑑𐑼'
Step 0: Char '𐑢' -> Consonant Vala
  [Emit Consonant] Vala (U+E015)
Step 1: Char '𐑦' -> Queue Pending Short Vowel i-tehta
Step 2: Detected Nasal Pair '𐑯𐑑' (Númen + Tinco) WITH active vowel.
  [Emit Consonant] Númen (U+E010)
    └─ Attached: i-tehta (U+E044)
Step 3: Char '𐑑' -> Consonant Tinco
  [Emit Consonant] Tinco (U+E000)
Step 4: Char '𐑼' -> R-Vowel lettER (Unadorned Óre)
Final CSUR Output String: ''
Final Hex Code Points:   U+E015 U+E010 U+E044 U+E000 U+E014
```

---

## Testing & Cross-Implementation Verification

The repository includes a language-agnostic test suite driven by `test_cases.json`. The runner script pipes inputs to `stdin` and verifies exact byte-level UTF-8 output strings.

### Running Tests

```bash
# Test the Python reference implementation
python3 test_runner.py --cmd "python3 main.py"

# Test future Go, Rust, or C++ implementations
python3 test_runner.py --cmd "./shave2tengwar_go"
python3 test_runner.py --cmd "./target/release/shave2tengwar"
```
