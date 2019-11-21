package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	str, _ := reader.ReadString('\n')
	str = str[:len(str)-1]
	arr := strings.Split(str, " ")
	r1, _ := strconv.Atoi(arr[0])
	s1, _ := strconv.Atoi(arr[1])
	fmt.Println((s1 * 2) - r1)
}
