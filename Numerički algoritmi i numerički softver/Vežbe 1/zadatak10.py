import numpy as np
import math

def diameter(matrix):
    x, y = matrix.shape
    maxi = 0

    for i in range(x):
        for j in range(i,x):
            if (matrix[i][0] < 0 and matrix[j][0] > 0) or (matrix[i][0] > 0 and matrix[j][0] < 0):
                rast_x = abs(matrix[i][0]) + abs(matrix[j][0])
            else:
                rast_x = abs(matrix[i][0] - matrix[j][0])

            if matrix[i][1] < 0 and matrix[j][1] > 0 or matrix[i][1] > 0 and matrix[j][1] < 0:
                rast_y = abs(matrix[i][1]) + abs(matrix[j][1])
            else:
                rast_y = abs(matrix[i][1] - matrix[j][1])

            rastojanje = math.sqrt(rast_y**2 + rast_x**2)

            if rastojanje > maxi:
                maxi = rastojanje

    return maxi

if __name__ == "__main__":
    points = np.array([[1.0, 0.0],
                       [4.0, 8.0],
                       [2.1, 1.2],
                       [3.2, 1.9],
                       [5.6, 4.3],
                       [7.9, 2.3],
                       [-1.0, 3.1]])

    print(diameter(points))
