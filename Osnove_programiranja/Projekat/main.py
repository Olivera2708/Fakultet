import za_sve
import za_neregistrovane
import za_domacina
import za_administratora
import za_gosta
import datetime


def datum():
    with open("datumi.txt") as datumi:
        linije = datumi.readlines()
    with open("datumi.txt", "w") as datumi:
        for linija in linije:
            lista = linija.split("|")
            poc_kraj = lista[1].split("-")
            dan, mesec, godina = poc_kraj[0].split(".")
            trenutni_p = datetime.date(int(godina), int(mesec), int(dan))
            dan, mesec, godina = poc_kraj[1].split(".")
            trenutni_k = datetime.date(int(godina), int(mesec), int(dan))
            if datetime.date.today() >= trenutni_k:
                continue
            elif datetime.date.today() >= trenutni_p:
                datumi.write(f"{lista[0]}|{datetime.date.today().day + 1}.{datetime.date.today().month}.{datetime.date.today().year}-{poc_kraj[1]}")
            else:
                datumi.write(linija)
    za_gosta.spajanje_datuma()


def zavrsene_rezervacije():
    with open("rezervacije.txt") as rezervacije:
        linije = rezervacije.readlines()
        for linija in linije:
            lista = linija.split("|")
            poc_kraj = lista[4].split("-")
            dan, mesec, godina = poc_kraj[1].split(".")
            kraj = datetime.date(int(godina), int(mesec), int(dan))
            dan, mesec, godina = poc_kraj[0].split(".")
            pocetak = datetime.date(int(godina), int(mesec), int(dan))
            with open("korisnici.txt") as korisnik:
                for line in korisnik.readlines():
                    lista1 = line.split("|")
                    if lista[2] == lista1[0] and lista[-1].replace("\n", "") == "Kreirana" and lista1[-1].replace("\n", "") == "Blokiran":
                        with open("rezervacije.txt", "w") as upis:
                            for line in linije:
                                lista_upis = line.split("|")
                                if lista_upis[0] == lista[0]:
                                    upis.write(f"{lista_upis[0]}|{lista_upis[1]}|{lista_upis[2]}|{lista_upis[3]}|{lista_upis[4]}|{lista_upis[5]}|{lista_upis[6]}|{lista_upis[7]}|Odustanak\n")
                                else:
                                    upis.write(line)
            if lista[-1].replace("\n", "") == "Kreirana" and datetime.date.today() + datetime.timedelta(days=1) >= pocetak:
                with open("rezervacije.txt", "w") as upis:
                    for line in linije:
                        lista_upis = line.split("|")
                        if lista_upis[0] == lista[0]:
                            upis.write(f"{lista_upis[0]}|{lista_upis[1]}|{lista_upis[2]}|{lista_upis[3]}|{lista_upis[4]}|{lista_upis[5]}|{lista_upis[6]}|{lista_upis[7]}|Odbijena\n")
                            with open("datumi.txt", "a") as datumi:
                                datumi.write(f"{lista_upis[1]}|{lista_upis[4]}")
                        else:
                            upis.write(line)
            elif "Prihvacena" in lista[-1] and datetime.date.today() > kraj:
                with open("rezervacije.txt", "w") as upis:
                    for line in linije:
                        lista_upis = line.split("|")
                        if lista_upis[0] == lista[0]:
                            upis.write(f"{lista_upis[0]}|{lista_upis[1]}|{lista_upis[2]}|{lista_upis[3]}|{lista_upis[4]}|{lista_upis[5]}|{lista_upis[6]}|{lista_upis[7]}|Zavrsena, {poc_kraj[1]}\n")
                        else:
                            upis.write(line)


def meni_za_sve(pocetni, prijavljen):
    za_sve_lista = ["Izlazak iz aplikacije", "Pregled aktivnih apartmana", "Pretraga apartmana", "Najpopularniji gradovi", "Prijava na sistem"]
    for el in za_sve_lista:
        if prijavljen != 0 and za_sve_lista[-1] == el:
            continue
        else:
            print(f"{pocetni}. {el}")
            pocetni += 1
    return pocetni

def meni_za_neregistrovane(pocetni):
    za_neregistrovane_lista = "Registracija"
    print(f"{pocetni}. {za_neregistrovane_lista}")

def meni_za_registrovane(pocetni):
    za_registrovane_lista = "Odjava"
    print(f"{pocetni}. {za_registrovane_lista}")

