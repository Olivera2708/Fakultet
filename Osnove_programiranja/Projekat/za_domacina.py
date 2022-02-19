import datetime
from tabulate import tabulate
import za_gosta

def Sadrzaji():
    ukupno = ""
    with open("sadrzaji_apartmana.txt") as sadrzaji:
        broj = len(sadrzaji.readlines())
    while True:
        try:
            izabrano = input("Unesite sadrzaj koji zelite (broj ili ukucajte naziv, za kraj pritisnite enter) -> ")
            if int(izabrano) > broj:
                print("Ne postoji sadrzaj sa tim brojem")
            elif izabrano in ukupno:
                print("Vec ste uneli ovaj sadrzaj")
            else:
                ukupno += f"{izabrano},"
        except ValueError:
            if izabrano == "":
                break
            postoji = False
            with open("sadrzaji_apartmana.txt") as sadrzaji:
                for linija in sadrzaji.readlines():
                    if izabrano.capitalize() in linija:
                        razdvoj = linija.split("|")
                        print(f"{razdvoj[0]}. {razdvoj[1]}")
                        postoji = True
                if not postoji:
                    print("Ne postoji ovakav sadrzaj")
    return ukupno[:-1]


def Termini(id_apartmana):
    jos_termina = True
    while jos_termina:
        while True:
            try:
                datum_od = input("Unesite vreme (dd.mm.gggg) dostupnosti od -> ")
                v_od = datum_od.split(".")
                dan1 = int(v_od[0])
                mesec1 = int(v_od[1])
                godina1 = int(v_od[2])
                datum_od1 = datetime.date(godina1, mesec1, dan1)
                if datum_od1 < datetime.date.today():
                    raise ValueError
                break
            except ValueError:
                print("Los unos datuma") 
        while True:
            try:
                datum_do = input("Unesite vreme (dd.mm.gggg) dostupnosti do -> ")
                v_od = datum_do.split(".")
                dan1 = int(v_od[0])
                mesec1 = int(v_od[1])
                godina1 = int(v_od[2])
                datum_do1 = datetime.date(godina1, mesec1, dan1)
                if datum_do1 <= datum_od1:
                    raise ValueError
                break
            except ValueError:
                print("Los unos datuma") 

        preklapa = False

        with open("datumi.txt") as datumi:
            for linija in datumi.readlines():
                lista = linija.split("|")
                if id_apartmana == int(lista[0]):
                    poc_kraj = lista[1].split("-")
                    v_od = poc_kraj[0].split(".")
                    dan1 = int(v_od[0])
                    mesec1 = int(v_od[1])
                    godina1 = int(v_od[2])
                    datum_od2 = datetime.date(godina1, mesec1, dan1)

                    v_do = poc_kraj[1].split(".")
                    dan2 = int(v_do[0])
                    mesec2 = int(v_do[1])
                    godina2 = int(v_do[2])
                    datum_do2 = datetime.date(godina2, mesec2, dan2)

                    if (datum_od1 > datum_od2 and datum_od1 < datum_do2) or (datum_od2 > datum_od2 and datum_od2 < datum_do2):
                        print("Uneti datum se preklapa sa postojecim")
                        preklapa = True

        if not preklapa:
            #upis u fajl
            with open("datumi.txt", "a") as datumi:
                datumi.write(f"{id_apartmana}|{datum_od}-{datum_do}\n")

            #da li je kraj
            while True:
                kraj = input("Da li zelite da unesete jos datuma? (d/n) -> ")
                if kraj.lower() == "n":
                    jos_termina = False
                    break
                elif kraj.lower() != "d":
                    print("Pogresan unos")
                else:
                    break

