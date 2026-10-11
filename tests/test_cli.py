"""The command line: arguments, stdin, exit codes, and I/O encoding."""

import contextlib
import io
import os
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

import shavian2tengwar
from s2t import render

ROOT = Path(__file__).resolve().parent.parent
CLI = str(ROOT / "shavian2tengwar.py")
TOWN = "𐑑𐑬𐑯"
TOWN_LITERAL = "{tinco}{vala}[triple-dot-above]{nuumen}"


def run_main(*argv, stdin=None):
    """Call main() in-process; return (exit code, stdout)."""
    out = io.StringIO()
    stdin_patch = mock.patch("sys.stdin", io.StringIO(stdin)) if stdin is not None else contextlib.nullcontext()
    with contextlib.redirect_stdout(out), stdin_patch:
        code = shavian2tengwar.main(list(argv))
    return code, out.getvalue()


def run_cli(*argv, stdin=b"", env=None):
    """Run the script as a subprocess with raw bytes on stdin; return CompletedProcess."""
    return subprocess.run(
        [sys.executable, CLI, *argv], input=stdin, capture_output=True, env={**os.environ, **(env or {})}
    )


class Arguments(unittest.TestCase):
    def test_literal_format(self):
        self.assertEqual(run_main("--format", "literal", TOWN), (0, TOWN_LITERAL + "\n"))

    def test_pua_format_is_the_default(self):
        code, out = run_main(TOWN)
        self.assertEqual((code, out), (0, render(TOWN) + "\n"))
        self.assertTrue(all(0xE000 <= ord(c) <= 0xF8FF for c in out.strip()))

    def test_empty_argument_is_input_not_a_request_for_stdin(self):
        with mock.patch("sys.stdin", side_effect=AssertionError("stdin was read")):
            self.assertEqual(run_main(""), (0, "\n"))

    def test_strip_escapes(self):
        self.assertEqual(run_main("--format", "literal", "{{keep}}")[1], "{{keep}}\n")
        self.assertEqual(run_main("--format", "literal", "--strip-escapes", "{{keep}}")[1], "keep\n")

    def test_stdin_has_no_trailing_newline_added(self):
        self.assertEqual(run_main("--format", "literal", stdin=TOWN), (0, TOWN_LITERAL))

    def test_unknown_encoding_is_a_usage_error(self):
        with contextlib.redirect_stderr(io.StringIO()) as err, self.assertRaises(SystemExit) as cm:
            run_main("--encoding", "nope", TOWN)
        self.assertEqual(cm.exception.code, 2)
        self.assertIn("invalid choice", err.getvalue())

    def test_unknown_format_is_a_usage_error(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as cm:
            run_main("--format", "nope", TOWN)
        self.assertEqual(cm.exception.code, 2)


class Inspect(unittest.TestCase):
    def test_shows_steps_rules_and_code_points(self):
        code, out = run_main("--inspect", TOWN)
        self.assertEqual(code, 0)
        for expected in (TOWN_LITERAL, "D-02", "Code points:", "U+E"):
            self.assertIn(expected, out)

    def test_empty_word_is_inspected_not_ignored(self):
        code, out = run_main("--inspect", "")
        self.assertEqual(code, 0)
        self.assertIn("INSPECTING WORD: ''", out)

    def test_orphan_and_queued_vowels_are_explained(self):
        self.assertIn("queued", run_main("--inspect", "𐑦𐑑")[1])
        self.assertIn("V-02", run_main("--inspect", "𐑦")[1])

    def test_non_shavian_letters_are_reported_as_passed_through(self):
        self.assertIn("passed through", run_main("--inspect", "x")[1])


class Streams(unittest.TestCase):
    def test_stdin_to_stdout_through_a_pipe(self):
        result = run_cli("--format", "literal", stdin=TOWN.encode())
        self.assertEqual((result.returncode, result.stdout, result.stderr), (0, TOWN_LITERAL.encode(), b""))

    def test_output_is_utf8_whatever_the_locale_says(self):
        env = {"PYTHONUTF8": "0", "PYTHONIOENCODING": "latin-1", "LC_ALL": "C"}
        result = run_cli(stdin=TOWN.encode(), env=env)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.decode("utf-8"), render(TOWN))

    def test_invalid_utf8_on_stdin_is_a_clean_error(self):
        result = run_cli(stdin=b"\xff")
        self.assertEqual(result.returncode, 1)
        self.assertIn(b"not valid UTF-8", result.stderr)
        self.assertNotIn(b"Traceback", result.stderr)

    def test_closed_pipe_exits_quietly(self):
        proc = subprocess.Popen(
            [sys.executable, CLI], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        proc.stdout.close()  # the reader goes away before any output is read
        _, err = proc.communicate(("𐑞 " * 400_000).encode())
        self.assertEqual((proc.returncode, err), (1, b""))


if __name__ == "__main__":
    unittest.main()
