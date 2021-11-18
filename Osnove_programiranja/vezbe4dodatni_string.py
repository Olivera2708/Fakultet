#zadatak1
s = input("Unesite string -> ").lower()
provera = True
r1 = 0
r2 = 0
for i in range(len(s)//2):
    if s[i+r1] == " ":
        r1 += 1
    if s[-1-i-r2] == " ":
        r2 += 1
    if s[i+r1] != s[-i-1-r2]:
        provera = False
        break
if provera:
    print("Jeste")
else:
    print("Nije")

#zadatak2
import random
duzina = int(input("Unesite duzinu lozinke -> "))
lozinka = ""
for i in range(duzina):
    lozinka += chr(random.randint(33, 122))
print(f"Vasa lozinka je: {lozinka}")