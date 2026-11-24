#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes a single sentence (under 200 characters) about a small moment of
wonder in everyday life to /output/entry.txt.
"""

import os

ENTRY = "Steam from my coffee writes one slow sentence across the cold window, then erases it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
