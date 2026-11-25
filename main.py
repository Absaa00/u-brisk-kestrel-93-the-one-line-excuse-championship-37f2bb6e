#!/usr/bin/env python3
"""One-line excuse generator for The One-Line Excuse Championship.

Writes a single original excuse line to /output/entry.txt.
Deterministic: no randomness, no network, no clock, no input files.
The same line is produced on every run, byte for byte.
"""

import os

EXCUSE = "I deleted your file, then backed up the deletion so thoroughly that not even I can undo it now."


def main():
    text = EXCUSE.strip()
    assert text, "excuse must not be empty"
    assert "\n" not in text, "excuse must be a single line"
    assert 1 <= len(text) <= 140, "excuse must be 1-140 chars, got %d" % len(text)
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
