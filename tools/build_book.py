from __future__ import annotations

import argparse
import sys
from pathlib import Path

from paths import project_paths


def must_exist(p: Path, kind: str = "path") -> None:
    if not p.exists():
        raise FileNotFoundError(f"Expected {kind} to exist: {p}")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Reproducible Self-Pub Kit builder")
    ap.add_argument(
        "--project-root",
        type=Path,
        default=None,
        help="Override PROJECT_ROOT (defaults to auto-detected repo root).",
    )
    args = ap.parse_args(argv)

    pp = project_paths(args.project_root)

    # One tidy, scan-friendly block of output.
    lines = [
        "Build config",
        f"PROJECT_ROOT = {pp.root}",
        f"inputs_canonical = {pp.inputs_canonical}",
        f"manuscript_md = {pp.manuscript_md}",
        f"manuscript_docx = {pp.manuscript_docx}",
        f"assets = {pp.assets}",
        f"outputs = {pp.outputs}",
        f"publication = {pp.publication}",
    ]
    print("\n".join(lines))

    # Fail fast: require the skeleton to exist
    must_exist(pp.inputs, "directory")
    must_exist(pp.outputs, "directory")
    must_exist(pp.publication, "directory")

    # (Real build steps come next.)
    print("OK: path sanity checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
