package Combinatorics

fun <T> combinationsWithReplacement(pool: List<T>, r: Int): Sequence<List<T>> {
  val n = pool.size
  var indices = IntArray(r)
  indices.fill(0)

  return sequence<List<T>> {
    var current = indices.map { pool[it] }
    var i: Int

    yield(current)

    while (true) {
      i = r - 1 - (r - 1 downTo 0).takeWhile { indices[it] == n - 1 }.size

      if (0 > i) break

      indices[i]++

      indices.fill(indices[i], i)
      current = indices.map { pool[it] }
      yield(current)
    }
  }
}
