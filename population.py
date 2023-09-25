import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

a = []
b = []
with open("1.txt") as f:  # 打开文件并绑定对象f
    s = f.read().splitlines()  # 返回每一行的数据
for i in range(0, len(s), 2):  # 读入奇数行数据
    d1 = s[i].split("\t")
    for j in range(len(d1)):
        if d1[j] != "": a.append(eval(d1[j]))  # 把非空的字符串转换为年代数据
for i in range(1, len(s), 2):  # 读入偶数行数据
    d2 = s[i].split("\t")
    for j in range(len(d2)):
        if d2[j] != "": b.append(eval(d2[j]))  # 把非空的字符串转换为人口数据
c = np.vstack((a, b))  # 构造两行的数组
np.savetxt("2.txt", c)  # 把数据保存起来供下面使用
x = lambda t, r, xm: xm / (1 + (xm / 6766.90 - 1) * np.exp(-r * (t - 1990)))
bd = ((0, 500), (0.01, 30000))  # 约束两个参数的下界和上界
popt, pcov = curve_fit(x, a[1:], b[1:], bounds=bd)
print(popt)
print("2021年的预测值为：", x(2021, *popt))
x1 = np.linspace(1990, 2060, 2000)
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(x1, x(x1, *popt), c='r')
plt.scatter(c[0], c[1], c='black', s=3)
plt.xlabel('年份')
plt.ylabel('常住人口（万人）')
plt.title('常住人口预测模型')
plt.savefig('./output/常住人口预测模型')
plt.show()
columns = ['年份', '常住人口（万人）']
a1 = np.arange(2021, 2061).astype(np.float64)
b1 = x(a1, *popt)
df = pd.DataFrame(np.vstack((a1, b1)).transpose(), columns=columns)
df.to_excel('./output/population.xlsx')
