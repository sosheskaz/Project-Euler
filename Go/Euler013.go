package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	const inputFile = "input/Euler013.txt"
	const digits = 10

	nums := LoadFile(inputFile)

	var sum float64
	for _, num := range *nums {
		sum += num
	}

	exponentAdjustment := int(math.Ceil(math.Log10(sum)) - digits)
	sumAdjustment := math.Pow10(exponentAdjustment)
	firstDigits := int(sum / sumAdjustment)

	fmt.Println(firstDigits)
}

func LoadFile(path string) *[]float64 {
	dat, err := ioutil.ReadFile(path)
	if err != nil {
		log.Fatal(err)
		os.Exit(1)
	}

	contents := string(dat)
	rowStrings := strings.Split(contents, "\n")
	result := make([]float64, len(rowStrings))
	for idx, rowString := range rowStrings {
		result[idx], _ = strconv.ParseFloat(rowString, 64)
	}

	return &result
}
