#!/usr/bin/env node
const euler011 = require('./Euler011.js');

function main() {
  console.log(getTriangleBiggestSum("input/Euler018.txt"));
}

function getTriangleBiggestSum(ofFile) {
  triangle = euler011.loadFile(ofFile);

  for (var row = triangle.length - 2; row >= 0; row--) {
    // calculating subtriangles. The bigger option of each "edge" in a subtriangle is the optimal route.
    // we work by modifying each element to be the max of its available paths.
    for (var col = 0; col < triangle[row].length; col++) {
      let lchild = triangle[row + 1][col];
      let rchild = triangle[row + 1][col + 1];

      if (lchild > rchild) {
        triangle[row][col] += lchild;
      } else {
        triangle[row][col] += rchild;
      }
    }
  }

  return triangle[0][0];
}
exports.getTriangleBiggestSum = getTriangleBiggestSum;

if (require.main == module) {
  main();
}
