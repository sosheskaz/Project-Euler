function* combinationsWithReplacement(arr, r) {
  if (r < 0) return;

  const pool = Array.from(arr);
  const n = pool.length;

  var indices = Array(r).fill(0);
  var current = indices.map((index) => pool[index]);
  var i;

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

function* permutations(arr, r) {
  const pool = Array.from(arr);
  const n = pool.length;
  if (r === undefined) r = n;
  if (r < 0 || r > n) return;

  var indices = Array(r).fill(0).map((_, index) => index);
  var cycles = indices.map((idx) => n - idx);
  yield indices.map((index) => pool[index]);;
  var i, j;

  while (true) {
    for (let i = r - 1; i >= 0; i--) {
      cycles[i] -= 1
      if (cycles[i] == 0) {
        let tmp = indices[i]
        indices[i] = indices[indices.length - 1]
        indices[indices.length - 1] = tmp
        cycles[i] = n - i
      } else {
        j = cycles[i]
        indices[i], indices[-j] = indices[-j], indices[i]
        yield indices.map((index) => pool[index]);
        break
      }
    }

    if (i < 0) break;

    indices[i]++;

    indices.fill(indices[i], i);
    current = indices.map((index) => pool[index]);
    yield current;
  }
}
