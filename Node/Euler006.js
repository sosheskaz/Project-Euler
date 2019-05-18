#!/usr/bin/env node

function main() {
  const n = 100;

  var squareOfSum = 0;
  var sumOfSquares = 0;

  for (let i = 1; i <= n; i++) {
    squareOfSum += i;
    sumOfSquares += i * i;
  }
  squareOfSum *= squareOfSum;

  console.log(squareOfSum - sumOfSquares);
}

if (require.main === module) {
  main();
}
