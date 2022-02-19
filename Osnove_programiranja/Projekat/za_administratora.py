import datetime
from tabulate import tabulate

def registracija_novih_domacina():
    kraj = False
    while not kraj:
        #ispis svih gostiju
        svi_gosti = []
        header = ["Gosti"]
        with open("korisnici.txt") as korisnici:
            for linija in korisnici.readlines():
                lista = linija.split("|")
                if lista[-1].replace("\n", "") == "Gost":
                    svi_gosti.append([lista[0]])
        print(tabulate(svi_gosti, headers=header, stralign="center", numalign="center", tablefmt="grid"))

        izmena = ""
        postoji = False
        while not postoji:
            unos = input("Ukucajte korisnicko ime gosta koji treba da postane domacin -> ")
            with open("korisnici.txt") as korisnici:
                linije = korisnici.readlines()
                for linija in linije:
                    lista = linija.split("|")
                    if lista[0] == unos and lista[-1].replace("\n", "") == "Gost":
                        postoji = True
                        izmena = f"{lista[0]}|{lista[1]}|{lista[2]}|{lista[3]}|{lista[4]}|{lista[5]}|{lista[6]}|Domacin\n"
            if postoji:
                break
            else:
                print("Ne postoji gost sa unetim korisnickim imenom")
        with open("korisnici.txt", "w") as korisnici:
            for linija in linije:
                lista = linija.split("|")
                if lista[0] != unos:
                    korisnici.write(linija)
                else:
                    korisnici.write(izmena)
        print(f"Korisnik {unos} je sada domacin")

        while True:
            jos = input("\nDa li zelite da registrujete jos domacina? (d/n) -> ")
            if jos.lower() == "n":
                kraj = True
                break
            elif jos.lower() != "d":
                print("Potrebno je ukucati 'd' ili 'n'")
            else:
                break


def kreiranje_dodatne_opreme():
    header = ["ID", "Dodatna oprema"]
    while True:
        za_ispis = []
        with open("sadrzaji_apartmana.txt") as sadrzaji:
            linije = sadrzaji.readlines()
            for linija in linije:
                lista = linija.split("|")
                za_ispis.append([lista[0], lista[1]])
        print(tabulate(za_ispis,headers=header, stralign="center", numalign="center", tablefmt="grid"))

        kraj = False
        unos = input("Unesite novu dodatnu opremu -> ")
        if unos == "":
            print("Unesen je prazan string")
        else:
            try:
                redni_br = int(linije[-1].split("|")[0])+1
            except IndexError:
                redni_br = 1
            with open("sadrzaji_apartmana.txt", "a") as sadrzaji:
                sadrzaji.write(f"{redni_br}|{unos}\n")
            print("Unos uspesan!")
            while True:
                potvrda = input("Da li zelite da unesete jos dodatne opreme? (d/n) -> ")
                if potvrda.lower() == "n":
                    kraj = True
                    break
                elif potvrda.lower() != "d":
                    print("Potrebno je uneti 'd' ili 'n'")
                else:
                    break
        if kraj:
            break


