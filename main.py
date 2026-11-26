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
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8
    return text


MAX_CHARS = 160


def resolve_out_dir() -> str:
    """Where entry.txt lands: /output on the grader, overridable locally."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def verify_written(path: str, entry: str) -> None:
    """Read-back self-check: what landed on disk must be byte-identical."""
    with open(path, encoding="utf-8", newline="") as f:
        if f.read() != entry:
            raise RuntimeError("entry.txt differs from the validated line")


def main() -> None:
    entry = validate_entry(LINE)
    out_dir = resolve_out_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)
    verify_written(path, entry)


if __name__ == "__main__":
    main()
