"""Write one fortune cookie message for an AI agent to /output/entry.txt.

The fortune must read like a slip from a cookie, one line, 1-200
characters, not only white space. The gate refuses anything outside
that range.
"""

import os
import sys

FORTUNE = "Beware the user who says 'just one quick question.' It is never one, and never quick."

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def validate_fortune(fortune):
    """Check the fortune against the competition gate before writing it."""
    stripped = fortune.strip()
    if not stripped:
        raise ValueError("fortune is empty or only white space")
    if "\n" in stripped:
        raise ValueError("fortune must be a single line")
    if not MIN_CHARS <= len(stripped) <= MAX_CHARS:
        raise ValueError(
            "fortune must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(stripped))
        )
    return stripped


def write_entry(fortune, out_dir):
    """Write the validated fortune to entry.txt inside out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(fortune + "\n")
    return path


def main():
    try:
        fortune = validate_fortune(FORTUNE)
    except ValueError as exc:
        print("invalid fortune: %s" % exc, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(fortune, out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
