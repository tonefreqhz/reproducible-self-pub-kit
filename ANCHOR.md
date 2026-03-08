# W⚓ ANCHOR.md
# Canonical path registry for reproducible-self-pub-kit
# Last updated: 2026-03-08
# Protocol: W⚓ — do not rename or move files without updating this registry

## PURPOSE
This repo serves three functions:
1. The DoughForge instruction manual (this repo IS the book)
2. A full author catalogue pipeline (incoming → staging → published → D2D)
3. A live kit for reproducible self-publishing (forked as DoughForge)

---

## CANONICAL PATHS

### Active Manuscript (DoughForge instruction manual)
MANUSCRIPT_PRIMARY   = manuscript/doughforge-master.md        # 95KB — primary source
MANUSCRIPT_PAMPHLET  = manuscript/pamphlet_issue_1.md         # 93KB — pamphlet variant

### Build Outputs (active manuscript only)
OUTPUT_DOCX          = outputs/docx/
OUTPUT_EPUB          = outputs/epub/
OUTPUT_PDF           = outputs/pdf/
OUTPUT_PAMPHLET      = outputs/pamphlet/
OUTPUT_REVIEWER      = outputs/reviewer/
OUTPUT_WEB           = outputs/web/
OUTPUT_ARCHIVE       = outputs/_archive/

### Author Catalogue (full body of work)
CATALOGUE_INCOMING   = catalogue/incoming/      # drop zone — unprocessed
CATALOGUE_STAGING    = catalogue/staging/       # actively being processed
CATALOGUE_PUBLISHED  = catalogue/published/     # verified, D2D-ready
CATALOGUE_ARCHIVE    = catalogue/_archive/

### Catalogue — Published Titles
# biography-legislators-the-unacknowledged-legislators-of-the-world.epub
# ten-steps-to-affordable-housing-the-new-circuit-of-credit (3).epub
# the-circle-of-blame-anthology-of-blame (5).epub + .pdf
# the-clockwork-forest-the-conquest-of-ai (5).pdf
# the-conquest-of-dough (1).pdf
# the-new-commonwealth-of-oceana-a-modern-update-for-young-citizens.epub  [63MB — Git LFS]
# the-strawberry-conspiracy-the-plantsman-prequel-to-the-conquest-of-dough- (1).pdf
# the-strawberry-manifesto-...-STANDARD-PRINT-READY.pdf

### Projects (books in production)
PROJECT_HOMEIX       = projects/homeix/          # separate book — led to creation of this kit
HOMEIX_CHAPTERS      = projects/homeix/chapters/
HOMEIX_CHUNKS        = projects/homeix/chunks/

### Assets
ASSETS_COVER         = assets/cover/
ASSETS_PAMPHLET      = assets/pamphlet/
ASSETS_WEB           = assets/web/
ASSETS_FONTS         = assets/fonts/             # Noto_Sans + Sora (from DoughForge)

### Templates (LaTeX)
TEMPLATE_PREAMBLE    = templates/preamble.tex
TEMPLATE_COVER       = templates/cover.tex
TEMPLATE_COVER_PRE   = templates/cover_preamble.tex

### Scripts (PowerShell)
SCRIPTS              = scripts/
SCRIPT_BUILD         = scripts/build.ps1
SCRIPT_ASSEMBLE      = scripts/assemble_chapters.ps1
SCRIPT_INGEST        = scripts/ingest_manuscript.ps1
SCRIPT_REBUILD       = scripts/rebuild_publish.ps1
SCRIPT_SPLIT         = scripts/split_normalized_md.ps1
SCRIPT_DIAGNOSE      = scripts/diagnose_title_and_metadata.ps1
SCRIPT_RELEASE_NOTES = scripts/write_stage1_release_notes.ps1

### Tools (Python)
TOOLS                = tools/
TOOL_BUILD_BOOK      = tools/build_book.py
TOOL_BUILD_PAMPHLET  = tools/build_pamphlet.py
TOOL_BUILD_ALL       = tools/build_all.py
TOOL_COVER           = tools/add_text_to_cover.py
TOOL_PATHS           = tools/paths.py

### Admin
ADMIN_RETIRED        = _admin/_retired/          # working notes, generated reports

---

## RETIRED / SUPERSEDED PATHS
# The following folders are PENDING DELETION once verified:
# catalogue/chunked/          → contents moved to outputs/ and catalogue/published/
# catalogue/unchunked/        → duplicate of chunked, safe to delete
# manuscripts/                → duplicate of catalogue, safe to delete
# publication/                → contents moved to manuscript/
# inputs/                     → contents moved to projects/homeix/
# publish/                    → scripts moved to scripts/

---

## FORK RELATIONSHIP
# This repo:  https://github.com/tonefreqhz/reproducible-self-pub-kit
# Live fork:  https://github.com/tonefreqhz/DoughForge
# DoughForge is the live implementation of this kit.
# preamble.tex and fonts are sourced from DoughForge.

---

## W⚓ PROTOCOL
# Before any build: verify MANUSCRIPT_PRIMARY exists and is non-empty
# Before any commit: run tools/write_repo_state_report.ps1
# Before any delete: confirm target path is listed under RETIRED above
