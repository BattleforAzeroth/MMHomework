# 3. 糖果加工
import cvxpy as cp
import numpy as np

x = cp.Variable((3, 3), nonneg=True)
r1 = np.array([2., 1.5, 1.])  # 原料成本
r2 = np.array([0.5, 0.4, 0.3])  # 加工费
p = np.array([3.4, 2.85, 2.25])  # 售价
mr = np.array([2000., 2500., 1200.])  # 原料限制
obj = cp.Maximize((p - r2) @ cp.sum(x, axis=0) - r1 @ cp.sum(x, axis=1))  # 构造目标函数
con = [cp.sum(x, axis=1) <= mr,
       x[0][0] >= 0.6 * cp.sum(x[:, 0]),
       x[2][0] <= 0.2 * cp.sum(x[:, 0]),
       x[0][1] >= 0.3 * cp.sum(x[:, 1]),
       x[2][1] <= 0.5 * cp.sum(x[:, 1]),
       x[2][2] <= 0.6 * cp.sum(x[:, 2])]  # 构造约束条件
prob = cp.Problem(obj, con)  # 构造模型
prob.solve(solver='GLPK_MI')  # 求解模型
print("最优值为：", prob.value)
print("最优解为：\n", x.value)
print("生产甲、乙、丙糖果质量为：(单位：kg)\n", np.sum(x.value, axis=0))
