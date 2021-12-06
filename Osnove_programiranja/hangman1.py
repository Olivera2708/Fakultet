import random

cikica = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def uzmi_rec(ime_fajla):
    with open(ime_fajla) as fajl:
        lista_reci = fajl.readlines()
        return random.choice(lista_reci).replace("\n", "")

def graficki_prikaz():
    print(cikica[zivot])
    print(f"{pogadja}\n")

def dodavanje_slova():
    broj = 0
    pomoc = ""
    for el in pogadja:
        if slovo == rec[broj]:
            pomoc += slovo
        else:
            pomoc += el
        broj += 1
    return pomoc

rec = uzmi_rec("dictionary.txt")
zivot = 6
vec_ukucao = []
pogadja = ""
for s in rec:
   pogadja += "_"
graficki_prikaz()

while 1:
    string = ""
    for el in vec_ukucao:
        string += f" {el.lower()}" 
    print(f"Ukucana slova su:{string}")
    while 1:
        slovo = input("Predlog slova -> ").upper()
        if slovo.isalpha() and len(slovo) == 1 and slovo not in vec_ukucao:
            vec_ukucao.append(slovo)
            break
        elif slovo in vec_ukucao:
            print("Vec ste uneli ovo slovo")
        else:
            print("Unos nije dobar, unesite jedno slovo")

    if slovo not in rec:
        print(f"Slovo {slovo} se ne nalazi u reci")
        zivot -= 1
        if zivot == 0:
            print(cikica[0])
            print(f"Izgubio si, nemas vise zivota!\nRec je bila {rec}")
            break
        else:
            print(f"Broj preostalih zivota je {zivot}")

    pogadja = dodavanje_slova()
    graficki_prikaz()
    if "_" not in pogadja:
        print("Pogodio si rec!")
        break