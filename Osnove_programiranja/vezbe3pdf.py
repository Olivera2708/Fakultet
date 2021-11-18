#zadatak5
# import math
# r = int(input("Unesite poluprecnik -> "))
# v = 4/3*math.pi*r**3
# p = 4*math.pi*r**2
# print(f"Zapremina je {v:.2f}, a povrsina {p:.2f}")

#zadatak6
# import math
# r = int(input("Unesite poluprecnik pice -> "))
# kc = math.pi*r
# c = math.pi*r**2
# print(f"Cena po kvadratnom cm je {kc:.2f}, a cela pica je {c:.2f}")

#zadatak7
# H = 1.0079
# C = 12.011
# h, c = input("Unesite broj atoma vodonika, a zatim ugljenika -> ").split()
# masa = H*int(h) + int(c)*C
# print(f"Masa je {masa}")

#zadatak8
# C = 340
# t = int(input("Unesite broj sekundi -> "))
# s = C/t
# print(f"Udaljenost je {s:.2f} metara")

#zadatak9
# PO_KG = 105
# DO_PO_KG = 18
# FIKSNA = 15

# kafa = int(input("Unesite koliko kg kafe zelite -> "))
# cena = kafa*(PO_KG+DO_PO_KG) + FIKSNA
# print(f"Cena vase porudzbine je {cena} dinara")

#zadatak10
# x1, y1 = input("Unesite x1 i y1 -> ").split()
# x2, y2 = input("Unesite x2 i y2 -> ").split()
# m = (int(y2) + int(y1))/(int(x2) - int(x1))
# print(f"Nagib je {m}")

#zadatak11
# from math import sqrt 
# x1, y1 = input("Unesite x1 i y1 -> ").split()
# x2, y2 = input("Unesite x2 i y2 -> ").split()
# d = sqrt((int(x2)-int(x1))**2+(int(y2)-int(y1))**2)
# print(f"Rastojanje je {d:.2f}")

#zadatak12
# godina = int(input("Unesite godinu (4 cifre) -> "))
# c = godina/100
# epakt = (8+c/4-c+((8*c+13)/25)+11*(godina%19))%30
# print(f"Epakt je {epakt}")

#zadatak13
# import math
# s = 0
# a = []
# for i in range(3):
#     br = int(input("Unesite stranicu -> "))
#     a.append(br)
#     s += br
# s /= 2
# p = math.sqrt(s*(s-a[0])*(s-a[1])*(s-a[2]))
# print(f"Povrsina je {p:.2f}")

#zadatak14
# import math
# ugao = int(input("Unesite ugao -> "))
# visina = int(input("Unesite visinu -> "))
# d = visina/math.sin(ugao)
# print(f"Duzina merdevina je {d:.3f}")

#zadatak15
# n = int(input("Unesite n -> "))
# zbir = 0
# for i in range (1, n+1):
#     zbir += i
# print(f"Zbir prvih {n} brojeva je {zbir}")

#zadatak16
# n = int(input("Unesite n -> "))
# zbir = 0
# for i in range (1, n+1):
#     zbir += i**2
# print(f"Zbir kvadrata prvih {n} brojeva je {zbir}")

#zadatak17
# zbir = 0
# n = int(input("Unesite broj -> "))
# for i in range(n):
#     zbir += int(input("Unesite broj -> "))
# print(zbir)

#zadatak18
# zbir = 0
# n = int(input("Unesite broj -> "))
# for i in range(n):
#     zbir += int(input("Unesite broj -> "))
# print(f"Prosek je {zbir/n:.2f}")

#zadatak19
# n = int(input("Unesite n -> "))
# pi = 0
# br = 1
# for i in range(n):
#     if i % 2 == 0:
#         pi += 4/br
#     else:
#         pi -= 4/br
#     br += 2
# print(pi)

#zadatak20
# n = int(input("Unesite n (n > 2) -> "))
# prvi = 1
# drugi = 1
# for i in range(2, n):
#     pom = drugi
#     drugi += prvi
#     prvi = pom
# print(drugi)

#zadatak21
# import math
# x = int(input("Unesite broj koji zelite da korenujete -> "))
# n = int(input("Unesite broj iteracija -> "))
# guess = x/2
# for i in range(n):
#     if round(guess, 6) == round(math.sqrt(x), 6):
#         break
#     guess = (guess + x/guess)/2
# print(f"Dobijeno resenje je {guess}, a tacno resenje je {math.sqrt(x)}")