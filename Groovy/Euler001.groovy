#!/usr/bin/env groovy

class Euler001 {
  public static void main(String[] args) {

    int sum = (3..999).by(3).sum()

    sum += (5..999).by(5).findAll { it % 3 != 0 }.sum()

    println sum
  }
}
