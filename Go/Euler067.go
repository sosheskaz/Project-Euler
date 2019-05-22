package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	triangle := *LoadFile("input/Euler067.txt")

	for row := len(triangle) - 2; row >= 0; row-- {
		// calculating subtriangles. The bigger option of each "edge" in a subtriangle is the optimal route.
		// we work by modifying each element to be the max of its available paths.
		for col := 0; col < len(triangle[row]); col++ {
			lchild := triangle[row+1][col]
			rchild := triangle[row+1][col+1]

			if lchild > rchild {
				triangle[row][col] += lchild
			} else {
				triangle[row][col] += rchild
			}
		}
	}

	greatest := triangle[0][0]
	fmt.Println(greatest)
}

func LoadFile(path string) *[][]int {
	dat, err := ioutil.ReadFile(path)
	if err != nil {
		log.Fatal(err)
		os.Exit(1)
	}

	var result [][]int

	contents := string(dat)
	rowStrings := strings.Split(contents, "\n")
	for _, rowString := range rowStrings {
		var row []int

		values := strings.Split(rowString, " ")
		for _, value := range values {
			if value == "" {
				continue
			}
			intValue, _ := strconv.Atoi(value)
			row = append(row, intValue)
		}

		// Ignore empty lines
		if len(row) > 0 {
			result = append(result, row)
		}
	}

	return &result
}
