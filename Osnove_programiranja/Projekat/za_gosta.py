from tabulate import tabulate
import za_sve
import datetime


def kalkulator_cene(cena, datum, unos_dana, dodatni_popust):
    ukupna_cena = 0
    vikend = [4, 5, 6]
    for i in range(unos_dana):
        vikend_popust = 1
        praznicni_popust = 1
        if (datum + datetime.timedelta(days=i)).weekday() in vikend:
            vikend_popust = 90/100
        with open("praznici.txt") as praznici:
            for linija in praznici.readlines():
                lista = linija.split("|")
                dan, mesec, godina = lista[1].replace("\n", "").split(".")
                trenutni = datetime.date(int(godina), int(mesec), int(dan))
                if trenutni == (datum + datetime.timedelta(days=i)):
                    praznicni_popust = 105/100
        ukupna_cena += cena*vikend_popust*praznicni_popust
    if dodatni_popust:
        ukupna_cena *= 95/100
    return ukupna_cena

def spajanje_datuma():
    za_upis = []
    za_brisanje = []
    with open("datumi.txt") as datumi:
        linije = datumi.readlines()
    for linija1 in linije:
        if linija1 in za_brisanje:
            continue
        spojen = False
        lista1 = linija1.split("|")
        poc_kraj1 = lista1[1].split("-")
        poc1 = poc_kraj1[0]
        dan, mesec, godina = poc1.split(".")
        poc11 = datetime.date(int(godina), int(mesec), int(dan))
        kraj1 = poc_kraj1[1]
        dan, mesec, godina = kraj1.split(".")
        kraj11 = datetime.date(int(godina), int(mesec), int(dan))
        for linija2 in linije:
            if linija2 in za_brisanje:
                continue
            lista2 = linija2.split("|")
            poc_kraj2 = lista2[1].split("-")
            poc2 = poc_kraj2[0]
            dan, mesec, godina = poc2.split(".")
            poc22 = datetime.date(int(godina), int(mesec), int(dan))
            kraj2 = poc_kraj2[1]
            dan, mesec, godina = kraj2.split(".")
            kraj22 = datetime.date(int(godina), int(mesec), int(dan))
            if lista1[0] == lista2[0]:
                if poc1 == kraj2.replace("\n", ""):
                    za_upis.append(f"{lista1[0]}|{poc2}-{kraj1}")
                    spojen = True
                elif poc2 == kraj1.replace("\n", ""):
                    ima = False
                    for linija3 in linije:
                        if linija3 in za_brisanje:
                            continue
                        lista3 = linija3.split("|")
                        poc_kraj3 = lista3[1].split("-")
                        poc3 = poc_kraj3[0]
                        kraj3 = poc_kraj3[1]
                        if kraj2.replace("\n", "") == poc3 and lista3[0] == lista1[0]:
                            za_upis.append(f"{lista1[0]}|{poc1}-{kraj3}")
                            za_brisanje.append(f"{lista1[0]}|{poc2}-{kraj2}")
                            za_brisanje.append(f"{lista1[0]}|{poc3}-{kraj3}")
                            ima = True
                    if not ima:
                        za_upis.append(f"{lista1[0]}|{poc1}-{kraj2}")
                    spojen = True
                elif (poc11 >= poc22 and kraj11 < kraj22) or (poc11 > poc22 and kraj11 <= kraj22):
                    spojen = True
                elif poc22 < kraj11 and poc22 > poc11:
                    za_upis.append(f"{lista1[0]}|{poc1}-{kraj2}")
                    spojen = True
                elif kraj22 < kraj11 and kraj22 > poc11:
                    za_upis.append(f"{lista1[0]}|{poc2}-{kraj1}")
        if not spojen:
            za_upis.append(linija1)
    za_upis = list(dict.fromkeys(za_upis)) ##resavanje duplikata
    konacna = [el for el in za_upis if el not in za_brisanje]
    with open("datumi.txt", "w") as datumi:
        for el in konacna:
            datumi.write(el)
                    

