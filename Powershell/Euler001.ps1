#!/usr/bin/env pwsh

Function main() {
    Write-Output (3..999 |Where-Object {$_ % 3 -eq 0 -or $_ % 5 -eq 0} |Measure-Object -sum).Sum
}

main
