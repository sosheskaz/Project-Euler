#!/usr/bin/env node
var fs = require('fs');

function main() {
  const factorCt = 13;

  var contents = fs.readFileSync('input/Euler008.txt', 'utf8');
  contents = contents
    .split('')
    .filter((c) => c >= '0' && c <= '9')
    .map((c) => parseInt(c));

  // Keep track of the last n digits in this circular buffer.
  buffer = Array(factorCt);
  buffer.fill(0);

  var product = 0;
  contents.forEach((c, index) => {
    buffer[index % factorCt] = c;
    product = Math.max(product, buffer.reduce((collector, value) => collector * value));
  })
  console.log(product);
}

if (require.main === module) {
  main();
}
