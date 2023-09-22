from sympy.plotting import plot3d
from sympy.abc import x, y

plot3d(x ** 2 / 10 + y ** 2 / 6, (x, -10, 10), (y, -10, 10))
