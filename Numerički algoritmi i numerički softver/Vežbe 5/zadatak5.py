import numpy as np
from matplotlib import pyplot as plt
from lagrangeInterpolation import lagrange_interpolation

if __name__ == '__main__':
    f = lambda x: x ** 2 * np.sin(x)
    a = -np.pi
    b = np.pi

    # a) nacrtati funkciju na intervalu
    x = np.linspace(a, b, 100)
    fX = f(x)
    plt.plot(x, fX, 'blue')

    # b) odabrati i nacratiti potreban broj tacaka
    # za aproksimaciju polinomom 3. stepena

    # polinom 3. stepena -> trebaju nam 4 tacke
    points = np.linspace(a, b, 4)
    f_points = f(points)
    plt.scatter(points, f_points, c='g')

    # c) interpolacijom naci polinom koji zadovoljava
    # odabrane tacke i nacrtati ga
    p = lagrange_interpolation(points, f_points)
    print(np.round(p, 4))

    pX = np.polyval(p, x)
    plt.plot(x, pX, 'red')

    plt.show()
