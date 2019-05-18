#!/usr/bin/env groovy

class Euler011 {
  public static void main(String[] args) {
    final int target = 4
    List<List<Integer>> table = loadFile('input/Euler011.txt')
    println maxProduct(table, target)
  }

  private static List<List<Integer>> loadFile(path) {
    String raw = new File(path).text
    List<List<Integer>> result = raw.split('\n')
      .collect { it.split(' ').findAll { it }.collect { Integer.parseInt(it) } }
      .findAll { it }
    return result
  }

  private static Integer maxProduct(List<List<Integer>> table, int length) {
    int biggest = -1

    for (i in (0..(table.size()-1))) {
      for (j in (length-1)..(table[i].size()-1)) {
        // println "horz ${table[i][((j-length+1)..(j))]}"
        int horizProduct = table[i][((j-length+1)..(j))].inject { a, b -> a * b }

        // println "vert ${table[((j-length+1)..(j))].collect { it[i] }}"
        int vertProduct = table[((j-length+1)..(j))].collect { it[i] }.inject { a, b -> a * b }

        int diagWest = -1
        int diagEast = -1
        // println "dwst ${(0..(length-1)).collect { table[i - it][j - it] }}"
        if (i >= length) {
          diagWest = (0..(length-1)).collect { table[i - it][j - it] }.inject { a, b -> a * b }
          if (table[i].size() > j + 4) {
            // println "dest ${(0..(length-1)).collect { table[i - it][j - it] }}"
            diagEast = (0..(length-1)).collect { table[i - it][j + it] }.inject { a, b -> a * b }
          }
        }
        biggest = [biggest, horizProduct, vertProduct, diagEast, diagWest].max()
      }
    }

    return biggest
  }
}
