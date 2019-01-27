#!/usr/bin/env pwsh

Function main() {
  Write-Output (primeFactors 600851475143) | Select-Object -Last 1
}

Function primeFactors([Int64]$ofLong) {

  While ($ofLong % 2 -eq 0) {
    $ofLong /= 2
    Write-Output 2
  }

  For ($i = [Int64]3; $i -le $ofLong; $i+=1) {
    If ($ofLong -eq 1) { break }

    While ($ofLong % $i -eq 0) {
      $ofLong /= $i
      Write-Output $i
    }
  }
}

main
