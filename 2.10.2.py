from sympy.plotting import plot3d
from sympy.abc import x, y
from sympy.functions import sqrt

plot3d(sqrt(x ** 2 - 8 / 12 * y ** 2 - 8), (x, -10, 10), (y, -10, 10))