def brisanje_dodatne_opreme():
    kraj = False
    while not kraj:
        header = ["ID", "Dodatna oprema", "Koristi se"]
        za_ispis = []
        upotreba = []
        with open("sadrzaji_apartmana.txt") as sadrzaji:
            linije = sadrzaji.readlines()
            for linija in linije:
                lista = linija.split("|")
                koristi_se = False
                with open("apartmani.txt") as apartmani:
                    linije_apartmana = apartmani.readlines()
                    for linija_apartmana in linije_apartmana:
                        lista_apartmana = linija_apartmana.split("|")
                        if lista[0] in lista_apartmana[-1]:
                            koristi_se = True
                if koristi_se:
                    za_ispis.append([lista[0], lista[1], "Da"])
                    upotreba.append("Da")
                else:
                    za_ispis.append([lista[0], lista[1], "Ne"])
                    upotreba.append("Ne")
        if za_ispis == []:
            print("Trenutno ne postoji uneta dodatna oprema")
            kraj = True
        else:
            print(tabulate(za_ispis, headers=header, stralign="center", numalign="center", tablefmt="grid"))
            prekid = False
            pogresno = False
            while not pogresno:
                try:
                    unos = int(input("Unesite id dodatne opreme koju zelite da obrisete (0 za odustanak) -> "))
                    if unos == 0:
                        prekid = True
                        kraj = True
                    else:
                        brojac = 0
                        with open("sadrzaji_apartmana.txt") as sadrzaji:
                            linije = sadrzaji.readlines()
                            for linija in linije:
                                lista = linija.split("|")
                                if lista[0] == unos:
                                    break
                                brojac += 1
                        if upotreba[brojac-1] == "Da":
                            raise ValueError
                    break
                except ValueError:
                    print("Potrebno je uneti id dodatne opreme, koja se ne koristi")
            if not prekid:
                with open("sadrzaji_apartmana.txt", "w") as sadrzaji:
                    for linija in linije:
                        lista = linija.split("|")
                        if int(lista[0]) != unos:
                            sadrzaji.write(linija)
                print("Obrisano")

                while True:
                    jos = input("\nDa li zelite da obrisete jos sadrzaja? (d/n) -> ")
                    if jos.lower() == "n":
                        kraj = True
                        break
                    elif jos.lower() != "d":
                        print("Potrebno je ukucati 'd' ili 'n'")
                    else:
                        break
                
    
def blokiranje_korisnika():
    kraj = False
    while not kraj:
        tip_radnje = ""
        svi_korisnici = []
        header = ["Korisnik", "Uloga"]
        with open("korisnici.txt") as korisnici:
            linije = korisnici.readlines()
            for linija in linije:
                lista = linija.split("|")
                if lista[-1].replace("\n", "") != "Administrator" and lista[-1].replace("\n", "") != "Blokiran":
                    svi_korisnici.append([lista[0], lista[-1]])
        print(tabulate(svi_korisnici, headers=header, stralign="centar", numalign="center", tablefmt="grid"))
        print("\n")
        blokirani_korisnici = []
        header = ["Blokirani korisnici"]
        with open("korisnici.txt") as korisnici:
            linije = korisnici.readlines()
            for linija in linije:
                lista = linija.split("|")
                if lista[-1].replace("\n", "") == "Blokiran":
                    blokirani_korisnici.append([lista[0]])
        print(tabulate(blokirani_korisnici, headers=header, stralign="centar", numalign="center", tablefmt="grid"))

        izmena = ""
        postoji = False
        while not postoji:
            unos = input("Unesite korisnicko ime korisnika koga zelite da blokirate ili odblokirate-> ")
            for linija in linije:
                lista = linija.split("|")
                if lista[0] == unos and lista[-1].replace("\n", "") != "Administrator" and lista[-1].replace("\n", "") != "Blokiran":
                    postoji = True
                    izmena = f"{lista[0]}|{lista[1]}|{lista[2]}|{lista[3]}|{lista[4]}|{lista[5]}|{lista[6]}|Blokiran\n"
                    tip_radnje = "blokiran"
                if lista[0] == unos and lista[-1].replace("\n", "") == "Blokiran":
                    postoji = True
                    izmena = f"{lista[0]}|{lista[1]}|{lista[2]}|{lista[3]}|{lista[4]}|{lista[5]}|{lista[6]}|Gost\n"
                    tip_radnje = "odblokiran"
            if postoji:
                break
            else:
                print("Ne postoji korisnik sa unetim korisnickim imenom")

        with open("korisnici.txt", "w") as korisnici:
            for linija in linije:
                lista = linija.split("|")
                if lista[0] != unos:
                    korisnici.write(linija)
                else:
                    korisnici.write(izmena)
        id_apartmana_korisnika = []
        izmena_apartmana = []
        with open("apartmani.txt") as apartmani:
            linije = apartmani.readlines()
            for linija in linije:
                lista = linija.split("|")
                if lista[7] == unos:
                    id_apartmana_korisnika.append(lista[0])
                    apartman = f"{lista[0]}|{lista[1]}|{lista[2]}|{lista[3]}|{lista[4]}|{lista[5]}|{lista[6]}|{lista[7]}|{lista[8]}|Neaktivan|{lista[10]}"
                    izmena_apartmana.append(apartman)
        br = 0
        with open("apartmani.txt", "w") as apartmani:
            for linija in linije:
                lista = linija.split("|")
                if lista[0] in id_apartmana_korisnika:
                    apartmani.write(izmena_apartmana[br])
                    br += 1
                else:
                    apartmani.write(linija)

        print(f"Korisnik {unos} je {tip_radnje}")

        while True:
            jos = input("\nDa li zelite da blokirate/odblokirate jos korisnika? (d/n) -> ")
            if jos.lower() == "n":
                kraj = True
                break
            elif jos.lower() != "d":
                print("Potrebno je ukucati 'd' ili 'n'")
            else:
                break


