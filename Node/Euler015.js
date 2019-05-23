#!/usr/bin/env node

function main() {
  const target = 20

  console.log(Math.round(combinatoric(target * 2, target)))
}

function combinatoric(n, r) {
  numer = factorial(n)
  denom = factorial(r) * factorial(n - r)
  return numer / denom
}

function factorial(n) {
  var p = 1
  for (var x = n; x > 1; x--) {
    p *= x
  }
  return p
}
exports.factorial = factorial

if (require.main == module) {
  main();
}
