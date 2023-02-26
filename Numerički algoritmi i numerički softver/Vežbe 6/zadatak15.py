import numpy as np
import matplotlib.pyplot as plt
import leastsquares
import zero_false_position

a = -np.pi/2
b = 5*np.pi/9

f = lambda x : x**3*np.cos(x)
ra = np.linspace(a, b, 100)
plt.plot(ra, f(ra))

peti = np.linspace(a, b, 6)
p = leastsquares.least_squares_regression(peti, f(peti), 5)
plt.plot(ra, np.polyval(p, ra))

presek = lambda x : np.polyval(p, x) + 0.5
nula, _ = zero_false_position.zero_false_position(presek, 0, 2)
plt.plot(nula, np.polyval(p, nula), 'o')
print(f"{nula:.4f}")

nula, _ = zero_false_position.zero_false_position(presek, -1, 0)
plt.plot(nula, np.polyval(p, nula), 'o')
print(f"{nula:.4f}")

nula, _ = zero_false_position.zero_false_position(presek, -2, -1)
plt.plot(nula, np.polyval(p, nula), 'o')
print(f"{nula:.4f}")

plt.show()