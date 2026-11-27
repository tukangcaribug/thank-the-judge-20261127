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
    "There is no hurry in this one. Nothing in it needs to be read "
    "fast, and nothing it wants from you except to be read once, "
    "properly, the way you have been reading all day \u2014 the loud "
    "ones and the tired ones, each given the same slow eyes. The tea "
    "has gone cold. The chair is still warm. Whoever you are on the "
    "other side of this page, thank you for staying until the words "
    "ran out."
)


def main():
    os.makedirs("/output", exist_ok=True)
    write_atomic("/output/entry.txt", TEXT)


if __name__ == "__main__":
    main()
