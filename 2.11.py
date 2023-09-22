import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection='3d')
t = np.linspace(0, 2 * np.pi, 1000)
s = np.linspace(-1, 1, 1000)
S, T = np.meshgrid(s, t)
X = (2 + S / 2 * np.cos(T / 2)) * np.cos(T)
Y = (2 + S / 2 * np.cos(T / 2)) * np.sin(T)
Z = S / 2 * np.sin(T / 2)
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.show()
