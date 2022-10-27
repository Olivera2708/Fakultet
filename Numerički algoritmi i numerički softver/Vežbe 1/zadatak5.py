import numpy as np

def minDijagonala(matrix):
    x, y = matrix.shape
    nula = np.zeros(2)
    nula[0] = 0
    nula[1] = 0

    mini = matrix[0][0]
    for i in range(x):
        for j in range(y):
            if (i == x-j-1 or i == j) and mini > matrix[i][j]:
                mini = matrix[i][j]
                nula[0] = i
                nula[1] = j

    return nula

if __name__ == "__main__":
    a = np.array([[-2, 5, -3],
                  [-1, -1, 0],
                  [-3, -5, 1]])

    print(minDijagonala(a))
