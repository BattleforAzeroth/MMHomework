# 3.7 两个线性方程组数值解
import numpy as np
import numpy.linalg as LA


def solve(A, b):
    RA = LA.matrix_rank(A)
    C = np.append(A, b, axis=1)  # 增广阵
    # print(C)
    RAb = LA.matrix_rank(C)
    if RA < RAb:
        print("无解，最小二乘解为：", LA.pinv(A).dot(b))
    elif RA == A.shape[1]:
        print("有唯一解：", LA.solve(A, b))
    else:
        print("有多解，最小范数解为：", LA.pinv(A).dot(b))


if __name__ == '__main__':
    A1 = np.array([[4, 2, -1], [3, -1, 2], [11, 3, 0]])
    b1 = np.array([[2, 10, 8]])
    b1 = b1.reshape(3, 1)
    A2 = np.array([[2, 3, 1], [1, -2, 4], [3, 8, -2], [4, -1, 9]])
    b2 = np.array([[4, -5, 13, -6]])
    b2 = b2.reshape(4, 1)
    solve(A1, b1)
    solve(A2, b2)
