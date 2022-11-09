import numpy as np
import matplotlib.pyplot as plt

x1v = np.arange(-5, 5, 0.01);
x2v = np.arange(-5, 5, 0.01);
x1, x2 = np.meshgrid(x1v, x2v);

f1 = x1**2/4000 + x2**2/4000 - np.cos(x1)*np.cos(x2/np.sqrt(2)) + 1
fig = plt.figure();
ax = fig.add_subplot(projection='3d');
pl = ax.plot_surface(x1, x2, f1);
plt.show();