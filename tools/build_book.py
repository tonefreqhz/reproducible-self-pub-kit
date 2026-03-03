from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from paths import project_paths


@dataclass(frozen=True)
class Targets:
    pdf: bool
    epub: bool
    docx: bool


def must_exist_dir(p: Path, label: str) -> None:
    if not p.exists() or not p.is_dir():
        raise FileNotFoundError(f"Expected {label} directory to exist: {p}")


def must_exist_file(p: Path, label: str) -> None:
    if not p.exists() or not p.is_file():
        raise FileNotFoundError(f"Expected {label} file to exist: {p}")


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def run(cmd: list[str], cwd: Path) -> None:
    print("RUN:", " ".join(cmd))
    subprocess.check_call(cmd, cwd=cwd)


def parse_args(argv: list[str]) -> tuple[Path | None, Targets]:
    ap = argparse.ArgumentParser(description="Reproducible Self-Pub Kit builder (sequential)")
    ap.add_argument(
        "--project-root",
        type=Path,
        default=None,
        help="Override PROJECT_ROOT (defaults to auto-detected repo root).",
    )

    ap.add_argument("--all", action="store_true", help="Build PDF + EPUB + DOCX (sequential).")
    ap.add_argument("--pdf", action="store_true", help="Build PDF.")
    ap.add_argument("--epub", action="store_true", help="Build EPUB.")
    ap.add_argument("--docx", action="store_true", help="Build DOCX.")

    args = ap.parse_args(argv)

    any_flag = args.all or args.pdf or args.epub or args.docx
    if not any_flag or args.all:
        targets = Targets(pdf=True, epub=True, docx=True)
    else:
        targets = Targets(pdf=args.pdf, epub=args.epub, docx=args.docx)

    return args.project_root, targets


def print_config(pp) -> None:
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


def validate_skeleton(pp) -> None:
    must_exist_dir(pp.inputs, "inputs")
    must_exist_dir(pp.outputs, "outputs")
    must_exist_dir(pp.publication, "publication")
    print("OK: path sanity checks passed.")


def manuscript_source(pp) -> Path:
    # Change this if your main markdown file has a different name/location.
    return pp.publication / "manuscript.md"


def build_pdf(pp) -> None:
    out_dir = pp.outputs / "pdf"
    ensure_dir(out_dir)

    src = manuscript_source(pp)
    must_exist_file(src, "manuscript markdown")

    out = out_dir / "book.pdf"
    run(
        [
            "pandoc",
            str(src),
            "-o",
            str(out),
            "--pdf-engine=xelatex",
        ],
        cwd=pp.root,
    )
    print(f"Built PDF: {out}")


def build_epub(pp) -> None:
    out_dir = pp.outputs / "epub"
    ensure_dir(out_dir)

    src = manuscript_source(pp)
    must_exist_file(src, "manuscript markdown")

    out = out_dir / "book.epub"
    run(
        [
            "pandoc",
            str(src),
            "-o",
            str(out),
        ],
        cwd=pp.root,
    )
    print(f"Built EPUB: {out}")


def build_docx(pp) -> None:
    out_dir = pp.outputs / "docx"
    ensure_dir(out_dir)

    src = manuscript_source(pp)
    must_exist_file(src, "manuscript markdown")

    out = out_dir / "book.docx"
    run(
        [
            "pandoc",
            str(src),
            "-o",
            str(out),
        ],
        cwd=pp.root,
    )
    print(f"Built DOCX: {out}")


def main(argv: list[str]) -> int:
    project_root, targets = parse_args(argv)
    pp = project_paths(project_root)

    print_config(pp)
    validate_skeleton(pp)

    if targets.pdf:
        build_pdf(pp)
    if targets.epub:
        build_epub(pp)
    if targets.docx:
        build_docx(pp)

    print("OK: build finished (sequential).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
