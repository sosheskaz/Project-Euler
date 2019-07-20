#!/usr/bin/env node

function main() {
  const target = 10000;
  let properDivisorsSums = {};
  let amicableSum = 0;

  for (let i = 1; i < target; i++) {
    let divisorsSum = properDivisorsSums[i];
    if (divisorsSum === undefined) {
      divisorsSum = getProperDivisorsSum(i);
      properDivisorsSums[i] = divisorsSum;
    }

    let otherDivisorsSum = properDivisorsSums[divisorsSum];
    if (otherDivisorsSum === undefined) {
      otherDivisorsSum = getProperDivisorsSum(divisorsSum);
      properDivisorsSums[divisorsSum] = otherDivisorsSum;
    }

    if (otherDivisorsSum == i && i != divisorsSum) {
      amicableSum += i;
    }
  }

  console.log(amicableSum);
}

function getProperDivisorsSum(n) {
  let sum = 1;
  let limit = Math.ceil(Math.sqrt(n));

  for (let i = 2; i <= limit; i++) {
    if (n % i == 0) {
      sum += i;
      let otherDivisor = n / i;
      if (otherDivisor != i) {
        sum += otherDivisor;
      }
    }
  }

  return sum
}

if (require.main == module) {
  main();
}
