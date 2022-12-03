import numpy as np
from matplotlib import pyplot as plt

def zeroNewton(f, df, x0, errMax=0.0001, itMax=100, plotSpeed=-1, plotA=-5, plotB=5):
    if df(x0) == 0:
        raise('Invalid input: df(x0) == 0!')
    
    if plotSpeed <= 0:
        return zeroNewtonNoPlot(f, df, x0, errMax, itMax)
    
    return zeroNewtonPlot(f, df, x0, errMax, itMax, plotSpeed, plotA, plotB)


def zeroNewtonNoPlot(f, df, x0, errMax, itMax):

    for it in range(itMax):
        zero = x0 - f(x0)/df(x0)

        fZero = f(zero)
        if abs(fZero) < errMax:
            return zero, it + 1
        
        x0 = zero

    return zero, it + 1

def zeroNewtonPlot(f, df, x0, errMax, itMax, plotSpeed, plotA, plotB):
    
    x = np.linspace(plotA, plotB, 100)

    fX = f(x)
    fMin = min(fX)
    fMax = max(fX)
    plt.plot(x, fX, 'b', [plotA, plotB], [0, 0], 'k')

    for it in range(itMax):
        fX0 = f(x0)
        zero = x0 - fX0/df(x0)

        plt.plot([x0, zero], [fX0, 0], 'r', zero, 0, 'rx')

        fZero = f(zero)
        plt.plot([zero, zero], [fMin, fMax], 'g', zero, fZero, 'go')

        if np.abs(fZero) < errMax:
            break
        plt.pause(1/plotSpeed)
        
        x0 = zero

        plt.plot([zero, zero], [fMin, fMax], 'r', zero, fZero, 'ro')
        
    plt.show()
    return zero, it + 1