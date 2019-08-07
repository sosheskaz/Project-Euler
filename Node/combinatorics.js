function* combinationsWithReplacement(arr, r) {
  // if (count < 1) {
  //   throw "Error: Argument 'count' cannot be less than 1, got: " + count;
  // }
  // else if (count % 1 != 0) {
  //   throw "Error: Argument 'count' must be an integer, got: " + count;
  // } else if (count == 1) {
  //   for (let item of arr) {
  //     yield [item];
  //   }
  // } else {
  //   for (let i = 0; i < arr.length; i++) {
  //     for (let baseResult of combinationsWithReplacement(arr.slice(i), count-1)) {
  //       baseResult.push(arr[i]);
  //       yield baseResult;
  //     }
  //   }
  // }

  if (r < 0) return

  const pool = Array.from(arr);
  const n = pool.length;

  var indices = Array(r).fill(0);
  var current = indices.map((index) => pool[index]);
  var i, j;

  yield current;

  while (true) {
    for (i = r - 1; i >= 0 && indices[i] == n - 1; i--);

    if (i < 0) break;

    indices[i]++;

    indices.fill(indices[i], i);
    current = indices.map((index) => pool[index]);
    yield current;
  }
}
exports.combinationsWithReplacement = combinationsWithReplacement;
