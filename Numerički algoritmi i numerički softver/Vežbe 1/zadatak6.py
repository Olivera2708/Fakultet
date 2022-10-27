import numpy as np

def obrniNeparne(matrix):
    x, y = matrix.shape
    nula = np.zeros((x, y))

    for i in range(x):
        if i % 2 == 0:
            for j in range(y)[::-1]:
                nula[i][x-1-j] = matrix[i][j]
        else:
            for j in range(y):
                nula[i][j] = matrix[i][j]

    return nula

if __name__ == "__main__":
    a = np.array([[-2, 5, -3],
                  [-1, -1, 0],
                  [-3, -5, 1]])

    print(obrniNeparne(a))
