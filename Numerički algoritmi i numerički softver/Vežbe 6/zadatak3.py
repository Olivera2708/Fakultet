import numpy as np
import matplotlib.pyplot as plt
import leastsquares
import zero_false_position

if __name__ == '__main__':
    # a)
    f = lambda x: x ** 2 * np.sin(x)
    a = -np.pi
    b = np.pi

    x = np.linspace(a, b, 100)
    fX = f(x)
    plt.plot(x, fX, 'blue')

    # b)
    fX = f(x)
    p = leastsquares.least_squares_regression(x, fX, 3)

    x = np.linspace(a, b, 100)
    pX = np.polyval(p, x)
    plt.plot(x, pX, 'red')

    # c)
    h = lambda x: f(x) - np.polyval(p, x)

    inter1, _ = zero_false_position.zero_false_position(h, -1/2, 1/2)
    print('x1 = ', np.round(inter1))

    plt.scatter(inter1, f(inter1), c='g')
    plt.show()
