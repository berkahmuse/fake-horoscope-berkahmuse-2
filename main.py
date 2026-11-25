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


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
