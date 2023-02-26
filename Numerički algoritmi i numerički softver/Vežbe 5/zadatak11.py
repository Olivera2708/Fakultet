import numpy as np
import matplotlib.pyplot as plt
import lagrangeInterpolation

x = np.array([0.7854, 1.9635, 3.1416, 4.3197, 5.4978])
fx = np.array([0.7071, 0.9239, 0.0, -0.9239, -0.7071])

plt.plot(x, fx, 'o', color = 'red')

p = lagrangeInterpolation.lagrange_interpolation(x, fx)
print(p)

ra = np.linspace(np.min(x), np.max(x), 100)
y = np.polyval(p, ra)
plt.plot(ra, y)

plt.show()