import numpy as np
import matplotlib.pyplot as plt
import leastsquares

x = np.array([1, 2, 3, 5, 6])
fx = np.array([2, 4, 4, 1, 3])

plt.plot(x, fx, 'o')

p = leastsquares.least_squares_regression(x, fx, 4)
ra = np.linspace(1, 6, 100)
plt.plot(ra, np.polyval(p, ra))

print(p)

plt.plot(4, np.polyval(p, 4), 'o', c = 'red')
print(np.polyval(p, 4))

plt.show()