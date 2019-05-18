#!/usr/bin/env node

function main() {
  var biggest = -1;
  for (var a = 100; a < 1000; a++) {
    for (var b = a + 1; b < 1000; b++) {
      let product = a * b;
      if (product > biggest && isPalindrome(product)) {
        biggest = product;
      }
    }
  }
  console.log(biggest);
}

function isPalindrome(number) {
  let asString = number.toString();
  let reversed = [...asString].reverse().join("");
  return asString == reversed;
}

if (require.main === module) {
  main();
}
