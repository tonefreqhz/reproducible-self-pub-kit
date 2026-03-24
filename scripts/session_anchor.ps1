Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"

$SCRIPT_DIR = $PSScriptRoot
$PROJECT_ROOT = (Resolve-Path (Join-Path $SCRIPT_DIR "..")).Path
$DRIFT_LOG = Join-Path $PROJECT_ROOT "logs\DRIFT_LOG.csv"
$ATTESTATION_JSON = Join-Path $PROJECT_ROOT "outputs\BUILD_ATTESTATION.json"

Write-Host ""
Write-Host "================================================================"
Write-Host " SESSION ANCHOR — reproducible-self-pub-kit — M4"
Write-Host "================================================================"
Write-Host ""

Push-Location $PROJECT_ROOT
$branch = (git branch --show-current 2>&1) -join ""
$lastHash = (git rev-parse --short HEAD 2>&1) -join ""
$lastMsg = (git log -1 --format="%s" 2>&1) -join ""
$status = git status --porcelain 2>&1
$clean = if ($status) { "DIRTY" } else { "CLEAN" }

Write-Host "  Branch   : $branch"
Write-Host "  Commit   : $lastHash — $lastMsg"
Write-Host "  Status   : $clean"
Pop-Location
Write-Host ""

Write-Host "  Key Paths:" -ForegroundColor Cyan
@("scripts/","tools/","publish/","publication/","assets/","widgets/","logs/") | ForEach-Object {
    $p = Join-Path $PROJECT_ROOT $_
    $s = if (Test-Path $p) { "[OK     ]" } else { "[MISSING]" }
    Write-Host "    $s $_"
}
Write-Host ""

Write-Host "  Drift Log (last 3):" -ForegroundColor Cyan
if (Test-Path $DRIFT_LOG) {
    (Get-Content $DRIFT_LOG | Select-Object -Skip 1 | Select-Object -Last 3) | ForEach-Object { Write-Host "    $_" }
} else { Write-Host "    [MISSING] logs/DRIFT_LOG.csv" -ForegroundColor Yellow }
Write-Host ""

Write-Host "  Build Attestation:" -ForegroundColor Cyan
if (Test-Path $ATTESTATION_JSON) {
    try {
        $att = Get-Content $ATTESTATION_JSON -Raw | ConvertFrom-Json
        Write-Host "    Status: $(if ($att.overall_pass) {'PASS'} else {'FAIL'})" -ForegroundColor $(if ($att.overall_pass) {'Green'} else {'Red'})
    } catch { Write-Host "    [ERROR] parse failed" -ForegroundColor Red }
} else { Write-Host "    [not yet] Run: python scripts/build_attestation.py" -ForegroundColor Yellow }
Write-Host ""
