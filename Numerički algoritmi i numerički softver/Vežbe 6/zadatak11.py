import numpy as np
import matplotlib.pyplot as plt
import leastsquares

x = np.array([0, 1.25, 2.5, 3.75, 5])
fx = np.array([1.7499, 0.9830, 1.2554, 3.0802, 2.3664])

plt.plot(x, fx, 'o')

p = leastsquares.least_squares_regression(x, fx, 3)
ra = np.linspace(0, 5, 100)
plt.plot(ra, np.polyval(p, ra))

print(p)

plt.show()