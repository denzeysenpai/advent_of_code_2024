package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	fmt.Println("")
}

func importData(filePath string) ([]string, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer file.Close()
	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		return nil, err
	}
	return lines, nil
}

func split() {
	data, err := importData("../../input/day1.txt")
	if err != nil {

	}
	left := []string{}
	right := []string{}
	for i := 0; i < len(data); i++ {
		curr := data[i]
		// row =
		// not finished
	}
}