def pretraga_registracija():
    print(
'''
          PRETRAGA REZERVACIJA
         ----------------------
''')
    uslovi = ["Status", "Adresa", "Korisnicko ime domacina"]
    za_ispis = []
    uneseno  = ""
    br = 1
    for el in uslovi:
        print(f"{br}. {el}")
        br += 1

    while True:
        header = ["ID rezervacije", "ID apartmana", "Korisnik", "Domacin", "Gosti", "Adresa", "Cena", "Datum", "Status"]
        try:
            unos = int(input("Unesite broj kriterijuma po kojem zelite da izvrsite pretragu -> "))
            if unos > 3 or unos < 1:
                raise ValueError
            break
        except ValueError:
            print("Potrebno je uneti broj koji se nalazi pored kriterijuma")

    if unos == 1:
        while True:
            unos1 = input("Unesite 'p' za potvrdjen ili 'o' za odbijen -> ")
            if unos1 == "p":
                uneseno = "Prihvacena"
                break
            elif unos1  == "o":
                uneseno = "Odbijena"
                break
            else:
                print("Potrebno je uneti 'p' ili 'o'")
    elif unos == 2:
        unos1 = input("Unesite adresu ili deo adrese -> ")
        uneseno = unos1
    elif unos == 3:
        unos1 = input("Unesite korisnicko ime domacina -> ")
        uneseno = unos1

    with open("rezervacije.txt") as rezervacije:
        linije = rezervacije.readlines()
        for linija in linije:
            lista = linija.split("|")
            if unos == 1 and uneseno in lista[-1]:
                za_ispis.append([lista[0], lista[1], lista[2], lista[3], lista[7], lista[6], lista[5], lista[4], lista[-1]])
            elif unos == 2 and uneseno in lista[6]:
                za_ispis.append([lista[0], lista[1], lista[2], lista[3], lista[7], lista[6], lista[5], lista[4], lista[-1]])
            elif unos == 3 and uneseno == lista[3]:
                za_ispis.append([lista[0], lista[1], lista[2], lista[3], lista[7], lista[6], lista[5], lista[4], lista[-1]])
    print(tabulate(za_ispis, headers=header, stralign="center", numalign="center", tablefmt="grid"))


