# BuildAndPublish.ps1 — double-click front door
# Repaired 03 May 2026 · born half-finished b2191d0 ·
# completed-broken by tools/rebuild_publish.ps1 deletion
# W-Anchor c9ced1a
$ErrorActionPreference = "Stop"
$PROJECT_ROOT = $PSScriptRoot
Set-Location $PROJECT_ROOT
& "$PROJECT_ROOT\publish\rebuild_publish.ps1" @args
Write-Host "Build complete. Check outputs/ for PDF, EPUB, DOCX."
Read-Host "Press Enter to exit"
