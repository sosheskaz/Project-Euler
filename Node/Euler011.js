#!/usr/bin/env node
const fs = require("fs")

function main() {
  const target = 4;
  table = loadFile("input/Euler011.txt");
  biggest = maxProduct(table, target);
  console.log(biggest);
}

function loadFile(path) {
  var contents = fs.readFileSync(path, 'utf8');
  table = contents.split("\n").filter((line) => line).map((line) => {
    return line.split(" ").filter((item) => item).map((item) => parseInt(item));
  });
  return table;
}

function maxProduct(table, length) {
  biggest = 1;

  for (let i = 0; i < table.length; i++) {
    for (let j = length - 1; j < table[0].length; j++) {
      var horizProduct = 1;
      var vertProduct = 1;
      var diagEastProduct= 1;
      var diagWestProduct = 1;

      for (let cursor = 0; cursor < length; cursor++) {
        horizProduct *= table[i][j-cursor];
        vertProduct *= table[j-cursor][i];
        if (i >= length) {
          diagWestProduct *= table[i-cursor][j-cursor];
          if (j <= table[0].length - length) {
            diagEastProduct *= table[i-cursor][j+cursor];
          }
        }
      }

      biggest = Math.max(biggest, horizProduct, vertProduct, diagEastProduct, diagWestProduct);
    }
  }

  return biggest;
}

if (require.main === module) {
  main();
}
