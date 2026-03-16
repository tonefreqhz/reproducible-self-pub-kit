import os

# W-Anchor Protocol — reproducible-self-pub-kit
# Every path in the build derives from here. Never hardcode elsewhere.

REPO_ROOT   = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR  = os.path.join(REPO_ROOT, "assets")
COVER_DIR   = os.path.join(ASSETS_DIR, "cover")
COVERS_DIR  = os.path.join(REPO_ROOT, "covers")
DOCS_DIR    = os.path.join(REPO_ROOT, "docs")
FONTS_DIR   = os.path.join(ASSETS_DIR, "fonts")
SCRIPTS_DIR = os.path.join(REPO_ROOT, "scripts")
WIDGETS_DIR = os.path.join(REPO_ROOT, "widgets")
README      = os.path.join(REPO_ROOT, "README.md")
ANCHOR_MD   = os.path.join(REPO_ROOT, "ANCHOR.md")

if __name__ == "__main__":
    paths = {
        "Repo Root"  : REPO_ROOT,
        "Assets Dir" : ASSETS_DIR,
        "Cover Dir"  : COVER_DIR,
        "Covers Out" : COVERS_DIR,
        "Docs Dir"   : DOCS_DIR,
        "Fonts Dir"  : FONTS_DIR,
        "Scripts Dir": SCRIPTS_DIR,
        "Widgets Dir": WIDGETS_DIR,
        "README"     : README,
        "ANCHOR.md"  : ANCHOR_MD,
    }
    print("\n=== W-Anchor Protocol — reproducible-self-pub-kit ===\n")
    all_ok = True
    for name, path in paths.items():
        status = "OK     " if os.path.exists(path) else "MISSING"
        if not os.path.exists(path):
            all_ok = False
        print(f"  [{status}] {name}: {path}")
    print()
    if all_ok:
        print("  All paths verified. You are anchored.\n")
    else:
        print("  One or more paths missing. Fix before building.\n")
