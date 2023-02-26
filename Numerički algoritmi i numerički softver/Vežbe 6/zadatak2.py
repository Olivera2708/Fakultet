import numpy as np
import matplotlib.pyplot as plt
import leastsquares

if __name__ == '__main__':
    # a)
    x = np.array([1, 2, 3, 5, 6])
    fX = np.array([2, 4, 4, 1, 3])

    plt.scatter(x, fX, c='black')

    # b)
    p = leastsquares.least_squares_regression(x, fX, 4)

    x = np.linspace(np.min(x), np.max(x), 100)
    pX = np.polyval(p, x)
    plt.plot(x, pX, 'r')

    # c)
    x_new = 4
    fX_new = np.polyval(p, x_new)
    plt.scatter(x_new, fX_new, c='g')
    print('f(4) = ', fX_new)

    plt.show()
