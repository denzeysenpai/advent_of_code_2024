package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func extractNumbers(expression string) (int, int) {
	re := regexp.MustCompile(`\d+,\d+`)
	match := re.FindString(expression)
	if match == "" {
		return 0, 0
	}
	parts := strings.Split(match, ",")
	first, _ := strconv.Atoi(parts[0])
	second, _ := strconv.Atoi(parts[1])
	return first, second
}

func evaluateLine(line string) int {
	re := regexp.MustCompile(`mul\(\d+,\d+\)`) // Matches expressions like mul(2,3)
	matches := re.FindAllString(line, -1)
	sum := 0

	for _, expr := range matches {
		if len(expr) <= 12 {
			num1, num2 := extractNumbers(expr)
			sum += num1 * num2
		}
	}

	return sum
}

func partOne() int {
	file, err := os.Open("../../input/day3.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	total := 0

	for scanner.Scan() {
		total += evaluateLine(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	return total
}

func partTwo() int {
	file, err := os.Open("../../input/day3.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	dos := []string{}
	for _, line := range lines {
		parts := strings.Split(line, "do()")
		for _, part := range parts {
			doPart := strings.Split(part, "don't()")[0]
			dos = append(dos, doPart)
		}
	}

	result := 0
	for _, line := range dos {
		result += evaluateLine(line)
	}

	return result
}

func main() {
	fmt.Println(partTwo())
}
