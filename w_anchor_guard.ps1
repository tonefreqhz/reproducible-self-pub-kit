# W-ANCHOR GUARD — Per-Prompt Verification
# Run this BEFORE every AI prompt, not just session start.
# Paste the output into the AI chat as the first message.
# The AI must confirm it has read the state block before proceeding.
#
# Usage: .\w_anchor_guard.ps1
# Or:    .\w_anchor_guard.ps1 -Repo "C:\path\to\any\repo"

param(
    [string]$Repo = (Get-Location).Path
)

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "═══════════════════════════════════════════════════════"
Write-Host " W-ANCHOR GUARD — Per-Prompt State Verification"
Write-Host "═══════════════════════════════════════════════════════"
Write-Host ""

# 1. Verify we're in a git repo
$gitDir = Join-Path $Repo ".git"
if (-not (Test-Path $gitDir)) {
    Write-Host "  [FAIL] Not a git repository: $Repo"
    Write-Host "  STOP. Do not prompt the AI."
    exit 1
}

# 2. Get last commit hash and message
$lastHash = git -C $Repo log -1 --format="%H" 2>$null
$lastShort = git -C $Repo log -1 --format="%h" 2>$null
$lastMsg = git -C $Repo log -1 --format="%s" 2>$null
$lastDate = git -C $Repo log -1 --format="%ci" 2>$null
Write-Host "  [ANCHOR] Last commit: $lastShort"
Write-Host "           $lastMsg"
Write-Host "           $lastDate"

# 3. Check for uncommitted changes
$status = git -C $Repo status --porcelain 2>$null
$modified = ($status | Where-Object { $_ -match "^\s?M" }).Count
$untracked = ($status | Where-Object { $_ -match "^\?\?" }).Count
if ($modified -gt 0 -or $untracked -gt 0) {
    Write-Host "  [WARN ] $modified modified, $untracked untracked files"
} else {
    Write-Host "  [CLEAN] Working tree clean"
}

# 4. Check .py files not modified since last commit
$pyFiles = git -C $Repo diff --name-only HEAD -- "*.py" 2>$null
if ($pyFiles) {
    Write-Host "  [FAIL ] Python files modified since last commit:"
    $pyFiles | ForEach-Object { Write-Host "           $_" }
    Write-Host "  STOP. .py files must not be altered by AI."
    Write-Host "  Revert with: git checkout -- *.py"
} else {
    Write-Host "  [SAFE ] No .py files modified"
}

# 5. Check existing build outputs
$outputDirs = @("dist", "outputs", "manuscript/build", "output")
$existingBuilds = @()
foreach ($d in $outputDirs) {
    $fullPath = Join-Path $Repo $d
    if (Test-Path $fullPath) {
        $files = Get-ChildItem -Path $fullPath -Recurse -File -Include "*.epub","*.pdf","*.docx","*.html" -ErrorAction SilentlyContinue
        if ($files.Count -gt 0) {
            $existingBuilds += $files
            Write-Host "  [BUILD] $d/ contains $($files.Count) output files"
        }
    }
}
if ($existingBuilds.Count -eq 0) {
    Write-Host "  [EMPTY] No existing builds found"
}

# 6. Check BUILD_ATTESTATION.json
$attestation = Join-Path $Repo "outputs/BUILD_ATTESTATION.json"
if (Test-Path $attestation) {
    $att = Get-Content $attestation | ConvertFrom-Json -ErrorAction SilentlyContinue
    Write-Host "  [ATTEST] BUILD_ATTESTATION.json present"
} else {
    Write-Host "  [NONE ] No BUILD_ATTESTATION.json"
}

# 7. Check path persistence — key paths resolve
$keyPaths = @(
    "book.yaml", "CLAUDE.md", "README.md",
    "anchor.py", "anchor_verify.ps1"
)
$pathOk = $true
foreach ($p in $keyPaths) {
    $full = Join-Path $Repo $p
    if (-not (Test-Path $full)) {
        # Not all repos have all files — only warn, don't fail
    }
}

# 8. Read standing orders summary
$poshClaude = Join-Path $Repo "PoshClaude.md"
$claudeMd = Join-Path $Repo "CLAUDE.md"
$hasPosh = Test-Path $poshClaude
$hasClaude = Test-Path $claudeMd
Write-Host ""
if ($hasPosh) { Write-Host "  [ORDERS] PoshClaude.md present — brand routing active" }
if ($hasClaude) { Write-Host "  [ORDERS] CLAUDE.md present — build rules active" }

# 9. Output the state block for pasting into AI
Write-Host ""
Write-Host "═══════════════════════════════════════════════════════"
Write-Host " PASTE THE FOLLOWING INTO YOUR AI PROMPT:"
Write-Host "═══════════════════════════════════════════════════════"
Write-Host ""
Write-Host "W-ANCHOR STATE BLOCK"
Write-Host "Repo: $Repo"
Write-Host "Hash: $lastShort ($lastDate)"
Write-Host "Message: $lastMsg"
Write-Host "Status: $modified modified, $untracked untracked"
Write-Host "Python: $(if ($pyFiles) { 'MODIFIED — DO NOT PROCEED' } else { 'safe' })"
Write-Host "Builds: $($existingBuilds.Count) existing outputs"
if ($existingBuilds.Count -gt 0) {
    Write-Host "  Existing:"
    $existingBuilds | ForEach-Object {
        Write-Host "    $($_.Name) ($([math]::Round($_.Length/1024))KB, $($_.LastWriteTime))"
    }
}
Write-Host "Standing orders: $(if ($hasPosh) { 'PoshClaude.md' } else { 'NONE' }) + $(if ($hasClaude) { 'CLAUDE.md' } else { 'NONE' })"
Write-Host ""
Write-Host "AI: Confirm you have read this state block."
Write-Host "AI: Do NOT build, compile, or generate output without"
Write-Host "    checking existing builds listed above."
Write-Host "AI: .py files are READ-ONLY. Do not modify them."
Write-Host ""
Write-Host "═══════════════════════════════════════════════════════"
Write-Host ""
