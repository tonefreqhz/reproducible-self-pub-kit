#!/usr/bin/env python3
"""
Build Attestation — reproducible-self-pub-kit — M1, M2, M3, M7, M11
This is the CANONICAL toolkit repo. Source manifest covers the tools themselves.
"""

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OUTPUTS_DIR = os.path.join(REPO_ROOT, "outputs")
ATTESTATION_JSON = os.path.join(OUTPUTS_DIR, "BUILD_ATTESTATION.json")
SUMMARY_MD = os.path.join(OUTPUTS_DIR, "BUILD_SUMMARY.md")

# The Kit's "sources" are its tools and templates — the things other repos depend on
EXPECTED_SOURCES = [
    "tools/build_book.py",
    "tools/paths.py",
    "anchor.py",
    "anchor_verify.ps1",
    "session_start.ps1",
    "scripts/build.ps1",
    "scripts/build_cover.py",
    "scripts/write_docs.py",
    "publish/assemble_chapters.ps1",
    "publish/rebuild_publish.ps1",
    "publish/ingest_manuscript.ps1",
    "publication/manuscript.md",
    "publication/pamphlet_issue_1.md",
]

EXTRA_SOURCES = [
    "CLAUDE.md",
    "requirements.in",
    "BuildAndPublish.ps1",
]

EXPECTED_OUTPUTS = [
    "manuscripts/catalogue staging/epub/manuscript.epub",
    "manuscripts/catalogue staging/docx/manuscript.docx",
    "manuscripts/catalogue staging/pdf/manuscript.pdf",
    "manuscripts/catalogue staging/epub/doughforge-pamphlet-issue-1.epub",
]


def run_cmd(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=10,
                           cwd=REPO_ROOT)
        return r.stdout.strip()
    except Exception:
        return ""


def sha256_file(path):
    if not os.path.isfile(path):
        return None
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def get_tool_version(cmd):
    out = run_cmd(cmd)
    return out.split("\n")[0] if out else "not installed"


def get_git_info():
    commit = run_cmd(["git", "rev-parse", "HEAD"])
    status = run_cmd(["git", "status", "--porcelain"])
    return commit or "unknown", len(status) == 0


def build_source_manifest():
    manifest = {}
    for rel in EXPECTED_SOURCES + EXTRA_SOURCES:
        full = os.path.join(REPO_ROOT, rel)
        h = sha256_file(full)
        if h:
            manifest[rel] = h
    return manifest


def build_output_manifest():
    manifest = {}
    for rel in EXPECTED_OUTPUTS:
        full = os.path.join(REPO_ROOT, rel)
        h = sha256_file(full)
        if h:
            manifest[rel] = h
    return manifest


def check_manifest_consistency(source_manifest):
    missing = [r for r in EXPECTED_SOURCES if r not in source_manifest]
    return {"pass": len(missing) == 0, "missing": missing, "extra": []}


def check_dirty_outputs(source_manifest, output_manifest):
    unexplained = []
    if not output_manifest or not os.path.isfile(ATTESTATION_JSON):
        return {"pass": True, "unexplained_deltas": []}
    try:
        with open(ATTESTATION_JSON, "r", encoding="utf-8") as f:
            prev = json.load(f)
        prev_sources = prev.get("source_manifest", {})
        prev_outputs = prev.get("output_manifest", {})
        for rel, h in output_manifest.items():
            prev_h = prev_outputs.get(rel)
            if prev_h and prev_h != h:
                source_changed = any(
                    prev_sources.get(s) != source_manifest.get(s)
                    for s in source_manifest
                )
                if not source_changed:
                    unexplained.append(rel)
    except (json.JSONDecodeError, KeyError):
        pass
    return {"pass": len(unexplained) == 0, "unexplained_deltas": unexplained}


def write_summary(att):
    lines = [
        "# Build Attestation Summary — reproducible-self-pub-kit",
        "",
        f"**Timestamp:** {att['timestamp']}",
        f"**Commit:** `{att['commit_hash'][:12]}`",
        f"**Repo clean:** {'Yes' if att['repo_clean'] else 'No — uncommitted changes'}",
        "", "## Tool Versions", "",
    ]
    for tool, ver in att["tool_versions"].items():
        lines.append(f"- **{tool}:** {ver}")
    lines += ["", "## Source Manifest", "",
              "| File | SHA-256 (first 12) |", "|------|--------------------|"]
    for f, h in sorted(att["source_manifest"].items()):
        lines.append(f"| `{f}` | `{h[:12]}` |")
    lines += ["", "## Output Manifest", "",
              "| File | SHA-256 (first 12) |", "|------|--------------------|"]
    if att["output_manifest"]:
        for f, h in sorted(att["output_manifest"].items()):
            lines.append(f"| `{f}` | `{h[:12]}` |")
    else:
        lines.append("| *(no outputs built yet)* | — |")
    mc = att["manifest_consistency"]
    dd = att["dirty_output_detection"]
    lines += ["", "## Checks", "",
              f"- **M3 Manifest Consistency:** {'PASS' if mc['pass'] else 'FAIL'}"]
    if mc["missing"]:
        lines.append(f"  - Missing: {', '.join(mc['missing'])}")
    lines.append(f"- **M7 Dirty Output Detection:** {'PASS' if dd['pass'] else 'FAIL'}")
    if dd["unexplained_deltas"]:
        lines.append(f"  - Unexplained: {', '.join(dd['unexplained_deltas'])}")
    lines += ["", f"## Overall: {'PASS' if att['overall_pass'] else 'FAIL'}", ""]
    return "\n".join(lines)


def main():
    commit, clean = get_git_info()
    tool_versions = {
        "python": get_tool_version([sys.executable, "--version"]),
        "pandoc": get_tool_version(["pandoc", "--version"]),
        "lualatex": get_tool_version(["lualatex", "--version"]),
    }
    source_manifest = build_source_manifest()
    output_manifest = build_output_manifest()
    manifest_consistency = check_manifest_consistency(source_manifest)
    dirty_output = check_dirty_outputs(source_manifest, output_manifest)
    overall = manifest_consistency["pass"] and dirty_output["pass"]

    attestation = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "commit_hash": commit,
        "repo_clean": clean,
        "tool_versions": tool_versions,
        "source_manifest": source_manifest,
        "output_manifest": output_manifest,
        "manifest_consistency": manifest_consistency,
        "dirty_output_detection": dirty_output,
        "overall_pass": overall,
    }

    os.makedirs(OUTPUTS_DIR, exist_ok=True)
    with open(ATTESTATION_JSON, "w", encoding="utf-8") as f:
        json.dump(attestation, f, indent=2)
    print(f"[OK] BUILD_ATTESTATION.json written to {ATTESTATION_JSON}")
    summary = write_summary(attestation)
    with open(SUMMARY_MD, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"[OK] BUILD_SUMMARY.md written to {SUMMARY_MD}")
    print()
    print(summary)
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
