#!/usr/bin/env node

function main() {
  var s = 0;
  for (let i = 3; i < 1000; i +=3 ) {
    s += i;
  }

  for (let i = 5; i < 1000; i += 5) {
    if (i % 3 != 0) {
      s += i;
    }
  }

  console.log(s);
}

if (require.main === module) {
  main();
}
