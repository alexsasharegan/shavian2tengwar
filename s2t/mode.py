"""The phonemic English Tengwar mode (spec/mode.md).

Turns one Shavian word into glyph cells. Every cell records the IDs of the
spec rules that produced it, so the corpus can check that the rules it cites
really fire.
"""

from collections.abc import Iterable

from .glyphs import Cell, Item

# --- C-01: consonants -------------------------------------------------------
CONSONANTS = {
    "𐑐": "parma",
    "𐑚": "umbar",
    "𐑑": "tinco",
    "𐑛": "ando",
    "𐑒": "quesse",
    "𐑜": "ungwe",
    "𐑗": "calma",
    "𐑡": "anga",
    "𐑓": "formen",
    "𐑝": "ampa",
    "𐑔": "thuule",
    "𐑞": "anto",
    "𐑖": "harma",
    "𐑠": "anca",
    "𐑕": "silme",
    "𐑟": "esse",
    "𐑥": "malta",
    "𐑯": "nuumen",
    "𐑙": "nwalme",
    "𐑤": "lambe",
    "𐑮": "roomen",
    "𐑢": "vala",
    "𐑘": "anna",
    "𐑣": "hyarmen",
}

# --- N-01, N-02: nasal + homorganic stop -> stop + [bar-above] --------------
NASAL_PAIRS = {
    "𐑯𐑑": ("tinco", "N-01"),
    "𐑯𐑛": ("ando", "N-01"),
    "𐑥𐑐": ("parma", "N-01"),
    "𐑥𐑚": ("umbar", "N-01"),
    "𐑙𐑒": ("quesse", "N-02"),
    "𐑙𐑜": ("ungwe", "N-02"),
}

# --- V-11..V-17: short vowels (mark on the next consonant, V-01) ------------
SHORT_VOWELS = {
    "𐑦": ("dot-above", "V-11"),
    "𐑧": ("acute", "V-12"),
    "𐑨": ("triple-dot-above", "V-13"),
    "𐑩": ("breve", "V-14"),
    "𐑪": ("right-curl", "V-15"),
    "𐑳": ("grave", "V-16"),
    "𐑫": ("left-curl", "V-17"),
}

# --- V-21..V-24: long vowels (always on the long carrier, V-03) -------------
LONG_VOWELS = {
    "𐑰": ("dot-above", "V-21"),
    "𐑭": ("triple-dot-above", "V-22"),
    "𐑷": ("right-curl", "V-23"),
    "𐑵": ("left-curl", "V-24"),
}

# --- D-01..D-05: diphthongs (glide letter carries the nucleus mark) ---------
DIPHTHONGS = {
    "𐑲": ("anna", "triple-dot-above", "D-01"),
    "𐑬": ("vala", "triple-dot-above", "D-02"),
    "𐑱": ("anna", "acute", "D-03"),
    "𐑴": ("vala", "right-curl", "D-04"),
    "𐑶": ("anna", "right-curl", "D-05"),
}

# --- L-01..L-08: ligatures expand to their components first -----------------
LIGATURES = {
    "𐑸": ("𐑭𐑮", "L-01"),
    "𐑹": ("𐑷𐑮", "L-02"),
    "𐑺": ("𐑧𐑮", "L-03"),
    "𐑽": ("𐑦𐑮", "L-04"),
    "𐑻": ("𐑳𐑮", "L-05"),
    "𐑼": ("𐑩𐑮", "L-06"),
    "𐑿": ("𐑘𐑵", "L-07"),
    "𐑾": ("𐑦𐑩", "L-08"),
}

# --- W-01..W-03: whole-word shorthands --------------------------------------
SHORTHANDS = {
    "𐑞": ("the-shorthand", "W-01"),
    "𐑝": ("of-shorthand", "W-02"),
    "𐑯": ("and-shorthand", "W-03"),
}

# --- L-09, L-10 (W-04): the words 𐑑 and 𐑓 are weak forms, /tə/ and /fər/ -----
WEAK_FORMS = {
    "𐑑": ("𐑑𐑩", "L-09"),
    "𐑓": ("𐑓𐑼", "L-10"),
}

type Letter = tuple[str, tuple[str, ...]]  # (Shavian letter, rules that produced it)
type Trace = list[tuple[str, list[Item]]]  # (consumed text, items it produced)


def _expand(word: str, extra: tuple[str, ...] = ()) -> list[Letter]:
    out: list[Letter] = []
    for ch in word:
        if ch in LIGATURES:
            components, rule = LIGATURES[ch]
            out.extend((c, extra + (rule,)) for c in components)
        else:
            out.append((ch, extra))
    return out


