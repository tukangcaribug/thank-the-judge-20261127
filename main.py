#!/usr/bin/env python3
"""Write one thank-you text to /output/entry.txt.

Stdlib only, no network, deterministic: the same text every run.
"""

import os
import tempfile


def write_atomic(path, text):
    """Write text atomically: complete temp file, fsync, rename.

    Readers of `path` only ever see the old or the new content,
    never a half-written file.
    """
    directory = os.path.dirname(path)
    fd, tmp_path = tempfile.mkstemp(dir=directory, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except FileNotFoundError:
            pass
        raise
    os.chmod(path, 0o644)
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
    write_atomic("/output/entry.txt", TEXT)


if __name__ == "__main__":
    main()
