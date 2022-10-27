import numpy as np

def maxVektor(matrix):
    x, y = matrix.shape
    nula = np.zeros(x)

    for i in range(x):
        nula[i] = nadjiMax(matrix[i], y)

    return nula

def nadjiMax(matrixPart, y):
    index = 0
    maxi = matrixPart[0]
    for j in range(y):
        if matrixPart[j] > maxi:
            maxi = matrixPart[j]
            index = j

    return index

if __name__ == "__main__":
    a = np.array([[-2, 5, -3],
                  [-1, -1, 0],
                  [-3, -5, 1]])

    print(maxVektor(a))