def _uniq(*groups: Iterable[str]) -> tuple[str, ...]:
    seen: list[str] = []
    for g in groups:
        for r in g:
            if r not in seen:
                seen.append(r)
    return tuple(seen)


def translate_word(word: str, trace: Trace | None = None) -> list[Item]:
    """Translate one Shavian word into a list of Cells.

    Letters outside the Shavian alphabet are passed through as raw strings.
    If ``trace`` is a list, (consumed_text, items) steps are appended to it.
    """
    word = word.replace("·", "")  # namer dot
    if not word:
        return []

    if word in SHORTHANDS:
        base, rule = SHORTHANDS[word]
        cell = Cell(base, (), (rule,))
        if trace is not None:
            trace.append((word, [cell]))
        return [cell]

    if word in WEAK_FORMS:
        expansion, rule = WEAK_FORMS[word]
        letters = _expand(expansion, ("W-04", rule))
    else:
        letters = _expand(word)
    cells: list[Item] = []
    pending: tuple[str, tuple[str, ...]] | None = None  # (mark, rules)

    def step(consumed: str, *emitted: Cell) -> None:
        cells.extend(emitted)
        if trace is not None:
            trace.append((consumed, list(emitted)))

    def flush_orphan(consumed: str = "") -> None:
        """V-02: a short vowel with no consonant after it sits on {telco}."""
        nonlocal pending
        if pending is not None:
            mark, rules = pending
            step(consumed, Cell("telco", (mark,), _uniq(rules, ("V-02",))))
            pending = None

    def cluster(base: str, consumed: str, rules: Iterable[str], nasal: bool = False, geminate: bool = False) -> None:
        """Emit a consonant cluster in K-01 order: vowel, nasal, gemination."""
        nonlocal pending
        marks: list[str] = []
        fired = list(rules)
        if pending is not None:
            marks.append(pending[0])
            fired += list(pending[1]) + ["V-01"]
            pending = None
        if nasal:
            marks.append("bar-above")
        if geminate:
            marks.append("bar-below")
        if base in ("silme", "esse"):
            fired.append("S-01")
            if marks and marks != ["bar-below"]:  # any above-mark (S-02)
                base += "-nuquerna"
                fired.append("S-02")
        if len(marks) > 1:
            fired.append("K-01")
        step(consumed, Cell(base, tuple(marks), _uniq(fired)))

    i = 0
    n = len(letters)
    while i < n:
        ch, extra = letters[i]
        nxt = letters[i + 1] if i + 1 < n else None

        # C-02: aspirated wh
        if nxt and ch == "𐑣" and nxt[0] == "𐑢":
            cluster("hwesta", ch + nxt[0], _uniq(extra, nxt[1], ("C-02",)))
            i += 2
            continue

        # N-01 / N-02: nasal + homorganic stop
        if nxt and (ch + nxt[0]) in NASAL_PAIRS:
            base, rule = NASAL_PAIRS[ch + nxt[0]]
            cluster(base, ch + nxt[0], _uniq(extra, nxt[1], (rule,)), nasal=True)
            i += 2
            continue

        # G-01: true phonetic gemination
        if nxt and ch == nxt[0] and ch in CONSONANTS:
            rules = _uniq(extra, nxt[1], ("R-01",) if ch == "𐑮" else ("C-01",), ("G-01",))
            cluster(CONSONANTS[ch], ch + ch, rules, geminate=True)
            i += 2
            continue

        if ch in CONSONANTS:
            rule = "R-01" if ch == "𐑮" else "C-01"
            cluster(CONSONANTS[ch], ch, _uniq(extra, (rule,)))
        elif ch in SHORT_VOWELS:
            flush_orphan()
            mark, rule = SHORT_VOWELS[ch]
            pending = (mark, _uniq(extra, (rule,)))
            if trace is not None:
                trace.append((ch, []))  # queued until a consonant or the word end
        elif ch in LONG_VOWELS:
            flush_orphan()
            mark, rule = LONG_VOWELS[ch]
            step(ch, Cell("aara", (mark,), _uniq(extra, (rule, "V-03"))))
        elif ch in DIPHTHONGS:
            flush_orphan()
            glide, mark, rule = DIPHTHONGS[ch]
            step(ch, Cell(glide, (mark,), _uniq(extra, (rule,))))
        else:
            flush_orphan()
            step(ch, ch)  # not a Shavian letter we know: pass through
        i += 1

    flush_orphan()
    return cells