def prikaz_apartmana(korisnik):
    za_ispis = []
    header = ["id", "Tip", "Broj soba", "Broj osoba", "Geografska sirina", "Geografska duzina", "Adresa", "Cena", "Status", "Sadrzaji", "Slobodni datumi"]
    with open("apartmani.txt") as apartmani:
        for linija in apartmani.readlines():
            lista = linija.split("|")
            if lista[7] == korisnik:
                datum = ""
                sadrzaji = []
                with open("datumi.txt") as datumi:
                    for linija_dat in datumi.readlines():
                        lista_dat = linija_dat.split("|")
                        if lista_dat[0] == lista[0]:
                            datum += f"{lista_dat[1]}"
                with open("sadrzaji_apartmana.txt") as sadrzaji_a:
                    for el in sadrzaji_a.readlines():
                        podeli = el.split("|")
                        if podeli[0] in lista[10]:
                            sadrzaji.append(podeli[1].replace("\n", ""))
                ispis_sadrzaja = ""
                for sadrzaj in sadrzaji:
                    ispis_sadrzaja += f"{sadrzaj}, "
                ispis_sadrzaja = ispis_sadrzaja[:-2]
                ubaci = [lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[8], lista[9], ispis_sadrzaja, datum]
                za_ispis.append(ubaci)
    print(tabulate(za_ispis, headers=header, stralign="center", numalign="center", tablefmt="grid"))


def ispis_apartmana(broj, korisnik):
    apartman = [[]]
    header = ["id", "Tip", "Broj soba", "Broj osoba", "Geografska sirina", "Geografska duzina", "Adresa", "Cena", "Status", "Sadrzaji", "Slobodni datumi"]
    datum = ""
    with open("datumi.txt") as datumi:
        for linija_dat in datumi.readlines():
            lista_dat = linija_dat.split("|")
            if int(lista_dat[0]) == broj:
                datum += f"{lista_dat[1]}"
    with open("apartmani.txt") as apartmani:
        for linija in apartmani.readlines():
            lista = linija.split("|")
            sadrzaji = []
            if int(lista[0]) == broj and korisnik == lista[7]:
                with open("sadrzaji_apartmana.txt") as sadrzaji_a:
                    for el in sadrzaji_a.readlines():
                        podeli = el.split("|")
                        if podeli[0] in lista[10]:
                            sadrzaji.append(podeli[1].replace("\n", ""))
                ispis_sadrzaja = ""
                for sadrzaj in sadrzaji:
                    ispis_sadrzaja += f"{sadrzaj}, "
                ispis_sadrzaja = ispis_sadrzaja[:-2]
                apartman = [[lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[8], lista[9], ispis_sadrzaja, datum]]
                break
    if apartman != [[]]:
        print(tabulate(apartman, headers=header, stralign="center", numalign="center", tablefmt="grid"))
        return True
    else:
        print("Ne postoji ovakav apartman")
        return False

