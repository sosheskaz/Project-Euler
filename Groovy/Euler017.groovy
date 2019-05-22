#!/usr/bin/env groovy

class Euler017 {
  private static final int target = 1000

  public static void main(String[] args) {
    int sum = (1..target).collect { wordForNumber(it).length() }.sum()
    println sum
  }

  private static String wordForNumber(int n) {
    String word = ""
    if (n >= 1000000) {
      throw new Exception("Number was too big: " + n)
    }
    if (n >= 1000) {
      word += "${wordForNumber((int)(n / 1000))}thousand"
      n %= 1000
    }
    if (n >= 100) {
      word += "${wordForNumber((int)(n / 100))}hundred"
      n %= 100
      if (n != 0) {
        word += "and"
      }
    }

    switch ((int)(n / 10)) {
    case 2:
      word += "twenty"
      break
    case 3:
      word += "thirty"
      break
    case 4:
      word += "forty"
      break
    case 5:
      word += "fifty"
      break
    case 6:
      word += "sixty"
      break
    case 7:
      word += "seventy"
      break
    case 8:
      word += "eighty"
      break
    case 9:
      word += "ninety"
      break
    }
    if (n >= 20) {
      n %= 10
    }

    switch (n) {
    case 0:
      break
    case 1:
      word += "one"
      break
    case 2:
      word += "two"
      break
    case 3:
      word += "three"
      break
    case 4:
      word += "four"
      break
    case 5:
      word += "five"
      break
    case 6:
      word += "six"
      break
    case 7:
      word += "seven"
      break
    case 8:
      word += "eight"
      break
    case 9:
      word += "nine"
      break
    case 10:
      word += "ten"
      break
    case 11:
      word += "eleven"
      break
    case 12:
      word += "twelve"
      break
    case 13:
      word += "thirteen"
      break
    case 14:
      word += "fourteen"
      break
    case 15:
      word += "fifteen"
      break
    case 16:
      word += "sixteen"
      break
    case 17:
      word += "seventeen"
      break
    case 18:
      word += "eighteen"
      break
    case 19:
      word += "nineteen"
      break
    default:
      throw new Exception("Error: Number was too big: " + n)
    }
    return word
  }
}
