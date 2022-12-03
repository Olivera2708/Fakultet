import numpy as np
from gs import gauss_seidel

A = np.array([
    [1.1960, 0.3424, 0.1747],
    [0.2449, 1.0565, 0.0751],
    [0.1980, 0.2631, 0.9159]
])

A = np.sin(A)

b = np.array([-2.6827, -3.7424, 0.9456])

x0 = [0, 0, 0]

r = gauss_seidel(A, b, x0)

print(r)