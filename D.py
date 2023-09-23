import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 一次读取一张整表
def read_sheet(file, sheet):
    return pd.read_excel(file, sheet_name=sheet)


# 读取能耗品种结构数据
# 数据来自《经济与能源》71-88行
def read_energy_consumption_variety_structure(df):
    l = np.vsplit(df.values[69:87, 5:16], 3)
    l.append(df.values[87:91, 5:16])
    return l


# 能耗品种结构图表绘制
# 数据来自《经济与能源》71-88行
def plot_energy_consumption_variety_structure(consumables, name):
    x = range(2010, 2021)
    labels = ['总量', '发电', '供热', '其他加工转化', '损失', '其他消费']
    markers = ['.', '+', 'o', 'v', '^', '*']
    if len(consumables) == 4:
        labels = ['新能源热力', '新能源电力', '外地调入电', '其他新能源']

    for i in range(len(labels)):
        plt.plot(x, consumables[i], marker=markers[i], label=labels[i])
    plt.xlabel('年份')
    plt.ylabel('消耗量（万tce）')
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))  # x轴刻度间隔设为1
    plt.title(name)
    plt.legend()
    plt.show()


# 读取能耗品种结构数据
# 数据来自《经济与能源》22-70行
def read_structure_of_consumption(df):
    return np.vsplit(df.values[21:69, 5:16], 8)


# 能耗品种结构图表绘制
# 数据来自《经济与能源》22-70行
def plot_structure_of_consumption(consumption, name):
    x = range(2010, 2021)
    labels = ['煤炭', '油品', '天然气', '热力', '电力', '其他能源']
    pos_sum = np.zeros((1, len(x))).reshape(-1)
    neg_sum = np.zeros((1, len(x))).reshape(-1)

    # 画子图是为了legend显示完全
    fig, ax = plt.subplots()
    for i in range(len(labels)):
        if consumption[i][0] >= 0:
            plt.bar(x, consumption[i], label=labels[i], alpha=0.2, bottom=pos_sum, width=0.5)
            pos_sum += consumption[i].astype(np.float64)
        else:
            plt.bar(x, consumption[i], label=labels[i], alpha=0.2, bottom=neg_sum, width=0.5)
            neg_sum += consumption[i].astype(np.float64)

    plt.legend(bbox_to_anchor=(1.01, 0.4), loc=3, borderaxespad=0)

    plt.xlabel('年份')
    plt.ylabel('消耗量（万tce）')
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))  # x轴刻度间隔设为1
    plt.title(name)

    # 通过画子图的方式，使legend显示完全，如果不用这种方法，legend放在图像外面时，legend显示不全
    fig.subplots_adjust(right=0.8)
    plt.show()


if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['FangSong']
    plt.rcParams['axes.unicode_minus'] = False
    file_path = 'data.xlsx'
    df_economy_and_energy = read_sheet(file_path, '经济与能源')  # 表《经济与能源》中的数据
    df_carbon_emission = read_sheet(file_path, '碳排放')  # 表《碳排放》中的数据

    energy_consumption_variety_title = ['煤炭消费量及子项变化趋势', '油品消费量及子项变化趋势',
                                        '天然气消费量及子项变化趋势',
                                        '新能源消费量变化趋势']
    energy_consumption_title = ['第一产业（农林）能耗结构变化趋势', '第二产业能耗结构变化趋势',
                                '能源供应部门能耗结构变化趋势',
                                '工业消费部门能耗结构变化趋势', '第三产业能耗结构变化趋势',
                                '交通消费部门能耗结构变化趋势',
                                '建筑消费部门能耗结构变化趋势', '居民生活能耗结构变化趋势']

    energy_consumption_variety = read_energy_consumption_variety_structure(df_economy_and_energy)
    for i, consumption in enumerate(energy_consumption_variety):
        plot_energy_consumption_variety_structure(consumption, energy_consumption_variety_title[i])

    energy_consumption_structure = read_structure_of_consumption(df_economy_and_energy)
    for i, consumption in enumerate(energy_consumption_structure):
        plot_structure_of_consumption(consumption, energy_consumption_title[i])
