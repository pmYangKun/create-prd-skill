$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Target = Join-Path $HOME ".claude\skills\create-prd"

Write-Host "Installing create-prd skill..."
Write-Host "Source: $Root"
Write-Host "Target: $Target"

py -3 "$Root\scripts\install_skill.py" --source $Root --target $Target

Write-Host ""
Write-Host "Done!"
Write-Host "Usage:"
Write-Host "  1. Open Claude Code"
Write-Host "  2. Run: /create-prd"
Write-Host "     or describe your requirement and let the skill auto-trigger"
