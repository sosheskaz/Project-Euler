package main

import (
	"reflect"
	"testing"
)

type CombinationsTestSuite struct {
	r        int
	source   []int
	expected [][]int
}

func TestGetCombinations5C0(t *testing.T) {
	src := []int{1, 2, 3, 4, 5}
	expected := [][]int{}
	suite := CombinationsTestSuite{
		r:        0,
		source:   src,
		expected: expected,
	}
	runCombinationsSuite(t, suite)
}

func TestGetCombinationsReplacement5C0(t *testing.T) {
	src := []int{1, 2, 3, 4, 5}
	expected := [][]int{}
	suite := CombinationsTestSuite{
		r:        0,
		source:   src,
		expected: expected,
	}
	runCombinationsReplacementSuite(t, suite)
}

func TestGetCombinations5C1(t *testing.T) {
	src := []int{1, 2, 3, 4, 5}
	expected := [][]int{
		[]int{1},
		[]int{2},
		[]int{3},
		[]int{4},
		[]int{5},
	}
	suite := CombinationsTestSuite{
		r:        1,
		source:   src,
		expected: expected,
	}
	runCombinationsSuite(t, suite)
}

func TestGetCombinationsReplacement5C1(t *testing.T) {
	src := []int{1, 2, 3, 4, 5}
	expected := [][]int{
		[]int{1},
		[]int{2},
		[]int{3},
		[]int{4},
		[]int{5},
	}
	suite := CombinationsTestSuite{
		r:        1,
		source:   src,
		expected: expected,
	}
	runCombinationsReplacementSuite(t, suite)
}

func TestGetCombinations5C2(t *testing.T) {
	src := []int{1, 2, 3, 4, 5}
	expected := [][]int{
		[]int{1, 2},
		[]int{1, 3},
		[]int{1, 4},
		[]int{1, 5},
		[]int{2, 3},
		[]int{2, 4},
		[]int{2, 5},
		[]int{3, 4},
		[]int{3, 5},
		[]int{4, 5},
	}
	suite := CombinationsTestSuite{
		r:        2,
		source:   src,
		expected: expected,
	}
	runCombinationsSuite(t, suite)
}

func TestGetCombinationsReplacement5C2(t *testing.T) {
	src := []int{1, 2, 3, 4, 5}
	expected := [][]int{
		[]int{1, 1},
		[]int{1, 2},
		[]int{1, 3},
		[]int{1, 4},
		[]int{1, 5},
		[]int{2, 2},
		[]int{2, 3},
		[]int{2, 4},
		[]int{2, 5},
		[]int{3, 3},
		[]int{3, 4},
		[]int{3, 5},
		[]int{4, 4},
		[]int{4, 5},
		[]int{5, 5},
	}
	suite := CombinationsTestSuite{
		r:        2,
		source:   src,
		expected: expected,
	}
	runCombinationsReplacementSuite(t, suite)
}

func TestGetCombinations5C3(t *testing.T) {
	src := []int{1, 2, 3, 4, 5}
	expected := [][]int{
		[]int{1, 2, 3},
		[]int{1, 2, 4},
		[]int{1, 2, 5},
		[]int{1, 3, 4},
		[]int{1, 3, 5},
		[]int{1, 4, 5},
		[]int{2, 3, 4},
		[]int{2, 3, 5},
		[]int{2, 4, 5},
		[]int{3, 4, 5},
	}
	suite := CombinationsTestSuite{
		r:        3,
		source:   src,
		expected: expected,
	}
	runCombinationsSuite(t, suite)
}

func TestGetCombinationsReplacement5C3(t *testing.T) {
	src := []int{1, 2, 3, 4, 5}
	expected := [][]int{
		[]int{1, 1, 1},
		[]int{1, 1, 2},
		[]int{1, 1, 3},
		[]int{1, 1, 4},
		[]int{1, 1, 5},
		[]int{1, 2, 2},
		[]int{1, 2, 3},
		[]int{1, 2, 4},
		[]int{1, 2, 5},
		[]int{1, 3, 3},
		[]int{1, 3, 4},
		[]int{1, 3, 5},
		[]int{1, 4, 4},
		[]int{1, 4, 5},
		[]int{1, 5, 5},
		[]int{2, 2, 2},
		[]int{2, 2, 3},
		[]int{2, 2, 4},
		[]int{2, 2, 5},
		[]int{2, 3, 3},
		[]int{2, 3, 4},
		[]int{2, 3, 5},
		[]int{2, 4, 4},
		[]int{2, 4, 5},
		[]int{2, 5, 5},
		[]int{3, 3, 3},
		[]int{3, 3, 4},
		[]int{3, 3, 5},
		[]int{3, 4, 4},
		[]int{3, 4, 5},
		[]int{3, 5, 5},
		[]int{4, 4, 4},
		[]int{4, 4, 5},
		[]int{4, 5, 5},
		[]int{5, 5, 5},
	}
	suite := CombinationsTestSuite{
		r:        3,
		source:   src,
		expected: expected,
	}
	runCombinationsReplacementSuite(t, suite)
}

func TestGetCombinations5C4(t *testing.T) {
	src := []int{1, 2, 3, 4, 5}
	expected := [][]int{
		[]int{1, 2, 3, 4},
		[]int{1, 2, 3, 5},
		[]int{1, 2, 4, 5},
		[]int{1, 3, 4, 5},
		[]int{2, 3, 4, 5},
	}
	suite := CombinationsTestSuite{
		r:        4,
		source:   src,
		expected: expected,
	}
	runCombinationsSuite(t, suite)
}

func TestGetCombinations5C5(t *testing.T) {
	src := []int{1, 2, 3, 4, 5}
	expected := [][]int{
		[]int{1, 2, 3, 4, 5},
	}
	suite := CombinationsTestSuite{
		r:        5,
		source:   src,
		expected: expected,
	}
	runCombinationsSuite(t, suite)
}

func runCombinationsReplacementSuite(t *testing.T, suite CombinationsTestSuite) {
	src := suite.source
	r := suite.r

	combos, err := GetCombinationsWithReplacement(src, r)
	if err != nil {
		t.Fatal(err)
	}

	combinationsAssertions(t, suite, combos)
}

func runCombinationsSuite(t *testing.T, suite CombinationsTestSuite) {
	src := suite.source
	r := suite.r

	combos, err := GetCombinations(src, r)
	if err != nil {
		t.Fatal(err)
	}

	combinationsAssertions(t, suite, combos)
}

func combinationsAssertions(t *testing.T, suite CombinationsTestSuite, actual <-chan []int) {
	expected := suite.expected
	actualArr := [][]int{}

	idx := 0
	for combo := range actual {
		actualArr = append(actualArr, combo)
		if idx >= len(expected) {
			continue
		}
		if !reflect.DeepEqual(combo, expected[idx]) {
			t.Logf("Expected %+v at combination %d, got %+v", expected[idx], idx+1, combo)
			t.Fail()
		}
		idx++
	}

	if idx != len(expected) {
		t.Logf("Expected %d combinations, got %d", len(expected), idx)
		t.Fail()
	}

	if t.Failed() {
		t.Logf("Expected: %+v", expected)
		t.Logf("Got:      %+v", actualArr)
	}
}
