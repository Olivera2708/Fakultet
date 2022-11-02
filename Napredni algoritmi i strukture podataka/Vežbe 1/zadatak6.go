package main

import (
	"fmt"
	"math"
)

func armstrongov(n int) bool {
	var broj int = 0
	var jos int = n
	var cifara int = 0

	for jos > 0 {
		jos = int(jos / 10)
		cifara++
	}

	jos = n

	for jos != 0 {
		var br int = jos % 10
		jos = int(jos / 10)

		broj += int(math.Pow(float64(br), float64(cifara)))
	}

	return broj == n
}

func main() {
	var b bool = armstrongov(153)
	fmt.Print(b)
}
