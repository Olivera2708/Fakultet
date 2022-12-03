import numpy as np
from gs import gauss_seidel


# smena: 1/z = w
# 4x + 2y = 1
# x + 2y = -1
# 2x + y + 4w = 0

A = np.array([
    [4, 2, 0],
    [1, 2, 0],
    [2, 1, 4]
])

b = np.array([1, -1, 0])

s0 = [0, 0, 0]

s = gauss_seidel(A, b, s0)

x, y, w = s

# vracanje smene
z = 1/w

print('r:', x, y, z)

# provera
print('Provera:')
print(4*x + 2*y)
print(x + 2*y)
print(z*(2*x + y))
