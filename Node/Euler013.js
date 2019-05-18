#!/usr/bin/env node
const fs = require('fs');

function main() {
  const inFile = "input/Euler013.txt"
  const digits = 10

  const nums = loadFile(inFile)
  const sum = nums.reduce((aggregator, value) => aggregator + value)

  const exponentAdjustment = Math.ceil(Math.log10(sum)) - digits
  const sumAdjustment = Math.pow(10, exponentAdjustment)

  const adjustedSum = Math.round(sum / sumAdjustment)
  console.log(adjustedSum)
}

function loadFile(path) {
  const contents = fs.readFileSync(path, 'utf8');
  values = contents.split("\n").filter((line) => line).map((line) => parseFloat(line) );
  return values
}

if (require.main == module) {
  main();
}
