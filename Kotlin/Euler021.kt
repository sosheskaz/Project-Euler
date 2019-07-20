import java.lang.Math

fun main(args: Array<String>) {
    val target = 10000
    var properDivisorsSums: MutableMap<Int, Int> = mutableMapOf()
    var amicableSum = 0

    for (i in 1..(target-1)) {
        var divisorsSum = properDivisorsSums[i]
        if (divisorsSum == properDivisorsSums[i]) {
            divisorsSum = getProperDivisorsSum(i)
            properDivisorsSums[i] = divisorsSum
        }

        var otherDivisorsSum = properDivisorsSums[divisorsSum]
        if (otherDivisorsSum == null) {
            otherDivisorsSum = getProperDivisorsSum(divisorsSum as Int)
            properDivisorsSums[divisorsSum] = otherDivisorsSum
        }

        if (otherDivisorsSum == i && i != divisorsSum) {
            amicableSum += i
        }
    }

    println(amicableSum)
}

fun getProperDivisorsSum(n: Int): Int {
    var sum: Int = 1
    var lim: Int = Math.ceil(Math.sqrt(n.toDouble())).toInt()

    for (i: Int in 2..lim) {
        if (n % i == 0) {
            sum += i

            if (n != lim) {
                sum += n / i
            }
        }
    }

    return sum
}
