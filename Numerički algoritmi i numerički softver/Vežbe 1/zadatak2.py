from tkinter import Y
import numpy as np

def sum_grater(matrix):
    x, y = matrix.shape
    avg = 0

    for i in range(x):
        for j in range(y):
            avg += matrix[i][j]
    avg /= x*y

    sum = 0
    for i in range(x):
        for j in range(y):
            if matrix[i][j] > avg:
                sum += matrix[i][j]

    return sum


if __name__ == "__main__":
    a = np.array([[2, 1, 2, 6, 8, 1, -2],
                  [15, 4, 7, 18, 4, 0, 12],
                  [11, 6, 9, -1, 4, 8, 0],
                  [2, 8, 6, 8, 1, 8, 7]])

    print(sum_grater(a))
