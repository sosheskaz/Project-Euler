package Euler018

import java.io.File

fun main() {
  val triangle = loadFile("input/Euler018.txt")

  for (row in triangle.size - 2 downTo 0) {
    for (col in 0..(triangle[row].size - 1)) {
      val lchild = triangle[row + 1][col]
      val rchild = triangle[row + 1][col + 1]

      if (lchild > rchild) {
        triangle[row][col] += lchild
      } else {
        triangle[row][col] += rchild
      }
    }
  }

  println(triangle[0][0])
}

fun loadFile(path: String): MutableList<MutableList<Int>> {
  val table: MutableList<MutableList<Int>> = mutableListOf()

  File(path).forEachLine { line ->
    table.add(line.split(" ").asSequence().filter { numStr -> numStr != "" }.map { numStr -> numStr.toInt() }.toMutableList())
  }

  return table
}
