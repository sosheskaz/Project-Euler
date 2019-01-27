#!/usr/bin/env pwsh

Function main() {
    $sum = (3..999 |Where-Object {$_ % 3 -eq 0} |Measure-Object -sum).Sum

    $sum += (5..999 |Where-Object {$_ % 5 -eq 0 -and $_ % 3 -ne 0} |Measure-Object -sum).Sum

    Write-Output $sum
}

main
