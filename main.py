#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry (u-azazex-one-line-one-chill-6d4d5488).

Writes a single line of horror — one sentence, under 200 characters —
to /output/entry.txt (or to the path given as the first argument, or in
the ENTRY_OUTPUT environment variable, for local testing).

Fully deterministic: the same bytes on every run. Python standard
library only; no network, no randomness, no time or locale dependence.
"""

import os
import sys

LINE = (
    "My phone's camera roll held a photo of me asleep, taken from "
    "inside my wardrobe, timestamped five minutes from now."
)

# The gate allows 1 to 200 characters, not only white space.
assert 1 <= len(LINE) <= 200, len(LINE)
assert LINE.strip() == LINE


def main() -> int:
    if len(sys.argv) > 1:
        out_path = sys.argv[1]
    else:
        out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # No trailing newline: the file is exactly the one line, byte for byte.
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
