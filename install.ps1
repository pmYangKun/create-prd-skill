$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Target = Join-Path $HOME ".claude\skills\create-prd"

Write-Host "正在安装 create-prd skill..."
Write-Host "源目录：$Root"
Write-Host "目标目录：$Target"

py -3 "$Root\scripts\install_skill.py" --source $Root --target $Target

Write-Host ""
Write-Host "安装完成！"
Write-Host "使用方式："
Write-Host "  1. 打开 Claude Code"
Write-Host "  2. 输入 /create-prd"
Write-Host "     或直接描述你的需求，Claude 会自动触发该 skill"