def rezervisanje_apartmana(korisnik):
    kraj = False
    while not kraj:
        print(
'''
          REZERVACIJA APARTMANA
         -----------------------
'''       
        )

        print(
'''1. Pretraga apartmana
2. Unos id apartmana
'''
        )
        while True:
            try:
                unos = int(input("Izaberite opciju -> "))
                if unos < 3:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Potrebno je uneti broj opcije koju zeite da upotrebite")
        if unos == 1:
            za_sve.pretraga_apartmana(2)
        while True:
                try:
                    unos1 = int(input("Unesite id apartmana koji zelite da rezervisete -> "))
                    break
                except ValueError:
                    print("Potrebno je uneti broj")

        #provera jel id postoji i da li je aktivan
        postoji = False
        aktivan = False
        cena = 0
        domacin = ""
        adresa = ""
        kraj = False
        with open("apartmani.txt") as apartmani:
            for linija in apartmani.readlines():
                lista = linija.split("|")
                if int(lista[0]) == unos1 and lista[-2] == "Neaktivno":
                    print("Izabrani apartman je neaktivan.")
                    kraj = True
                elif int(lista[0]) == unos1:
                    cena = int(lista[8])
                    domacin = lista[7]
                    adresa = lista[6]
                    postoji = True
                    aktivan = True
            if kraj:
                pass
            elif not postoji and aktivan:
                print("Ne postoji apartman sa unetim id")
            else:
                ne_sort_termini = []
                termini = []
                with open("datumi.txt") as datumi:
                    for linija in datumi.readlines():
                        lista = linija.split("|")
                        if int(lista[0]) == unos1:
                            #provera da li je u narednih mesec dana pocetak termina i sort od najblizeg
                            poc_kraj = lista[1].split("-")
                            poc_lista = poc_kraj[0].split(".")
                            pocetni = datetime.date(int(poc_lista[2]), int(poc_lista[1]), int(poc_lista[0]))
                            if pocetni <= datetime.date.today() + datetime.timedelta(days=30):
                                #cuvanje termina koji su zadovoljili uslove redom
                                ne_sort_termini.append(pocetni)
                #sortiranje
                ne_sort_termini.sort()
                for el in ne_sort_termini:
                    with open("datumi.txt") as datumi:
                        for linija in datumi.readlines():
                            lista = linija.split("|")
                            poc_kraj = lista[1].split("-")
                            if poc_kraj[0] == f"{el.day}.{el.month}.{el.year}" and unos1 == int(lista[0]):
                                termini.append([lista[1]])
                if termini == []:
                    print("Za izabrani apartman trenutno nema slobodnih termina")
                else:
                    print(tabulate(termini, headers=["Slobodni termini"], stralign="center", numalign="center", tablefmt="grid"))

                    #unos datuma i broja dana
                    while True:
                        try:
                            unos_datum = input("Unesite datum pocetka rezervacije (dd.mm.gggg)-> ")
                            v_od = unos_datum.split(".")
                            dan = int(v_od[0])
                            mesec = int(v_od[1])
                            godina = int(v_od[2])
                            datum = datetime.date(godina, mesec, dan)
                            break
                        except (ValueError, IndexError) as error:
                            print("Los unos datuma")
                    while True:
                        try:
                            unos_dana = int(input("Unesite broj dana -> "))
                            break
                        except ValueError:
                            print("Potrebno je uneti broj")

                    #provera jel postoji termin koji odgovara uslovima
                    postoji = False
                    for el in termini:
                        poc_kraj = el[0].split("-")
                        dp, mp, gp = poc_kraj[0].split(".")
                        dk, mk, gk = poc_kraj[1].split(".")
                        poc_dat = datetime.date(int(gp), int(mp), int(dp))
                        kraj_dat = datetime.date(int(gk), int(mk), int(dk.replace("\n", "")))
                        if poc_dat <= datum <= kraj_dat and datum + datetime.timedelta(days=unos_dana) <= kraj_dat:
                            postoji = True
                            break
                    if not postoji:
                        print("Ne postoji slobodan termin za unete parametre")
                    else:
                        sve_uneto = False
                        gosti = []
                        br = 1
                        max_broj_osoba = 0
                        print("Unesite imena i prezimena ostalih gostiju, pritisnite enter kada zavrsite sa unosom")
                        with open("apartmani.txt") as apartmani:
                            for linija in apartmani.readlines():
                                lista = linija.split("|")
                                if int(lista[0]) == unos1:
                                    max_broj_osoba = int(lista[3])
                        while not sve_uneto:
                            if br == max_broj_osoba:
                                print("Uneli ste maksimalan broj osoba za ovaj smestaj")
                                break
                            gost = input(f"{br}. ")
                            if gost == "":
                                sve_uneto = True
                            else:
                                gosti.append(gost)
                                br += 1

                        while True:
                            potvrda = input("\nDa li potvrdjujete rezervaciju? (d/n) -> ")
                            if potvrda == "d":
                                #azuriranje dostupnih termina
                                with open("datumi.txt") as datumi:
                                    linije = datumi.readlines()
                                with open("datumi.txt", "w") as datumi:
                                    for linija in linije:
                                        lista = linija.split("|")
                                        poc_kraj = lista[1].split("-")
                                        dp, mp, gp = poc_kraj[0].split(".")
                                        dk, mk, gk = poc_kraj[1].split(".")
                                        poc_dat = datetime.date(int(gp), int(mp), int(dp))
                                        kraj_dat = datetime.date(int(gk), int(mk), int(dk.replace("\n", "")))
                                        if datum < poc_dat or datum > kraj_dat or int(lista[0]) != unos1:
                                            datumi.write(linija)
                                        else:
                                            novi = poc_dat + datetime.timedelta(days=unos_dana)
                                            if datum == poc_dat and novi != kraj_dat:
                                                datumi.write(f"{unos1}|{novi.day}.{novi.month}.{novi.year}-{poc_kraj[1]}")
                                            else:
                                                if poc_dat != datum:
                                                    datumi.write(f"{unos1}|{poc_kraj[0]}-{unos_datum}\n")
                                                novi = datum + datetime.timedelta(days=unos_dana)
                                                if novi != kraj_dat:
                                                    datumi.write(f"{unos1}|{novi.day}.{novi.month}.{novi.year}-{poc_kraj[1]}")
                                novi = datum + datetime.timedelta(days=unos_dana)
                                #upis u fajl rezervacije
                                dodatni_popust = False
                                with open("rezervacije.txt") as rezervacije:
                                    linije = rezervacije.readlines()
                                    try:
                                        id_rezervacije = int(linije[-1].split("|")[0]) + 1
                                    except IndexError:
                                        id_rezervacije = 1
                                    for linija in linije:
                                        lista = linija.split("|")
                                        if lista[2] == korisnik:
                                            dodatni_popust = True
                                with open("rezervacije.txt", "a") as rezervacije:
                                    #id_rezervacije, id_apartmana, korisnik, domacin, rezervisan_datum, potrebno_platiti, adresa, imena_gostiju, status
                                    #cena
                                    ukupna_cena = kalkulator_cene(cena, datum, unos_dana, dodatni_popust)
                                    imena_gostiju = ""
                                    for ime in gosti:
                                        imena_gostiju += f"{ime}, "
                                    imena_gostiju = imena_gostiju[:-2]
                                    rezervacije.write(f"{id_rezervacije}|{unos1}|{korisnik}|{domacin}|{unos_datum}-{novi.day}.{novi.month}.{novi.year}|{int(ukupna_cena)}|{adresa}|{imena_gostiju}|Kreirana\n")
                                break
                            elif potvrda != "n":
                                print("Potrebno je ukucati 'd' ili 'n'")
                            else:
                                print("Otkazano")

                        while True:
                            print("\nNa svaku sledecu rezervaciju imate 5% popusta")
                            jos = input("Da li zelite da rezervisete jos apartmana? (d/n) -> ")
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
    header = ["ID rezervacije", "ID apartmana","Gosti", "Mesto", "Cena", "Datum", "Status"]
    ispis = []
    with open("rezervacije.txt") as rezervacije:
        for linija in rezervacije.readlines():
            lista = linija.split("|")
            if lista[2] == korisnik:
                ispis.append([lista[0], lista[1], lista[7], lista[6], lista[5], lista[4], lista[-1]])
    print(tabulate(ispis, headers=header, stralign="center", numalign="center", tablefmt="grid"))

