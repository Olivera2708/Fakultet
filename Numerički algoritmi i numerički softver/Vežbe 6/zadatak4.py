import numpy as np
import matplotlib.pyplot as plt
from zero_false_position import zero_false_position
from leastsquares import least_squares_regression

if __name__ == '__main__':
    # a)
    x = np.array([0,1,2,3,4,5])
    fX = np.array([5,3,5,1,3,5])

    plt.scatter(x, fX, c='black')

    # b)
    p = least_squares_regression(x, fX, 5)

    x = np.linspace(np.min(x), np.max(x), 100)
    pX = np.polyval(p, x)
    plt.plot(x, pX, 'r')

    # c)
    p_diff = np.polyder(p)
    h = lambda x: np.polyval(p_diff, x)

    x_min, _ = zero_false_position(h, 3, 4)
    print('x_min = ', x_min)
    fX_min = np.polyval(p, np.round(x_min, 4))
    plt.scatter(x_min, fX_min, c='y')


    x_max, _ = zero_false_position(h, 4, 5)
    print('x_max = ', np.round(x_max, 4))
    fX_max = np.polyval(p, x_max)

    plt.scatter(x_max, fX_max, c='y')
    plt.show()
