#!/usr/bin/env node
const fs = require("fs")
const baseLetterScore = 'a'.charCodeAt(0) - 1

function main() {
  var names = loadFile("input/names.txt")
  names.sort()
  var scores = names.map((name, idx) => scoreName(name) * (idx + 1))
  var s = scores.reduce((a, b) => a + b)
  console.log(s)
}

function loadFile(path) {
  var contents = fs.readFileSync(path, 'utf8')
  return contents.split(",").map((s) => s.replace(/\W/g, ""))
}

function scoreName(name) {
  return name.toLowerCase().split("").map((l) => scoreLetter(l)).reduce((a, b) => a + b)
}

function scoreLetter(l) {
  return l.charCodeAt(0) - baseLetterScore
}

if (require.main == module) {
  main();
}
