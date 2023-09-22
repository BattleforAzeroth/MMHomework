# 习题4.1
from scipy.stats import norm
from scipy.optimize import fsolve

f = lambda sigma: norm.cdf(200, 160, sigma) - norm.cdf(120, 160, sigma) - 0.8
print("sigma=", fsolve(f, 10))
