package Euler013

import java.io.File
import java.lang.Math

fun main() {
  val inFile = "input/Euler013.txt"
  val digits = 10

  val sum = loadFile(inFile).sum()
  val exponentAdjustment = Math.ceil(Math.log10(sum)) - digits
  val sumAdjustment = Math.pow(10.0, exponentAdjustment)
  val firstDigits = (sum / sumAdjustment).toLong()
  println(firstDigits)
}

fun loadFile(path: String): List<Double> {
  var lines: MutableList<Double> = mutableListOf()

  File(path).forEachLine { line -> lines.add(line.toDouble()) }

  return lines
}
