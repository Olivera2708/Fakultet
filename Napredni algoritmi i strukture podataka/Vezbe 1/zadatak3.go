package main

import (
	"fmt"
)

func prosti(n int) (int, error) {
	if n <= 1 {
		return 0, fmt.Errorf("Prosledjen broj manji ili jednak sa 1")
	}
	var brojac int = 0
	var prost int = 1
	var jelProst bool = true

	for brojac < n {
		prost++
		jelProst = true

		for i := 2; i <= int(prost/2); i++ {
			if prost%i == 0 {
				jelProst = false
				break
			}
		}
		if jelProst {
			brojac++
		}
	}
	return prost, nil
}

func main() {
	var x int
	var e error
	x, e = prosti(5)
	if e == nil {
		fmt.Printf("%d\n", x)
	} else {
		print(e)
	}
}
