param([switch]$ChinaMirrors, [switch]$AllSources, [switch]$WithoutHongguo)
$ErrorActionPreference = "Stop"
$BuildArguments = @()
if ($ChinaMirrors) { $BuildArguments += "--cn-mirrors" }
if ($AllSources) { $BuildArguments += "--all-sources" }
if ($WithoutHongguo) { $BuildArguments += "--without-hongguo" }
python (Join-Path $PSScriptRoot "build_windows.py") @BuildArguments
exit $LASTEXITCODE
