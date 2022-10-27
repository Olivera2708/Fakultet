import numpy as np

def zbirNesporedne(matrix):
    x, y = matrix.shape
    nula = np.zeros(x)

    for i in range(x):
        red = 0
        for j in range(y):
            if i != x-j-1:
                red += matrix[i][j]
        nula[i] = red

    return nula

if __name__ == "__main__":
    a = np.array([[-2, 5, -3],
                  [-1, -1, 0],
                  [-3, -5, 1]])

    print(zbirNesporedne(a))
