import os

# Anchor: Define repo root and key paths (harmonize from here)
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(REPO_ROOT, "assets")
COVER_DIR = os.path.join(ASSETS_DIR, "cover")
BASE_COVER = os.path.join(COVER_DIR, "base_cover.png")
FINAL_COVER = os.path.join(COVER_DIR, "front_cover.jpg")

# Print for verification (optional, remove in production)
print(f"Repo Root: {REPO_ROOT}")
print(f"Base Cover Path: {BASE_COVER}")
print(f"Final Cover Path: {FINAL_COVER}")

# You can import this in scripts: from anchor import REPO_ROOT, etc.
