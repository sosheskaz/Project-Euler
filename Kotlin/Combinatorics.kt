package Combinatorics

fun <T> combinationsWithReplacement(list: List<T>, count: Int): Sequence<List<T>> {
  if (count < 1) {
    throw Exception("Error: Argument 'count' cannot be less than 1, got: " + count)
  } else if (count == 1) {
    return list.asSequence().map { i -> listOf(i) }
  } else {
    return sequence {
      for ((idx, item) in list.asSequence().withIndex()) {
        for (baseResult in combinationsWithReplacement(list.slice(idx..(list.size - 1)), count - 1)) {
          yield(baseResult + listOf(item))
        }
      }
    }
  }
}
