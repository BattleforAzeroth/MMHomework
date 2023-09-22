import cvxpy as cp
import numpy as np

f = np.array([[14, 16, 21],
              [19, 17, 10],
              [10, 15, 12],
              [9, 12, 13]])
t = cp.Variable((4, 3), nonneg=True)
# r = cp.Variable(4, integer=True)
m = cp.Variable((4, 4), integer=True)
y = cp.Variable(nonneg=True)
obj = cp.Minimize(y)
con = [m >= 0, m <= 1,
       cp.sum(m, axis=0) == 1,
       cp.sum(m, axis=1) == 1]
# con += [r.value[i] == k for i in range(4) for k in range(4) if m[i][k] == 1]
for i in range(4):
    for k in range(4):
        for j in range(3):
            if m[i][k] == 1:
                con += [t[i][j] >= t[k][j] + m[i][:] @ f[k][j]]
            if j > 0:
                con += [t[i][j] >= t[i, j - 1] + f[i, j - 1]]
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print("最优值为:", prob.value)
print("最优解为：\n", m.value)
