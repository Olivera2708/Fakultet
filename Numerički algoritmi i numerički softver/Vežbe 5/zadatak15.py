import numpy as np
import matplotlib.pyplot as plt
import lagrangeInterpolation

f = lambda x : x**2*np.sin(x)
a = -np.pi
b = np.pi
x = np.linspace(a, b, 100)
plt.plot(x, f(x))

treci = np.linspace(a, b, 4)
plt.plot(treci, f(treci), 'o')

p = lagrangeInterpolation.lagrange_interpolation(treci, f(treci))
print(p)

plt.plot(x, np.polyval(p, x))

plt.show()