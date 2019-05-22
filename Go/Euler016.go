package main

import (
	"fmt"
	"math"
	"math/big"
)

func main() {
	// exponent of two to target
	const target = 1000
	const bits = 8

	zeroByteCount := target / bits
	bytes := make([]byte, zeroByteCount+1)

	headBytePow := float64(target % bits)
	headByte := byte(math.Pow(2, headBytePow))
	bytes[0] = headByte

	var asInt big.Int
	asInt.SetBytes(bytes)

	var sum uint64
	big10 := big.NewInt(10)

	mod := big.NewInt(0)
	cursor := &asInt
	for len(cursor.Bytes()) > 0 {
		cursor.DivMod(cursor, big10, mod)
		sum += mod.Uint64()
	}

	fmt.Println(sum)
}