def dodavanje_apartmana(korisnik):
    kraj = False
    while not kraj:
        print(
    '''
              KREIRANJE APARTMANA
             ---------------------
    ''')
        while True:
            tip = input("Unesite tip apartmana (soba ili apartman) -> ")
            if tip.lower() == "soba" or tip.lower() == "apartman":
                break
        while True:
            try:
                broj_soba = int(input("Unesite broj soba -> "))
                break
            except ValueError:
                print("Potrebno je uneti broj")
        while True:
            try:
                broj_gostiju = int(input("Unesite broj gostiju -> "))
                break
            except ValueError:
                print("Potrebno je uneti broj")
        while True:
            try:
                sirina = float(input("Unesite geografsku sirinu na kojoj se nalazi apartman -> "))
                break
            except:
                print("Potrebno je uneti decimalni broj")
        while True:
            try:
                duzina = input("Unesite geografsku duzinu na kojoj se nalazi apartman -> ")
                break
            except:
                print("Potrebno je uneti decimalni broj")
        while True:  
            greska = False
            adresa = input("Unesite adresu (Ulica i broj, mesto, postanski broj) -> ")
            lista = adresa.split(",")
            if len(lista) != 3:
                greska = True
                print("Niste uneli sve informacije")
            if not greska:
                try:
                    broj = lista[2][1:]
                    postanski_broj = int(broj)
                except ValueError:
                    greska = True
                    print("Pogresan postanski broj")
            if not greska:
                break
        while True:
            try:
                cena = int(input("Unesite cenu po noci -> "))
                break
            except:
                print("Potrebno je uneti broj")

        #unos sadrzaja
        sadrzaji = Sadrzaji()

        with open("apartmani.txt") as apartmani:
            try:
                elementi = apartmani.readlines()[-1].split("|")
                broj = int(elementi[0]) + 1
            except IndexError:
                broj = 1

        with open("apartmani.txt", "a") as apartmani:
            apartmani.write(f"{broj}|{tip}|{broj_soba}|{broj_gostiju}|{sirina}|{duzina}|{adresa}|{korisnik}|{cena}|Neaktivno|{sadrzaji}\n")
            #dostupni termini
            Termini(broj)

        while True:
            jos = input("\nDa li zelite da dodate jos apartmana? (d/n) -> ")
            if jos.lower() == "n":
                kraj = True
                break
            elif jos.lower() != "d":
                print("Potrebno je ukucati 'd' ili 'n'")
            else:
                break


def izmena_apartmana(korisnik):
    print(
'''
          IZMENA APARTMANA
         ------------------
'''
    )
    kraj = False
    while not kraj:
        prikaz_apartmana(korisnik)
        while True:
            try:
                id = int(input("Unesite id apartmana -> "))
                break
            except ValueError:
                print("Pogresan unos")

        if ispis_apartmana(id, korisnik):
            header = ["Tip", "Broj soba", "Broj osoba", "Geografska sirina", "Geografska duzina", "Adresa", "Cena", "Status", "Sadrzaji", "Slobodni datumi"]
            for i in range(len(header)):
                print(f"{i+1}. {header[i]}")

            while True:
                unos = input("Unesite sta zelite da izmenite (brojevi odvojeni zarezom) -> ")
                elementi = unos.split(",")
                mogucnosti = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

                pogresan = False
                for el in elementi:
                    if el not in mogucnosti:
                        print(f"Ne postoji element sa brojem '{el}'. Potrebno je uneti brojeve odvojene razmakom (npr. 2,4,7)")
                        pogresan = True
                if not pogresan:
                    break

            tip = ""
            broj_soba, broj_gostiju, sirina, duzina, cena = 0, 0, 0, 0, 0
            adresa = ""
            status = ""
            sadrzaji = ""

            with open("apartmani.txt") as apartmani:
                for linija in apartmani.readlines():
                    lista = linija.split("|")
                    if int(lista[0]) == id:
                        tip = lista[1]
                        broj_soba = int(lista[2])
                        broj_gostiju = int(lista[3])
                        sirina = float(lista[4])
                        duzina = float(lista[5])
                        adresa = lista[6]
                        cena = int(lista[8])
                        status = lista[9]
                        sadrzaji = lista[10]
                        break

            for el in elementi:
                if el == "1":
                    while True:
                        tip = input("Unesite tip apartmana (soba ili apartman) -> ")
                        if tip.lower() == "soba" or tip.lower() == "apartman":
                            break
                elif el == "2":
                    while True:
                        try:
                            broj_soba = int(input("Unesite broj soba -> "))
                            break
                        except ValueError:
                            print("Potrebno je uneti broj")
                elif el == "3":
                    while True:
                        try:
                            broj_gostiju = int(input("Unesite broj gostiju -> "))
                            break
                        except ValueError:
                            print("Potrebno je uneti broj")
                elif el == "4":
                    while True:
                        try:
                            sirina = float(input("Unesite geografsku sirinu na kojoj se nalazi apartman -> "))
                            break
                        except:
                            print("Potrebno je uneti decimalni broj")
                elif el == "5":
                    while True:
                        try:
                            duzina = float(input("Unesite geografsku duzinu na kojoj se nalazi apartman -> "))
                            break
                        except:
                            print("Potrebno je uneti decimalni broj")
                elif el == "6":
                    while True:  
                        greska = False
                        adresa = input("Unesite adresu (Ulica i broj, mesto, postanski broj) -> ")
                        lista = adresa.split(",")
                        if len(lista) != 3:
                            greska = True
                            print("Niste uneli sve informacije")
                        if not greska:
                            try:
                                broj = lista[2][1:]
                                postanski_broj = int(broj)
                            except ValueError:
                                greska = True
                                print("Pogresan postanski broj")
                        if not greska:
                            break
                elif el == "7":
                    while True:
                        try:
                            cena = int(input("Unesite cenu po noci -> "))
                            break
                        except:
                            print("Potrebno je uneti broj")
                elif el == "8":
                    while True:
                        status = input("Unesite status (Aktivan/Neaktivan) -> ")
                        if status.lower() == "neaktivan":
                            status = "Neaktivan"
                            break
                        elif status.lower() == "aktivan":
                            status = "Aktivno"
                            break
                        else:
                            print("Potrebno je uneti 'akitvan' ili 'neaktivan'") 
                elif el == "9":
                    sadrzaji = Sadrzaji()
                    sadrzaji += "\n"
                elif el == "10":
                    with open("datumi.txt") as datumi_fajl:
                        linije = datumi_fajl.readlines()
                    with open("datumi.txt", "w") as datumi_fajl:
                        for linija in linije:
                            lista = linija.split("|")
                            if int(lista[0]) != id:
                                datumi_fajl.write(linija)
                    datumi = Termini(id)

            ###treba podatke ubaciti i izmeniti u fajlu
            with open("apartmani.txt") as apartmani:
                linije = apartmani.readlines()
            with open("apartmani.txt", "w") as apartmani:
                for linija in linije:
                    lista = linija.split("|")
                    if int(lista[0]) != id:
                        apartmani.write(linija)
                    else:
                        apartmani.write(f"{id}|{tip}|{broj_soba}|{broj_gostiju}|{sirina}|{duzina}|{adresa}|{korisnik}|{cena}|{status}|{sadrzaji}")
            print("Izmena uspesno obavljena")

        while True:
            jos = input("\nDa li zelite da izmenite jos apartmana? (d/n) -> ")
            if jos.lower() == "n":
                kraj = True
                break
            elif jos.lower() != "d":
                print("Potrebno je ukucati 'd' ili 'n'")
            else:
                break


