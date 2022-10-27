import numpy as np

def sum_d(matrix):
    x, y = matrix.shape
    if (x != y):
        raise Exception("Matrica nije kvadratna")

    sum = 0
    for i in range(x):
        for j in range(y):
            if (i == j):
                sum += matrix[i][j]
    
    return sum


if __name__ == "__main__":
    a = np.array([[2, 1, 6, 1],
                  [1, 3, 8, 2],
                  [5, 9, 4, 3],
                  [1, 1, 8, 5]])

    print(sum_d(a))