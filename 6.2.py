import pandas as pd
import cvxpy as cp

a0 = pd.read_excel("Pan6_1.xlsx")  # 读入第1个表单
b0 = pd.read_excel("Pan6_1.xlsx", 1)  # 读入第2个表单
a0 = a0.values
b0 = b0.values  # 提取数值
M = 1000000

u = cp.Variable(6, nonneg=True)
v = cp.Variable(6, nonneg=True)
t = cp.Variable((6, 6), integer=True)

obj = cp.Minimize(cp.sum(u + v))
con = [u + v <= 30,
       t >= 0, t <= 1]

for i in range(5):
    for j in range(i + 1, 6):
        con += [-(b0[i][j] + 0.5 * (u[i] - v[i] + u[j] - v[j])) >= a0[i][j] - t[i][j] * M,
                b0[i][j] + 0.5 * (u[i] - v[i] + u[j] - v[j]) >= a0[i][j] - (1 - t[i][j]) * M,
                b0[i][j] + 0.5 * (u[i] - v[i] + u[j] - v[j]) >= -(1 - t[i][j]) * M,
                b0[i][j] + 0.5 * (u[i] - v[i] + u[j] - v[j]) <= t[i][j] * M]

prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print("最优值为:", prob.value)
print("最优解为：\n", (u-v).value)
