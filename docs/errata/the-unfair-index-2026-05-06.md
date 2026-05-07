# Errata · *The Unfair Index* — First Edition (Standard Print, 6 May 2026)

**W-Anchor c9ced1a · Banked 7 May 2026 · 08:45 local · Roger G. Lewis**
**Title:** *The Unfair Index: A Surveyor's Levels Survey of the Financial Terrain*
**Author:** Roger G. Lewis
**Imprint:** Pimpernell Press / DoughForge
**Edition:** First (Standard Print, 6 May 2026)
**Typesetter:** Reedsy
**Pages:** 108

---

## §0 · The discipline this errata exists to enforce

The book argues that knowledge should be reproducible, evidence-based, and open to challenge. That argument applies to the book itself.

Books written with AI assistance, like books written without it, contain mistakes. Some of those mistakes are minor — a date misremembered, a name transliterated imperfectly, a place-name spelled by phonetic recognition rather than by reference. Others are substantive — an explanation of an engineering history that gets the dominant cause wrong, a methodological description that simplifies a known nuance into a misleading shape. Both kinds appeared in the first-edition manuscript of *The Unfair Index*.

The discipline this kit honours, and that this book is a worked example of, is to **document the mistakes rather than scrub them.** A scrubbed second edition that quietly corrects errors leaves no record of which mistakes were made, when they were made, who or what made them, or how they were detected. A documented first edition with a hashed errata anchored to a published date does the opposite: it preserves the evidence of imperfection, names the imperfection, and gives a future reader the tools to verify both the original and the correction.

If a future critic — or a future automated content-quality classifier, or a future bad-faith attack — asserts that this book is unreliable because it contains an error, the answer is in this file. The error is named. The hash of the as-published file is recorded. The corrected text is preserved. The book did not pretend the mistake was not there. The book made the mistake, recorded the mistake, and printed the record alongside the mistake. **That is what reproducibility means when it is applied to authorship and not only to data.**

---

## §1 · Hash anchors — the as-published artefacts

The errors below are present in the following files. Future verification of "what the book actually shipped" should hash these files and compare against the SHA-256 values recorded here.

| File | Size (bytes) | SHA-256 |
|---|---|---|
| `the-unfair-index-STANDARD-PRINT-READY.pdf` | 1,709,605 | `75cb72f36a3e541dfaa38e4a5219fe6da8af0e49a8821123725227977aecaac3` |
| `the-unfair-index-STANDARD.pdf` | 1,729,026 | `9c048f7631f50e239fc771ccf4a470a4cf5b40430575fab3e983cb212c6b7afe` |
| `The-Unfair-Index-A-Surveyors-Levels-Survey-of-the-Financial-Terrain.epub` | 1,386,893 | `d4fa8df583448271a2f6f8f81b535e6cec94655d116b5f3dc507867484aa798d` |

PDF metadata records: `CreationDate D:20260506101222Z`, `Producer: Typeset by Reedsy`, `Author: Roger Lewis`, `PTEX.FullBanner: This is LuaHBTeX, Version 1.15.0 (TeX Live 2022/Debian)`. PDF/X-1a:2001 conformant.

Hash computation method: SHA-256 over the full file contents, computed by `hashlib` (Python 3.12), 1 MB chunks. Anyone with the file can reproduce the hash with `sha256sum the-unfair-index-STANDARD-PRINT-READY.pdf` (Linux/macOS) or `Get-FileHash -Algorithm SHA256` (Windows PowerShell).

---

## §2 · Documented errata · First Edition

### Erratum 1 · Wankel passage — Coda chapter, page 89 (PDF page 101)

**Severity:** Substantive. The passage misattributes a well-known engineering history.

**Detection:** Roger G. Lewis, 6 May 2026, 16:30 local — during a proofreading pass on the Reedsy-typeset PDF.

