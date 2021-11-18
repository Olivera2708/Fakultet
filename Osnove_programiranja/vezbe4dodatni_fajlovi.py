#zadtak1a
ime = input("Unesite ime -> ")
br = 0
with open("names.txt") as names:
    for linija in names:
        lista = linija.split(" ")
        for el in lista:
            if el == ime:
                br += 1
print(f"Broj pojavljivanja {ime} u fajlu je {br}")

#zadatak1b
with open("names.txt") as names:
    lista = []
    ucitaj = names.readlines()
    for linija in ucitaj:
        lista += linija.replace("\n", "").split(" ")
    lista.sort()
    trenutni = lista[0]
    maxi = lista[0]
    broj = 0
    maxi_br = 0
    for rec in lista:
        if rec == trenutni:
            broj += 1
            if broj > maxi_br:
                maxi_br = broj
                maxi = trenutni
        else:
            broj = 1
            trenutni = rec
print(f"Rec {maxi} se pojavljuje {maxi_br} puta.")

#zadatak2
with open("primes.txt") as f1:
    with open("happy.txt") as f2:
        with open("overleap.txt", "a") as upis:
            lista = []
            lista1 = []
            ucitaj = f1.readlines()
            for linija in ucitaj:
                lista += linija.replace("\n", "").split(" ")
            file2 = f2.readlines()
            for linija in file2:
                lista1 += linija.replace("\n", "").split(" ")
            for el in lista:
                if el in lista1:
                    upis.write(f"{el} ")
