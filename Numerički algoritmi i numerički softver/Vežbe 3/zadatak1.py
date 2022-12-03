import numpy as np
from gs import gauss_seidel

A = np.array([
    [9, 3, 1],
    [7, 8, 9],
    [4, 1, 9]
])

b = np.array([33, 54, 13])

x0 = [0, 0, 0]

r = gauss_seidel(A, b, x0)

print(r)