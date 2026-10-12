"""corpus/review.html is generated; fail if it is stale."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class ReviewSheet(unittest.TestCase):
    def test_every_sheet_is_current(self):
        from s2t import ENCODINGS
        from tools.render_corpus import sheet_path

        for name in ENCODINGS:
            with self.subTest(name), tempfile.TemporaryDirectory() as tmp:
                out = Path(tmp) / "review.html"
                subprocess.run(
                    [sys.executable, str(ROOT / "tools/render_corpus.py"), "--encoding", name, "-o", str(out)],
                    check=True,
                    capture_output=True,
                )
                committed = sheet_path(name)
                self.assertTrue(committed.is_file(), f"{committed.name} is missing: run npm run corpus")
                self.assertEqual(
                    out.read_text(encoding="utf8"),
                    committed.read_text(encoding="utf8"),
                    f"corpus/{committed.name} is stale: run npm run corpus",
                )

    def test_shareable_sheet_embeds_its_font_and_drops_the_install_note(self):
        from tools.render_corpus import build_sheet

        plain = build_sheet()
        shareable = build_sheet('@font-face { font-family: "Alcarin Tengwar"; src: url(x); }', shareable=True)
        self.assertIn("install the Alcarin Tengwar font", plain)
        self.assertNotIn("install the Alcarin Tengwar font", shareable)
        self.assertIn("@font-face", shareable)
        self.assertEqual(shareable.count('class="row'), plain.count('class="row'))

    def test_each_encoding_sets_its_own_font_family(self):
        from s2t import ENCODINGS, get_encoding
        from tools.render_corpus import build_sheet

        for name in ENCODINGS:
            with self.subTest(name):
                family = get_encoding(name).families[0]
                sheet = build_sheet(encoding=name)
                self.assertIn(f'.tw {{ font-family: "{family}"', sheet)
                self.assertIn(f"install the {family} font", sheet)


if __name__ == "__main__":
    unittest.main()
