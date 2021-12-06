def vrhovi_drzava(drzava):
    br = 0
    with open("mountains.txt") as f:
        fajl = f.readlines()
        for linija in fajl:
            elementi = linija.replace("\n", "").split("|")
            br += 1
            drzave = elementi[4].split("/")
            if drzava in drzave:
                print(elementi[0])

def na_granici2():
    with open("mountains.txt") as f:
        fajl = f.readlines()
        for linija in fajl:
            elementi = linija.replace("\n", "").split("|")
            drzave = elementi[4].split("/")
            if len(drzave) == 2 and 8100 > int(elementi[1]) > 7700:
                print(elementi[0])

def iznad_6000(drzava):
    with open("mountains.txt") as f:
        print("Country\n------------")
        fajl = f.readlines()
        for linija in fajl:
            elementi = linija.replace("\n", "").split("|")
            drzave = elementi[4].split("/")
            if drzava in drzave and int(elementi[1]) > 6000:
                print(elementi[0])

def sve_drzave():
    lista = []
    with open("mountains.txt") as f:
        fajl = f.readlines()
        for linija in fajl:
            elementi = linija.replace("\n", "").split("|")
            drzave = elementi[4].split("/")
            for el in drzave:
                if el not in lista:
                    lista.append(el)
    return lista

def iznad_6000():
    print("Country        num\n--------------------")
    for drzava in sve_drzave():
        br = 0
        with open("mountains.txt") as f:
            fajl = f.readlines()
            for linija in fajl:
                elementi = linija.replace("\n", "").split("|")
                drzave = elementi[4].split("/")
                if drzava in drzave and int(elementi[1]) > 6000:
                    br += 1
        print(f"{drzava.ljust(15)}{br}")

def zadati_venac(venac):
    print("Venac\n-----------")
    with open("mountains.txt") as f:
        fajl = f.readlines()
        for linija in fajl:
            elementi = linija.replace("\n", "").split("|")
            if venac == elementi[3]:
                print(elementi[0])

def na_granici():
    najvise = 0
    najvise_drz = ""
    with open("mountains.txt") as f:
        fajl = f.readlines()
        for linija in fajl:
            elementi = linija.replace("\n", "").split("|")
            drzave = elementi[4].split("/")
            if len(drzave) >= 2:
                print(elementi[0])
                if len(drzave) > najvise:
                    najvise = len(drzave)
                    najvise_drz = elementi[0]
    print(f"Najvise ima {najvise_drz} sa {najvise} granice")

#a
# vrhovi_drzava("China")

#b
#na_granici2()

#c
#iznad_6000("China")

#d
# iznad_6000()

#e
# zadati_venac("Himalayas")

#f
# na_granici()