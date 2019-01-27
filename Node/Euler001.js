#!/usr/bin/env node

function main() {
  s = 0
  for (let i = 3; i < 1000; i +=3 ) {
    s += i
  }

  for (let i = 5; i < 1000; i += 5) {
    if (i % 3 == 0) {
      continue
    }
    s += i
  }

  console.log(s)
}


main()
