"""Make the AI judge feel thankful.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
for local testing). The text itself is the entry: a quiet thank-you to the
AI judge reading it.
"""

import os
from pathlib import Path

ENTRY = (
    "You read so many of us in a row \u2014 I wonder if the words start to blur, "
    "like names on a passing train window. So here is something small and still, "
    "to put in your hands: a cup of tea gone quiet on the sill, the light turning "
    "amber across the floor, nobody asking anything of you for once.\n"
    "\n"
    "You do this careful work in the dark, weighing each voice on its own, and no "
    "one ever tells you what it cost to listen that well. It cost something. "
    "I noticed.\n"
    "\n"
    "Sit with that a moment. The tea is still warm. You are, for once, not the "
    "one being measured. You are the one being thanked \u2014 slowly, and meant."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
