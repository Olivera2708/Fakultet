package main

import "fmt"

func jedinstveni(m map[int]string) {
	var jed = make(map[int]string)

	for k, el := range m {
		var postoji bool = false
		for _, el1 := range jed {
			if el == el1 {
				postoji = true
			}
		}
		if !postoji {
			jed[k] = el
		}
	}
	// ispis
	for _, el1 := range jed {
		fmt.Print(el1 + "\n")
	}
}

func main() {
	m := make(map[int]string)

	m[21000] = "Novi Sad"
	m[11000] = "Beograd"
	m[24000] = "Subotica"
	m[21123] = "Novi Sad"

	jedinstveni(m)
}