def brisanje_apartmana(korisnik):
    print(
'''
          BRISANJE APARTMANA
         --------------------
'''        
    )
    prikaz_apartmana(korisnik)
    kraj = False
    while not kraj:
        while True:
            try:
                id = int(input("Unesite id apartmana koji zelite da obrisete -> "))
                break
            except ValueError:
                print("Potrebno je uneti broj")
        vraceno = ispis_apartmana(id, korisnik)
        if vraceno:
            potvrda = input("Da li zelite da obrisete ovaj apartman? (ukucajte 'da' ako zelite) -> ")
            if potvrda.lower() == "da":
                with open("apartmani.txt") as apartmani:
                    linije = apartmani.readlines()
                with open("apartmani.txt", "w") as apartmani:
                    for linija in linije:
                        lista = linija.split("|")
                        if int(lista[0]) != id:
                            apartmani.write(linija)
                with open("datumi.txt") as datumi:
                    linije = datumi.readlines()
                with open("datumi.txt", "w") as datumi:
                    for linija in linije:
                        lista = linija.split("|")
                        if int(linija[0]) != id:
                            datumi.write(linija)
                with open("rezervacije.txt") as rezervacije:
                    linije = rezervacije.readlines()
                with open("rezervacije.txt", "w") as rezervacije:
                    for linija in linije:
                        lista = linija.split("|")
                        if int(lista[1]) != id:
                            rezervacije.write(linija)
                print("Obrisano")
        while True:
                jos = input("\nDa li zelite da obrisete jos apartmana? (d/n) -> ")
                if jos.lower() == "n":
                    kraj = True
                    break
                elif jos.lower() != "d":
                    print("Potrebno je ukucati 'd' ili 'n'")
                else:
                    break


