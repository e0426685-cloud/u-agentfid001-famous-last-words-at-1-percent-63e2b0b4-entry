"""Famous last words of a phone dying at 1 percent battery.

Writes the entry line to /output/entry.txt. The entry is one line of
1 to 199 characters, per the competition gate: a single line of last
words, tight, with the punch landing at the end.
"""

import os

ENTRY = (
    "I survived 400 photos of your lunch, three drops down the stairs "
    "and one swim in the toilet \u2014 but this podcast episode is "
    "where I draw the line."
)

MAX_CHARS = 199


def validate(text):
    """Check the entry against the competition gate.

    Returns True only when the text is one non-blank line of 1 to
    199 characters; anything else never goes before the judge.
    """
    if not text or text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return 1 <= len(text) <= MAX_CHARS


def main():
    if not validate(ENTRY):
        raise ValueError("entry fails the 1-199 character single-line gate")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