def ponistavanje_rezervacije(korisnik):
    pregled_rezervacija(korisnik)
    postoji = False
    odustao = False
    rezervisan_datum = ""
    while True:
        try:
            unos = input("Unesite ID rezervacije koju zelite da ponistite (0 za odustanak) -> ")
            if unos == "0":
                odustao = True
                break
            with open("rezervacije.txt") as rezervacije:
                linije = rezervacije.readlines()
                for linija in linije:
                    lista = linija.split("|")
                    if lista[0] == unos and lista[-1].replace("\n", "") == "Kreirana":
                        rezervisan_datum = lista[4]
                        postoji = True
                        break
            if postoji:
                break
            else:
                raise ValueError
        except ValueError:
            print("Potrebno je uneti ID (broj) rezervacije koja ima status 'Kreirana'")
    if not odustao:
        while True:
            id_apartmana = 0
            unos1 = input("Da li ste sigurni da zelite da ponistite rezervaciju? (d/n) -> ")
            if unos1.lower() == "d":
                #ponistavam
                with open("rezervacije.txt", "w") as rezervacije:
                    for linija in linije:
                        lista = linija.split("|")
                        if lista[0] == unos:
                            id_apartmana = lista[1]
                            rezervacije.write(f"{lista[0]}|{lista[1]}|{lista[2]}|{lista[3]}|{lista[4]}|{lista[5]}|{lista[6]}|{lista[7]}|Odustanak\n")
                        else:
                            rezervacije.write(linija)
                #vracanje datuma
                with open("datumi.txt", "a") as datumi:
                    datumi.write(f"{id_apartmana}|{rezervisan_datum}\n")
                #spajanje datuma
                spajanje_datuma()
                print("Rezervacija otkazana")
                break
            elif unos1.lower() != "n":
                print("Potrebno je ukucati 'd' ili 'n'")
            else:
                break
            