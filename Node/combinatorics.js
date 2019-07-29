function* combinationsWithReplacement(arr, count) {
  if (count < 1) {
    throw "Error: Argument 'count' cannot be less than 1, got: " + count;
  }
  else if (count % 1 != 0) {
    throw "Error: Argument 'count' must be an integer, got: " + count;
  } else if (count == 1) {
    for (let item of arr) {
      yield [item];
    }
  } else {
    for (let i = 0; i < arr.length; i++) {
      for (let baseResult of combinationsWithReplacement(arr.slice(i), count-1)) {
        baseResult.push(arr[i]);
        yield baseResult;
      }
    }
  }
}

exports.combinationsWithReplacement = combinationsWithReplacement;
