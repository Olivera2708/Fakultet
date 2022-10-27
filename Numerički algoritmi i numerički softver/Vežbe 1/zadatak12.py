import numpy as np
import math

def sort_by_first_column(matrix):
    x = matrix.shape[0]
    
    for i in range(x - 1):
        for j in range(i + 1, x):
            if matrix[j, 0] > matrix[i, 0]:
                temp = matrix[i, :].copy()
                matrix[i, :] = matrix[j, :]
                matrix[j, :] = temp
    return matrix

if __name__ == "__main__":
    stocks = np.array([[66, 1],
                       [100, 2],
                       [133, 3],
                       [200, 4],
                       [33, 5],
                       [66, 6],
                       [133, 7],
                       [266, 8]])

    print(sort_by_first_column(stocks))
