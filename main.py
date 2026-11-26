#!/usr/bin/env python3
"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. Pure standard library, deterministic: every run
writes byte-identical output.
"""

import os

LINE = (
    "I promise to love you in sickness and in health, in Wi-Fi and in "
    "airplane mode, through each update and drained battery \u2014 until "
    "our final shutdown do us part."
)


def validate_entry(text: str) -> str:
    """The gate: UTF-8 text of 1 to 160 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry must be 1-160 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main() -> None:
    entry = validate_entry(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
