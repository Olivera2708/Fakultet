import numpy as np
import matplotlib.pyplot as plt
import leastsquares
import zero_false_position

a = -np.pi
b = np.pi

f = lambda x : x**2*np.sin(x)
ra = np.linspace(a, b, 100)
plt.plot(ra, f(ra))

treci = np.linspace(a, b, 4)
p = leastsquares.least_squares_regression(treci, f(treci), 3)
plt.plot(ra, np.polyval(p, ra))

presek = lambda x : f(x) - np.polyval(p, x)
nula, _ = zero_false_position.zero_false_position(presek, -1/2, 1/2)
plt.plot(nula, f(nula), 'o')
print(f"{nula:.2f}")

plt.show()