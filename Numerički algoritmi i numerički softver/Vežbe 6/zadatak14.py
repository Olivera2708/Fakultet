import numpy as np
import matplotlib.pyplot as plt
import leastsquares
import zero_false_position

x = np.array([0, 1, 2, 3, 4, 5])
fx = np.array([5, 3, 5, 1, 3, 5])

plt.plot(x, fx, 'o')

p = leastsquares.least_squares_regression(x, fx, 5)
ra = np.linspace(0, 5, 100)
plt.plot(ra, np.polyval(p, ra))

df = np.polyder(p)

dff = lambda x : np.polyval(df, x)

nula, _ = zero_false_position.zero_false_position(dff, 3, 4)
plt.plot(nula, np.polyval(p, nula), "o", c = 'red')
print(nula)

nula, _ = zero_false_position.zero_false_position(dff, 4, 5)
plt.plot(nula, np.polyval(p, nula), "o", c = 'red')
print(nula)


plt.show()