def meni_za_gosta(pocetni):
    pocetni += 1
    za_gosta_lista = ["Rezervacija apartmana", "Pregled rezervacija", "Ponistavanje rezervacija"]
    for el in za_gosta_lista:
        print(f"{pocetni}. {el}")
        pocetni += 1

def meni_za_domacina(pocetni):
    pocetni += 1
    za_domacina_lista = ["Dodajavanje apartmana", "Izmena podataka o apartmanu", "Brisanje apartmana", "Pregled rezervacija", "Potvrda ili odbijanje rezervacije"]
    for el in za_domacina_lista:
        print(f"{pocetni}. {el}")
        pocetni += 1

def meni_za_administratora(pocetni):
    pocetni += 1
    za_administratora_lista = ["Pretraga rezervacija", "Registracija domacina", "Kreiranje dodatne opreme", "Brisanje dodatne opreme", "Blokiranje korisnika", "Izvestaj", "Unos praznika"]
    for el in za_administratora_lista:
        print(f"{pocetni}. {el}")
        pocetni += 1

def broj_korisnika(korisnik):
    if korisnik == "Gost":
        return 1
    elif korisnik == "Domacin":
        return 2
    elif korisnik == "Administrator":
        return 3
    return 0


korisnik = ""
prijavljen = 0
vrsta_korisnika = ""
# 0 - neregistrovan, 1 - gost, 2 - domacin, 3 - admin
while True:
    zavrsene_rezervacije()
    datum()
    print(
'''
          MENI
         ------
''')
    pocetak = 1
    pocetak = meni_za_sve(pocetak, prijavljen)
    if prijavljen == 0:
        meni_za_neregistrovane(pocetak)
    else:
        meni_za_registrovane(pocetak)
    if prijavljen == 1:
        meni_za_gosta(pocetak)
    elif prijavljen == 2:
        meni_za_domacina(pocetak)
    elif prijavljen == 3:
        meni_za_administratora(pocetak)
    
    while True:
        try:
            unos = int(input("Izaberite sta zelite da radite -> "))
            break
        except ValueError:
            print("Potrebno je uneti broj!")
    
    #obrada za_sve
    if unos == 1:
        break
    elif unos == 2:
        za_sve.pregled_aktivnih_apartmana()
    elif unos == 3:
        za_sve.pretraga_apartmana(1)
    elif unos == 4:
        #najpopularniji gradovi
        za_sve.prikaz_10_najpopularnijih()
    elif unos == 5 and prijavljen == 0:
        vrsta_korisnika, korisnik = za_sve.prijava() 
    #obrada za neregistrovane
    elif unos == 6 and prijavljen == 0:
        za_neregistrovane.registracija()
    #obrada za registrovane
    elif unos == 5:
        vrsta_korisnika = ""
        korisnik = ""
        print("Odjavljeni ste")
    #obrada za gosta
    elif unos == 6 and prijavljen == 1:
        za_gosta.rezervisanje_apartmana(korisnik)
    elif unos == 7 and prijavljen == 1:
        za_gosta.pregled_rezervacija(korisnik)
    elif unos == 8 and prijavljen == 1:
        za_gosta.ponistavanje_rezervacije(korisnik)
    #obrada za domacina
    elif unos == 6 and prijavljen == 2:
        za_domacina.dodavanje_apartmana(korisnik)
    elif unos == 7 and prijavljen == 2:
        za_domacina.izmena_apartmana(korisnik)
    elif unos == 8 and prijavljen == 2:
        za_domacina.brisanje_apartmana(korisnik)
    elif unos == 9 and prijavljen == 2:
        za_domacina.pregled_rezervacija(korisnik)
    elif unos == 10 and prijavljen == 2:
        za_domacina.potvrda_odbijanje_rezervacija(korisnik)
    #obrada za administratora
    elif unos == 6 and prijavljen == 3:
        za_administratora.pretraga_registracija()
    elif unos == 7 and prijavljen == 3:
        za_administratora.registracija_novih_domacina()
    elif unos == 8 and prijavljen == 3:
        za_administratora.kreiranje_dodatne_opreme()
    elif unos == 9 and prijavljen == 3:
        za_administratora.brisanje_dodatne_opreme()
    elif unos == 10 and prijavljen == 3:
        za_administratora.blokiranje_korisnika()
    elif unos == 11 and prijavljen == 3:
        za_administratora.izvestaji()
    elif unos == 12 and prijavljen == 3:
        za_administratora.definisanje_praznika()
    else:
        print("Unesite jedan od ponudjenih brojeva")

    prijavljen = broj_korisnika(vrsta_korisnika)
    print("\n")
