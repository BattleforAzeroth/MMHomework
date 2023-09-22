from gurobipy import *
import pandas as pd


def sudoku(matrix):
    #  创建模型
    model = Model('solve_sudoku')
    #  创建变量
    x = model.addVars(9, 9, 9, vtype=GRB.BINARY)
    #  更新变量环境
    model.update()
    #  创建目标函数
    model.setObjective(1, GRB.MINIMIZE)
    #  创建约束条件
    model.addConstrs(x[i, j, k] == 1 for i in range(9) for j in range(9) for k in range(9)
                     if isinstance(matrix.at[i, j], int) and k == matrix.at[i, j] - 1)
    model.addConstrs(sum(x.select(i, j, '*')) == 1 for i in range(9) for j in range(9))
    model.addConstrs(sum(x.select(i, '*', j)) == 1 for i in range(9) for j in range(9))
    model.addConstrs(sum(x.select('*', i, j)) == 1 for i in range(9) for j in range(9))
    model.addConstrs(sum(x[i + 3 * I, j + 3 * J, k] for i in range(3) for j in range(3)) == 1
                     for k in range(9) for I in range(3) for J in range(3))
    #  执行线性规划模型
    model.optimize()
    #  输出结果
    result = pd.DataFrame()
    for k, v in model.getAttr('x', x).items():
        if v == 1:
            result.at[k[0], k[1]] = k[2] + 1
    return result.astype(int)


if __name__ == '__main__':
    matrix = pd.read_excel('sudoku_test.xlsx', index_col=False, header=None, na_filter=False)
    print(sudoku(matrix))
