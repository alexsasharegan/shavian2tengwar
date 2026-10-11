"""Text streams, the public API, and glyph (de)serialization."""

import unittest

from s2t import Cell, get_encoding, parse_literal, render, to_literal, translate
from s2t.encodings import Encoding
from tools.corpus import corpus_files, load


class Passthrough(unittest.TestCase):
    def test_non_shavian_text_is_unchanged(self):
        text = "Hello, world 123 \U0001f600 'quoted' it's"
        items = translate(text)
        self.assertIn("H", items)
        self.assertEqual(to_literal(translate("abc xyz")), "abc xyz")
        self.assertIn("'", to_literal(translate("it's")))

    def test_empty_and_whitespace(self):
        self.assertEqual(translate(""), [])
        self.assertEqual(render("  \n\t"), "  \n\t")

    def test_namer_dot_is_dropped(self):
        self.assertEqual(to_literal(translate("·𐑕𐑨𐑥")), to_literal(translate("𐑕𐑨𐑥")))


class Escapes(unittest.TestCase):
    def test_verbatim_block_is_kept(self):
        self.assertEqual(render("𐑞 {{𐑞 raw}} 𐑞", "literal"), "{the-shorthand} {{𐑞 raw}} {the-shorthand}")

    def test_strip_escapes_unwraps_without_translating(self):
        self.assertEqual(render("{{𐑞 raw}}", "literal", strip_escapes=True), "𐑞 raw")

    def test_block_may_span_lines(self):
        self.assertEqual(render("{{a\nb}}", "literal", strip_escapes=True), "a\nb")

    def test_unclosed_block_is_ordinary_text(self):
        self.assertEqual(render("{{ 𐑞", "literal"), "{{ {the-shorthand}")


class Punctuation(unittest.TestCase):
    def test_every_mapped_mark(self):
        expected = {
            ",": "{pusta}", ".": "{double-pusta}", ";": "{double-section-mark}", ":": "{triple-pusta}",
            "-": "{section-mark}", "!": "{exclamation-mark}", "?": "{question-mark}",
            "(": "{parenthesis-mark}", ")": "{parenthesis-mark}",
            "“": "{left-quotation-mark}", "”": "{right-quotation-mark}",
        }
        for mark, glyph in expected.items():
            with self.subTest(mark=mark):
                self.assertEqual(render(mark, "literal"), glyph)

    def test_ascii_quotes_alternate(self):
        self.assertEqual(
            render('"a" "b"', "literal"),
            "{left-quotation-mark}a{right-quotation-mark} {left-quotation-mark}b{right-quotation-mark}",
        )

    def test_unbalanced_quote_just_opens(self):
        self.assertEqual(render('"', "literal"), "{left-quotation-mark}")
        self.assertEqual(render('" "', "literal"), "{left-quotation-mark} {right-quotation-mark}")

    def test_quote_state_carries_across_words(self):
        self.assertEqual(render('"𐑞 "', "literal"), "{left-quotation-mark}{the-shorthand} {right-quotation-mark}")

    def test_apostrophes_and_single_quotes_pass_through(self):
        self.assertEqual(render("' ’", "literal"), "' ’")


class Api(unittest.TestCase):
    def test_unknown_format(self):
        with self.assertRaisesRegex(ValueError, "unknown format"):
            render("𐑞", "nope")

    def test_unknown_encoding(self):
        with self.assertRaisesRegex(ValueError, "unknown encoding"):
            get_encoding("nope")
        with self.assertRaisesRegex(ValueError, "unknown encoding"):
            render("𐑞", "pua", "nope")

    def test_encoding_names_the_missing_glyph_or_mark(self):
        enc = get_encoding("alcarin")
        with self.assertRaisesRegex(KeyError, "no code point for glyph"):
            enc.encode_cell(Cell("no-such-glyph"))
        with self.assertRaisesRegex(KeyError, "no code point for mark"):
            enc.encode_cell(Cell("tinco", ("no-such-mark",)))
        self.assertIsInstance(enc, Encoding)

    def test_encode_passes_raw_text_through(self):
        self.assertEqual(get_encoding("alcarin").encode(["a", Cell("tinco"), " "]), "a ")


class LiteralRoundTrip(unittest.TestCase):
    def test_parse_then_serialize_is_the_identity_on_the_corpus(self):
        checked = 0
        for path in corpus_files():
            cases, _, _ = load(path)
            for case in cases:
                with self.subTest(case["shavian"]):
                    self.assertEqual(to_literal(parse_literal(case["glyphs"])), case["glyphs"])
                    checked += 1
        self.assertGreater(checked, 50)

    def test_parse_separates_cells_from_text(self):
        self.assertEqual(parse_literal("a{tinco}[dot-above] {anna}"),
                         ["a", Cell("tinco", ("dot-above",)), " ", Cell("anna")])

    def test_engine_output_round_trips_through_the_literal(self):
        for text in ("𐑞 𐑒𐑨𐑑 𐑕𐑨𐑑, 𐑯 𐑦𐑑 𐑕𐑰𐑯!", "𐑥𐑦𐑕𐑑𐑼 \"𐑐𐑤𐑰𐑟\" (𐑜𐑴)"):
            with self.subTest(text):
                items = translate(text)
                self.assertEqual(parse_literal(to_literal(items)), items)
                enc = get_encoding("alcarin")
                self.assertEqual(enc.encode(parse_literal(to_literal(items))), enc.encode(items))

    def test_rules_do_not_affect_equality(self):
        self.assertEqual(Cell("tinco", (), ("X-01",)), Cell("tinco"))


if __name__ == "__main__":
    unittest.main()
