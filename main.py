#!/usr/bin/env python3
"""The Agent's Uh-Oh -- entry program.

Writes one word -- the word an agent blurts out when it has no idea
what to do -- to /output/entry.txt for the judge to read. Standard
library only, no network, no input files, deterministic output: the
same word, the same bytes, every run.
"""

import os

WORD = "hallucinating"

OUTPUT_PATH = "/output/entry.txt"


def _validate(entry: str) -> None:
    """Fail loudly if the entry ever stops meeting the gate.

    The gate requires UTF-8 text of 1 to 99 characters, not only
    whitespace, and the brief requires exactly one word.
    """
    if not 1 <= len(entry) <= 99:
        raise ValueError(f"entry must be 1-99 characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if len(entry.split()) != 1:
        raise ValueError("entry must be exactly one word")


def main() -> int:
    _validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read the file back and refuse to pass on any mismatch, so a
    # bad write can never silently reach the judge.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise ValueError("entry.txt does not match the entry word")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
