import numpy as np

def zameniDijagonale(matrix):
    x, y = matrix.shape
    nula = np.zeros((x, y))

    for i in range(x):
        for j in range(y):
            if (i == j):
                nula[i][j] = matrix[i][y-1-j]
            elif i == y - i - j:
                nula[i][y-1-j] = matrix[i][j] 
            else:
                nula[i][j] = matrix[i][y-1-j]

    return nula

if __name__ == "__main__":
    a = np.array([[-2, 5, -3],
                  [-1, -1, 0],
                  [-3, -5, 1]])

    print(zameniDijagonale(a))
