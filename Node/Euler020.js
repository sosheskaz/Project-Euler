#!/usr/bin/env node

function main() {
  const target = 100n
  result = bigFactorial(target)

  var sum = 0n
  while (result > 0n) {
    sum += result % 10n
    result /= 10n
  }

  console.log(String(sum))
}

function bigFactorial(n) {
  var p = 1n
  for (var x = n; x > 1n; x--) {
    p *= x
  }
  return p
}
exports.bigFactorial = bigFactorial

if (require.main == module) {
  main();
}
