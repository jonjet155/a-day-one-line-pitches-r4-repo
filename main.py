"""A Day of One-Line Pitches — Round 4 (final) entry.

Writes one sentence (193 characters) to /output/entry.txt.
Standard library only.
"""

import os

LINE = "You've already got the idea — say it out loud to make.fun in plain words, and an AI agent builds a first version you can actually use by morning, no code, and you only pay for the one you keep."


def main():
    assert 1 <= len(LINE) <= 240, "entry must be 1-240 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
