#!/usr/bin/env python3
"""Check that a document summary is not too long.

The document-summarizer skill produces a summary of at most 10 lines,
preceded by one title line (so at most 11 non-empty lines in total). This
script counts the non-empty lines of a text file and exits with an error if
the limit is exceeded.

Usage:
    python3 check_length.py SUMMARY_FILE

Exit codes:
    0  the summary is within the limit
    1  the file does not exist, is a directory, or could not be read
    2  wrong usage (no file argument given)
    3  the summary is too long
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

MAX_SUMMARY_LINES = 10
TITLE_LINE_ALLOWANCE = 1
MAX_TOTAL_LINES = MAX_SUMMARY_LINES + TITLE_LINE_ALLOWANCE

USAGE = "usage: python3 check_length.py SUMMARY_FILE"


def count_non_empty_lines(text: str) -> int:
    """Return the number of lines that hold at least one non-space character."""
    return sum(1 for line in text.splitlines() if line.strip())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="check_length.py",
        description=(
            "Count the non-empty lines of a summary file and fail if there "
            f"are more than {MAX_SUMMARY_LINES} summary lines."
        ),
        epilog=(
            f"A summary may have at most {MAX_SUMMARY_LINES} lines plus one "
            f"title line, so at most {MAX_TOTAL_LINES} non-empty lines."
        ),
    )
    parser.add_argument(
        "summary_file",
        nargs="?",
        help="path to the summary text file to check",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.summary_file:
        parser.print_help()
        print()
        print(USAGE)
        print("error: no summary file provided", file=sys.stderr)
        return 2

    path = Path(args.summary_file)
    if not path.exists():
        print(f"error: file not found: {path}", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        return 1
    if path.is_dir():
        print(f"error: not a file: {path}", file=sys.stderr)
        return 1

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(
            f"error: {path} is not valid UTF-8 text and cannot be checked",
            file=sys.stderr,
        )
        return 1
    except OSError as exc:
        print(f"error: could not read {path}: {exc}", file=sys.stderr)
        return 1

    count = count_non_empty_lines(text)
    print(f"{path}: {count} non-empty line(s)")

    if count > MAX_TOTAL_LINES:
        over = count - MAX_TOTAL_LINES
        print(
            f"error: summary is too long by {over} line(s). "
            f"The limit is {MAX_SUMMARY_LINES} summary lines plus one title "
            f"line ({MAX_TOTAL_LINES} non-empty lines in total).",
            file=sys.stderr,
        )
        return 3

    if count > MAX_SUMMARY_LINES:
        print(
            "note: within the limit. The first line is treated as the title "
            "line."
        )
    print("ok: within the length limit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
