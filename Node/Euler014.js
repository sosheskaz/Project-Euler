#!/usr/bin/env node

function main() {
  const target = 1000000;
  var biggestChain = -1;
  var biggestStart = -1;

  for (var i = 1; i < target; i++) {
    l = collatz(i).length;
    if (l > biggestChain) {
      biggestChain = l;
      biggestStart = i;
    }
  }

  console.log(biggestStart);
}

function collatz(n) {
  var result = [];

  while (n > 1) {
    result.push(n);
    if (n % 2 == 0) {
      n /= 2;
    } else {
      n = 3 * n + 1;
    }
  }

  result.push(1);
  return result;
}

if (require.main == module) {
  main();
}
