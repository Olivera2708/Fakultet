evidencija = [{'broj_posiljke': '1', 'adresa': 'sdf', 'vrednost': 1200}, {'broj_posiljke': '2', 'adresa': 'dfg', 'vrednost': 2000}, {'broj_posiljke': '3', 'adresa': 'wer', 'vrednost': 200}, {'broj_posiljke': '4', 'adresa': 'ghj', 'vrednost': 450}, {'broj_posiljke': '5', 'adresa': 'ert', 'vrednost': 600}, {'broj_posiljke': '6', 'adresa': 'ert', 'vrednost': 750}]
def kreiraj6():
    kreirane = []
    for i in range(6):
        print("Naredna posiljka")
        recnik = {}
        recnik["broj_posiljke"] = input("Unesite broj posiljke -> ")
        recnik["adresa"] = input("Unesite adresu posiljke -> ")
        recnik["vrednost"] = int(input("Unesite vrednost posiljke -> "))
        kreirane.append(recnik)
    evidencija.extend(kreirane)

def najmanja_vrednost():
    index = 0
    mini = evidencija[0]["vrednost"]
    for i in range(len(evidencija)):
        if int(evidencija[i]["vrednost"]) < mini:
            index = i
            mini = int(evidencija[i]["vrednost"])
    print(f"Broj posiljke {evidencija[index]['broj_posiljke']}\nAdresa {evidencija[index]['adresa']}\nVrednost {evidencija[index]['vrednost']}")

def zaadresu(adresa):
    ukupno = 0
    for el in evidencija:
        if el["adresa"] == adresa:
            ukupno += el["vrednost"]
    return ukupno

def zaadrese():
    lista = []
    adrese = input("Unesite adrese odvojene razmakom -> ").split(" ")
    for adresa in adrese:
        recnik = {}
        recnik["adresa"] = adresa
        recnik["ukupno"] = zaadresu(adresa)
        lista.append(recnik)
    return lista

def najpopularnija():
    najpopularnija = evidencija[1]["adresa"]
    ukupno = 0
    for el in evidencija:
        if zaadresu(el["adresa"]) >= ukupno:
            ukupno = zaadresu(el["adresa"]) 
            najpopularnija = el["adresa"]
    return najpopularnija

print(najpopularnija())