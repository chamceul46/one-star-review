#!/usr/bin/env python3
"""Entry for the make.fun bounty "One-Star Review of Something
Essential" (u-0xb3e689-one-star-review-of-something-essential-c7234629).

The brief asks for one single-line one-star review, at most 160
characters, of an everyday essential, deadpan throughout: the sharpest
true grievance in the thing — the small daily annoyance everyone
recognises but has never seen written down — no winking, no explaining
the joke, and the turn in the last few words, with one joke told
cleanly and no second joke crowding it. So the review is of the sun,
whose one unforgivable habit is rising straight into your eyes on the
single morning you could have slept in.

The program writes that line to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR locally, /output in the grader).
"""

import os

LINE = (
    "The sun. Has risen every day of my life without fail, and still "
    "chooses to do it directly into my eyes on the one morning I "
    "could sleep in."
)


def validate(line: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 160 characters,
    and not only white space. Refuse to hand in anything else."""
    encoded = line.encode("utf-8")  # raises if it cannot be encoded
    if not line.strip():
        raise ValueError("entry is only white space")
    if not 1 <= len(line) <= 160:
        raise ValueError(f"entry is {len(line)} characters, outside 1..160")
    if len(encoded) > 160:
        raise ValueError("entry encodes to more than 160 bytes")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
  
