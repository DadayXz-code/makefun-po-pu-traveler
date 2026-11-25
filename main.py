"""Write one sentence explaining the modern internet to a traveler from 1800.

The sentence uses only things a person from 1800 already knows -- a road,
a post office, a library, a letter, a book, a song -- and no word coined
after their time. It is written to <output dir>/entry.txt with no trailing
newline, so the file holds exactly the sentence and nothing else.
"""

import os
import sys

SENTENCE = (
    "Picture a single road joining every post office and library on earth, "
    "so any letter, book, or song reaches anyone in a blink, "
    "and anyone may answer back."
)


def validate(sentence: str) -> None:
    """Check the sentence meets the brief: one sentence, 1 to 200 chars."""
    text = sentence.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(SENTENCE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir and len(sys.argv) > 1:
        output_dir = sys.argv[1]
    if not output_dir:
        output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
