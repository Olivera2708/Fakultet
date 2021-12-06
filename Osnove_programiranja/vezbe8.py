from tabulate import tabulate

def ufajl(knjiga, fajl):
    string = ""
    with open(fajl, "a") as fajl:
        for el in knjiga[1].keys():
            string += f"{el},"
        header = string[:-1]
        fajl.write(f"{header}\n")
        for el in knjiga:
            string = ""
            for value in el.values():
                string += f"{value},"
            string = string[:-1]
            fajl.write(f"{string}\n")

def izfajla(fajl):
    with open(fajl) as fajl:
        linijefajla = fajl.readlines()
        header = linijefajla[0].split(",")
        header = [el.replace("\n", "") for el in header]
        knjige = []
        for i in range(len(linijefajla)):
            recnik = {}
            if i == 0:
                continue
            for j in range(len(header)):
                pomoc = [el.replace("\n", "") for el in linijefajla[i].split(",")]
                recnik[header[j]] = pomoc[j]
            knjige.append(recnik)
    return knjige

def dodaj(knjige):
    recnik = {}
    recnik["id"] = input("Id -> ")
    recnik["naslov"] = input("Naslov -> ")
    recnik["autori"] = input("Autori -> ")
    recnik["izdavac"] = input("Izdavac -> ")
    recnik["cena"] = input("Cena -> ") 
    recnik["kolicina"] = input("Kolicina -> ")
    recnik["godina"] = input("Godina -> ")
    knjige.append(recnik)

def pregled(knjiga):
    tabela = []
    hearders = []
    for el in knjiga[1].keys():
        hearders.append(el)
    for el in knjiga:
        tabel = []
        for value in el.values():
            tabel.append(value)
        tabela.append(tabel)
    print(tabulate(tabela, headers=hearders))

knjige = [{
    "id": 1,
    "naslov": "bitak i vreme",
    "autori": "martin hajdeger",
    "izdavac": "sluzbeni glasnik",
    "cena": 1500,
    "kolicina": 5,
    "godina": 2008
},
{   
    "id": 1,
    "naslov": "pojam strepnje",
    "autori": "soren abi kjerkegor",
    "izdavac": "plato",
    "cena": 800,
    "kolicina": 10,
    "godina": 2003
}]

print(izfajla("listarecnika.txt"))