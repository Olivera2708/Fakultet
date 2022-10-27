import numpy as np

def obrniNeparneKolone(matrix):
    x, y = matrix.shape
    nula = np.zeros((x, y))

    for i in range(x):
        if i % 2 == 0:
            for j in range(y)[::-1]:
                nula[i][x-1-j] = matrix.T[i][j]
        else:
            for j in range(y):
                nula[i][j] = matrix.T[i][j]

    return nula.T

if __name__ == "__main__":
    a = np.array([[-2, 5, -3],
                  [-1, -1, 0],
                  [-3, -5, 1]])

    print(obrniNeparneKolone(a))
