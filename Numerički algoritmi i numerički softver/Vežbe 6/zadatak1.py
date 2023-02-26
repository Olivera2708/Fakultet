import numpy as np
from matplotlib import pyplot as plt
from numpy.core.function_base import linspace

from leastsquares import least_squares_regression


x = np.array([0.0000, 1.2500, 2.5000, 3.7500, 5.0000])
fX = np.array([1.7499, 0.9830, 1.2554, 3.0802, 2.3664])

plt.plot(x, fX, 'ko')

p = least_squares_regression(x, fX, 3)
print(p)

x = linspace(np.min(x), np.max(x), 100)
pX = np.polyval(p, x)

plt.plot(x, pX, 'r')
plt.show()
