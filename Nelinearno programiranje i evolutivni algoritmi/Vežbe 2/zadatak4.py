import math
import numpy as np
import sympy
import matplotlib.pyplot as plt

def FibonacijevMetod(y, a, b, eps):
    c = (3 - math.sqrt(5))/2

    x1 = a + c*(b-a)
    x2 = a + b - x1
    
    while (b-a >= eps):
        if (y.evalf(subs = {'x' : x1}) <= y.evalf(subs = {'x' : x2})):
            b = x2
            x2 = x1
            x1 = a + c*(b-a)
        else:
            a = x1
            x1 = x2
            x2 = b - c*(b-a)

    if (y.evalf(subs = {'x' : x1}) < y.evalf(subs = {'x' : x2})):
        return x1
    else:
        return x2


x = sympy.Symbol('x');
y = x**2 - sympy.sin(2*x) + 6

tacka1 = FibonacijevMetod(y, -2, 2, 0.01)

r = np.arange(-5, 5, 0.01)
f = r**2 - np.sin(r*2) + 6
plt.plot(r, f)
plt.plot(tacka1, y.evalf(subs = {'x' : tacka1}), 'o', color = 'red') #prikaz tacke
plt.show()