#!/usr/bin/env node

function main() {
  const target = 1000n
  const big10 = 10n

  var x = 2n ** target
  var sum = 0n

  while (x > 0) {
    sum += x % big10
    x /= big10
  }

  console.log(String(sum))
}

if (require.main == module) {
  main();
}
