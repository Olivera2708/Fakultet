import numpy as np
import matplotlib.pyplot as plt
from zero_false_position import zero_false_position
from leastsquares import least_squares_regression

if __name__ == '__main__':
    # a)
    f = lambda x: x ** 3 * np.cos(x)
    a = -np.pi / 2
    b = 5 * np.pi / 9

    x = np.linspace(a, b, 6)
    fX = f(x)

    p = least_squares_regression(x, fX, 5)

    x = np.linspace(a, b, 100)
    pX = np.polyval(p, x)
    plt.plot(x, pX, 'red')


    # b)
    val = -0.5
    h = lambda x: np.polyval(p, x) - val

    x1, _ = zero_false_position(h, -1.5, -1)
    print('x1 = ', np.round(x1, 4))
    plt.scatter(x1, f(x1), c='g')

    x2, _ = zero_false_position(h, -1, 0)
    print('x2 = ', np.round(x2, 4))
    plt.scatter(x2, f(x2), c='g')

    x3, _ = zero_false_position(h, 1.5, 2)
    print('x3 = ', np.round(x3, 4))
    plt.scatter(x3, f(x3), c='g')

    plt.show()


