package main

import "fmt"

func main() {
	sl := [7]int{1, 6, 4, 2, 8, 4, 6}

	for i, br := range sl {
		if br < i {
			fmt.Printf("%d\n", br)
		}
	}
}
