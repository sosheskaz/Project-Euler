package Euler017

fun noop() {}

fun main() {
  val target = 1000

  val sum = (1..target).asSequence().map { n -> wordForNumber(n).length }.sum()

  println(sum)
}

fun wordForNumber(num: Int): String {
  var n = num
  var word = ""

  if (n >= 1000000) {
    throw Exception("Number was too big: ${n}")
  }
  if (n >= 1000) {
    word += "${wordForNumber(n / 1000)}thousand"
    n %= 1000
  }
  if (n >= 100) {
    word += "${wordForNumber(n / 100)}hundred"
    n %= 100
    if (n != 0) word += "and"
  }

  when (n / 10) {
    2 -> word += "twenty"
    3 -> word += "thirty"
    4 -> word += "forty"
    5 -> word += "fifty"
    6 -> word += "sixty"
    7 -> word += "seventy"
    8 -> word += "eighty"
    9 -> word += "ninety"
  }

  if (n >= 20) n %= 10

  when (n) {
    0 -> noop()
    1 -> word += "one"
    2 -> word += "two"
    3 -> word += "three"
    4 -> word += "four"
    5 -> word += "five"
    6 -> word += "six"
    7 -> word += "seven"
    8 -> word += "eight"
    9 -> word += "nine"
    10 -> word += "ten"
    11 -> word += "eleven"
    12 -> word += "twelve"
    13 -> word += "thirteen"
    14 -> word += "fourteen"
    15 -> word += "fifteen"
    16 -> word += "sixteen"
    17 -> word += "seventeen"
    18 -> word += "eighteen"
    19 -> word += "nineteen"
    else -> throw Exception("Error: Number was too big: ${n}")
  }

  return word
}
