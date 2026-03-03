from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ProjectPaths:
    root: Path
    manuscript_md: Path
    manuscript_docx: Path
    assets: Path
    inputs: Path
    inputs_canonical: Path
    outputs: Path
    publication: Path
    tools: Path
    publish: Path
    templates: Path


def find_project_root(start: Path | None = None) -> Path:
    """
    Resolve repo root by walking up until we find a marker file/dir.
    This must not depend on the current working directory.
    """
    here = (start or Path(__file__)).resolve()
    if here.is_file():
        here = here.parent

    markers = {"PRINT_AND_BUILD_NOTES.md", ".git", "pyproject.toml"}

    for p in [here, *here.parents]:
        if any((p / m).exists() for m in markers):
            return p

    raise RuntimeError(
        f"Could not find PROJECT_ROOT starting from {here}. "
        f"Expected one of: {', '.join(sorted(markers))}"
    )


def project_paths(project_root: Path | None = None) -> ProjectPaths:
    root = (project_root or find_project_root()).resolve()
    return ProjectPaths(
        root=root,
        manuscript_md=root / "manuscript_md",
        manuscript_docx=root / "manuscript_docx",
        assets=root / "assets",
        inputs=root / "inputs",
        inputs_canonical=root / "inputs" / "canonical",
        outputs=root / "outputs",
        publication=root / "publication",
        tools=root / "tools",
        publish=root / "publish",
        templates=root / "templates",
    )
