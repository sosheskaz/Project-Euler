package main

import (
	"fmt"
	"log"
)

func main() {
	const target = 1000
	sum := 0

	for i := 1; i <= target; i++ {
		sum += len(wordForNumber(i))
	}
	fmt.Println(sum)
}

func wordForNumber(n int) string {
	var word string
	if n >= 1000000 {
		log.Fatal("Error: Number was too big: ", n)
	}
	if n >= 1000 {
		word += wordForNumber(n/1000) + "thousand"
		n %= 1000
	}
	if n >= 100 {
		word += wordForNumber(n/100) + "hundred"
		n %= 100
		if n != 0 {
			word += "and"
		}
	}

	switch n / 10 {
	case 2:
		word += "twenty"
	case 3:
		word += "thirty"
	case 4:
		word += "forty"
	case 5:
		word += "fifty"
	case 6:
		word += "sixty"
	case 7:
		word += "seventy"
	case 8:
		word += "eighty"
	case 9:
		word += "ninety"
	}
	if n >= 20 {
		n %= 10
	}

	switch n {
	case 0:
	case 1:
		word += "one"
	case 2:
		word += "two"
	case 3:
		word += "three"
	case 4:
		word += "four"
	case 5:
		word += "five"
	case 6:
		word += "six"
	case 7:
		word += "seven"
	case 8:
		word += "eight"
	case 9:
		word += "nine"
	case 10:
		word += "ten"
	case 11:
		word += "eleven"
	case 12:
		word += "twelve"
	case 13:
		word += "thirteen"
	case 14:
		word += "fourteen"
	case 15:
		word += "fifteen"
	case 16:
		word += "sixteen"
	case 17:
		word += "seventeen"
	case 18:
		word += "eighteen"
	case 19:
		word += "nineteen"
	default:
		log.Fatal("Error: Number was too big: ", n)
	}
	return word
}
