#zadatak1
# import random

# nasumican = random.randint(0, 9)
# pogodjen = False

# while not pogodjen:
#     unesi = int(input("Unesi broj -> "))
#     if not (0 <= unesi <= 9):
#         print("Unet broj van opsega") 
#     elif unesi == nasumican:
#         print("Bravo, pogodili ste broj")
#         pogodjen = True
#     elif unesi > nasumican:
#         print("Uneli ste preveliki broj")
#     else:
#         print("Uneli ste premali broj")



# #zadatak2
# donja_granica = int(input("Unesi donju granicu -> "))
# gornja_granica = int(input("Unesi gornju granicu -> "))

# while gornja_granica < donja_granica:
#     donja_granica = int(input("Unesi donju granicu -> "))
#     gornja_granica = int(input("Unesi gornju granicu -> "))

# pogodjeno = False

# while not pogodjeno:
#     pokusaj = (gornja_granica-donja_granica) // 2
#     odg = input(f"Da li je zamisljen broj {pokusaj}? d/v/m -> ")
#     if odg == "d":
#         pogodjeno = True
#         print("Pogodio sam")
#     elif odg =="v":
#         donja_granica = pokusaj
#     else:
#         gornja_granica = pokusaj
