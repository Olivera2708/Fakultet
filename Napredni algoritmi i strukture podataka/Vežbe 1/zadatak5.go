package main

import "fmt"

type Student struct {
	ime     string
	prezime string
	indeks  string
}

func (s *Student) izmaneIndeksa(novi string) {
	s.indeks = novi
}

func main() {
	var ja Student
	ja.ime = "Olivera"
	ja.prezime = "Radovanovic"
	ja.indeks = "SV46/2021"

	fmt.Print(ja)

	ja.izmaneIndeksa("sv46/2021")

	fmt.Print(ja)
}
