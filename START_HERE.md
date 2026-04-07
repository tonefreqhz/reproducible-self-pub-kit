# START HERE

You have 5 steps to go from clone to compiled book.

## Prerequisites

1. Install Python 3.12+ from https://python.org
2. Install Pandoc from https://pandoc.org

## Build Your Book

3. Install Python dependencies:

```
pip install -r requirements.txt
```

4. Write your book in a single Markdown file. An example is provided:

```
publication/manuscript.md
```

You can also combine your chapter files into one manuscript:

```
cat manuscript/chapter_01.md manuscript/chapter_02.md manuscript/chapter_03.md > publication/manuscript.md
```

On Windows (PowerShell):

```powershell
Get-Content manuscript\chapter_01.md, manuscript\chapter_02.md, manuscript\chapter_03.md | Set-Content publication\manuscript.md
```

5. Run the build:

```
python tools/build_book.py --epub
```

This produces an EPUB file in `outputs/epub/`.

## Build Options

Build all formats (PDF requires xelatex):

```
python tools/build_book.py --all
```

Build only EPUB (no LaTeX needed):

```
python tools/build_book.py --epub
```

Build only DOCX:

```
python tools/build_book.py --docx
```

Use a metadata file to set title, author, date:

```
python tools/build_book.py --epub --meta example_book.yaml
```

## Where Things Live

- Your manuscript goes in: `publication/manuscript.md`
- Example chapters are in: `manuscript/`
- Metadata template: `example_book.yaml` (edit title, author, etc.)
- Build output appears in: `outputs/epub/`, `outputs/pdf/`, `outputs/docx/`

That is it. Everything else in this repo is for the DoughForge ecosystem and AI-assisted sessions.
