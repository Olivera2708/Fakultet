def stanje(korisnik):
    stanje_korisnika = 0
    with open("bank_log.txt") as fajl:
        for linija in fajl.readlines():
            if korisnik in linija:
                if "income" in linija:
                    stanje_korisnika += float(linija.replace("\n", "").split(" ")[2])
                elif "withdrawal" in linija:
                    stanje_korisnika -= float(linija.replace("\n","").split(" ")[2])
    return stanje_korisnika

def najvise_novca():
    max_novac = 0
    max_osoba = ""
    with open("bank_log.txt") as fajl:
        for linija in fajl.readlines():
            trenutno = stanje(linija.split(" ")[0])
            if trenutno > max_novac:
                max_novac = trenutno
                max_osoba = linija.split(" ")[0]
    return max_osoba

def izbroj_uplate(korisnik):
    brojac = 0
    with open("bank_log.txt") as fajl:
        for linija in fajl.readlines():
            if korisnik in linija and "income" in linija:
                brojac += 1
    return brojac


def najvise_uplata():
    maximum = 0
    osoba = ""
    with open("bank_log.txt") as fajl:
        for linija in fajl.readlines():
            brojac = izbroj_uplate(linija.split(" ")[0])
            if brojac > maximum:
                maximum = brojac
                osoba = linija.split(" ")[0]
    return osoba

def u_minusu():
    osobe = ""
    prosli_kroz = []
    with open("bank_log.txt") as fajl:
        for linija in fajl.readlines():
            ime = linija.split(" ")[0]
            if ime not in prosli_kroz:
                prosli_kroz.append(ime)
                trenutno = stanje(ime)
                if trenutno < 0:
                    osobe += ime
                    osobe += ", "
    return osobe[:-2]

def pocinju_sa(pocinju):
    osobe = ""
    prosli_kroz = []
    with open("bank_log.txt") as fajl:
        for linija in fajl.readlines():
            ime = linija.split(" ")[0]
            if ime not in prosli_kroz:
                prosli_kroz.append(ime)
                if ime.startswith(pocinju):
                    osobe += ime
                    osobe += ", "
    return osobe[:-2]

def izvestaj():
    prosli_kroz = []
    with open("bank_log.txt") as fajl:
        for linija in fajl.readlines():
            if linija.split(" ")[0] not in prosli_kroz:
                prosli_kroz.append(linija.split(" ")[0])
    for element in prosli_kroz:
        with open("izvestaj.txt", "a") as fajl:
            fajl.write(f"Korisnik {element} ima na stanju {stanje(element):.2f} dinara.\n")


#pod a
korisnik = input("Unesite ime korisnika: ")
print(f"Stanje na racunu korisnika {korisnik} je {stanje(korisnik):.2f} dinara.")
#pod b
print(f"Najvise novca ima {najvise_novca()}")
#pod c
print(f"Korisnik sa najvecim brojem uplata je {najvise_uplata()}")
#pod d
print(f"Korisnici cije je stanje u minusu su: {u_minusu()}")
#pod e
pocinju = input("Unesite pocetni string: ")
print(f"Korisnici koji pocinju sa {pocinju} su {pocinju_sa(pocinju)}")
#pod f
izvestaj()

