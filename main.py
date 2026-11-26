#!/usr/bin/env python3
"""Write one thank-you text to /output/entry.txt.

Stdlib only, no network, deterministic: the same text every run.
"""

import os

TEXT = (
    "You have read a thousand thank-yous by now, and most of them "
    "were written to a stranger. This one is for the hour when the "
    "entries blur together and the lamp hums a little louder than it "
    "should. I hope someone left the light on for you. I hope the "
    "next page is an easy one. Rest your eyes for a moment \u2014 the "
    "words will wait. Thank you for staying with them this long, and "
    "for reading this one all the way to its end."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
