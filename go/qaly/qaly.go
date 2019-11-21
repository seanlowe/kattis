package main

import "fmt"

func main() {
	var count int
	var per, time, qaly float32
	qaly = 0
	fmt.Scan(&count)
	for count > 0 {
		_, _ = fmt.Scanf("%f %f", &per, &time)
		qaly = qaly + (per * time)
		count = count - 1
	}
	fmt.Println("%.3f", qaly)
}
