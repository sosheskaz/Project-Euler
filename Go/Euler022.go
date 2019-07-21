package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"sort"
	"strings"
	"unicode"
)

func main() {
	names, err := readFile("input/names.txt")
	if err != nil {
		fmt.Println(err.Error())
		os.Exit(1)
	}

	sort.Strings(names)

	var score int
	for idx, name := range names {
		score += (idx + 1) * scoreName(name)
	}

	fmt.Println(score)
}

func readFile(path string) ([]string, error) {
	raw, err := ioutil.ReadFile(path)
	if err != nil {
		return nil, fmt.Errorf("Error when opening file %s: %+v", path, err)
	}

	// We add logic to ignore quotes in scoreLetter.
	strs := strings.Split(string(raw), ",")

	return strs, nil
}

func scoreName(name string) int {
	runes := []rune(strings.ToLower(name))
	score := 0

	for _, r := range runes {
		if !unicode.IsLetter(r) {
			continue
		}
		score += scoreRune(r)
	}

	return score
}

// Assumes lowercase
func scoreRune(r rune) int {
	return int(r - 'a' + 1)
}
