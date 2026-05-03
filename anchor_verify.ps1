Write-Host ""
Write-Host "============================================================"
Write-Host " REPRODUCIBLE SELF-PUB KIT — ANCHOR VERIFY"
Write-Host "============================================================"
Write-Host ""

$root = $PSScriptRoot

$paths = @{
    "Repo Root"         = $root
    "Scripts Dir"       = "$root\scripts"
    "Assets Dir"        = "$root\assets"
    "Cover Dir"         = "$root\assets\cover"
    "Fonts Dir"         = "$root\assets\fonts"
    "Covers Output Dir" = "$root\covers"
    "Docs Dir"          = "$root\docs"
    "Widgets Dir"       = "$root\widgets"
    "README"            = "$root\README.md"
    "anchor_verify.ps1" = "$root\anchor_verify.ps1"
}

$allOk = $true

foreach ($label in $paths.Keys | Sort-Object) {
    $p = $paths[$label]
    if (Test-Path $p) {
        Write-Host ("  [OK     ] {0,-30} {1}" -f $label, $p)
    } else {
        Write-Host ("  [MISSING] {0,-30} {1}" -f $label, $p)
        $allOk = $false
    }
}

Write-Host ""
if ($allOk) {
    Write-Host "  OK All paths verified. You are anchored."
} else {
    Write-Host "  WARNING: Missing paths detected. Fix before proceeding."
}
Write-Host ""
