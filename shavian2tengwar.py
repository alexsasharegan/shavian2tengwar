#!/usr/bin/env python3
import argparse
import re
import sys

SHAVIAN_WORD_PATTERN = re.compile(r'([\u00B7\U00010450-\U0001047F]+)')

# --- STATIC CSUR MAPPINGS ---
TENGWAR_CONSONANTS = {
    '𐑐': ('\uE001', 'Parma'), '𐑚': ('\uE005', 'Umbar'), '𐑑': ('\uE000', 'Tinco'), '𐑛': ('\uE004', 'Ando'),
    '𐑒': ('\uE003', 'Quesse'), '𐑜': ('\uE007', 'Ungwe'), '𐑗': ('\uE002', 'Calma'), '𐑡': ('\uE006', 'Anga'),
    '𐑓': ('\uE009', 'Formen'), '𐑝': ('\uE00D', 'Ampa'), '𐑔': ('\uE008', 'Thúle'), '𐑞': ('\uE00C', 'Anta'),
    '𐑖': ('\uE00A', 'Harma'), '𐑠': ('\uE00E', 'Anca'), '𐑕': ('\uE01C', 'Silme'), '𐑟': ('\uE01E', 'Esse'),
    '𐑥': ('\uE011', 'Malta'), '𐑯': ('\uE010', 'Númen'), '𐑙': ('\uE012', 'Noldo'), '𐑤': ('\uE01A', 'Lamba'),
    '𐑣': ('\uE020', 'Hyarmen'), '𐑢': ('\uE015', 'Vala'), '𐑘': ('\uE016', 'Anna')
}

SHORT_VOWELS = {
    '𐑦': ('\uE044', 'i-tehta'), '𐑧': ('\uE046', 'e-tehta'), '𐑨': ('\uE040', 'a-tehta'),
    '𐑪': ('\uE04A', 'o-tehta'), '𐑷': ('\uE04A', 'awe-tehta'), '𐑳': ('\uE04C', 'u-tehta'),
    '𐑫': ('\uE04C', 'foot-tehta'), '𐑩': ('\uE045', 'schwa-tehta')
}

DIPHTHONGS = {
    '𐑲': ('\uE016', '\uE040', 'PRICE (Anna + a-tehta)'),
    '𐑶': ('\uE016', '\uE04A', 'CHOICE (Anna + o-tehta)'),
    '𐑱': ('\uE016', '\uE046', 'FACE (Anna + e-tehta)'),
    '𐑬': ('\uE015', '\uE040', 'MOUTH (Vala + a-tehta)'),
    '𐑴': ('\uE015', '\uE04A', 'GOAT (Vala + o-tehta)'),
    '𐑾': ('\uE016', '\uE044', 'IAN (Anna + i-tehta)'),
    '𐑿': ('\uE016', '\uE04C', 'YEW (Anna + u-tehta)'),
}

# R-Colored Vowels
R_VOWELS = {
    '𐑸': ('\uE018', '\uE040', 'START (Rómen + a-tehta)'),
    '𐑹': ('\uE018', '\uE04A', 'NORTH (Rómen + o-tehta)'),
    '𐑺': ('\uE018', '\uE046', 'SQUARE (Rómen + e-tehta)'),
    '𐑽': ('\uE018', '\uE044', 'NEAR (Rómen + i-tehta)'),
    '𐑻': ('\uE018', '\uE04C', 'NURSE (Rómen + u-tehta)'),  # Fixed: mapped to u-tehta (U+E04C)
    '𐑼': ('\uE014', None,     'lettER (Unadorned Óre)'),
}

NASAL_BAR_ABOVE = '\uE04E'
ROMEN = '\uE018'
ORE = '\uE014'
SHORT_CARRIER = '\uE028' # Telco
LONG_CARRIER = '\uE029'  # Ára

