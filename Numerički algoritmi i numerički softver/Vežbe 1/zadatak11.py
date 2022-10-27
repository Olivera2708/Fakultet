import numpy as np
import math

def stocksShare(years, total_stocks):
    nula = np.zeros(years.shape[0])
    suma = 0
    one = 0

    for i in range(years.shape[0]):
        suma += years[i]
    
    one = total_stocks/suma

    for i in range(years.shape[0]):
        nula[i] = one * years[i]


    return nula

if __name__ == "__main__":
    years = np.array([2, 3, 4, 6, 1, 2, 4, 8])

    print(stocksShare(years, 1000))
