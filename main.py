#!/usr/bin/env python3
"""The Internet in One Word: Tabnado.

A tabnado is a tornado made of browser tabs: it starts with one quick
lookup, spins up forty-seven open tabs, and by the time you look away it
has carried off your afternoon, your battery, and any memory of what you
came here to do. That is the whole internet in seven letters.

The program writes exactly that one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), with no trailing newline, then reads the file back and
refuses to exit cleanly unless what it reads is byte for byte the word it
meant to write. No network, no clock, no randomness, no input: the same
word every run.
"""

import os
import sys

WORD = "Tabnado"


def _check(word):
    """Mirror the competition gate: 1-30 chars, one word, not blank."""
    if not 1 <= len(word) <= 30:
        return "word must be 1-30 characters, got %d" % len(word)
    if not word.strip():
        return "word must not be only whitespace"
    if any(ch.isspace() for ch in word):
        return "word must be a single word with no whitespace"
    return None


def main():
    problem = _check(WORD)
    if problem:
        print("gate failed: %s" % problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != WORD.encode("utf-8"):
        print("self-check failed: entry.txt does not match the word",
              file=sys.stderr)
        return 1
    print(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
