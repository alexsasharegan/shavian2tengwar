"""Tests. They need Python 3.14, so say so once instead of failing in every module."""

import sys

if sys.version_info < (3, 14):  # noqa: UP036 - deliberate: a clear message instead of a SyntaxError later
    sys.exit(f"The tests need Python 3.14 or newer; this is {sys.version.split()[0]} ({sys.executable}).")
