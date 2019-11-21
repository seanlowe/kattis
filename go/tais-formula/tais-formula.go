package main

import "fmt"

func main() {
	var oldt, t, oldv, v, ans float64
	var count, i int
	i = 0
	oldv, oldt, ans = 0.0, 0.0, 0.0
	fmt.Scan(&count)
	for i < count {
		_, _ = fmt.Scanf("%f %f", &t, &v)
		if i >= 1 {
			ans = ans + ((oldv+v)/float64(2))*((t-oldt)/float64(1000))
		}
		oldv = v
		oldt = t
		i = i + 1
	}
	fmt.Println("%f\n", ans)
}
