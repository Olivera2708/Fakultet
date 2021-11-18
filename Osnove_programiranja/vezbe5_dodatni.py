#zadatak1
# def palindrom(s):
#     s = s.lower()
#     r1 = 0
#     r2 = 0
#     for i in range(len(s)//2):
#         if s[i+r1] == " ":
#             r1 += 1
#         if s[-1-i-r2] == " ":
#             r2 += 1
#         if s[i+r1] != s[-i-1-r2]:
#             return False
#     return True

#zadatak2
# def duplikati(niz):
#     return list(dict.fromkeys(niz))

# print(duplikati(["a", "b", "a", "c"]))

#zadatak3
# def kalkulator(a, b, operacija):
#     if operacija == "+":
#         return a+b
#     elif operacija == "-":
#         return a-b
#     elif operacija == "*":
#         return a*b
#     elif operacija == "/":
#         return a/b
#     else:
#         print("Pogresna operacija")
