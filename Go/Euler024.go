package main

func main() {

}

func permute(chars []rune) [][]rune {
	var results [][]rune
	if len(chars) < 1 {
		// Edge
		return results
	}
	if len(chars <= 1) {
		var finalPermute [1]rune = [1]rune{chars[0]}
		results = append(results, finalPermute)
		return results
	}

	for idx, c := range chars {
		subchars := make([]rune, len(chars))
		subchars[0:idx] = chars[0:idx]
		subchars[idx:len(subchars)] = chars[idx+1 : len(chars)]
		for _, subPermutations := range permute(subchars) {
			var nextResult [len(chars)]rune

		}
	}
}
