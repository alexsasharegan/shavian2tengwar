"""tools/font_gate.py: the gate page covers every registered encoding, in both mark orders."""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from s2t import ENCODINGS
from tools.font_gate import CASES, main, parse_column, rows


class FontGate(unittest.TestCase):
    def test_every_case_encodes_in_every_encoding(self):
        columns = [parse_column(name) for name in ENCODINGS]
        seen = {label for label, _, _ in rows(columns)}
        self.assertEqual(seen, {label for label, _ in CASES})

    def test_two_marks_above_are_shown_in_both_orders(self):
        columns = [parse_column("alcarin")]
        int_rows = {order: texts["alcarin"] for label, order, texts in rows(columns) if label.endswith(" int")}
        self.assertEqual(int_rows, {"nearest-first": "", "top-first": ""})

    def test_writes_the_page_for_installed_fonts(self):
        with tempfile.TemporaryDirectory() as tmp:
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main([tmp, *ENCODINGS]), 0)
            page = (Path(tmp) / "gate.html").read_text(encoding="utf-8")
            for name in ENCODINGS:
                self.assertIn(f">{name}<", page)
            self.assertTrue((Path(tmp) / "gate.rtf").read_text(encoding="ascii").startswith("{\\rtf1"))


if __name__ == "__main__":
    unittest.main()
