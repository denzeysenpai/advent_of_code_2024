package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func CheckDifference(bigger, smaller int) bool {
	dif := bigger - smaller
	return dif > 0 && dif <= 3
}

func partOne() ([][]int, int) {
	file, err := os.Open("../../input/day2.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var unsafeRows [][]int
	safeCount := 0

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		rowR := strings.Fields(scanner.Text())
		var rowS []int
		for _, val := range rowR {
			num, _ := strconv.Atoi(val)
			rowS = append(rowS, num)
		}

		isIncreasing := rowS[0] <= rowS[len(rowS)-1]
		isValid := true

		for i := 0; i < len(rowS)-1; i++ {
			curr := rowS[i]
			next := rowS[i+1]
			if !isIncreasing {
				curr = rowS[len(rowS)-1-i]
				next = rowS[len(rowS)-2-i]
			}

			if !CheckDifference(curr, next) {
				isValid = false
				unsafeRows = append(unsafeRows, rowS)
				break
			}
		}

		if isValid {
			safeCount++
		}
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	return unsafeRows, safeCount
}

func partTwo() int {
	unsafeRows, safeCount := partOne()

	for _, row := range unsafeRows {
		for i := range row {
			var newRow []int
			newRow = append(newRow, row[:i]...)
			newRow = append(newRow, row[i+1:]...)

			dampener := 1
			for j := 0; j < len(newRow)-1; j++ {
				if !CheckDifference(newRow[j], newRow[j+1]) {
					dampener--
				}
				if dampener < 0 {
					break
				}
			}

			if dampener >= 0 {
				safeCount--
			}
		}
	}

	return safeCount
}

func main() {
	fmt.Println(partTwo())
}
