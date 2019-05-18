#!/usr/bin/env node
const generators = require("./generators.js");

function main() {
  const target = 500;

  var triangles = generators.filter(generate_triangles(), (t) => { return getFactors(t).size > target });
  for (let t of triangles) {
    console.log(t);
    break;
  }
}

function getFactors(ofInt) {
  const max = Math.ceil(Math.sqrt(ofInt));
  var factors = new Set();
  for (var factor = 1; factor <= max; factor++) {
    if (ofInt % factor == 0) {
      factors.add(factor);
      factors.add(ofInt / factor);
    }
  }
  return factors;
}

function* generate_triangles() {
  var triangle = 0;
  var incrementer = 1;
  while (true) {
    triangle += incrementer;
    yield triangle;
    incrementer++;
  }
}

if (require.main == module) {
  main();
}
