package Euler011

import java.io.File

fun main() {
  val target = 4
  val table = loadFile("input/Euler011.txt")
  println(maxProduct(table, target))
}

fun loadFile(path: String): List<List<Int>> {
  val table: MutableList<List<Int>> = mutableListOf()

  File(path).forEachLine { line ->
    table.add(line.split(" ").asSequence().filter { numStr -> numStr != "" }.map { numStr -> numStr.toInt() }.toList())
  }

  return table
}

fun maxProduct(table: List<List<Int>>, length: Int): Int {
  var biggest = -1
  for (i in 0..(table.size - 1)) {
    for (j in (length - 1)..(table[i].size - 1)) {
      val horizProduct = table[i].slice((j-length+1)..j).reduce { a, b -> a * b }
      val vertProduct = table.slice((j-length+1)..j).map { row -> row[i] }.reduce { a, b -> a * b }

      var diagWest = -1
      var diagEast = -1
      if (i >= length) {
        diagWest = (0..(length-1)).map { cursor -> table[i - cursor][j - cursor] }.reduce { a, b -> a * b }
        if (table[i].size > j + 4) {
          diagEast = (0..(length-1)).map { cursor -> table[i - cursor][j + cursor] }.reduce { a, b -> a * b }
        }
      }

      biggest = sequenceOf(biggest, horizProduct, vertProduct, diagEast, diagWest).max() as Int
    }
  }

  return biggest
}
