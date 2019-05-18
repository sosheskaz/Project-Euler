#!/usr/bin/env node

function main() {
  let sum = 0;

  let previous = 1;
  let current = 1;
  while (current < 4000000) {
    let oldPrev = previous;
    previous = current;
    current = previous + oldPrev;

    if (current % 2 == 0) {
      sum += current;
    }
  }

  console.log(sum);
}

if (require.main === module) {
  main();
}
