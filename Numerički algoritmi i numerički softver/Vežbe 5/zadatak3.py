import numpy as np
from matplotlib import pyplot as plt
from lagrangeInterpolation import lagrange_interpolation
import zero_false_position

if __name__ == '__main__':
    x = np.array([1, 4, 5])
    fX = np.array([1, 3, 3])

    # a) nacrtati poznate tacke
    plt.scatter(x, fX, c='black')

    # b) interpolacijom naci polinom i nacrtati ga
    p = lagrange_interpolation(x, fX)

    x = np.linspace(np.min(x), np.max(x), 100)
    pX = np.polyval(p, x)
    plt.plot(x, pX, 'red')

    # c) vrednost x kad je f(x)=2 i nacrtati
    fX_new = 2
    h = lambda x: np.polyval(p, x) - fX_new

    x_new, _ = zero_false_position.zero_false_position(h, np.min(x), np.max(x))
    print('x1 = ', x_new)

    plt.scatter(x_new, fX_new, c='g')
    plt.show()
