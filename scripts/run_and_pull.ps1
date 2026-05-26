# run_and_pull.ps1 — Run inference on GPU server and pull results back.
#
# Usage:
#   .\scripts\run_and_pull.ps1 -Host 77.48.24.239 -Port 43789 [-Limit 10] [-TestFile <path>] [-Out <path>]
#
# Examples:
#   # Smoke test 10 questions
#   .\scripts\run_and_pull.ps1 -Host 77.48.24.239 -Port 43789 -Limit 10
#
#   # Full golden run
#   .\scripts\run_and_pull.ps1 -Host 77.48.24.239 -Port 43789

param(
    [Parameter(Mandatory=$true)][string]$HostAddr,
    [Parameter(Mandatory=$true)][int]$Port,
    [int]$Limit = 0,
    [string]$TestFile = "app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv",
    [string]$Out = "app/physics_solution/versions/v05_code_execution/output/results_golden.json"
)

$SshTarget = "root@$HostAddr"
$SshOpts = "-p $Port -o StrictHostKeyChecking=no"
$RemoteProject = "/root/project"

# Build inference command
$InferCmd = "cd $RemoteProject && source $RemoteProject/.venv/bin/activate && python -m app.physics_solution.cli.inference --version v05_code_execution --test-file $TestFile --out $Out"
if ($Limit -gt 0) {
    $InferCmd += " --limit $Limit"
}

Write-Host "`n=== Running inference on $SshTarget (port $Port) ===" -ForegroundColor Cyan
Write-Host "Command: $InferCmd`n" -ForegroundColor DarkGray

# Run inference on server
$sshExitCode = $null
& ssh $SshOpts.Split(" ") $SshTarget $InferCmd
$sshExitCode = $LASTEXITCODE

if ($sshExitCode -ne 0) {
    Write-Host "`nInference failed with exit code $sshExitCode" -ForegroundColor Red
    exit $sshExitCode
}

Write-Host "`n=== Inference complete. Pulling results... ===" -ForegroundColor Cyan

# Ensure local output dir exists
$LocalOutDir = "app\physics_solution\versions\v05_code_execution\output"
if (-not (Test-Path $LocalOutDir)) {
    New-Item -ItemType Directory -Path $LocalOutDir -Force | Out-Null
}

# Pull results (json + csv)
$RemotePattern = "${RemoteProject}/${Out}"
$RemoteBase = $RemotePattern -replace '\.json$', ''

& scp "-P" $Port "-o" "StrictHostKeyChecking=no" "${SshTarget}:${RemoteBase}.json" $LocalOutDir/
& scp "-P" $Port "-o" "StrictHostKeyChecking=no" "${SshTarget}:${RemoteBase}.csv" $LocalOutDir/

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n=== Results pulled to $LocalOutDir ===" -ForegroundColor Green
    Get-ChildItem $LocalOutDir | Format-Table Name, Length, LastWriteTime
} else {
    Write-Host "`nFailed to pull some result files" -ForegroundColor Yellow
}
