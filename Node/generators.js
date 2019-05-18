
function* map(iter, fn) {
  for (let x of iter) {
    yield fn(x)
  }
}

function* filter(iter, fn) {
  for (let x of iter) {
    if (fn(x)) {
      yield x
    }
  }
}
exports.filter = filter

exports.map = map

function reduce (iter, start, fn) {
  var result = start
  for (let x of iter) {
    result = fn(result, x)
  }
  return result
}
exports.reduce = reduce

function* takeWhile (iter, fn) {
  for (let x of iter) {
    if (fn(x))
      yield x;
    else
      break;
  }
}
exports.takeWhile = takeWhile