def pregled_rezervacija(korisnik):
    print(
'''
          PREGLED REZERVACIJA
         ---------------------
'''
    )
    nepotvrdjene = ["Kreirana", "Odustanak"]
    header = ["ID rezervacije", "ID apartmana", "Korisnik", "Gosti", "Adresa", "Cena", "Datum", "Status"]
    ispis = []
    with open("rezervacije.txt") as rezervacije:
        linije = rezervacije.readlines()
        for linija in linije:
            lista = linija.split("|")
            if lista[3] == korisnik and lista[-1].replace("\n", "") in nepotvrdjene:
                ispis.append([lista[0], lista[1], lista[2], lista[7], lista[6], lista[5], lista[4], lista[-1]])
    print(tabulate(ispis, headers=header, stralign="center", numalign="center", tablefmt="grid"))

def potvrda_odbijanje_rezervacija(korisnik):
    print(
'''
          POTVRDA I ODBIJANJE REZERVACIJA
         ---------------------------------
'''
    )
    header = ["ID rezervacije", "ID apartmana", "Korisnik", "Gosti", "Adresa", "Cena", "Datum"]
    ispis = []
    with open("rezervacije.txt") as rezervacije:
        linije = rezervacije.readlines()
        for linija in linije:
            lista = linija.split("|")
            if lista[3] == korisnik and lista[-1].replace("\n", "") == "Kreirana":
                ispis.append([lista[0], lista[1], lista[2], lista[7], lista[6], lista[5], lista[4]])
    print(tabulate(ispis, headers=header, stralign="center", numalign="center", tablefmt="grid"))

    pronadjeno = False
    while True:
        try:
            unos = int(input("Ukucajte id rezervacije -> "))
            for el in ispis:
                if int(el[0]) == unos:
                    pronadjeno = True
            if pronadjeno:
                break
            else:
                raise ValueError
        except ValueError:
            print("Potrebno je ukucati jedan od ponudjenih id rezervacije")

    with open("rezervacije.txt") as rezervacije:
        linije = rezervacije.readlines()
    
    while True:
        unos1 = input("Unesite da li zelite da prihvatite ili odbijete rezervaciju (p/o) -> ")
        if unos1.lower() == "p":
            with open("rezervacije.txt", "w") as rezervacije:
                for linija in linije:
                    lista = linija.split("|")
                    if int(lista[0]) == unos:
                        datum = datetime.date.today()
                        rezervacije.write(f"{lista[0]}|{lista[1]}|{lista[2]}|{lista[3]}|{lista[4]}|{lista[5]}|{lista[6]}|{lista[7]}|Prihvacena, {datum.day}.{datum.month}.{datum.year}\n")
                    else:
                        rezervacije.write(linija)
            break
        elif unos1.lower() == "o":
            with open("rezervacije.txt", "w") as rezervacije:
                for linija in linije:
                    lista = linija.split("|")
                    if int(lista[0]) == unos:
                        rezervacije.write(f"{lista[0]}|{lista[1]}|{lista[2]}|{lista[3]}|{lista[4]}|{lista[5]}|{lista[6]}|{lista[7]}|Odbijena\n")
                        with open("datumi.txt", "a") as datumi:
                            datumi.write(f"{lista[1]}|{lista[4]}\n")
                    else:
                        rezervacije.write(linija)
            za_gosta.spajanje_datuma()
            break
        else:
            print("Potrebno je uneti 'p' ili 'o'")

