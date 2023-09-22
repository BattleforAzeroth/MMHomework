import numpy as np
import scipy.stats as ss

r = 1
bins = np.arange(0, 6)
fi = np.array([22, 37, 20, 13, 6, 2])
n = fi.sum()
p = ss.poisson.pmf(bins, mu=1)
cha = (fi - n * p) ** 2 / (n * p)
st = cha.sum()
bd = ss.chi2.ppf(0.95, len(bins) - 1)  # 计算上alpha分位数
print("统计量为：{}，临界值为：{}".format(st, bd))
if st > bd:
    print("拒绝H0，不服从均值为1的poisson分布")
else:
    print("接受H0，服从均值为1的poisson分布")
