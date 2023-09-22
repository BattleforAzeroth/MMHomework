import numpy as np
import statsmodels.api as sm
import pandas as pd

alpha = 0.05
df = pd.read_excel("4_6.xlsx", header=None)
y = df.values  # 提取数据矩阵
y = y.flatten()
a = np.array(range(1, 8))
x = np.tile(a, (1, 10)).flatten()
d = {'x': x, 'y': y}  # 构造字典
model = sm.formula.ols("y~C(x)", d).fit()  # 构建模型
anovat = sm.stats.anova_lm(model)  # 进行单因素方差分析
print(anovat)
if anovat.loc['C(x)', 'PR(>F)'] > alpha:
    print("实验室对测量值无显著性影响")
else:
    print("实验室对测量值有显著性影响")
