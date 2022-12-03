import numpy as np
from gs import gauss_seidel

# smena: w = 1/y
# 2x + w = 1
# x + 2w = -2

A = np.array([
    [2, 1],
    [1, 2]
])

b = np.array([1, -2])

s0 = [0, 0]

s = gauss_seidel(A, b, s0)

x = s[0]
w = s[1]

# vracanje smene
y = 1/w

print('r:', x, y)

# provera
print('Provera: ')
print(2*x + 1/y)
print(x + 2/y)