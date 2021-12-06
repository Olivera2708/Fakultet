#zadatak1
# def racunanjeZarade(file, sat):
#     with open(file) as f:
#         fajl = f.readlines()
#         for linija in fajl:
#             info = linija.replace("\n", "").split("|")
#             num = 0
#             for i in range(1, 6):
#                 num += int(info[i])
#             if num > 40:
#                 zarada = num*1.5*sat
#             else:
#                 zarada = num*sat
#             print(f"ime: {info[0]}\nzarada: {zarada}")
# racunanjeZarade("radnici.txt", 1000)

#zadatak2
# def ocenjivanje(bodovi):
#     if bodovi > 94:
#         return 10
#     elif bodovi > 84:
#         return 9
#     elif bodovi > 74:
#         return 8
#     elif bodovi > 64:
#         return 7
#     elif bodovi > 54:
#         return 6
#     else:
#         return 5
# print(ocenjivanje(77))

#zadatak3
# def indeksTelesneMase(masa, visina):
#     bmi = masa/visina**2
#     if bmi < 18.5:
#         return "Pothranjenost"
#     elif bmi < 25:
#         return "Idealna telesna masa"
#     elif bmi <=30:
#         return "Preterana telesna masa"
#     else:
#         return "Gojaznost"
# print(indeksTelesneMase(81,1.8))

#zadatak4
# def kazna(brzina, ogranicenje):
#     if brzina > ogranicenje:
#         sat = (brzina-ogranicenje)*500
#         if brzina > 120:
#             return f"Vasa kazna iznosi {sat + 5000 + 10000}din"
#         else:
#             return f"Vasa kazna iznosi {sat + 5000}din"
#     else:
#         return "Niste prekoracili brzinu"
# print(kazna(130,60))

#zadatak5
# def dadilja(pocetak, kraj):
#     pocetak = pocetak.split(":")
#     pocetak = [int(el) for el in pocetak]
#     kraj = kraj.split(":")
#     kraj = [int(el) for el in kraj]
#     if kraj[0] >= 21 and pocetak[0] <= 21:
#         jeftinije = (21 - pocetak[0] - 1 + (60-pocetak[1])/60)*150
#         skuplje = (kraj[0]-21 + kraj[1]/60)*100
#         ukupno = jeftinije + skuplje 
#     elif pocetak > 21:
#         if kraj[1] >= kraj[0]:
#             ukupno = (kraj[0] - pocetak[0] + (kraj[1]-pocetak[1])/60)*100
#         else:
#             ukupno = (kraj[0] - pocetak[0] - 1 + (kraj[1]-pocetak[1])/60)*100
#     else:
#         if kraj[1] >= kraj[0]:
#             ukupno = (kraj[0] - pocetak[0] + (kraj[1]-pocetak[1])/60)*150
#         else:
#             ukupno = (kraj[0] - pocetak[0] - 1 + (kraj[1]-pocetak[1])/60)*150
#     return int(round(ukupno))
# print(dadilja("18:35", "22:50"))

#zadatak6
# def uskrs(godina):
#     if godina < 1982 or godina > 2048:
#         return "Nije uneta godina u opsegu"
#     a = godina % 19
#     b = godina % 4
#     c = godina % 7
#     d = (19 * a + 24) % 30
#     e = (2*b + 4*c + 6*d + 5) % 7
#     datum = 22 + d + e
#     if datum > 31:
#         return f"Datum je {datum-31}. april"
#     else:
#         return f"Datum je {datum}. mart"
# print(uskrs(2011))

#zadatak7
# def uskrs(godina):
#     godine = [1954, 1981, 2049, 2076]
#     if godina < 1900 or godina > 2099:
#         return "Nije uneta godina u opsegu"
#     a = godina % 19
#     b = godina % 4
#     c = godina % 7
#     d = (19 * a + 24) % 30
#     e = (2*b + 4*c + 6*d + 5) % 7
#     datum = 22 + d + e
#     if godina in godine:
#         datum -= 7
#     if datum > 31:
#         return f"Datum je {datum-31}. april"
#     else:
#         return f"Datum je {datum}. mart"
# print(uskrs(2011))

#zadatak8
# def prestupna(godina):
#     return (godina % 4 == 0 and godina % 100 != 0) or godina % 400 == 0
# print(prestupna(1984))

#zadatak9
# def provera(datum):
#     datumi = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     datum = datum.split("/")
#     datum = [int(el) for el in datum]
#     if datum[1] == 2:
#         if prestupna(datum[2]) and datum[0] < 30:
#             return True
#         elif not prestupna(datum[2]) and datum[0] < 29:
#             return True
#         return False
#     elif datum[1] <= 12 and datum[0] <= datumi[datum[1]-1]:
#         return True
#     else:
#         return False
# print(provera("31/2/1962"))

#zadatak10
# def rednibr(datum):
#     datumi = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     broj = 0
#     datum = datum.split("/")
#     datum = [int(el) for el in datum]
#     for i in range(datum[1]-2):
#         broj += datumi[i]
#     broj += datum[0]
#     if prestupna(datum[2]) and datum[1] > 2:
#         broj += 1
#     return broj
# print(rednibr("25/12/2021"))
