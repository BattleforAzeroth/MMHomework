from sympy.plotting import plot3d
from sympy.abc import x, y
from sympy.functions import sqrt

plot3d(sqrt(6 / 8 * x ** 2 + 6 / 10 * y ** 2 - 6), (x, -10, 10), (y, -10, 10))
