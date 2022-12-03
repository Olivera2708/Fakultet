import numpy as np
from matplotlib import pyplot as plt

def zeroBisection(f, a, b, errMax=0.001, itMax=100, plotSpeed=-1):
    if f(a)*f(b) > 0:
        raise Exception('Invalid parameters: f(a)*f(b) > 0!')

    if plotSpeed <= 0:
        return zeroBisectionNoPlot(f, a, b, errMax, itMax)

    return zeroBisectionPlot(f, a, b, errMax, itMax, plotSpeed)

def zeroBisectionNoPlot(f, a, b, errMax, itMax):
    for it in range(itMax):
        zero = (a + b)/2
        fZero = f(zero)

        if abs(fZero) < errMax or abs(b - a) < errMax:
            return zero, it + 1
        
        if f(a)*fZero < 0:
            b = zero
        else:
            a = zero

    return zero, it + 1

def zeroBisectionPlot(f, a, b, errMax, itMax, plotSpeed):

    x = np.linspace(a, b, 100)
    fX = f(x)
    fMin = min(fX)
    fMax = max(fX)

    plt.plot(x, fX, 'b', [a, b], [0, 0], 'k')
    plt.plot([a, a], [fMin, fMax], 'r', [b, b], [fMin, fMax], 'r')

    for it in range(itMax):
        zero = (a + b)/2
        fZero = f(zero)

        plt.plot([zero, zero], [fMin, fMax], 'g', zero, fZero, 'go')

        if abs(fZero) < errMax or abs(b - a) < errMax:
            break

        plt.pause(1/plotSpeed)
        
        if f(a)*fZero < 0:
            b = zero
        else:
            a = zero

        plt.plot([zero, zero], [fMin, fMax], 'r', zero, fZero, 'ro')

    plt.show()
    return zero, it
