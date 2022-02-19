from tabulate import tabulate
import datetime


def prijava():
    print(
'''
          PRIJAVA
         ---------
''')
    while True:
        ime = input("Unesite korisnicko ime -> ")
        lozinka = input("Unesite lozinku -> ")
        with open("korisnici.txt") as korisnici:
            for linija in korisnici.readlines():
                lista = linija.split("|")
                if ime == lista[0] and lozinka == lista[1] and lista[-1].replace("\n", "") != "Blokiran":
                    print("Uspesno logovanje!")
                    return lista[-1].replace("\n", ""), ime
            print("Ne postoji korisnik sa zadatim korisnickim imenom ili lozinkom!")
        

def pregled_aktivnih_apartmana():
    print(
'''
          PREGLED AKTIVNIH APARTMANA
         ----------------------------
''')
    header = ["Sifra", "Broj soba", "Broj gostiju", "Adresa", "Cena po noci", "Sadrzaji", "Dostupno"]
    apartmani = []
    sadrzaji = []
    with open("apartmani.txt") as apartmani_fajl:
        for linija in apartmani_fajl.readlines():
            sadrzaji = []
            lista = linija.split("|")
            if lista[-2] != "Aktivno":
                continue
            brojevi = lista[-1].split(",")
            brojevi = [br.replace("\n", "") for br in brojevi]
            with open("sadrzaji_apartmana.txt") as sadrzaji_a:
                for el in sadrzaji_a.readlines():
                    podeli = el.split("|")
                    if podeli[0] in brojevi:
                        sadrzaji.append(podeli[1].replace("\n", ""))
            ispis_sadrzaja = ""
            for sadrzaj in sadrzaji:
                ispis_sadrzaja += f"{sadrzaj}, "
            ispis_sadrzaja = ispis_sadrzaja[:-2]
            datum = ""
            with open("datumi.txt") as datumi:
                for linija_dat in datumi.readlines():
                    lista_dat = linija_dat.split("|")
                    if lista_dat[0] == lista[0]:
                        datum += f"{lista_dat[1]}"
            apartman = [lista[0], lista[2], lista[3], lista[6], lista[8], ispis_sadrzaja, datum]
            apartmani.append(apartman)
    print(tabulate(apartmani, headers=header, stralign="center", numalign="center", tablefmt="grid"))


