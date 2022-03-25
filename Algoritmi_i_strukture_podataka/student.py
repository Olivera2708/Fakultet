class Student(object):
    def __init__(self, ime, prz, ind):
        self._ime = ime
        self._prz = prz
        self._ind = ind
        self._ocene = []
    
    def upisi_ocenu(self, ocena):
        self._ocene.append(ocena)

    def ponisti_ocenu(self, ocena):
        self._ocene.remove(ocena)

    def ispis_ocena(self):
        print("Vase ocene su ", end="")
        for el in self._ocene:
            print(f"{el} ", end="")
        print("")

    def racunanje_ocena(self):
        prosek = 0
        for el in self._ocene:
            prosek += el
        prosek /= len(self._ocene)
        print(f"Vas prosek je {prosek}")


if __name__ == "__main__":
    Student1 = Student("Pera", "Peric", "SV46/2021")
    Student1.upisi_ocenu(9)
    Student1.upisi_ocenu(7)
    Student1.ispis_ocena()
    Student1.racunanje_ocena()
