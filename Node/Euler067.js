#!/usr/bin/env node
const fs = require("fs")
const euler018 = require('./Euler018.js')

function main() {
  console.log(euler018.getTriangleBiggestSum("input/Euler067.txt"));
}

if (require.main == module) {
  main();
}
