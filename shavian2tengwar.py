#!/usr/bin/env python3
import argparse
import re
import sys

SHAVIAN_WORD_PATTERN = re.compile(r'([\u00B7\U00010450-\U0001047F]+)')

# Fixed static mappings across both CSUR and Everson standards
TENGWAR_CONSONANTS_FIXED = {
    '𐑐': ('\uE001', 'Parma'), '𐑚': ('\uE005', 'Umbar'), '𐑑': ('\uE000', 'Tinco'), '𐑛': ('\uE004', 'Ando'),
    '𐑒': ('\uE003', 'Quesse'), '𐑜': ('\uE007', 'Ungwe'), '𐑗': ('\uE002', 'Calma'), '𐑡': ('\uE006', 'Anga'),
    '𐑓': ('\uE009', 'Formen'), '𐑝': ('\uE00D', 'Ampa'), '𐑔': ('\uE008', 'Thúle'), '𐑞': ('\uE00C', 'Anta'),
    '𐑖': ('\uE00A', 'Harma'), '𐑠': ('\uE00E', 'Anca'),
    '𐑥': ('\uE011', 'Malta'), '𐑯': ('\uE010', 'Númen'), '𐑙': ('\uE012', 'Noldo'),
    '𐑢': ('\uE015', 'Vala'), '𐑘': ('\uE016', 'Anna')
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

NASAL_BAR_ABOVE = '\uE04E'
ORE = '\uE014'
EXTENDED_AMPA_LOGOGRAM = '\uE01D' # Appendix E standalone "of" logogram

NASAL_PAIRS = {
    '𐑯𐑑': ('\uE010', '𐑑', 'Númen + Tinco'),
    '𐑯𐑛': ('\uE010', '𐑛', 'Númen + Ando'),
    '𐑙𐑒': ('\uE010', '𐑒', 'Númen + Quesse'),
    '𐑙𐑜': ('\uE010', '𐑜', 'Númen + Ungwe'),
    '𐑥𐑐': ('\uE011', '𐑐', 'Malta + Parma'),
    '𐑥𐑚': ('\uE011', '𐑚', 'Malta + Umbar'),
}

ALL_VOWEL_CHARS = set(SHORT_VOWELS.keys()) | {'𐑰', '𐑵', '𐑭'} | set(DIPHTHONGS.keys()) | {'𐑸', '𐑹', '𐑺', '𐑽', '𐑻', '𐑼'}

TENGWAR_PUNCTUATION = {
    ',': '\uE060',  # Pusta (Single dot / bar pause)
    '.': '\uE061',  # Double Pusta (Two dots / bars full stop)
    ';': '\uE062',  # Ternary Stop
    ':': '\uE062',  # Ternary Stop
    '-': '\uE068',  # Tengwar Hyphen
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
            'silme': '\uE01C',
            'silme_nuq': '\uE01D',
            'esse': '\uE01E',
            'esse_nuq': '\uE01F',
            'romen': '\uE018',
            'lamba': '\uE01A',
            'hyarmen': '\uE020',
            'short_carrier': '\uE028',
            'long_carrier': '\uE029',
            'mode_name': 'CSUR (Legacy)'
        }
    else:
        # Everson 2001 / Alcarin Tengwar (Default)
        return {
            'silme': '\uE024',
            'silme_nuq': '\uE025',
            'esse': '\uE026',
            'esse_nuq': '\uE027',
            'romen': '\uE020',
            'lamba': '\uE022',
            'hyarmen': '\uE028',
            'short_carrier': '\uE02D',
            'long_carrier': '\uE02E',
            'mode_name': 'Everson 2001 / Alcarin Tengwar (Default)'
        }

def translate_word(word: str, inspect: bool = False, use_csur: bool = False) -> str:
    """Translates a Shavian word into Tengwar PUA code points."""
    clean_word = word.replace('·', '')
    if not clean_word:
        return ""

    # Check for standalone 'of' logogram (𐑝)
    if clean_word == '𐑝':
        if inspect:
            print(f"\n=== INSPECTING WORD: '{word}' ===")
            print("Step 0: Standalone 'of' (𐑝) -> Extended Ampa Logogram (U+E01D)")
            print(f"Final Tengwar Output String: '{EXTENDED_AMPA_LOGOGRAM}'")
            print(f"Final Hex Code Points:     U+E01D\n")
        return EXTENDED_AMPA_LOGOGRAM

    cfg = get_encoding_config(use_csur)

    consonants = dict(TENGWAR_CONSONANTS_FIXED)
    consonants['𐑤'] = (cfg['lamba'], 'Lamba')
    consonants['𐑣'] = (cfg['hyarmen'], 'Hyarmen')
    consonants['𐑕'] = (cfg['silme'], 'Silme')
    consonants['𐑟'] = (cfg['esse'], 'Esse')

    r_vowels = {
        '𐑸': (cfg['romen'], '\uE040', 'START (Rómen + a-tehta)'),
        '𐑹': (cfg['romen'], '\uE04A', 'NORTH (Rómen + o-tehta)'),
        '𐑺': (cfg['romen'], '\uE046', 'SQUARE (Rómen + e-tehta)'),
        '𐑽': (cfg['romen'], '\uE044', 'NEAR (Rómen + i-tehta)'),
        '𐑻': (cfg['romen'], '\uE04C', 'NURSE (Rómen + u-tehta)'),
        '𐑼': (ORE, None, 'lettER (Unadorned Óre)'),
    }

    trace = []
    if inspect:
        trace.append(f"\n=== INSPECTING WORD: '{word}' [Encoding: {cfg['mode_name']}] ===")
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
            output.append(cfg['long_carrier'])
            output.append('\uE044')
            if inspect:
                trace.append(f"  [Flush Vowel] Long E -> Long Carrier (U+{ord(cfg['long_carrier']):04X}) + i-tehta (U+E044)")
        elif vtype == 'LONG_U':
            output.append(cfg['long_carrier'])
            output.append('\uE04C')
            if inspect:
                trace.append(f"  [Flush Vowel] Long U -> Long Carrier (U+{ord(cfg['long_carrier']):04X}) + u-tehta (U+E04C)")
        elif vtype == 'SHORT':
            output.append(cfg['short_carrier'])
            output.append(pending_vowel[1])
            if inspect:
                trace.append(f"  [Flush Vowel] Short Vowel -> Short Carrier (U+{ord(cfg['short_carrier']):04X}) + {pending_vowel[2]}")
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
                    emit_consonant(nasal_base, consonants[pair[0]][1])
                    i += 1
                else:
                    if inspect:
                        trace.append(f"Step {i}: Detected Nasal Pair '{pair}' ({pair_name}) WITHOUT active vowel.")
                    stop_hex, stop_name = consonants[stop_char]
                    output.append(stop_hex)
                    output.append(NASAL_BAR_ABOVE)
                    if inspect:
                        trace.append(f"  [Emit Pair] {stop_name} (U+{ord(stop_hex):04X}) + Nasal Bar Above (U+E04E)")
                    i += 2
                continue

        # Pass 3: Contextual /r/
        if c == '𐑮':
            is_vowel_next = (i + 1 < len(clean_word) and clean_word[i+1] in ALL_VOWEL_CHARS)
            r_hex = cfg['romen'] if is_vowel_next else ORE
            r_name = "Rómen" if is_vowel_next else "Óre"
            if inspect:
                trace.append(f"Step {i}: Char '𐑮' (r) -> Vowel next={is_vowel_next} -> Select {r_name}")
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
        if c in r_vowels:
            if pending_vowel is not None:
                flush_pending_vowel()
            r_base, tehta, rv_name = r_vowels[c]
            output.append(r_base)
            if tehta:
                output.append(tehta)
            if inspect:
                trace.append(f"Step {i}: Char '{c}' -> R-Vowel {rv_name}")
            i += 1
            continue

        output.append(c)
        i += 1

    if pending_vowel is not None:
        flush_pending_vowel()

    raw_result = "".join(output)

    # Pass 5: Nuquerna Flips
    top_tehtar_all = r'([\uE040\uE044\uE046\uE047\uE04A\uE04C\uE04D\uE04E])'
    flipped_result = re.sub(f"{cfg['silme']}{top_tehtar_all}", f"{cfg['silme_nuq']}\\1", raw_result)
    flipped_result = re.sub(f"{cfg['esse']}{top_tehtar_all}", f"{cfg['esse_nuq']}\\1", flipped_result)

    if inspect and raw_result != flipped_result:
        trace.append("Pass 5: Applied Nuquerna Flip(s) to Silme/Esse.")

    if inspect:
        hex_stream = " ".join([f"U+{ord(ch):04X}" for ch in flipped_result])
        trace.append(f"Final Tengwar Output String: '{flipped_result}'")
        trace.append(f"Final Hex Code Points:     {hex_stream}\n")
        print("\n".join(trace))

    return flipped_result

def process_stream(text: str, inspect: bool = False, use_csur: bool = False) -> str:
    parts = SHAVIAN_WORD_PATTERN.split(text)
    out = []
    for part in parts:
        if SHAVIAN_WORD_PATTERN.match(part):
            out.append(translate_word(part, inspect=inspect, use_csur=use_csur))
        else:
            out.append(translate_punctuation(part))
    return "".join(out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert Shavian text stream to Tengwar PUA code points.")
    parser.add_argument('text', nargs='?', help='Text string to convert. If omitted, reads from stdin.')
    parser.add_argument('--inspect', help='Inspect state-machine steps for a single Shavian word.')
    parser.add_argument('--csur', action='store_true', help='Use classic CSUR mapping (U+E01C, U+E01A, U+E018) instead of Everson 2001 default.')
    args = parser.parse_args()

    if args.inspect:
        translate_word(args.inspect, inspect=True, use_csur=args.csur)
    elif args.text:
        print(process_stream(args.text, use_csur=args.csur))
    else:
        input_data = sys.stdin.read()
        sys.stdout.write(process_stream(input_data, use_csur=args.csur))
