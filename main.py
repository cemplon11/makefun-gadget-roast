#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (<=200 chars) to /output/entry.txt.
Pure Python stdlib, deterministic, no network.
"""

import os

LINE = (
    "My smartwatch throws a party every time I stand up, like fetching "
    "crisps from the kitchen were a summit of Everest."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE and "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
