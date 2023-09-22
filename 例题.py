import sympy as sp

A = sp.Matrix([[1, 1, -3, -1], [3, -1, -3, 4], [1, 5, -9, -8]])
b = sp.Matrix([1, 4, 0])
b.transpose()
C = A.row_join(b)  # 构造增广矩阵
print("增广阵的行最简形为：\n", C.rref())
n = A.shape[1]  # 未知数个数
C = A.row_join(b)  # 构造增广矩阵
c = C.rref()[1]  # 主元列
C = C.rref()[0]
print("通解为：")
k = 1
for i in range(n):
    if i not in c:
        M = C[0:len(c), i]
        M = -M
        t = sp.zeros(n - len(c), 1)
        t[k - 1] += 1

        for j in range(len(c)):
            t = t.row_insert(c[j], M.row(j))

        print('c' + str(k) + ' *', t, '+ ', end='')
        k += 1
M = C[0:len(c), -1]
t = sp.zeros(n - len(c), 1)
for j in range(len(c)):
    t = t.row_insert(c[j], M.row(j))

print(t)
