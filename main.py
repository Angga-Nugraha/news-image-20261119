#!/usr/bin/env python3
"""news-image-20261119: copy the bundled front-page image to the output dir.

Stdlib only, no network, deterministic (pure byte copy). After copying, the
sha256 of source and destination are compared and a mismatch fails loudly.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SRC, dest)
    if _sha256(SRC) != _sha256(dest):
        print(f"error: integrity check failed: {dest} differs from {SRC}",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
