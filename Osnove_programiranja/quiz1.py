def postavi_pitanje():
    pitanje = lista_el[broj_pitanja].replace("\n", "").split("|")
    tacan_odg = [odgovor for odgovor in pitanje if "!" in odgovor]
    tacan = pitanje.index(tacan_odg[0])
    pitanje = [element.replace("!", "") for element in pitanje]
    return pitanje, tacan_odg, tacan
    

with open("quiz.txt") as fajl:
    lista_el = fajl.readlines()

broj_pitanja = 0
broj_bodova = 0

while 1:
    try:
        pitanje, tacan_odg, tacan = postavi_pitanje()
    except IndexError:
        print(f"\nNema vise pitanja.\nVas broj bodova je {broj_bodova}")
        break

    print(f"\n{pitanje[0]}")
    for i in range(1, len(pitanje)):
        print(f"{i}. {pitanje[i]}")

    while 1:
        try:
            odgovor = int(input("Unesite redni broj odgovora -> "))
        except ValueError:
            print("Unesite broj ispred odgovora")
        else:
            if len(pitanje) <= odgovor or odgovor <= 0:
                print("Uneseni broj nije u zadatom opsegu")
            else:
                break

    if odgovor == tacan:
        print("Tacan odgovor!")
        broj_bodova += 1
    else:
        print("Netacan odgovor!")
    
    while 1:
        pitanje_kraj = input("Da li zelite da zavrsite kviz? (da/ne) -> ")
        if pitanje_kraj == "da" or pitanje_kraj == "ne":
            break

    if pitanje_kraj == "da":
        print(f"\nVas broj bodova je {broj_bodova} od mogucnih {broj_pitanja + 1}")
        break
    broj_pitanja += 1