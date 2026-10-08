#!/usr/bin/env python3
import argparse
import re
import sys

# Readable literal Shavian range for word parsing
SHAVIAN_WORD_PATTERN = re.compile(r"([·𐑐-𐑿]+)")
STREAM_PATTERN = re.compile(r"(\{\{.*?\}\}|[·𐑐-𐑿]+)", re.DOTALL)

# Fixed static mappings across both CSUR and Everson standards
TENGWAR_CONSONANTS_FIXED = {
    "𐑐": ("\ue001", "Parma"),
    "𐑚": ("\ue005", "Umbar"),
    "𐑑": ("\ue000", "Tinco"),
    "𐑛": ("\ue004", "Ando"),
    "𐑒": ("\ue003", "Quesse"),
    "𐑜": ("\ue007", "Ungwe"),
    "𐑗": ("\ue002", "Calma"),
    "𐑡": ("\ue006", "Anga"),
    "𐑓": ("\ue009", "Formen"),
    "𐑝": ("\ue00d", "Ampa"),
    "𐑔": ("\ue008", "Thúle"),
    "𐑞": ("\ue00c", "Anta"),
    "𐑖": ("\ue00a", "Harma"),
    "𐑠": ("\ue00e", "Anca"),
    "𐑥": ("\ue011", "Malta"),
    "𐑯": ("\ue010", "Númen"),
    "𐑙": ("\ue013", "Nwalme"),
    "𐑢": ("\ue015", "Vala"),
    "𐑘": ("\ue016", "Anna"),
}

SHORT_VOWELS = {
    "𐑦": ("\ue044", "i-tehta"),
    "𐑧": ("\ue046", "e-tehta"),
    "𐑨": ("\ue040", "a-tehta"),
    "𐑪": ("\ue04a", "o-tehta"),
    "𐑷": ("\ue04a", "awe-tehta"),
    "𐑳": ("\ue04c", "u-tehta"),
    "𐑫": ("\ue04c", "foot-tehta"),
    "𐑩": ("\ue045", "schwa-tehta"),
}

DIPHTHONGS = {
    "𐑲": ("\ue016", "\ue040", "PRICE (Anna + a-tehta)"),
    "𐑶": ("\ue016", "\ue04a", "CHOICE (Anna + o-tehta)"),
    "𐑱": ("\ue016", "\ue046", "FACE (Anna + e-tehta)"),
    "𐑬": ("\ue015", "\ue040", "MOUTH (Vala + a-tehta)"),
    "𐑴": ("\ue015", "\ue04a", "GOAT (Vala + o-tehta)"),
    "𐑾": ("\ue016", "\ue044", "IAN (Anna + i-tehta)"),
    "𐑿": ("\ue016", "\ue04c", "YEW (Anna + u-tehta)"),
}

NASAL_BAR_ABOVE = "\ue050"  # Tengwar Sign Nasalizer (Bar Above)
GEMINATION_BAR_BELOW = "\ue051"  # Tengwar Sign Geminator (Bar Below)
ORE = "\ue014"
EXTENDED_ANTA_LOGOGRAM = "\ue01c"  # Appendix E standalone "the" logogram
EXTENDED_AMPA_LOGOGRAM = "\ue01d"  # Appendix E standalone "of" logogram
AND_SHORTHAND_LOGOGRAM = (
    "\ue004\ue050"  # Appendix E standalone "and" shorthand (Ando + Nasal Bar Above)
)

NASAL_PAIRS = {
    "𐑯𐑑": ("\ue010", "𐑑", "Númen + Tinco"),
    "𐑯𐑛": ("\ue010", "𐑛", "Númen + Ando"),
    "𐑙𐑒": ("\ue010", "𐑒", "Númen + Quesse"),
    "𐑙𐑜": ("\ue010", "𐑜", "Númen + Ungwe"),
    "𐑥𐑐": ("\ue011", "𐑐", "Malta + Parma"),
    "𐑥𐑚": ("\ue011", "𐑚", "Malta + Umbar"),
}

ALL_VOWEL_CHARS = (
    set(SHORT_VOWELS.keys())
    | {"𐑰", "𐑵", "𐑭"}
    | set(DIPHTHONGS.keys())
    | {"𐑸", "𐑹", "𐑺", "𐑽", "𐑻", "𐑼"}
)

TENGWAR_PUNCTUATION = {
    ",": "\ue060",  # Pusta (Single dot / bar pause)
    ".": "\ue061",  # Double Pusta (Two dots / bars full stop)
    ";": "\ue062",  # Ternary Stop
    ":": "\ue062",  # Ternary Stop
    "-": "\ue068",  # Tengwar Hyphen
}


