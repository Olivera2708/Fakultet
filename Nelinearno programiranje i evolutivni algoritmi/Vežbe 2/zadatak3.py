import numpy as np
import sympy
import matplotlib.pyplot as plt

def odrediN(a, b, eps):
    n = 1
    while (True):
        if F(n) > (b-a)/eps:
            return n
        n += 1

def F(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    prvi = 0
    drugi = 1
    br = 2
    while (br != n):
        br += 1
        treci = prvi + drugi
        prvi = drugi
        drugi = treci
    return drugi
        

def FibonacijevMetod(y, a, b, eps):
    n = odrediN(a, b, eps)

    x1 = a + F(n-2)/F(n)*(b-a)
    x2 = a + b - x1
    
    for i in range(2, n+1):
        if (y.evalf(subs = {'x' : x1}) <= y.evalf(subs = {'x' : x2})):
            b = x2
            x2 = x1
            x1 = a + b - x2
        else:
            a = x1
            x1 = x2
            x2 = a + b - x1

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