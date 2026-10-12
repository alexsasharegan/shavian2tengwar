#!/usr/bin/env python3
"""Convert Shavian text to Tengwar (Alcarin Tengwar code points by default).

The conversion itself lives in the s2t package (see spec/mode.md); this file
is the command-line front end.
"""

import argparse
import os
import sys

from s2t import ENCODINGS, get_encoding, render, to_literal, translate_word
from s2t.encodings import DEFAULT_ENCODING
from s2t.glyphs import Cell
from s2t.mode import Trace


def inspect_word(word: str, encoding_name: str) -> None:
    enc = get_encoding(encoding_name)
    trace: Trace = []
    cells = translate_word(word, trace)
    print(f"\n=== INSPECTING WORD: '{word}' [Encoding: {enc.name}] ===")
    for consumed, items in trace:
        if not items:
            print(f"  {consumed}  queued: a vowel mark waits for the next consonant (V-01)")
            continue
        for item in items:
            if isinstance(item, Cell):
                rules = ", ".join(item.rules)
                print(f"  {consumed}  ->  {item.literal()}   [{rules}]")
            else:
                print(f"  {consumed}  ->  {item!r}   (passed through)")
    out = enc.encode(cells)
    print(f"Glyphs:      {to_literal(cells)}")
    print(f"Output:      '{out}'")
    print(f"Code points: {' '.join(f'U+{ord(c):04X}' for c in out)}\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Convert Shavian text to Tengwar. Reads stdin if no text is given.")
    parser.add_argument("text", nargs="?", help="Text to convert.")
    parser.add_argument("--inspect", metavar="WORD", help="Show how one Shavian word is converted, rule by rule.")
    parser.add_argument(
        "--format",
        choices=("pua", "literal"),
        default="pua",
        help="pua: font code points (default). literal: glyph names such as {tinco}[dot-above], "
        "which can be pasted into tecendil.com.",
    )
    parser.add_argument(
        "--encoding",
        choices=ENCODINGS,
        default=DEFAULT_ENCODING,
        help="Font encoding (default: %(default)s).",
    )
    parser.add_argument(
        "--strip-escapes",
        action="store_true",
        help="Strip the outer {{ and }} from verbatim pass-through blocks.",
    )
    args = parser.parse_args(argv)

    try:
        if args.inspect is not None:
            inspect_word(args.inspect, args.encoding)
            sys.stdout.flush()
            return 0

        text = args.text if args.text is not None else sys.stdin.read()
        out = render(text, args.format, args.encoding, args.strip_escapes)
        if args.text is not None:
            print(out)
        else:
            sys.stdout.write(out)
        sys.stdout.flush()
    except UnicodeDecodeError as exc:
        parser.exit(1, f"{parser.prog}: input is not valid UTF-8 ({exc.reason})\n")
    except BrokenPipeError:
        # The reader went away (`... | head`). Point stdout at /dev/null so the interpreter's
        # flush at exit does not raise again, and stop quietly.
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        return 1
    return 0


if __name__ == "__main__":
    # Tengwar is written as Private Use code points, so the I/O must be UTF-8 whatever the
    # locale says; otherwise Python substitutes or fails under a non-UTF-8 locale.
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
