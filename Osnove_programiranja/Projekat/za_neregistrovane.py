import re


def registracija():
    print(
'''
          REGISTRACIJA KORISNIKA
         ------------------------
''')
    while True:
        korisnicko_ime = input("Unesite korisnicko ime -> ")
        if not zauzeto_ime(korisnicko_ime) and len(korisnicko_ime) > 4:
            break
        else:
            print("Izabrano korisnicko ime je zauzeto ili je krace od 4 karaktera")
    while True:
        lozinka = input("Unesite lozinku -> ")
        if len(lozinka) <= 5:
            print("Lozinka mora biti duza od 5 karaktera")
        else:
            break
    while True:
        telefon = input("Unesite kontakt telefon -> ")
        ## \d - bilo koji broj, \s - razmak, ? - jedan ili nula
        re_telefon = r'((0\d\d|\+\d\d\d)(\/|\s|-)?\d(-|\s)?\d(-|\s)?\d(-|\s)?\d(-|\s)?\d(-|\s)?\d(-|\s)?(\d)?)'
        if re.fullmatch(re_telefon, telefon):
            break
        else:
            print("Uneti broj telefona nije validan")
    while True:
        email = input("Unesite email -> ")
        mail_re = r'\S+@\S+.\S+'
        if re.fullmatch(mail_re, email):
            break
        else:
            print("Uneti email nije validan")
    while True:
        ime = input("Unesite ime -> ")
        if ime != "":
            break
    while True:
        prezime = input("Unesite prezime -> ")
        if prezime != "":
            break
    while True:
        pol = input("Unesite pol (musko/zensko) -> ")
        if pol.lower() == "musko" or pol.lower() == "zensko":
            break

    with open("korisnici.txt", "a") as korisnici:
        korisnici.write(f"{korisnicko_ime}|{lozinka}|{ime}|{prezime}|{pol.lower()}|{telefon}|{email}|Gost\n")

def zauzeto_ime(ime):
    with open("korisnici.txt") as korisnici:
        for linija in korisnici.readlines():
            lista = linija.split("|")
            if ime == lista[0]:
                return True
        return False