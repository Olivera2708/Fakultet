import numpy as np
from gs import gauss_seidel

# A = np.array([
#     [ 0,  1,  2],
#     [ 1,  2,  0],
#     [-1, -1,  0]
# ])

# pravimo dijagonalno dominantnu matricu
A = np.array([
    [ 4,  1,  2],
    [ 1,  2,  0],
    [-1, -1,  2]
])

b = np.array([1, 2, 3])

x0 = [0, 0, 0]

r = gauss_seidel(A, b, x0)

print(r)