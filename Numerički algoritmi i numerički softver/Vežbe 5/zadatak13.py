import numpy as np
import matplotlib.pyplot as plt
import lagrangeInterpolation
import zero_false_position

x = np.array([1, 4, 5])
fx = np.array([1, 3, 3])

plt.plot(x, fx, 'o')

p = lagrangeInterpolation.lagrange_interpolation(x, fx)
ra = np.linspace(1, 5, 100)
plt.plot(ra, np.polyval(p, ra))

func = lambda x : np.polyval(p, x) - 2
nula, _ = zero_false_position.zero_false_position(func, 1, 5)
print(nula)

plt.plot(nula, 2, 'o', color = 'green')

plt.show()