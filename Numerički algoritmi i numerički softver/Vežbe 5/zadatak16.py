import numpy as np
import matplotlib.pyplot as plt
import lagrangeInterpolation

x = np.array([0.1, 0.3, 0.6, 1.2])
fx = np.array([1.023, 1.261, 2.368, 9.064])

p = lagrangeInterpolation.lagrange_interpolation(x, fx)

print(p[3], p[2], p[1], p[0])