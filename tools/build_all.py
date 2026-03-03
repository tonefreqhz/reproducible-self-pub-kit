from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> None:
    print("RUN:", " ".join(cmd))
    subprocess.check_call(cmd, cwd=cwd)


def main(argv: list[str]) -> int:
    root = Path(__file__).resolve().parents[1]

    run([sys.executable, "tools/build_book.py", "--all"], cwd=root)
    run([sys.executable, "tools/build_pamphlet.py", "--all"], cwd=root)

    print("OK: build_all finished.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
