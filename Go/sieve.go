package main
import (
	"math"
)

func Sieve(lim int) []int {
	sieve := make([]bool, lim + 1)
	sqrtlim := int(math.Sqrt(float64(lim)))

	for x := 1; x <= sqrtlim; x++ {
		x2 := x * x
		for y:= 1; y <= sqrtlim; y++ {
			y2 := y * y

			n := 4 * x2 + y2
			if n <= lim && (n % 12 == 1 || n % 12 == 5) {
				sieve[n] = !sieve[n]
			}

			n = 3 * x2 + y2
			if n <= lim && n % 12 == 7 {
				sieve[n] = !sieve[n]
			}

			n = 3 * x2 - y2
			if n <= lim && x2 > y2 && n % 12 == 11 {
				sieve[n] = !sieve[n]
			}
		}
	}

	sieve[2], sieve[3] = true, true

	for r := 5; r<= sqrtlim; r += 2 {
		if sieve[r] {
			s := r * r
			for k := s; k <= lim; k += s {
				sieve[k] = false
			}
		}
	}

	var primes []int
	if lim >= 2 {
		primes = append(primes, 2)
	}
	for index, isPrime := range sieve {
		if isPrime {
			primes = append(primes, index)
		}
	}

	return primes
}
