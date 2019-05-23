#!/usr/bin/env node

function main() {
  const sunday = 0;
  var sundays = 0;

  for (var year = 1901; year <= 2000; year++) {
    for (var month = 0; month < 12; month++) {
      var d = new Date(year, month, 1);
      if (d.getDay() == sunday) {
        sundays++;
      }
    }
  }

  console.log(sundays)
}

if (require.main == module) {
  main();
}