def translate_punctuation(text: str) -> str:
    """Translates standard ASCII punctuation marks into Tengwar PUA punctuation code points."""
    out = []
    for ch in text:
        out.append(TENGWAR_PUNCTUATION.get(ch, ch))
    return "".join(out)


def get_encoding_config(use_csur: bool):
    """Returns encoding-specific code points for CSUR vs Everson 2001 (Alcarin)."""
    if use_csur:
        return {
            "silme": "\ue01c",
            "silme_nuq": "\ue01d",
            "esse": "\ue01e",
            "esse_nuq": "\ue01f",
            "romen": "\ue018",
            "lamba": "\ue01a",
            "hyarmen": "\ue020",
            "short_carrier": "\ue028",
            "long_carrier": "\ue029",
            "mode_name": "CSUR (Legacy)",
        }
    else:
        # Everson 2001 / Alcarin Tengwar (Default)
        return {
            "silme": "\ue024",
            "silme_nuq": "\ue025",
            "esse": "\ue026",
            "esse_nuq": "\ue027",
            "romen": "\ue020",
            "lamba": "\ue022",
            "hyarmen": "\ue028",
            "short_carrier": "\ue02e",
            "long_carrier": "\ue02c",
            "mode_name": "Everson 2001 / Alcarin Tengwar (Default)",
        }