NASAL_PAIRS = {
    '𐑯𐑑': ('\uE010', '𐑑', 'Númen + Tinco'),
    '𐑯𐑛': ('\uE010', '𐑛', 'Númen + Ando'),
    '𐑙𐑒': ('\uE010', '𐑒', 'Númen + Quesse'),
    '𐑙𐑜': ('\uE010', '𐑜', 'Númen + Ungwe'),
    '𐑥𐑐': ('\uE011', '𐑐', 'Malta + Parma'),
    '𐑥𐑚': ('\uE011', '𐑚', 'Malta + Umbar'),
}

ALL_VOWEL_CHARS = set(SHORT_VOWELS.keys()) | {'𐑰', '𐑵', '𐑭'} | set(DIPHTHONGS.keys()) | set(R_VOWELS.keys())

def translate_word(word: str, inspect: bool = False) -> str:
    """Translates a Shavian word into CSUR Tengwar with optional step-by-step tracing."""
    clean_word = word.replace('·', '')
    if not clean_word:
        return ""

    trace = []
    if inspect:
        trace.append(f"\n=== INSPECTING WORD: '{word}' ===")
        trace.append(f"Pass 1 (Namer Dot Strip): '{clean_word}'")

    output = []
    pending_vowel = None  # Stores ('SHORT', tehta, name), ('LONG_E',), ('LONG_U',)
    i = 0

    def flush_pending_vowel():
        nonlocal pending_vowel
        if pending_vowel is None:
            return
        vtype = pending_vowel[0]
        if vtype == 'LONG_E':
            output.append(LONG_CARRIER)
            output.append('\uE044')
            if inspect:
                trace.append("  [Flush Vowel] Long E -> Long Carrier (U+E029) + i-tehta (U+E044)")
        elif vtype == 'LONG_U':
            output.append(LONG_CARRIER)
            output.append('\uE04C')
            if inspect:
                trace.append("  [Flush Vowel] Long U -> Long Carrier (U+E029) + u-tehta (U+E04C)")
        elif vtype == 'SHORT':
            output.append(SHORT_CARRIER)
            output.append(pending_vowel[1])
            if inspect:
                trace.append(f"  [Flush Vowel] Short Vowel -> Short Carrier (U+E028) + {pending_vowel[2]}")
        pending_vowel = None

    def emit_consonant(base_hex, base_name):
        nonlocal pending_vowel
        output.append(base_hex)
        if inspect:
            trace.append(f"  [Emit Consonant] {base_name} (U+{ord(base_hex):04X})")
        if pending_vowel is not None:
            vtype = pending_vowel[0]
            if vtype == 'LONG_E':
                output.append('\uE047')
                if inspect:
                    trace.append("    └─ Attached: Double Acute (U+E047)")
            elif vtype == 'LONG_U':
                output.append('\uE04D')
                if inspect:
                    trace.append("    └─ Attached: Double Left Curl (U+E04D)")
            elif vtype == 'SHORT':
                output.append(pending_vowel[1])
                if inspect:
                    trace.append(f"    └─ Attached: {pending_vowel[2]} (U+{ord(pending_vowel[1]):04X})")
            pending_vowel = None

    while i < len(clean_word):
        c = clean_word[i]

        # Pass 2: Preconsonantal Nasals
        if i < len(clean_word) - 1:
            pair = clean_word[i:i+2]
            if pair in NASAL_PAIRS:
                nasal_base, stop_char, pair_name = NASAL_PAIRS[pair]
                if pending_vowel is not None:
                    if inspect:
                        trace.append(f"Step {i}: Detected Nasal Pair '{pair}' ({pair_name}) WITH active vowel.")
                    emit_consonant(nasal_base, TENGWAR_CONSONANTS[pair[0]][1])
                    i += 1
                else:
                    if inspect:
                        trace.append(f"Step {i}: Detected Nasal Pair '{pair}' ({pair_name}) WITHOUT active vowel.")
                    stop_hex, stop_name = TENGWAR_CONSONANTS[stop_char]
                    output.append(stop_hex)
                    output.append(NASAL_BAR_ABOVE)
                    if inspect:
                        trace.append(f"  [Emit Pair] {stop_name} (U+{ord(stop_hex):04X}) + Nasal Bar Above (U+E04E)")
                    i += 2
                continue

        # Pass 3: Contextual /r/
        if c == '𐑮':
            is_vowel_next = (i + 1 < len(clean_word) and clean_word[i+1] in ALL_VOWEL_CHARS)
            r_hex = ROMEN if is_vowel_next else ORE
            r_name = "Rómen" if is_vowel_next else "Óre"
            if inspect:
                trace.append(f"Step {i}: Char '𐑮' (r) -> Vowel next={is_vowel_next} -> Select {r_name}")
            emit_consonant(r_hex, r_name)
            i += 1
            continue

        # Standard Consonants
        if c in TENGWAR_CONSONANTS:
            base_hex, base_name = TENGWAR_CONSONANTS[c]
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
            pending_vowel = ('SHORT', v_hex, v_name)
            if inspect:
                trace.append(f"Step {i}: Char '{c}' -> Queue Pending Short Vowel {v_name}")
            i += 1
            continue

        if c == '𐑭':
            if pending_vowel is not None:
                flush_pending_vowel()
            pending_vowel = ('SHORT', '\uE040', 'a-tehta')
            if inspect:
                trace.append(f"Step {i}: Char '𐑭' (PALM) -> Queue Pending a-tehta")
            i += 1
            continue

        # Long Vowels
        if c == '𐑰':
            if pending_vowel is not None:
                flush_pending_vowel()
            pending_vowel = ('LONG_E',)
            if inspect:
                trace.append(f"Step {i}: Char '𐑰' (FLEECE) -> Queue Pending Long E")
            i += 1
            continue

        if c == '𐑵':
            if pending_vowel is not None:
                flush_pending_vowel()
            pending_vowel = ('LONG_U',)
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
        if c in R_VOWELS:
            if pending_vowel is not None:
                flush_pending_vowel()
            r_base, tehta, rv_name = R_VOWELS[c]
            output.append(r_base)
            if tehta:
                output.append(tehta)
            if inspect:
                trace.append(f"Step {i}: Char '{c}' -> R-Vowel {rv_name}")
            i += 1
            continue

        # Fallback for unexpected characters
        if pending_vowel is not None:
            flush_pending_vowel()
        output.append(c)
        i += 1

    if pending_vowel is not None:
        flush_pending_vowel()

    raw_result = "".join(output)

    # Pass 5: Nuquerna Flips
    top_tehtar_all = r'([\uE040\uE044\uE046\uE047\uE04A\uE04C\uE04D\uE04E])'
    flipped_result = re.sub(f'\uE01C{top_tehtar_all}', '\uE01D\\1', raw_result)
    flipped_result = re.sub(f'\uE01E{top_tehtar_all}', '\uE01F\\1', flipped_result)

    if inspect and raw_result != flipped_result:
        trace.append("Pass 5: Applied Nuquerna Flip(s) to Silme/Esse.")

    if inspect:
        hex_stream = " ".join([f"U+{ord(ch):04X}" for ch in flipped_result])
        trace.append(f"Final CSUR Output String: '{flipped_result}'")
        trace.append(f"Final Hex Code Points:   {hex_stream}\n")
        print("\n".join(trace))

    return flipped_result

def process_stream(text: str, inspect: bool = False) -> str:
    parts = SHAVIAN_WORD_PATTERN.split(text)
    out = []
    for part in parts:
        if SHAVIAN_WORD_PATTERN.match(part):
            out.append(translate_word(part, inspect=inspect))
        else:
            out.append(part)
    return "".join(out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert Shavian text stream to CSUR Tengwar.")
    parser.add_argument('text', nargs='?', help='Text string to convert. If omitted, reads from stdin.')
    parser.add_argument('--inspect', help='Inspect state-machine steps for a single Shavian word.')
    args = parser.parse_args()

    if args.inspect:
        translate_word(args.inspect, inspect=True)
    elif args.text:
        print(process_stream(args.text))
    else:
        input_data = sys.stdin.read()
        sys.stdout.write(process_stream(input_data))
