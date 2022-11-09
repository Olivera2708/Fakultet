import numpy as np
import sympy
import matplotlib.pyplot as plt

def MetodSecice(y, a, b, eps):
    ydiff = sympy.diff(y)
    while (True):
        c = b - (b - a)/(ydiff.evalf(subs = {'x' : b}) - ydiff.evalf(subs = {'x' : a})) * ydiff.evalf(subs = {'x' : b})
        if (abs(c - b) < eps):
            return c
        a = b
        b = c


x = sympy.Symbol('x');
y = x**2 - sympy.sin(2*x) + 6

tacka1 = MetodSecice(y, 2, 6, 0.01)

r = np.arange(-5, 5, 0.01)
f = r**2 - np.sin(r*2) + 6
plt.plot(r, f)
plt.plot(tacka1, y.evalf(subs = {'x' : tacka1}), 'o', color = 'red') #prikaz tacke
plt.show()