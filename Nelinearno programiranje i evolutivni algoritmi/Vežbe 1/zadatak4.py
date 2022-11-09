import numpy as np
import matplotlib.pyplot as plt

a = 20
b = 0.2
x1v = np.arange(-5, 5, 0.01);
x2v = np.arange(-5, 5, 0.01);
x1, x2 = np.meshgrid(x1v, x2v);

f1 = -a*np.exp(-b*np.sqrt((x1**2 + x2**2)/2)) - np.exp((np.cos(2*np.pi*x1) + np.cos(2*np.pi*x2))/2) + 2- + np.exp(1);
fig = plt.figure();
ax = fig.add_subplot(projection='3d');
pl = ax.plot_surface(x1, x2, f1);
plt.show();