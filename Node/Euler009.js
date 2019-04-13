#!/usr/bin/env node

function main() {
  const target = 1000;

  for (let a = 3; a * 3 + 2 <= target; a++) {
    for (let b = a + 1;a + 2 * b + 1 <= target; b++) {
      let c = Math.sqrt(a * a + b * b);
      if (c == Math.floor(c)) {
        let sum = a + b + c;

        if (target % sum == 0) {
          // We have a match.
          let factor = target / sum;
          let aFinal = factor * a;
          let bFinal = factor * b;
          let cFinal = factor * c;

          console.log(aFinal * bFinal * cFinal);
          return;
        }
        else {
          break
        }
      }
    }
  }
}

main()