**Cross-reference:** The Wankel engine appears in *The Wandering Anchor* (Library #16 / forecast 16) in the Roger Merryweather narrowboat scene on the Kennet and Avon Canal. The two volumes carry the metaphor jointly. A reader cross-referencing across the trilogy may notice the Coda passage's emphasis on first-mover advantage and the Wandering Anchor passage's framing differ in their account of the engineering. The discrepancy is itself a tell that the Coda passage was AI-assisted prose under-reviewed at the engineering claim.

**Original text (as published, page 89):**

> *"The Wankel engine, for those who have not encountered it in the earlier volumes of this trilogy, is a rotary internal combustion engine invented by Felix Wankel in the 1950s. It is elegant, compact, and mechanically ingenious. **It is also, in the automotive industry, almost entirely extinct, not because it is inferior to the piston engine in every respect — it is not — but because the piston engine arrived first, established the infrastructure, trained the mechanics, and created the supply chains, and the Wankel engine, however elegant, could not displace an incumbent that had already enclosed the market.**"*

**Engineering issue with the original:**

The bolded sentence frames the Wankel's automotive marginalisation as essentially a first-mover-incumbent story. That is incomplete and arguably misleading. The dominant reason the Wankel engine is largely extinct in production cars is the **apex seal problem** — the rotor-tip sealing mechanism that has to maintain a moving line-contact against the epitrochoidal housing wall. Apex seals wear, lose tension, lose compression, and burn oil at the seam. Mazda spent forty years engineering carbon-aluminium then ceramic-composite seals plus chrome-plated rotor housings (RX-7 generation) and got close, but never close enough to meet fuel-economy and emissions standards that piston engines could meet, year after year, with conventional ring improvements. Mazda retired the rotary from production cars in 2012. The seal problem outlived Felix Wankel and Mazda's engineering will both. That is the engineering reason. First-mover infrastructure / supply-chain advantage was a real but secondary factor that operated in compound with the engineering disadvantage.

**Corrected text (for second edition or for reader's own annotation):**

> *"The Wankel engine, for those who have not encountered it in the earlier volumes of this trilogy, is a rotary internal combustion engine invented by Felix Wankel in the 1950s. It is elegant, compact, and mechanically ingenious. It is also, in the automotive industry, almost entirely extinct.*
>
> *The real reason is the apex seal. The Wankel rotor is a triangular shape that sweeps an epitrochoidal housing, and at each of the three rotor tips a small seal — the apex seal — has to maintain a moving line-contact against the housing wall to keep combustion pressure inside the working chamber and lubricating oil outside it. The problem is that this seal is asked to do, in a rotary engine, what three or four conventional rings do in a piston engine, and it is asked to do it under conditions of asymmetric heat and asymmetric wear that the rings of a reciprocating engine never see. Apex seals wear. They lose tension against the housing wall. Compression leaks past them. Oil burns at the seam. Hydrocarbon emissions rise as the seals age. Mazda spent forty years engineering solutions — carbon-aluminium seals, then ceramic-composite seals, then the chrome-plated rotor housing of the RX-7 generation — and got remarkably close, but never close enough to meet the fuel-economy and emissions standards that piston engines could meet, year after year, with conventional improvements. Mazda finally retired the rotary from production cars in 2012. The seal problem outlived Felix Wankel and Mazda's engineering will both. That is the engineering reason.*
>
> *It could be speculated that the engineering reason was not the only reason — that the piston engine had also arrived first, established the infrastructure, trained the mechanics, and created the supply chains, and that the Wankel, however elegant, faced an incumbent that had already enclosed the automotive market and had no commercial incentive to invest in solving the seal problem at any scale beyond Mazda's. **This is not a conspiracy. It is a misalignment of incentives.** The ICE majors had a fully amortised investment in the piston architecture; the Wankel's per-unit advantages did not justify the per-firm cost of engineering the seal problem to compliance. Mazda paid that cost on its own and could not, in the end, fully discharge it. The structural disadvantage and the engineering disadvantage operated in compound. Either alone would have been a serious obstacle. Together they were a closing door."*

**Subsequent paragraphs in the Coda** — the Roger Merryweather narrowboat scene, the FAIR-Index-as-Wankel methodological-superiority claim, the book-as-response-to-the-Wankel-problem closing arc, and the gatekeepers-policing-abundance line at the chapter end — all stand as published. The metaphor is preserved; the engineering correction sharpens it. Footnote 5 (Felix Wankel 1902–1988, philosophical about marginalisation) is also unchanged.

**Editorial source for correction:** `outputs/posh_claude/unfair_index/proofread_wankel_passage_06may2026.md` (in the DoughForge working directory; not in this kit repo). W-Anchor c9ced1a · Posh Claude lane · 6 May 2026 · 16:42 local.

**Why the framing change matters:** "Misalignment of incentives, not conspiracy" is a sharper formulation of the recursive enclosure thesis than "first-mover advantage." It elevates the chapter's argument from grievance to analysis. A reader running due diligence on the book's intellectual seriousness will notice the difference.

---

### Erratum 2 · Author birth date

**Severity:** Factual. Discoverable from public records.

**Status:** Detected by Roger G. Lewis during proofreading pass; specific location and incorrect/correct values to be filled in by Roger before next edition build.

**Original text (location TBC by Roger):** [INCORRECT BIRTH DATE — Roger to insert as published]
**Corrected text:** [CORRECT BIRTH DATE — Roger to insert]
**Source for correction:** Public birth records / author's own records.

---

### Erratum 3 · Various dates and details

**Severity:** Mixed — minor through factual.

**Status:** Detected by Roger G. Lewis during proofreading pass. Specific items to be enumerated by Roger as they are confirmed against source records. Each item, when added, will follow the format of Erratum 1: location, original text, issue, corrected text, source for correction.

This erratum entry exists as a placeholder so that the structure of this document is in place at first commit. Items will be added by amendment commits, each timestamped, each W-Anchored, each bearing its own correction-source citation. The book ships with these errors un-edited; the errata grows as the errors are detected and documented.

---

## §3 · Mojibake and AI-hallucination disclosure

This first edition was assembled with substantial AI-assistance: substack-archive lifts, voice-widget-controlled drafting, Reedsy typesetting. The author (a human) reviewed the manuscript prior to print but did not catch every imperfection. Some imperfections are typical AI-authorship artefacts — a confident over-simplified explanation that papers over a known nuance, a date or proper-name autocorrected by training-data context rather than by source-checking, a phonetically reasonable spelling that differs from the canonical spelling. Others are typical human-authorship artefacts — a quote remembered approximately rather than checked, a cross-reference inserted from memory rather than from the source.

This errata file does not distinguish between the two. The provenance of any specific error is, in many cases, unknowable after the fact. What is recordable is the fact of the error, the location, the corrected version, and the date of detection. **That is what is recorded.**

A reader or critic interested in the question of "AI authorship reliability" who finds an error in the book is invited to compare the error against this file. If the error is documented, the answer is "yes, the author detected it on date X and recorded it on date Y." If the error is not documented, the reader is invited to report it (contact details in the book's back-matter). The errata grows. The kit repo records each addition as a versioned commit.

---

## §4 · Why the book ships with errors un-edited

Several reasons:

1. **The print run is committed.** Reedsy-typesetting and Draft2Digital distribution have specific milestone gates; correcting and re-typesetting between gates is non-zero cost in time and expense.
2. **The errata structure is itself part of the argument.** The book argues for transparent, reproducible, evidence-based knowledge. A book that scrubs its own errors silently before second printing is not transparent. A book that documents its errors in a hashed errata file anchored to specific PDF/EPUB hashes is.
3. **Critical-attack defence.** A bad-faith critic who claims the book is unreliable because of error X meets a documented record of error X with author-disclosed correction and a hash that proves the disclosure pre-dates the criticism. The defence is constructed at print time, not retrofitted under attack.
4. **Cross-trilogy verification.** Several errors (notably the Wankel passage) are discoverable by a careful reader cross-referencing the rest of the Library. The cross-reference is itself the first-line correction mechanism. The errata is the second-line.

The framing is consistent with the broader Library discipline: the FAIR-Index data are publicly hosted at realrld.com/homeix-fair.html, the methodology repo is on public Git, the commit hashes are recorded, and the data sources can be re-pulled by any reader who wants to challenge the index. The same discipline applies to the book that argues for the discipline. **The Index applies to itself.**

---

## §5 · Process for adding errata

Any subsequent error detected, by Roger G. Lewis or by a reader who reports it, follows this format:

1. **Locate** the error in the book — chapter, page, paragraph, exact wording (verbatim).
2. **Classify** severity: typo / factual / substantive / methodological.
3. **State** the issue concisely.
4. **Provide** the corrected text.
5. **Cite** the correction's source (public record, primary text, calculation, etc.).
6. **Date** the entry. W-Anchor c9ced1a or the W-Anchor in force at the time of the addition.
7. **Commit** the addition to this file in the kit repo with a descriptive commit message: `errata: <book> · <erratum-N> · <one-line summary>`.
8. **Hash anchor** does not change unless the underlying PDF/EPUB is itself re-issued. If a corrected second edition is later published, that second edition gets its own errata file, and this file becomes the historical record of the first edition.

---

## §6 · Cross-references

- Original proofread / corrected-text source: `outputs/posh_claude/unfair_index/proofread_wankel_passage_06may2026.md` (DoughForge working directory)
- Coda framing record: `outputs/posh_claude/unfair_index_05may2026/06_path_a_confirmed_06may2026.md` and `07_gatekeepers_line_06may2026.md`
- Trilogy cross-reference: *The Wandering Anchor* (Library #16 / forecast 16) — Roger Merryweather Wankel scene on the Kennet and Avon Canal
- Project memory: `project_unfair_index_strategic_positioning.md`, `project_unfair_index_d2d_coda_framing.md`, `feedback_unfair_index_is_investor_lane.md`, `reference_fair_index_public_url.md`
- ISBN registry: this file's parent directory · `docs/ISBN_REGISTRY.md` (current state: slot 10 reserved; this title ships under D2D-assigned free EPUB ISBN per Roger's ruling 6 May 2026 09:50 local)

---

**W-Anchor c9ced1a · Banked 7 May 2026 · 08:45 local · First Edition errata committed honestly and at print time, hashed-as-published, ready to defend against attack and ready to correct in second edition. The Index applies to itself.**
