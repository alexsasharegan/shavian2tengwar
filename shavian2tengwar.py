#!/usr/bin/env python3
"""Convert Shavian text to Tengwar (Alcarin Tengwar code points by default).

The conversion itself lives in the s2t package (see spec/mode.md); this file
is the command-line front end.
"""

import argparse
import sys

from s2t import get_encoding, to_literal, translate, translate_word
from s2t.glyphs import Cell


def inspect_word(word: str, encoding_name: str) -> None:
    enc = get_encoding(encoding_name)
    trace: list = []
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


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Shavian text to Tengwar. Reads stdin if no text is given."
    )
    parser.add_argument("text", nargs="?", help="Text to convert.")
    parser.add_argument("--inspect", metavar="WORD", help="Show how one Shavian word is converted, rule by rule.")
    parser.add_argument(
        "--format",
        choices=("pua", "literal"),
        default="pua",
        help="pua: font code points (default). literal: glyph names such as {tinco}[dot-above], "
        "which can be pasted into tecendil.com.",
    )
    parser.add_argument("--encoding", default="alcarin", help="Font encoding (default: alcarin).")
    parser.add_argument(
        "--strip-escapes",
        action="store_true",
        help="Strip the outer {{ and }} from verbatim pass-through blocks.",
    )
    args = parser.parse_args()

    if args.inspect:
        inspect_word(args.inspect, args.encoding)
        return

    text = args.text if args.text else sys.stdin.read()
    items = translate(text, strip_escapes=args.strip_escapes)
    if args.format == "literal":
        out = to_literal(items)
    else:
        out = get_encoding(args.encoding).encode(items)
    if args.text:
        print(out)
    else:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()
