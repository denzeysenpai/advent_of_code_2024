package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func splitData() ([]int, []int) {
	file, err := os.Open("../../input/day1.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var left []int
	var right []int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		row := strings.Replace(scanner.Text(), "\n", "", -1)
		parts := strings.Split(row, "   ")
		if len(parts) == 2 {
			leftVal, _ := strconv.Atoi(parts[0])
			rightVal, _ := strconv.Atoi(parts[1])
			left = append(left, leftVal)
			right = append(right, rightVal)
		}
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	return left, right
}

func partOne() int {
	left, right := splitData()

	// Sort slices
	sort.Ints(left)
	sort.Ints(right)

	total := 0
	for i := range left {
		diff := abs(left[i] - right[i])
		total += diff
	}
	return total
}

func partTwo() int {
	left, right := splitData()
	total := 0

	for _, val := range left {
		count := countOccurrences(right, val)
		total += val * count
	}

	return total
}

func countOccurrences(arr []int, target int) int {
	count := 0
	for _, v := range arr {
		if v == target {
			count++
		}
	}
	return count
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	fmt.Println(partTwo())
}
