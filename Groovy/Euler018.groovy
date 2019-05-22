#!/usr/bin/env groovy

class Euler018 {
  public static void main(String[] args) {
    List<List<Integer>> triangle = loadFile('input/Euler018.txt')

    for (int row = triangle.size() - 2; row >= 0; row--) {
      for (int col = 0; col < triangle[row].size(); col++) {
        int lchild = triangle[row+1][col]
        int rchild = triangle[row+1][col+1]

        if (lchild > rchild) {
          triangle[row][col] += lchild
        } else {
          triangle[row][col] += rchild
        }
      }
    }

    println triangle[0][0]
  }

  private static List<List<Integer>> loadFile(path) {
    String raw = new File(path).text
    List<List<Integer>> result = raw.split('\n')
      .collect { it.split(' ').findAll { it }.collect { Integer.parseInt(it) } }
      .findAll { it }
    return result
  }
}
