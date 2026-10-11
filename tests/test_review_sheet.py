"""corpus/review.html is generated; fail if it is stale."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class ReviewSheet(unittest.TestCase):
    def test_sheet_is_current(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "review.html"
            subprocess.run(
                [sys.executable, str(ROOT / "tools/render_corpus.py"), "-o", str(out)],
                check=True, capture_output=True,
            )
            committed = (ROOT / "corpus/review.html").read_text(encoding="utf8")
            self.assertEqual(out.read_text(encoding="utf8"), committed,
                             "corpus/review.html is stale: run python3 tools/render_corpus.py")


if __name__ == "__main__":
    unittest.main()
