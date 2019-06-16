import java.lang.Math

fun main(args: Array<String>) {
    val target = 10000

    println(properDivisorsSum(220))
}

fun properDivisorsSum(n: Int): Int {
    var sum: Int = 1
    var lim: Int = Math.ceil(Math.sqrt(n as Double)) as Int

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
