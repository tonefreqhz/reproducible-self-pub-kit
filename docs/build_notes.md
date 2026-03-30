# DoughForge — Cover Build Notes

## What We Built

A Python cover compositor that:
- Loads a base AI-generated cover image (assets/cover/base_cover.png)
- Overlays VT323 monospace title, subtitle, and author text with green glow
- Composites an approval stamp (assets/cover/stamp_clean.png) centred below subtitle
- Purges and rebuilds the covers/ folder on every run
- Outputs front_cover.png, front_cover.jpg, front_cover.gif
- Mirrors final_cover.png and final_cover.jpg back to assets/cover/

## Canvas Spec

| Property     | Value                                       |
|--------------|---------------------------------------------|
| Dimensions   | 1024 x 1792 px                              |
| Colour space | RGBA during compositing, RGB for final JPG  |
| Print target | Draft2Digital (JPG, 96 DPI minimum)         |
| Font         | VT323-Regular.ttf @ 120pt / 60pt / 52pt     |

## File Locations

| File                           | Purpose                            |
|--------------------------------|------------------------------------|
| assets/cover/base_cover.png    | AI-generated background            |
| assets/cover/stamp_clean.png   | Transparent PNG approval stamp     |
| assets/fonts/VT323-Regular.ttf | Display font                       |
| scripts/build_cover.py         | Cover compositor script            |
| covers/front_cover.png         | Final PNG for web / GitHub         |
| covers/front_cover.jpg         | Final JPG for Draft2Digital upload |
| covers/front_cover.gif         | Final GIF for social / preview     |

## How to Run

    cd C:\Users\peewe\DoughForge
    python scripts\build_cover.py

## Key Design Decisions

- Purge before write: shutil.rmtree(covers/) prevents stale files reaching publisher
- Sized by height: stamp resized as 16% of H regardless of source PNG aspect ratio
- Percentage-based layout: all Y positions are fractions of H, resolution-independent
- Glow layer: Gaussian blur at 50% opacity gives terminal/CRT aesthetic

## Dependencies

    pip install Pillow numpy

## Adapting for Other Projects

Change only the config block at the top of build_cover.py:

    BASE_DIR = r'C:\Users\peewe\YourProject'
    TITLE    = 'Your Title'
    SUBTITLE = 'Your Subtitle'
    AUTHOR   = 'Your Name'

Eventually this config block will be replaced by a book.yaml reader.

---

## session_start.ps1 Audit — 30 March 2026

### Status: NOT READY TO SHIP

The session_start.ps1 coordinator exists in all five repos but is **not consistent
or fully deployed**. This repo (reproducible-self-pub-kit) is the KIT — what ships
to users. The session_start here must be the CLEAN, TESTED, SIMPLE version.

#### Issues Found Across the Five Repos

1. **homeix has the newest version** (224 lines) with auto-restore and deletion
   guard. This repo and three others run the older 189-line version WITHOUT
   these safety features.

2. **wandering-anchor-book anchor_verify.ps1 was pointing to THIS repo**
   instead of its own. Fixed 30 March.

3. **This repo uses hardcoded absolute path** in anchor_verify.ps1 instead
   of $PSScriptRoot. Works on Roger's machine, won't work for Kit users.

4. **No PoshClaude.md / W-Anchor CLAUDE.md call** in session_start.ps1.
   Brand compliance not invoked at session start.

5. **The W-Anchor CLAUDE.md** had path error: `tools/anchor_verify.ps1`
   should be `anchor_verify.ps1` (root, not tools/). Fixed 30 March.

#### What the Kit Needs Before Ship

- [ ] anchor_verify.ps1 must use $PSScriptRoot (portable for any user)
- [ ] session_start.ps1 must include CLAUDE.md read step
- [ ] Deletion guard from homeix version must be propagated
- [ ] Build notes must be repo-specific (currently all five are DoughForge cover notes)
- [ ] Test: clone Kit to fresh machine, run session_start, verify all paths
- [ ] Document: simple case (1 book, 1 repo) as default, power layers as optional

#### Forensic Evidence

See DoughForge/docs/build_notes.md for full hash table of all build failures
and fixes from 8–30 March 2026 beta production.

#### You Gotta Go There to Come Back

The Kit ships the clean version. The mess is in the git history. The mess is
the proof that the clean version works.
