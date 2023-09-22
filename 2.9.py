import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10 * np.pi, 10 * np.pi, 10000)
k = range(1, 7)
for i in k:
    ax = plt.subplot(2, 3, i)
    y = i * x ** 2 * np.sin(x) + 2 * i + np.cos(x ** 3)
    ax.plot(x,y,'r',label='k={}'.format(i))
    plt.legend()
plt.show()
