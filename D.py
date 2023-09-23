import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 读取能耗品种结构数据
# 数据来自《经济与能源》71-88行
def read_structure_of_consumables(file):
    sheet = '经济与能源'
    df = pd.read_excel(file, sheet_name=sheet)
    return df.values[69:75, 5:16], df.values[75:81, 5:16], df.values[81:87, 5:16]


# 能耗品种结构图表绘制
# 数据来自《经济与能源》71-88行
def plot_structure_of_consumables(consumables, name):
    x = range(2010, 2021)
    labels = ['总量', '发电', '供热', '其他加工转化', '损失', '其他消费']
    markers = ['.', '+', 'o', 'v', '^', '*']
    for i in range(len(labels)):
        plt.plot(x, consumables[i], marker=markers[i], label=labels[i])
    plt.xlabel('年份')
    plt.ylabel('消耗量（万tce）')
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))  # x轴刻度间隔设为1
    plt.title(name)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['FangSong']
    plt.rcParams['axes.unicode_minus'] = False
    file_path = 'data.xlsx'
    coal_consumables, oil_consumables, natural_gas_consumables = read_structure_of_consumables(file_path)
    plot_structure_of_consumables(coal_consumables, '煤炭消费量及子项变化趋势')
    plot_structure_of_consumables(oil_consumables, '油品消费量及子项变化趋势')
    plot_structure_of_consumables(natural_gas_consumables, '天然气消费量及子项变化趋势')
