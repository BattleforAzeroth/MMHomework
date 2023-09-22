import cvxpy as cp
import pandas as pd

df = pd.read_excel("6_1.xlsx", header=None)
c = df.values  # 提取数据矩阵

x = cp.Variable((4, 5), integer=True)
obj = cp.Minimize(cp.sum(cp.multiply(c, x)))
con = [0 <= x, x <= 1, cp.sum(x, axis=0, keepdims=True) == 1,
       cp.sum(x, axis=1, keepdims=True) <= 2]
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print("最优值为:", prob.value)
print("最优解为：\n", x.value)
