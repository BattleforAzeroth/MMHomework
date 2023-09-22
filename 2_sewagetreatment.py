# 2. 污水处理
import cvxpy as cp
import numpy as np

x = cp.Variable(2, nonneg=True)
A = np.array([[-0.8, -1.], [-1., 0.]])
b = np.array([-1.6, -1.])
c = np.array([1000, 800])
d = np.array([2, 1.4])
obj = cp.Minimize(c @ x)  # 构造目标函数
con = [A @ x <= b,
       x <= d]  # 构造约束条件
prob = cp.Problem(obj, con)  # 构造模型
prob.solve(solver='GLPK_MI')  # 求解模型
print("最优值为：", prob.value)
print("最优解为：\n", x.value)
