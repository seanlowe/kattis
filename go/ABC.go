package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	var arr, cop [3]int
	var order string
	reader := bufio.NewReader(os.Stdin)
	fmt.Scanf("%d %d %d", &arr[0], &arr[1], &arr[2])
	sort.Ints(arr[:])
	cop = arr
	order, _ = reader.ReadString('\n')
	order = order[:len(order)-1]
	i := 0
	for i < 3 {
		if order[i] == 'A' {
			cop[i] = arr[0]
		} else if order[i] == 'B' {
			cop[i] = arr[1]
		} else if order[i] == 'C' {
			cop[i] = arr[2]
		}
		i = i + 1
	}
	fmt.Printf("%d %d %d\n", cop[0], cop[1], cop[2])
}