def pretraga_apartmana(ulazak):
    #ulazak predstavlja broj 1 ili 2 u zavosti odakle se funkcija poziva
    print(
'''
          PRETRAGA APARTMANA
         --------------------
''')
    kriterijum = [["1", "Mesto"], ["2", "Vreme dostupnosti"], ["3", "Broj soba"], ["4", "Broj osoba"], ["5", "Cena"]]
    while True:
        tacan = True
        for el in kriterijum:
            print(f"{el[0]}. {el[1]}")
        unos = input("Unesite broj kriterijuma odvojene zarezom -> ")
        unos = unos.split(",")
        moguci = ["1", "2", "3", "4", "5"]
        for el in unos:
            if el not in moguci:
                print("Pogresan unos")
                tacan = False
                break
        if tacan:
            break
    unos = dict.fromkeys(unos)
    zadati_kriterijumi = []
    for el in unos:
        if el == "1":
            mesto = input("Unesite ime ili deo imena mesta -> ")
            zadati_kriterijumi.append(["1", mesto])
        elif el == "2":
            while True:
                try:
                    vreme_od = input("Unesite vreme (dd.mm.gggg) dostupnosti od -> ")
                    v_od = vreme_od.split(".")
                    dan1 = int(v_od[0])
                    mesec1 = int(v_od[1])
                    godina1 = int(v_od[2])
                    datum_od = datetime.date(godina1, mesec1, dan1)
                    vreme_do = input("Unesite vreme (dd.mm.gggg) dostupnosti do -> ")
                    v_do = vreme_do.split(".")
                    dan2 = int(v_do[0])
                    mesec2 = int(v_do[1])
                    godina2 = int(v_do[2])
                    datum_do = datetime.date(godina2, mesec2, dan2)
                    if datum_od < datetime.date.today() or datum_od >= datum_do:
                        raise ValueError
                    break
                except (ValueError, IndexError) as greska:
                    print("Greska u unosu")
            zadati_kriterijumi.append(["2", datum_od, datum_do])
        elif el == "3":
            dobro = False
            while not dobro:
                try:
                    broj_soba_od = int(input("Unesite broj soba od -> "))
                    broj_soba_do = int(input("Unesite broj soba do -> "))
                    if broj_soba_od <= broj_soba_do:
                        dobro = True
                    else:
                        print("Los unos")
                        dobro = False
                except ValueError:
                    print("Unesite broj")
            zadati_kriterijumi.append(["3", broj_soba_od, broj_soba_do])
        elif el == "4":
            dobro = False
            while not dobro:
                try:
                    broj_osoba_od = int(input("Unesite broj osoba od -> "))
                    broj_osoba_do = int(input("Unesite broj osoba do -> "))
                    if broj_osoba_od <= broj_osoba_do:
                        dobro = True
                    else:
                        print("Los unos")
                        dobro = False
                except ValueError:
                    print("Unesite broj")
            zadati_kriterijumi.append(["4", broj_osoba_od, broj_osoba_do])
        elif el == "5":
            dobro = False
            while not dobro:
                try:
                    cena_od = int(input("Unesite cenu od -> "))
                    cena_do = int(input("Unesite cenu do -> "))
                    dobro = True
                except ValueError:
                    print("Unesite broj")
            zadati_kriterijumi.append(["5", cena_od, cena_do])

    pretraga = []
    with open("apartmani.txt") as apartmani:
        for el in zadati_kriterijumi:
            match el[0]:
                case "1":
                    if pretraga == []:
                        nadjeno = False
                        for linija in apartmani.readlines():
                            lista = linija.split("|")
                            mesto = lista[6].split(", ")
                            if el[1].lower() in mesto[1].lower() and lista[-2] == "Aktivno":
                                pretraga.append(lista)
                                nadjeno = True
                    else:
                        pretraga1 = []
                        for linija in pretraga:
                            mesto = linija[6].split(", ")
                            if el[1].lower() in mesto[1].lower() and lista[-2] == "Aktivno":
                                pretraga1.append(linija)
                                nadjeno = True
                        if nadjeno:
                            pretraga = pretraga1
                    if not nadjeno:
                        print("Ne postoji rezultat ove pretrage")
                        break
                case "2":
                    nadjeno = False
                    if pretraga == []:
                        for linija in apartmani.readlines():
                            lista = linija.split("|")
                            #dobavljanje svih datum
                            with open("datumi.txt") as datumi:
                                for red in datumi.readlines():
                                    lista_datuma = red.split("|")
                                    if lista_datuma[0] == lista[0]:
                                        #ucitaj datum iz liste i obradi ga
                                        oba_datuma = lista_datuma[1].split("-")
                                        prvi = oba_datuma[0].split(".")
                                        drugi = oba_datuma[1].split(".")
                                        datum1 = datetime.date(int(prvi[2]), int(prvi[1]), int(prvi[0])) #datum od kog je dostupno
                                        datum2 = datetime.date(int(drugi[2]), int(drugi[1]), int(drugi[0])) #datum do kog je dostupno
                                        #provera jel moze
                                        if el[1] <= datum2 and el[1] >= datum1 and el[2] >= datum1 and el[2] <= datum2 and lista[-2] == "Aktivno":
                                            pretraga.append(lista)
                                            nadjeno = True
                        if not nadjeno:
                            print("Ne postoji rezultat ove pretrage")
                    else:
                        pretraga1 = []
                        for linija in pretraga:
                            with open("datumi.txt") as datumi:
                                for red in datumi.readlines():
                                    lista_datuma = red.split("|")
                                    if lista_datuma[0] == linija[0]:
                                        oba_datuma = lista_datuma[1].split("-")
                                        prvi = oba_datuma[0].split(".")
                                        drugi = oba_datuma[1].split(".")
                                        datum1 = datetime.date(int(prvi[2]), int(prvi[1]), int(prvi[0])) #datum od kog je dostupno
                                        datum2 = datetime.date(int(drugi[2]), int(drugi[1]), int(drugi[0])) #datum do kog je dostupno
                                        if el[1] <= datum2 and el[1] >= datum1 and el[2] >= datum1 and el[2] <= datum2 and lista[-2] == "Aktivno":
                                            nadjeno = True
                                            pretraga1.append(linija)
                        if nadjeno:
                            pretraga = pretraga1
                        if not nadjeno:
                            print("Ne postoji rezultat ove pretrage")                   
                case "3":
                    nadjeno = False
                    if pretraga == []:
                        for linija in apartmani.readlines():
                            lista = linija.split("|")
                            broj = int(lista[2])
                            if el[1] <= broj <= el[2] and lista[-2] == "Aktivno":
                                pretraga.append(lista)
                                nadjeno = True
                    else:
                        pretraga1 = []
                        for linija in pretraga:
                            broj = int(linija[2])
                            if el[1] <= broj <= el[2] and lista[-2] == "Aktivno":
                                pretraga1.append(linija)
                                nadjeno = True
                        if nadjeno:
                            pretraga = pretraga1
                    if not nadjeno:
                        print("Ne postoji rezultat ove pretrage")
                        break
                case "4":
                    nadjeno = False
                    if pretraga == []:
                        for linija in apartmani.readlines():
                            lista = linija.split("|")
                            broj = int(lista[3])
                            if el[1] <= broj <= el[2] and lista[-2] == "Aktivno":
                                pretraga.append(lista)
                                nadjeno = True
                    else:
                        pretraga1 = []
                        for linija in pretraga:
                            broj = int(linija[3])
                            if el[1] <= broj <= el[2] and lista[-2] == "Aktivno":
                                pretraga1.append(linija)
                                nadjeno = True
                        if nadjeno:
                            pretraga = pretraga1
                    if not nadjeno:
                        print("Ne postoji rezultat ove pretrage")
                        break
                case "5":
                    nadjeno = False
                    if pretraga == []:
                        for linija in apartmani.readlines():
                            lista = linija.split("|")
                            cena = int(lista[-3])
                            if el[1] <= cena <= el[2] and lista[-2] == "Aktivno":
                                pretraga.append(lista)
                                nadjeno = True
                    else:
                        pretraga1 = []
                        for linija in pretraga:
                            cena = int(linija[-3])
                            if el[1] <= cena <= el[2] and lista[-2] == "Aktivno":
                                pretraga1.append(linija)
                                nadjeno = True
                        if nadjeno:
                            pretraga = pretraga1
                    if not nadjeno:
                        print("Ne postoji rezultat ove pretrage")
                        break

    header = ["ID", "Broj soba", "Broj gostiju", "Adresa", "Cena po noci", "Sadrzaji"]
    apartmani = []
    sadrzaji = []
    for lista in pretraga:
        sadrzaji = []
        if lista[-2] != "Aktivno" and ulazak == 1:
            continue
        brojevi = lista[-1].split(",")
        brojevi = [br.replace("\n", "") for br in brojevi]
        with open("sadrzaji_apartmana.txt") as sadrzaji_a:
            for el in sadrzaji_a.readlines():
                podeli = el.split("|")
                if podeli[0] in brojevi:
                    sadrzaji.append(podeli[1].replace("\n", ""))
        ispis_sadrzaja = ""
        for sadrzaj in sadrzaji:
            ispis_sadrzaja += f"{sadrzaj}, "
        ispis_sadrzaja = ispis_sadrzaja[:-2]
        apartman = [lista[0], lista[2], lista[3], lista[6], lista[8], ispis_sadrzaja]
        apartmani.append(apartman)
    if nadjeno:
        print(tabulate(apartmani, headers=header, stralign="center", numalign="center", tablefmt="grid"))


def prikaz_10_najpopularnijih():
    header = ["Redni broj", "Mesto"]
    najpopularniji = []
    with open("rezervacije.txt") as rezervacije:
        for linija in rezervacije.readlines():
            lista = linija.split("|")
            poc_kraj = lista[4].split("-")
            dan, mesec, godina = poc_kraj[1].split(".")
            datum = datetime.date(int(godina), int(mesec), int(dan))
            if "Zavrsena" in lista[-1] and datum > datetime.date.today() - datetime.timedelta(days=356):
                mesto = lista[6].split(",")[1][1:]
                ima = False
                for el in najpopularniji:
                    if mesto == el[0]:
                        el[1] += 1
                        ima = True
                if not ima:
                    najpopularniji.append([mesto, 1])
    #ispis od najpopularnijeg
    najpopularniji.sort(key = lambda x:x[1])
    br = 1
    za_ispis = []
    for el in najpopularniji[::-1]:
        za_ispis.append([br, el[0]])
        br += 1
    print(tabulate(za_ispis[:10], headers=header, stralign="center", numalign="center", tablefmt="grid"))      
