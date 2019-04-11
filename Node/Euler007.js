#!/usr/bin/env node

function main() {
  const n = 10001;
  var primeList = [2];

  var i = 3;
  while (primeList.length < n) {
    if (primeList.every((prime) => { return i % prime != 0; })) {
      primeList.push(i)
    }

    i += 2
  }

  console.log(primeList[primeList.length-1])
}

main()
