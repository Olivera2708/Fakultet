import numpy as np
from matplotlib import pyplot as plt
from lagrangeInterpolation import lagrange_interpolation
import zero_false_position

if __name__ == '__main__':
    x = np.array([1, 3, 5])
    fX = np.array([0, 3, 0])

    # a) nacrtati poznate tacke
    plt.scatter(x, fX, c='black')

    # b) interpolacijom naci polinom i nacrtati ga
    p = lagrange_interpolation(x, fX)

    x = np.linspace(np.min(x), np.max(x), 100)
    pX = np.polyval(p, x)
    plt.plot(x, pX, 'red')

    # c) nacrtati pravu f(x) = 1
    f = lambda x: [1]
    fX = f(x)
    plt.plot([np.min(x), np.max(x)], [f(np.min(x)), f(np.max(x))], 'black')

    # d) naci i nacrtati sve preseke polinoma i prave

    h_inter = lambda x: np.polyval(p, x) - f(x)

    intersection1, _ = zero_false_position.zero_false_position(h_inter, 1, 2)
    print('x1 = ', intersection1)
    f_intersection1 = f(intersection1)
    plt.scatter(intersection1, f_intersection1, c='g')

    intersection2, _ = zero_false_position.zero_false_position(h_inter, 4, 5)
    print('x2 = ', intersection2)
    f_intersection2 = f(intersection2)
    plt.scatter(intersection2, f_intersection2, c='g')

    plt.show()
