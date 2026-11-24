#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (1-240 characters) to /output/entry.txt.
Deterministic, no network, no randomness: the same line every run.
"""

from pathlib import Path

ENTRY = (
    "After a year of falling off in the driveway, seventy-two-year-old "
    "Rosa rode her bicycle past the corner store without once putting "
    "a foot down."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 240:
        raise ValueError(f"entry is {len(text)} characters, must be 1-240")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    # Self-check: the file on disk must be byte-identical to the line.
    if OUTPUT_PATH.read_text(encoding="utf-8") != text:
        raise RuntimeError("output mismatch after write")


if __name__ == "__main__":
    main()
