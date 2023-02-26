import numpy as np
import matplotlib.pyplot as plt
import lagrangeInterpolation

x = np.array([1, 2, 4])
fx = np.array([4, 5, 4])

plt.plot(x, fx, 'o', c = 'red')

p = lagrangeInterpolation.lagrange_interpolation(x, fx)
ra = np.linspace(1, 4, 100)
func = np.polyval(p, ra)
plt.plot(ra, func)

plt.plot(3, np.polyval(p, 3), 'o', c = 'green')
print(np.polyval(p, 3))

plt.show()