import numpy as np
import matplotlib.pyplot as plt
import lagrangeInterpolation
import zero_false_position

x = np.array([1, 3, 5])
fx = np.array([0, 3, 0])
plt.plot(x, fx, 'o')

p = lagrangeInterpolation.lagrange_interpolation(x, fx)
ra = np.linspace(1, 5, 100)
plt.plot(ra, np.polyval(p, ra))

func = lambda x : np.polyval(p, x) - 1
nula1, _ = zero_false_position.zero_false_position(func, 4, 5)
plt.plot(nula1, 1, 'o')
print(nula1)

nula2, _ = zero_false_position.zero_false_position(func, 1, 2)
plt.plot(nula1, 1, 'o')
print(nula2)

plt.plot([1, 5], [1, 1])

presek = lambda x : np.polyval(p, x) - 1
nula1, _ = zero_false_position.zero_false_position(presek, 1, 2)
plt.plot(nula1, 1, 'o')
print(nula1)

nula2, _ = zero_false_position.zero_false_position(presek, 4, 5)
plt.plot(nula1, 1, 'o')
print(nula2)


plt.show()