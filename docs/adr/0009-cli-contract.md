# ADR-0009: CLI Contract

**Status:** Active
**Date:** 2026-10-11
**Affected:** shavian2tengwar.py, tests/test_cli.py
**Origin:** DECISIONS.md D-18
**Review:** Approved by merging PR #1
**Revert:** `e8ca735`

## Context

The output is Private Use Area code points. Under a non-UTF-8 locale Python substituted or garbled
them without any error. A bad `--encoding` crashed with a traceback, and `| head` printed a
`BrokenPipeError`.

## Decision

- stdin and stdout are forced to UTF-8, whatever the locale.
- `--encoding` is validated by argparse (exit 2).
- Input that is not valid UTF-8 prints a one-line error and exits 1.
- A closed pipe exits 1 quietly, with stdout pointed at `/dev/null` so the interpreter's own flush
  does not raise again.
- An empty-string argument is the text to convert, not "read stdin".
- `main(argv)` takes its arguments and returns the exit code, so tests call it directly.

## Consequences

- `tests/test_cli.py` pins each of these behaviours.
