# 1. 连续投资
import cvxpy as cp

a = 1.15  # a的利率
b = 1.25
c = 1.40
d = 1.06
mb = 4.  # b的最大投资额
mc = 3.
p = 10.  # 初始资金
x = cp.Variable((4, 5), nonneg=True)
obj = cp.Maximize(a * x[0][3] + b * x[1][2] + c * x[2][1] + d * x[3][4])  # 构造目标函数
con = [x[3][4] == a * x[0][2] + d * x[3][3],
       x[0][3] + x[3][3] == a * x[0][1] + d * x[3][2],
       x[0][2] + x[1][2] + x[3][2] == a * x[0][0] + d * x[3][1],
       x[0][1] + x[2][1] + x[3][1] == d * x[3][0],
       x[0][0] + x[3][0] == p,
       x[1][2] <= mb, x[2][1] <= mc]  # 构造约束条件
prob = cp.Problem(obj, con)  # 构造模型
prob.solve(solver='GLPK_MI')  # 求解模型
print("最优值为：", prob.value)
print("最优解为：\n", x.value)
