package main

import "fmt"

func main() {
	var jon, doc string
	fmt.Scanf("%s", &jon)
	fmt.Scanf("%s", &doc)
	jon = jon[:len(jon)-1]
	doc = doc[:len(doc)-1]
	if len(doc) <= len(jon) {
		fmt.Println("go")
	} else {
		fmt.Println("no")
	}
}
