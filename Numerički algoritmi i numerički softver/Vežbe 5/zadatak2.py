import numpy as np
from matplotlib import pyplot as plt
from lagrangeInterpolation import lagrange_interpolation

if __name__ == '__main__':
    x = np.array([1,2,4])
    fX = np.array([4,5,4])

    # a) nacrtati poznate tacke
    plt.scatter(x, fX, c='black')


    # b) interpolacijom naci polinom i nacrtati ga
    p = lagrange_interpolation(x, fX)

    x = np.linspace(np.min(x), np.max(x), 100)
    pX = np.polyval(p, x)
    plt.plot(x, pX, 'red')

    # c) vrednost f(x) kad je x=3 i nacrtati
    x_new = 3
    pX_new = np.polyval(p, x_new)
    print('f(3) = ', pX_new)

    plt.scatter(x_new, pX_new, c='g')

    plt.show()