def translate_word(word: str, inspect: bool = False, use_csur: bool = False) -> str:
    """Translates a Shavian word into Tengwar PUA code points."""
    clean_word = word.replace("·", "")
    if not clean_word:
        return ""

    # Pass 0: Standalone Big Five Logogram Shorthands
    if clean_word == "𐑞":
        if inspect:
            print(f"\n=== INSPECTING WORD: '{word}' ===")
            print("Step 0: Standalone 'the' (𐑞) -> Extended Tinco Logogram (U+E02C)")
        return EXTENDED_ANTA_LOGOGRAM

    if clean_word == "𐑝":
        if inspect:
            print(f"\n=== INSPECTING WORD: '{word}' ===")
            print("Step 0: Standalone 'of' (𐑝) -> Extended Ampa Logogram (U+E01D)")
        return EXTENDED_AMPA_LOGOGRAM

    if clean_word == "𐑯":
        if inspect:
            print(f"\n=== INSPECTING WORD: '{word}' ===")
            print(
                "Step 0: Standalone 'and' (𐑯) -> Ando + Nasal Bar Shorthand (U+E004 U+E04E)"
            )
        return AND_SHORTHAND_LOGOGRAM

    cfg = get_encoding_config(use_csur)

    consonants = dict(TENGWAR_CONSONANTS_FIXED)
    consonants["𐑤"] = (cfg["lamba"], "Lamba")
    consonants["𐑣"] = (cfg["hyarmen"], "Hyarmen")
    consonants["𐑕"] = (cfg["silme"], "Silme")
    consonants["𐑟"] = (cfg["esse"], "Esse")

    r_vowels = {
        "𐑸": ("\ue040", "START (a-tehta)"),
        "𐑹": ("\ue04a", "NORTH (o-tehta)"),
        "𐑺": ("\ue046", "SQUARE (e-tehta)"),
        "𐑽": ("\ue044", "NEAR (i-tehta)"),
        "𐑻": ("\ue04c", "NURSE (u-tehta)"),
        "𐑼": ("\ue045", "ARRAY/lettER (schwa-tehta)"),
    }

    trace = []
    if inspect:
        trace.append(
            f"\n=== INSPECTING WORD: '{word}' [Encoding: {cfg['mode_name']}] ==="
        )
        trace.append(f"Pass 1 (Namer Dot Strip): '{clean_word}'")

    output = []
    pending_vowel: tuple[str, str, str] | None = (
        None  # Uniform structure: (vtype, tehta_hex, tehta_name)
    )
    i = 0

    def flush_pending_vowel():
        nonlocal pending_vowel
        if pending_vowel is None:
            return
        vtype, tehta, name = pending_vowel
        if vtype == "LONG_E":
            output.append(cfg["long_carrier"])
            output.append("\ue044")
            if inspect:
                trace.append(
                    f"  [Flush Vowel] Long E -> Long Carrier (U+{ord(cfg['long_carrier']):04X}) + i-tehta (U+E044)"
                )
        elif vtype == "LONG_U":
            output.append(cfg["long_carrier"])
            output.append("\ue04c")
            if inspect:
                trace.append(
                    f"  [Flush Vowel] Long U -> Long Carrier (U+{ord(cfg['long_carrier']):04X}) + u-tehta (U+E04C)"
                )
        elif vtype == "SHORT":
            output.append(cfg["short_carrier"])
            output.append(tehta)
            if inspect:
                trace.append(
                    f"  [Flush Vowel] Short Vowel -> Short Carrier (U+{ord(cfg['short_carrier']):04X}) + {name}"
                )
        pending_vowel = None

    def emit_consonant(base_hex, base_name, modifier_hex=None):
        nonlocal pending_vowel
        output.append(base_hex)
        if modifier_hex:
            output.append(modifier_hex)
        if inspect:
            mod_str = f" + Modifier (U+{ord(modifier_hex):04X})" if modifier_hex else ""
            trace.append(
                f"  [Emit Consonant] {base_name} (U+{ord(base_hex):04X}){mod_str}"
            )
        if pending_vowel is not None:
            vtype, tehta, name = pending_vowel
            if vtype == "LONG_E":
                output.append("\ue048")
                if inspect:
                    trace.append("    └─ Attached: Double Acute (U+E047)")
            elif vtype == "LONG_U":
                output.append("\ue04c")
                if inspect:
                    trace.append("    └─ Attached: Double Left Curl (U+E04D)")
            elif vtype == "SHORT":
                output.append(tehta)
                if inspect:
                    trace.append(f"    └─ Attached: {name} (U+{ord(tehta):04X})")
            pending_vowel = None

    while i < len(clean_word):
        c = clean_word[i]

        # Pass 2a: Aspirated Wh Cluster (𐑣𐑢 -> Hwesta U+E00B)
        if i < len(clean_word) - 1 and clean_word[i : i + 2] == "𐑣𐑢":
            emit_consonant("\ue00b", "Hwesta")
            if inspect:
                trace.append(
                    f"Step {i}: Detected Aspirated Wh Cluster '𐑣𐑢' -> Hwesta (U+E00B)"
                )
            i += 2
            continue

        # Pass 2b: Universal Preconsonantal Nasals
        if i < len(clean_word) - 1:
            pair = clean_word[i : i + 2]
            if pair in NASAL_PAIRS:
                _, stop_char, pair_name = NASAL_PAIRS[pair]
                stop_hex, stop_name = consonants[stop_char]
                output.append(stop_hex)
                output.append(NASAL_BAR_ABOVE)
                if inspect:
                    trace.append(
                        f"Step {i}: Detected Universal Nasal Pair '{pair}' ({pair_name}) -> Stop {stop_name} + Nasal Bar Above"
                    )
                if pending_vowel is not None:
                    _, tehta, name = pending_vowel
                    output.append(tehta)
                    if inspect:
                        trace.append(
                            f"    └─ Attached Preceding Vowel Tehta: {name} (U+{ord(tehta):04X})"
                        )
                    pending_vowel = None
                i += 2
                continue

        # Pass 2c: Phonetic Gemination Intercept
        if i < len(clean_word) - 1 and clean_word[i] == clean_word[i + 1]:
            c_gem = clean_word[i]
            if c_gem in consonants:
                base_hex, base_name = consonants[c_gem]
                if inspect:
                    trace.append(
                        f"Step {i}: Detected Phonetic Gemination '{c_gem}{c_gem}' -> {base_name} + Gemination Bar Below"
                    )
                emit_consonant(base_hex, base_name, modifier_hex=GEMINATION_BAR_BELOW)
                i += 2
                continue

        # Pass 3: Contextual /r/
        if c == "𐑮":
            is_vowel_next = (
                i + 1 < len(clean_word) and clean_word[i + 1] in ALL_VOWEL_CHARS
            )
            r_hex = cfg["romen"] if is_vowel_next else ORE
            r_name = "Rómen" if is_vowel_next else "Óre"
            if inspect:
                trace.append(
                    f"Step {i}: Char '𐑮' (r) -> Vowel next={is_vowel_next} -> Select {r_name}"
                )
            emit_consonant(r_hex, r_name)
            i += 1
            continue

        # Standard Consonants
        if c in consonants:
            base_hex, base_name = consonants[c]
            if inspect:
                trace.append(f"Step {i}: Char '{c}' -> Consonant {base_name}")
            emit_consonant(base_hex, base_name)
            i += 1
            continue

        # Short Vowels
        if c in SHORT_VOWELS:
            v_hex, v_name = SHORT_VOWELS[c]
            if pending_vowel is not None:
                flush_pending_vowel()
            pending_vowel = ("SHORT", v_hex, v_name)
            if inspect:
                trace.append(
                    f"Step {i}: Char '{c}' -> Queue Pending Short Vowel {v_name}"
                )
            i += 1
            continue

        if c == "𐑭":
            if pending_vowel is not None:
                flush_pending_vowel()
            pending_vowel = ("SHORT", "\ue040", "a-tehta")
            if inspect:
                trace.append(f"Step {i}: Char '𐑭' (PALM) -> Queue Pending a-tehta")
            i += 1
            continue

        # Long Vowels
        if c == "𐑰":
            if pending_vowel is not None:
                flush_pending_vowel()
            pending_vowel = ("LONG_E", "\ue048", "Double Acute")
            if inspect:
                trace.append(f"Step {i}: Char '𐑰' (FLEECE) -> Queue Pending Long E")
            i += 1
            continue

        if c == "𐑵":
            if pending_vowel is not None:
                flush_pending_vowel()
            pending_vowel = ("LONG_U", "\ue04c", "Double Left Curl")
            if inspect:
                trace.append(f"Step {i}: Char '𐑵' (GOOSE) -> Queue Pending Long U")
            i += 1
            continue

        # Diphthongs
        if c in DIPHTHONGS:
            if pending_vowel is not None:
                flush_pending_vowel()
            carrier, tehta, d_name = DIPHTHONGS[c]
            output.append(carrier)
            output.append(tehta)
            if inspect:
                trace.append(f"Step {i}: Char '{c}' -> Diphthong {d_name}")
            i += 1
            continue

        # R-Colored Vowels
        if c in r_vowels:
            if pending_vowel is not None:
                flush_pending_vowel()
            tehta, rv_name = r_vowels[c]
            is_vowel_next = (
                i + 1 < len(clean_word) and clean_word[i + 1] in ALL_VOWEL_CHARS
            )
            r_hex = cfg["romen"] if is_vowel_next else ORE
            r_name = "Rómen" if is_vowel_next else "Óre"
            output.append(r_hex)
            if tehta:
                output.append(tehta)
            if inspect:
                trace.append(
                    f"Step {i}: Char '{c}' -> R-Vowel {rv_name} using {r_name}"
                )
            i += 1
            continue

        output.append(c)
        i += 1

    if pending_vowel is not None:
        flush_pending_vowel()

    raw_result = "".join(output)

    # Pass 5: Nuquerna Flips
    # Note: uses explicit hex escape ranges for PUA safety (do not rewrite)
    top_tehtar_all = r"([\uE040\uE044\uE046\ue048\uE04A\uE04C\uE04C\uE04E\uE050])"
    flipped_result = re.sub(
        f"{cfg['silme']}{top_tehtar_all}", f"{cfg['silme_nuq']}\\1", raw_result
    )
    flipped_result = re.sub(
        f"{cfg['esse']}{top_tehtar_all}", f"{cfg['esse_nuq']}\\1", flipped_result
    )

    if inspect and raw_result != flipped_result:
        trace.append("Pass 5: Applied Nuquerna Flip(s) to Silme/Esse.")

    if inspect:
        hex_stream = " ".join([f"U+{ord(ch):04X}" for ch in flipped_result])
        trace.append(f"Final Tengwar Output String: '{flipped_result}'")
        trace.append(f"Final Hex Code Points:     {hex_stream}\n")
        print("\n".join(trace))

    return flipped_result


