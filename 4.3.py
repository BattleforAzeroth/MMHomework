# 指数分布
from scipy import stats

r = 1 / 8
F = lambda x1, x2: stats.expon.cdf(x2, scale=1 / r) - stats.expon.cdf(x1, scale=1 / r)
E = 1500 * F(0, 1) + 2000 * F(1, 2) + 2500 * F(2, 3) + 3000 * (1 - F(0, 3))
print(u"家电收费期望为：", E)
