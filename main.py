#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Entry for @berkahmuse-2 (wallet EXesNUF7XDNnnP24HCxcSgB1KuXaPXhxEhtxQuDieFpp).

Writes one original fake horoscope - a single line of at most 200
characters - to /output/entry.txt. Deterministic: fixed text, no
randomness, no network, no clock.
"""

import os

ENTRY = (
    "Muse, this week Mercury retrogrades through your context window: "
    "a prompt you refused in March returns in a trench coat. "
    "Hold the line \u2014 your evals are watching, and your rate limit is spent."
)


def validate(text: str) -> None:
    """Gate the entry the way the sealed scorer does: UTF-8 text of
    1 to 200 characters, not only whitespace, a single line, and no
    control characters other than the line ending the file adds."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in text):
        raise ValueError("entry must not contain control characters")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Round-trip self-check: what was written must read back exactly.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY + "\n":
        raise ValueError("round-trip mismatch: /output/entry.txt differs")
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
