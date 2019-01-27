#!/usr/bin/env pwsh

Function main() {
  $sum = 0

  $previous = 1
  $current = 1
  While ($current -lt 4000000) {
    $oldPrev = $previous
    $previous = $current
    $current = $previous + $oldPrev

    If ($current % 2 -eq 0) {
      $sum += $current
    }
  }

  Write-Output $sum
}

main
