package main

import "fmt"

func main() {
	var count, winner, total, max, a, b, c, d int
	winner = 1
	count = 1
	max = 0
	for count < 6 {
		total = 0
		_, _ = fmt.Scanf("%d %d %d %d", &a, &b, &c, &d)
		total = a + b + c + d
		if total > max {
			winner = count
			max = total
		}
		count = count + 1
	}
	fmt.Println(winner, max)
}
