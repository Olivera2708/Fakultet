package main

import "fmt"

func proveraIf(n int) {
	if n < 0 {
		fmt.Print("Manji\n")
	} else if n > 0 {
		fmt.Print("Veci\n")
	} else {
		fmt.Print("Jednak\n")
	}
}

func proveraCase(n int) {
	switch {
	case n < 0:
		fmt.Print("Manji\n")
	case n > 0:
		fmt.Print("Veci\n")
	case n == 0:
		fmt.Print("Nula\n")
	}
}

func main() {
	proveraIf(5)
	proveraCase(-2)
}
