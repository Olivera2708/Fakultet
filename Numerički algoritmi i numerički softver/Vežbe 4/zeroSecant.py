import numpy as np
from matplotlib import pyplot as plt

def zeroSecant(f, a, b, errMax, itMax, plotSpeed):

    if f(a) == f(b):
        raise Exception('Invalid parameters: f(a) == f(b)!')

    if plotSpeed <= 0:
        return zeroSecantNoPlot(f, a, b, errMax, itMax)
    
    return zeroSecantPlot(f, a, b, errMax, itMax, plotSpeed)


def zeroSecantNoPlot(f, a, b, errMax, itMax):
    for i in range(itMax):
        fA = f(a)
        fB = f(b)
        zero = b - fB*(b - a)/(fB - fA)

        fZero = f(zero)

        if abs(fZero) < errMax:
            return zero, i + 1
        
        a = b
        b = zero

    return zero, i + 1

def zeroSecantPlot(f, a, b, errMax, itMax, plotSpeed):
    
    x = np.linspace(a, b, 100)
    fX = f(x)
    fMin = np.min(fX)
    fMax = np.max(fX)

    plt.plot(x, fX, 'b', [a, b], [0, 0], 'k')

    for i in range(itMax):
        fA = f(a)
        fB = f(b)
        zero = b - fB*(b - a)/(fB - fA)
        plt.plot([a, b], [fA, fB], 'r', zero, 0, 'rx')

        fZero = f(zero)
        
        plt.plot([zero, zero], [fMin, fMax], 'g', zero, fZero, 'og')

        if abs(fZero) < errMax:
            break
        
        plt.pause(1/plotSpeed)


        a = b
        b = zero

        plt.plot([zero, zero], [fMin, fMax], 'r', zero, fZero, 'og')

    plt.show()
    return zero, i + 1


