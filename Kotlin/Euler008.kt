package Euler008

import java.io.File
import java.lang.Math

fun main() {
  val factorCt = 13
  var product = 1L

  var buffer = LongArray(factorCt, { 0L })

  var fileContents = File("input/Euler008.txt").readText().asSequence().filter(Character::isDigit).map(Character::getNumericValue).map { i -> i.toLong() }

  fileContents.withIndex().forEach { it ->
    buffer[it.index % factorCt] = it.value
    product = Math.max(product, buffer.reduce { a, b -> a * b })
  }

  println(product)
}
