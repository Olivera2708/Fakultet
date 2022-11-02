package main

import (
	"fmt"
	"reflect"
)

func provera(word string, candidates [4]string) {
	var slova = make(map[byte]int)

	for i := 0; i < len(word); i++ {
		if _, ok := slova[word[i]]; ok {
			slova[word[i]] = 1
		} else {
			slova[word[i]]++
		}
	}

	for _, val := range candidates {
		var s = make(map[byte]int)

		for i := 0; i < len(word); i++ {
			if _, ok := s[val[i]]; ok {
				// fmt.Print(val[i])
				s[val[i]]++
			} else {
				s[val[i]] = 1
			}
		}

		if reflect.DeepEqual(s, slova) {
			fmt.Print(val + "\n")
		}
	}
}

func main() {
	var word string = "listen"
	candidates := [4]string{"enlist", "google", "inlets", "banana"}

	provera(word, candidates)

}
