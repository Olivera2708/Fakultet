import numpy as np

def fibonaciVektor(n):
    lista = [1, 1]

    for i in range(n-2):
        lista.append(lista[i] + lista[i+1])

    return np.array(lista)

print(fibonaciVektor(10))
    