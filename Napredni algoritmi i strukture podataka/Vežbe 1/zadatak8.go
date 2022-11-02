package main

import "fmt"

type Node struct {
	vrednost int
	sledeci  *Node
}

type LinkedList struct {
	duzina  int
	sledeci *Node
}

func (list *LinkedList) dodajElement(i int, n int) error {
	var br int = 1

	if i >= list.duzina {
		return fmt.Errorf("Indeks prevelik")
	}

	var novi Node
	novi.vrednost = n

	var trenutni *Node = list.sledeci
	for br != i {
		trenutni = trenutni.sledeci
		br++
	}

	novi.sledeci = trenutni.sledeci
	trenutni.sledeci = &novi
	list.duzina++

	return nil
}

func (list *LinkedList) obrisiElement(i int) error {
	var br int = 1

	if i >= list.duzina {
		return fmt.Errorf("Indeks prevelik")
	}

	var trenutni *Node = list.sledeci
	for br != i {
		trenutni = trenutni.sledeci
		br++
	}

	trenutni.sledeci = trenutni.sledeci.sledeci
	list.duzina--

	return nil
}

func (list *LinkedList) postojiElement(n int) bool {
	var novi Node
	novi.vrednost = n

	var trenutni *Node = list.sledeci
	for trenutni != nil {
		if trenutni.vrednost == n {
			return true
		}
		trenutni = trenutni.sledeci
	}
	return false
}

func (list *LinkedList) ispis() {
	var trenutni *Node = list.sledeci
	for trenutni != nil {
		fmt.Print(trenutni.vrednost)
		fmt.Print("\n")

		trenutni = trenutni.sledeci
	}
}

func main() {
	var list LinkedList
	list.duzina = 3

	var el1 Node
	el1.vrednost = 125

	list.sledeci = &el1

	var el2 Node
	el2.vrednost = 154

	el1.sledeci = &el2

	var el3 Node
	el3.vrednost = 142

	el2.sledeci = &el3

	list.ispis()
	fmt.Print("\n")

	var e error = list.dodajElement(1, 100)
	if e == nil {
		list.ispis()
		fmt.Print("\n")
	} else {
		fmt.Print(e)
		fmt.Print("\n")
	}

	e = list.obrisiElement(3)
	if e == nil {
		list.ispis()
		fmt.Print("\n")
	} else {
		fmt.Print(e)
		fmt.Print("\n")
	}

	fmt.Print(list.postojiElement(125))
}