def izvestaji():
    print(
'''
          IZVESTAJI
         -----------
'''
    )
    vrste = ["Lista potvrdjenih rezervisanih apartmana za izabran dan realizacije", "Lista potvrdjenih rezervisanih apartmana za izabranog domacina", "Godisnji pregled angazovanja domacina", "Mesecni pregled angazovanja po domacinu", "Ukupan broj i cena potvrdjenih rezervacija za izabran dan", "Pregled zastupljenosti pojedinacnih gradova u odnosu na ukupan broj rezervacija"]
    br = 1
    for el in vrste:
        print(f"{br}. {el}")
        br += 1

    za_ispis = []
    
    while True:
        try:
            unos = int(input("Izaberite koji izvestaj zelite -> "))
            if unos > 6:
                raise ValueError
            break
        except ValueError:
            print("Potrebno je ukucati jedan od ponudjenih brojeva")

    if unos == 1:
        while True:
            try:
                dat = input("Unesite datum (dd.mm.gggg) -> ")
                dan, mesec, godina = dat.split(".")
                datum = datetime.date(int(godina), int(mesec), int(dan))
                break
            except (IndexError, ValueError) as er:
                print("Los unos datuma")
        
        header = ["ID apartmana", "Domacin", "Adresa", "Datum"]
        with open("rezervacije.txt") as rezervacije:
            for linija in rezervacije.readlines():
                lista = linija.split("|")
                if lista[-1].replace("\n", "") == f"Prihvacena, {dat}":
                    za_ispis.append([lista[1], lista[3], lista[6], lista[4]])
        if za_ispis != []:
            print(tabulate(za_ispis, headers=header, stralign="center", numalign="center", tablefmt="grid"))
        else:
            print("Izvestaj je prazan")

    elif unos == 2:
        while True:
            unos1 = input("Unesite korisnicko ime domacina -> ")
            if unos1 != "":
                break
            else:
                print("Potrebno je uneti korisnicko ime domacina")
        
        header = ["ID apartmana", "Domacin", "Adresa", "Datum"]
        with open("rezervacije.txt") as rezervacije:
            for linija in rezervacije.readlines():
                lista = linija.split("|")
                if "Prihvacena" in lista[-1].replace("\n", "") and lista[3] == unos1:
                    za_ispis.append([lista[1], lista[3], lista[6], lista[4]])
        if za_ispis != []:
            print(tabulate(za_ispis, headers=header, stralign="center", numalign="center", tablefmt="grid"))
        else:
            print("Izvestaj je prazan")
    
    elif unos == 3:
        header = ["Domacin", "Broj rezervacija", "Zarada"]
        za_ispis = [] ##domacin, broj_rezervacija, zarada
        with open("rezervacije.txt") as rezervacije:
            for linija in rezervacije.readlines():
                lista = linija.split("|")
                poc_kraj = lista[4].split("-")
                dan, mesec, godina = poc_kraj[1].split(".")
                datum = datetime.date(int(godina), int(mesec), int(dan))
                if datum + datetime.timedelta(days=365) >= datetime.date.today() and "Zavrsena" in lista[-1]:
                    postoji = False
                    for el in za_ispis:
                        if lista[3] in el:
                            postoji = True
                            el[1] += 1
                            el[2] += int(lista[5])
                    if not postoji:
                        za_ispis.append([lista[3], 1, int(lista[5])])
        with open("korisnici.txt") as korisnici:
            for linija in korisnici.readlines():
                lista = linija.split("|")
                postoji = False
                if lista[-1].replace("\n", "") == "Domacin":
                    for el in za_ispis:
                        if lista[0] in el:
                            postoji = True
                    if not postoji:
                        za_ispis.append([lista[0], 0, 0])
        print(tabulate(za_ispis, headers=header, stralign="center", numalign="center", tablefmt="grid"))

    elif unos == 4:
        header = ["Domacin", "Broj rezervacija", "Zarada"]
        za_ispis = [] ##domacin, broj_rezervacija, zarada
        with open("rezervacije.txt") as rezervacije:
            for linija in rezervacije.readlines():
                lista = linija.split("|")
                if "Prihvacena" in lista[-1]:
                    poc_kraj = lista[-1].split(",")
                    dan, mesec, godina = poc_kraj[1].replace("\n", "").split(".")
                    datum = datetime.date(int(godina), int(mesec), int(dan))
                    if datum + datetime.timedelta(days=30) >= datetime.date.today():
                        postoji = False
                        for el in za_ispis:
                            if lista[3] in el:
                                postoji = True
                                el[1] += 1
                                el[2] += int(lista[5])
                        if not postoji:
                            za_ispis.append([lista[3], 1, int(lista[5])])
        with open("korisnici.txt") as korisnici:
            for linija in korisnici.readlines():
                lista = linija.split("|")
                postoji = False
                if lista[-1].replace("\n", "") == "Domacin":
                    for el in za_ispis:
                        if lista[0] in el:
                            postoji = True
                    if not postoji:
                        za_ispis.append([lista[0], 0, 0])
        print(tabulate(za_ispis, headers=header, stralign="center", numalign="center", tablefmt="grid"))

    elif unos == 5:
        header = ["Broj rezervacija", "Cena"]
        za_ispis = []
        while True:
            try:
                dat = input("Unesite datum (dd.mm.gggg) -> ")
                dan, mesec, godina = dat.split(".")
                datum = datetime.date(int(godina), int(mesec), int(dan))
                break
            except (IndexError, ValueError) as er:
                print("Los unos datuma")
        while True:
            doma = input("Unesite domacina -> ")
            if doma == "":
                print("Potrebno je uneti korisnicko ime domacina")
            else:
                break

        with open("rezervacije.txt") as rezervacije:
            el = [0, 0]
            for linija in rezervacije.readlines():
                lista = linija.split("|")
                datum_rez = lista[-1].replace(" ", "").replace("\n", "").split(",")
                if lista[3] == doma and "Prihvacena" == datum_rez[0] and dat == datum_rez[1]:
                    el[0] += 1
                    el[1] += int(lista[5])
            za_ispis.append(el)
            if za_ispis != []:
                print(tabulate(za_ispis, headers=header, stralign="center", numalign="center", tablefmt="grid"))
            else:
                print("Izvestaj je prazan")

    elif unos == 6:
        header = ["Grad", "Odnos", "Procenti"]
        za_ispis = []
        with open("rezervacije.txt") as rezervacije:
            linije = rezervacije.readlines()
            for linija in linije:
                lista = linija.split("|")
                grad = lista[6].split(", ")[1]
                postoji = False
                for el in za_ispis:
                    if grad in el:
                        el[1] += 1
                        postoji = True
                if not postoji:
                    za_ispis.append([grad, 1])
        for el in za_ispis:
            el.append(f"{int(el[1]/len(linije)*100)}%")
            el[1] = f"{el[1]}/{len(linije)}"
        with open("apartmani.txt") as apartmani:
            for linija in apartmani.readlines():
                lista = linija.split("|")
                grad = lista[6].split(", ")[1]
                postoji = False
                for el in za_ispis:
                    if grad in el:
                        postoji = True
                if not postoji:
                    za_ispis.append([grad, f"0/{len(linije)}", "0%"])
        print(tabulate(za_ispis, headers=header, stralign="center", numalign="center", tablefmt="grid"))
        

