#!/usr/bin/env groovy

class Euler004 {
  public static void main(String[] args) {
    int biggest = -1
    for (int a in 100..999) {
      for (int b in (a+1)..999) {
        int product = a * b
        if (product > biggest && isPalindrome(product)) {
          biggest = product
        }
      }
    }
    println biggest
  }

  private static boolean isPalindrome(number) {
    String asString = number.toString()
    return asString == asString.reverse()
  }
}
