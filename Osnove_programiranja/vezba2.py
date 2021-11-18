# #zadatak1
# print("Ovaj program pretvara temperaturu iz celzijusa u farenhajte")
# celsius = eval(input("Unesite temperaturu u C >> "))
# fahrenheit = 9/5 * celsius + 32
# print("Temperatura je", fahrenheit, "stepeni Farenhajta.")



# #zadatak2
# print("Izracunava prosek tri ocene.")

# score1, score2, score3 = eval(input("Unesite tri ocene razdvojene zarezom: "))
# average = (score1 + score2 + score3) / 3

# print("Prosecna ocena je:", average)



# #zadatak3
# print("Ovaj program izracunava stanje stednog racuna")
# broj_godina = int(input("Unesite broj godina: "))
# principal = eval(input("Unesite pocetni ulog: "))
# apr = eval(input("Unesite godisnju kamatu: "))
# for i in range(broj_godina):
#     principal = principal * (1 + apr)
# print(f"Stanje nakon {broj_godina} godina: {principal}")



# #zadatak4
# celsius = 0
# print("Celzijus      Farenhajt")
# while celsius <= 100:
#     fahrenheit = 9/5 * celsius + 32
#     print(f"{celsius}            {fahrenheit}")
#     celsius += 10



# #zadatak5
# farenhajt = int(input("Unesite temperaturu u F >> "))
# celzijus = (farenhajt - 32) * 5/9
# print("Temperatura je", celzijus, "stepeni Celzijusa.")



# #zadatak6
# broj_godina = int(input("Unesite broj godina: "))
# principal = eval(input("Unesite pocetni ulog: "))
# apr = eval(input("Unesite godisnju kamatu: "))
# inflation = eval(input("Unesite godisnji stepen inflacije:"))
# for i in range(broj_godina):
#     principal = principal * (1 + apr) / (1 + inflation)
# print(f"Stanje nakon {broj_godina} godina: {principal}")