def definisanje_praznika():
    print(
'''
          DODAVANJE PRAZNIKA
         --------------------
'''
    )
    header = ["ID", "Datum"]
    za_ispis = []
    id_poslednjeg = 0
    with open("praznici.txt") as praznici:
        linije = praznici.readlines()
        try:
            id_poslednjeg = int(linije[-1].split("|")[0])
        except IndexError:
            id_poslednjeg = 0
        for linija in linije:
            lista = linija.split("|")
            za_ispis.append([lista[0], lista[1]])
    print(tabulate(za_ispis, headers=header, numalign="center", stralign="center", tablefmt="grid"))
    while True:
        try:
            unos = input("Unesite datum koji zelite da uklonite ili novog praznika (dd.mm.gggg) -> ")
            dan, mesec, godina = unos.split(".")
            datum = datetime.date(int(godina), int(mesec), int(dan))
            break
        except (ValueError, IndexError) as error:
            print("Los unos datuma")
    postoji = False
    id_menja = ""
    for linija in linije:
        lista = linija.split("|")
        if lista[1].replace("\n", "") == unos:
            id_menja = lista[0]
            postoji = True
    if not postoji:
        with open("praznici.txt", "a") as praznici:
            praznici.write(f"{id_poslednjeg + 1}|{unos}\n")
    else:
        with open("praznici.txt") as praznici:
            linije = praznici.readlines()
        with open("praznici.txt", "w") as praznici:
            for linija in linije:
                lista = linija.split("|")
                if lista[0] != id_menja:
                    praznici.write(linija)
    while True:
        ponovo = input("Da li zelite da unesete jos praznika? (d/n) -> ")
        if ponovo.lower() == "d":
            definisanje_praznika()
            break
        elif ponovo.lower() != "n":
            print("Potrebno je uneti 'd' ili 'n'")
        else:
            break
