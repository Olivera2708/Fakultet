from tabulate import tabulate

#zadatak1
# def napravitabelu(v_min, v_max, t_min, t_max):
#     tabela = []
#     for i in range(v_min, v_max+1):
#         tab = [i]
#         for j in range(t_min, t_max+1):
#             formula = 3.74+0.6215*i-35.75*(j**0.16)+0.4275*i*(j**0.16)
#             tab.append(formula)
#         tabela.append(tab)
#     headers = [" "]
#     for i in range(t_min, t_max+1):
#         headers.append(i)
#     print(tabulate(tabela,headers))

# unos = input("Unesite sa razmakom -> ").split(" ")
# napravitabelu(int(unos[0]), int(unos[1]), int(unos[2]), int(unos[3]))
    
#zadatk2
# def brojGodina(kamata):
#     godina = 0
#     krajnje = 1
#     while krajnje < 2:
#         godina += 1
#         krajnje += krajnje*kamata 
#     return godina

# print(brojGodina(0.04))

#zadatak3
# def sirakuza(broj):
#     lista = [broj]
#     for i in range(broj):
#         if lista[i] % 2 == 0:
#             lista.append(lista[i]//2)
#         else:
#             lista.append(3*lista[i]+1)
#     return lista

# print(sirakuza(5))