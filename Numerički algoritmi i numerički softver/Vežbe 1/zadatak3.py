import numpy as np

def minVektor(matrix):
    x, y = matrix.shape
    nula = np.zeros(x)

    for i in range(x):
        nula[i] = nadjiMin(matrix.T[i], y)

    return nula

def nadjiMin(matrixPart, y):
    index = 0
    mini = matrixPart[0]
    for j in range(y):
        if matrixPart[j] < mini:
            mini = matrixPart[j]
            index = j

    return index

if __name__ == "__main__":
    a = np.array([[-2, 5, -3],
                  [-1, -1, 0],
                  [-3, -5, 1]])

    print(minVektor(a))