import numpy as np
import matplotlib.pyplot as plt
import sympy

def najbrziPad(f, x0, gama, eps, n):
    dx = sympy.diff(f, x)
    dy = sympy.diff(f, y)
    
    while (n != 0):
        n -= 1
        dg = np.array([dx.evalf(subs = {'x' : x0[0], 'y' : x0[1]}), dy.evalf(subs = {'x' : x0[0], 'y' : x0[1]})], dtype=float)
        x0 = x0 - gama * dg
        if (np.linalg.norm(dg) < eps):
            break

    return x0


x = sympy.Symbol('x')
y = sympy.Symbol('y')
fx = 0.01 * ((x-1)**2 + 2*(y-1)**2)*((x+1)**2+2*(y+1)**2+0.5)*((x+2)**2+2*(y-2)**2+0.7)

x0 = np.array([-1, 1])

tacka = najbrziPad(fx, x0, 0.15, 0.0001, 100)

a1 = np.arange(-5, 5, 0.01)
a2 = np.arange(-5, 5, 0.01)
r, q = np.meshgrid(a1, a2)
fxy = 0.01 * ((r-1)**2 + 2*(q-1)**2)*((r+1)**2+2*(q+1)**2+0.5)*((r+2)**2+2*(q-2)**2+0.7)

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax.plot_surface(r, q, fxy)
ax.scatter(tacka[0], tacka[1], fx.evalf(subs = {'x' : tacka[0], 'y' : tacka[1]}), 'o', color = 'red')
plt.show()
