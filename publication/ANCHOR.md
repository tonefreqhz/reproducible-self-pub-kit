\# Reproducible Self‑Pub Kit — Anchor (Ground Truth)



Last updated: 2026-03-03  

Owner machine: Windows (PowerShell)  

Repo: https://github.com/tonefreqhz/reproducible-self-pub-kit  

Branch: main



---



\## 1) Current state (what exists)

\- Repo root: `C:\\Users\\peewe\\OneDrive\\Desktop\\reproducible-self-pub-kit`

\- `tools/build\_book.py` exists and is committed/pushed.

\- Orchestrator:

&nbsp; - Sequential targets: PDF → EPUB → DOCX

&nbsp; - Flags: `--all`, `--pdf`, `--epub`, `--docx`

&nbsp; - No flags defaults to `--all`



---



\## 2) Commands that WORK on this machine

\- Use Python via launcher (\*\*python command not on PATH\*\*):

&nbsp; - `py --version` → Python 3.13.12 confirmed

&nbsp; - `py tools\\build\_book.py --all`



\- LaTeX engine present:

&nbsp; - `xelatex --version` works (TeX Live 2025)



---



\## 3) Git status (what was pushed)

\- Commit: `d43f679` on `main`

\- Message: "Add sequential multi-target build orchestration (pdf/epub/docx)"



---



\## 4) Pending installs / missing tools

\- Pandoc:

&nbsp; - once pandoc --version works, and under “Manuscript source” keep:

&nbsp; - Installed via: `winget install --id JohnMacFarlane.Pandoc -e`

&nbsp; - After install: reopen PowerShell, then run:

&nbsp;   - `pandoc --version`

&nbsp;   - `where.exe pandoc`



---



\## 5) Next build goal

Generate (from Markdown):

\- `outputs/pdf/book.pdf`

\- `outputs/epub/book.epub`

\- `outputs/docx/book.docx`



Toolchain target:

\- Pandoc for EPUB + DOCX

\- Pandoc + `--pdf-engine=xelatex` for PDF



---



\## 6) Manuscript source (update this)

Canonical source: Markdown  

Expected main file (change if different):

\- `publication\\manuscript.md`



Check:

\- `Test-Path .\\publication\\manuscript.md`



---



\## 7) Guardrails

\- Prefer `py` over `python` in all commands.

\- Keep builds deterministic + sequential.

\- Update this anchor whenever toolchain/paths change.

# Interim Progress Log — Reproducible Self‑Pub Kit (Long Form)

**Last updated:** 2026-03-03  
**Owner machine:** Windows (PowerShell)  
**Repo:** https://github.com/tonefreqhz/reproducible-self-pub-kit  
**Repo root:** `C:\Users\peewe\OneDrive\Desktop\reproducible-self-pub-kit`

---

## 1) Purpose (why this exists)
This is a running “lab notebook” that records what worked, why it worked, and where drift risk showed up.
It’s intentionally long-form so a future final write-up can explain *how* the ANCHOR prevented drift and what trade-offs appeared on a real Windows + OneDrive machine.

---

## 2) Toolchain & Environment (verified)

### Python
- Verified: `py --version` → Python 3.13.12  
- Location: `where.exe py` → `C:\Users\peewe\AppData\Local\Programs\Python\Launcher\py.exe`
- Guardrail: use `py` (python not on PATH on this machine)

### LaTeX (PDF engine)
- Verified: `xelatex --version` works (TeX Live 2025)
- Note: `where.exe xelatex` shows **two** installs:
  - `C:\texlive\2025\bin\windows\xelatex.exe`
  - `C:\Users\peewe\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe`
- Risk: PATH ambiguity possible, but current builds succeed.

### Pandoc
- Verified: `pandoc --version` → pandoc 3.9
- Location: `where.exe pandoc` → `C:\Users\peewe\AppData\Local\Pandoc\pandoc.exe`

---

## 3) Repo state (ground truth at time of validation)

### Remote
- `origin` → `https://github.com/tonefreqhz/reproducible-self-pub-kit.git`

### Branch / commit (main)
- `git status -sb` → `## main...origin/main`
- `git branch -vv` → `* main 3e898ad [origin/main] Derive book output filenames from metadata title (#1)`
- Recent history includes:
  - `3e898ad` Derive book output filenames from metadata title (#1)
  - `4a7f59f` Add pamphlet metadata (Issue 1)
  - `63d4b81` Implement Pandoc builds for book (PDF/EPUB/DOCX)

### Branch hygiene note
- Local `feature/book-output-stems` no longer exists.
- Remote branch still present: `origin/feature/book-output-stems` (optional cleanup later).

---

## 4) Build pipeline validation (end-to-end)

### Command executed
```powershell
py .\tools\build_book.py --all --meta .\publication\metadata_book.md

# Reproducible Self‑Pub Kit — ANCHOR (Ground Truth)

Last updated: 2026-03-03  
Owner machine: Windows (PowerShell)  
Repo: https://github.com/tonefreqhz/reproducible-self-pub-kit  
Branch: main

---

## 1) What this file is (and is not)
This ANCHOR is a **ground-truth contract**: paths, commands, and checks that keep the project reproducible.

- It **does not assume** any diagnostics were run.
- It lists **how to verify** and **what “good” looks like**.
- Long-form progress notes live in: `publication/INTERIM_PROGRESS_LOG.md`

---

## 2) Current state (expected repo layout)
- Repo root (example on owner machine): `C:\Users\peewe\OneDrive\Desktop\reproducible-self-pub-kit`
- Book builder exists: `tools/build_book.py`
- Book manuscript exists: `publication\manuscript.md`
- Book metadata exists: `publication\metadata_book.md`
- Outputs directory exists (created on build): `outputs\`

---

## 3) Commands expected to work (verification recipes)
Use Python via launcher (python may not be on PATH):

```powershell
py --version
py .\tools\build_book.py --all --meta .\publication\metadata_book.md



