import numpy as np
from matplotlib import pyplot as plt
from lagrangeInterpolation import lagrange_interpolation

if __name__ == '__main__':
    x = np.array([0.1, 0.3, 0.6, 1.2])
    fX = np.array([1.023, 1.261, 2.368, 9.064])

    p = lagrange_interpolation(x, fX)

    print(p[::-1])
