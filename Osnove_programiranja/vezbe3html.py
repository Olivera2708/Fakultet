#zadatak1 delioci
# br = int(input("Unesite broj -> "))
# for i in range(1, br//2 + 1):
#     if br % i == 0:
#         print(f"{i} ", end="")
# print("")

#zadatak2 prestupna godina
# godina = int(input("Unesite godinu -> "))
# if (godina % 4 == 0 and godina % 100 != 0) or godina % 400 == 0:
#     print("Godina je presturpna")
# else:
#     print("Godina nije prestupna")

#zadatak3 kamen, papir, makaze
# import random
# korisnik = int(input("Unesite 1 za kamen, 2 za papir, 3 za makaze. -> "))
# kompjuter = random.randint(1, 3)
# komp = ["kamen", "papir", "makaze"]
# print(f"Kompjuter je izabrao {komp[kompjuter - 1]}")
# if korisnik == 3 and kompjuter == 1:
#     print("Izgubio si")
# elif korisnik == 1 and kompjuter == 3:
#     print("Pobedio si")
# elif (korisnik == kompjuter):
#     print("Nereseno")
# elif (korisnik > kompjuter):
#     print("Pobedio si")
# else:
#     print("Izgubio si")