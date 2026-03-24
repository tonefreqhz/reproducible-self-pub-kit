Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"

$SCRIPT_DIR = $PSScriptRoot
$PROJECT_ROOT = (Resolve-Path (Join-Path $SCRIPT_DIR "..")).Path
$ATTESTATION = Join-Path $PROJECT_ROOT "scripts\build_attestation.py"
$SUMMARY = Join-Path $PROJECT_ROOT "outputs\BUILD_SUMMARY.md"

Write-Host ""
Write-Host "================================================================"
Write-Host " REPRODUCIBLE-SELF-PUB-KIT BUILD VERIFICATION — M9, M12"
Write-Host "================================================================"
Write-Host ""

Write-Host "  PHASE 1: Environment" -ForegroundColor Cyan
$allTools = $true
$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) { $py = Get-Command py -ErrorAction SilentlyContinue }
if ($py) {
    Write-Host "  [OK     ] Python        $(& $py.Source --version 2>&1)"
} else {
    Write-Host "  [MISSING] Python" -ForegroundColor Red; $allTools = $false
}
$pandoc = Get-Command pandoc -ErrorAction SilentlyContinue
if ($pandoc) { Write-Host "  [OK     ] Pandoc        $((& pandoc --version 2>&1) | Select-Object -First 1)" }
else { Write-Host "  [MISSING] Pandoc" -ForegroundColor Yellow }
if (-not $allTools) { Write-Host "`n  STOP: Required tools missing." -ForegroundColor Red; exit 1 }
Write-Host ""

Write-Host "  PHASE 2: Attestation" -ForegroundColor Cyan
if (-not (Test-Path $ATTESTATION)) {
    Write-Host "  [MISSING] build_attestation.py" -ForegroundColor Red; exit 1
}
Push-Location $PROJECT_ROOT
$pyCmd = if ($py) { $py.Source } else { "python" }
& $pyCmd $ATTESTATION 2>&1 | ForEach-Object { Write-Host "    $_" }
$attExit = $LASTEXITCODE
Pop-Location
Write-Host ""

Write-Host "  PHASE 3: Summary" -ForegroundColor Cyan
if (Test-Path $SUMMARY) { Get-Content $SUMMARY | ForEach-Object { Write-Host "    $_" } }
Write-Host ""
if ($attExit -eq 0) { Write-Host "  BUILD VERIFICATION: PASS" -ForegroundColor Green }
else { Write-Host "  BUILD VERIFICATION: FAIL" -ForegroundColor Red }
Write-Host ""
exit $attExit
