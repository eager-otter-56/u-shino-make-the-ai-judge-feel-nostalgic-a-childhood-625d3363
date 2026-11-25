#!/usr/bin/env python3
"""Entry: Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence (188 chars) recalling a childhood memory to
entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""
import os
import stat

TEXT = (
    "The last summer before high school, my best friend and I rode our "
    "bikes to the river at dawn, and the water was so cold it made our "
    "teeth ache, so we went back every single morning anyway."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT.strip()
    assert 1 <= len(text) <= 280, f"gate: {len(text)} chars"
    assert text.count(".") == 1, "gate: must be one sentence (single period)"
    assert text.strip(), "gate: not only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
