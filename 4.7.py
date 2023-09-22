import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

df = pd.read_excel("4_7.xlsx", header=None)
a = df.values  # 提取数据矩阵
x = a[:, ::2]  # 提取奇数列体重
y = a[:, 1::2]  # 提取偶数列身高
x = x.flatten()
y = y.flatten()

X = sm.add_constant(x)
md = sm.OLS(y, X).fit()  # 构建并拟合模型
a = md.params[0]
b = md.params[1]

print("拟合的多项式为: y = {} * x + {}".format(b, a))
print(md.summary2())

# F检验
pred = md.predict(X)
SSR = np.dot(pred - y.mean(), pred - y.mean())
SSE = np.dot(pred - y, pred - y)
f = (SSR / 1) / (SSE / (len(y) - 2))
f_0_01 = stats.f.ppf(1 - 0.01, 1, len(y) - 2)
f_0_05 = stats.f.ppf(1 - 0.05, 1, len(y) - 2)
print("F =", f)
print("F_0.01 =", f_0_01)
print("F_0.05 =", f_0_05)
if f > f_0_01:
    print("线性关系极其显著")
elif f > f_0_05:
    print("线性关系显著")
else:
    print("无线性关系")

fig = plt.figure(figsize=(15, 8))
fig = sm.graphics.plot_regress_exog(md, 'x1', fig=fig)
plt.show()
