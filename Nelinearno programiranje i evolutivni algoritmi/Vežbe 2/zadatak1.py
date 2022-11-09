import numpy as np
import sympy
import matplotlib.pyplot as plt

def NjutnRapsonov(y, a, eps):
    ydiff = sympy.diff(y)
    ydiff2 = sympy.diff(ydiff)
    while (True):
        b = a - ydiff.evalf(subs = {'x' : a})/ydiff2.evalf(subs = {'x' : a})
        if (abs(b - a) < eps):
            return b
        a = b


x = sympy.Symbol('x');
y = x**2 - sympy.sin(2*x) + 6

tacka = NjutnRapsonov(y, 2, 0.01)

r = np.arange(-5, 5, 0.01)
f = r**2 - np.sin(r*2) + 6
plt.plot(r, f)
plt.plot(tacka, y.evalf(subs = {'x' : tacka}), 'o', color = 'red') #prikaz tacke
plt.show()