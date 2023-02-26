import numpy as np
from matplotlib import pyplot as plt

from lagrangeInterpolation import lagrange_interpolation


if __name__ == '__main__':
    x = np.array([0.7854, 1.9635, 3.1416, 4.3197, 5.4978])
    fX = np.array([0.7071, 0.9239, 0.0000, -0.9239, -0.7071])

    plt.plot(x, fX, 'ko')

    p = lagrange_interpolation(x, fX)
    print(np.round(p, 4))

    x = np.linspace(np.min(x), np.max(x), 100)
    pX = np.polyval(p, x)

    plt.plot(x, pX, 'r')
    plt.show()
