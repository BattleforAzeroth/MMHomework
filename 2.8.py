import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10 * np.pi, 10 * np.pi, 10000)
k = range(1, 7)
plt.rc('font', size=16)
plt.rc('text', usetex=True)
plt.title('$y=kx^2sin(x)+2k+cos(x^3)$')
for i in k:
    y = i * x ** 2 * np.sin(x) + 2 * i + np.cos(x ** 3)
    plt.plot(x, y, label='k={}'.format(i))
plt.legend()
plt.show()