def process_stream(
    text: str,
    inspect: bool = False,
    use_csur: bool = False,
    strip_escapes: bool = False,
) -> str:
    """Processes a text stream, translating Shavian words and punctuation while preserving or stripping {{...}} escape blocks."""
    parts = STREAM_PATTERN.split(text)
    out = []
    for part in parts:
        if part.startswith("{{") and part.endswith("}}"):
            out.append(part[2:-2] if strip_escapes else part)
        elif SHAVIAN_WORD_PATTERN.match(part):
            out.append(translate_word(part, inspect=inspect, use_csur=use_csur))
        else:
            out.append(translate_punctuation(part))
    return "".join(out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert Shavian text stream to Tengwar PUA code points."
    )
    parser.add_argument(
        "text", nargs="?", help="Text string to convert. If omitted, reads from stdin."
    )
    parser.add_argument(
        "--inspect", help="Inspect state-machine steps for a single Shavian word."
    )
    parser.add_argument(
        "--csur",
        action="store_true",
        help="Use classic CSUR mapping (U+E01C, U+E01A, U+E018) instead of Everson 2001 default.",
    )
    parser.add_argument(
        "--strip-escapes",
        action="store_true",
        help="Strip outer {{ and }} escape brackets from verbatim pass-through blocks.",
    )
    args = parser.parse_args()

    if args.inspect:
        translate_word(args.inspect, inspect=True, use_csur=args.csur)
    elif args.text:
        print(
            process_stream(
                args.text, use_csur=args.csur, strip_escapes=args.strip_escapes
            )
        )
    else:
        input_data = sys.stdin.read()
        sys.stdout.write(
            process_stream(
                input_data, use_csur=args.csur, strip_escapes=args.strip_escapes
            )
        )
