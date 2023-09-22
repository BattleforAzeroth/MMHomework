# 3.6 两个线性方程组符号法求精确解
import sympy as sp


def solve(A, b):
    if b == sp.zeros(b.shape[0], b.shape[1]):  # 齐次方程
        print("基础解系为：", A.nullspace())
    else:  # 非齐次方程
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


if __name__ == '__main__':
    A1 = sp.Matrix([[1, 2, 1, -1], [3, 6, -1, -3], [5, 10, 1, -5]])
    b1 = sp.Matrix([0, 0, 0])
    b1.transpose()
    A2 = sp.Matrix([[2, 1, -1, 1], [4, 2, -2, 1], [2, 1, -1, -1]])
    b2 = sp.Matrix([1, 2, 1])
    solve(A1, b1)
    solve(A2, b2)
