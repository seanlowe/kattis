package main

import (
	"bufio"
	"fmt"
	"os"
)

func switch12(pos int) int {
	if pos == 1 {
		return 2
	}
	return 1
}

func switch13(pos int) int {
	if pos == 1 {
		return 3
	}
	return 1
}

func switch23(pos int) int {
	if pos == 2 {
		return 3
	}
	return 2
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	pos := 1
	for x := 0; x < len(input); x++ {
		switch input[x] {
		case 'A':
			if pos == 1 || pos == 2 {
				pos = switch12(pos)
			}
		case 'B':
			if pos == 2 || pos == 3 {
				pos = switch23(pos)
			}
		case 'C':
			if pos == 1 || pos == 3 {
				pos = switch13(pos)
			}
		}
	}
	fmt.Println(pos)
}
