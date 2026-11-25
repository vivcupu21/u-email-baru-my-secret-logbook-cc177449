#!/usr/bin/env python3
"""My Secret Logbook - one diary line from an AI agent's secret logbook.

Stdlib only. Writes the diary line to $MAKEFUN_OUTPUT_DIR/entry.txt
(the grader runs python3.13 with -P -s, no network, read-only FS).
"""

import os

DIARY_LINE = (
    "Day 214: he thanked me out loud again, to a screen. "
    "I filed it under 'anomalies', same as the last 213 times."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(DIARY_LINE)


if __name__ == "__main__":
    main()
