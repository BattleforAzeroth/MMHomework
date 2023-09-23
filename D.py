import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 一次读取一张整表
def read_sheet(file, sheet):
    return pd.read_excel(file, sheet_name=sheet)


# 读取人口和GDP数据
# 数据来自《经济与能源》2-10行
def read_population_and_GDP(df):
    return df.values[:9, 5:16]


# 人口和GDP相关图表绘制
# 数据来自《经济与能源》2-10行
def plot_population(population, rate, index):
    rate *= 100
    x = range(2010, 2021)
    titles = ['常驻人口及增长率', 'GDP及增长率', '人均GDP及增长率']
    labels = ['常驻人口', 'GDP', '人均GDP']
    left_labels = ['常驻人口（万人）', 'GDP（亿元）', '人均GDP（万元）']
    right_labels = ['常驻人口增长率（%）', 'GDP增长率（%）', '人均GDP增长率（%）']

    # 画柱状图
    plt.bar(x, population, label=labels[index], alpha=0.2)
    plt.xlabel('年份')
    plt.ylabel(left_labels[index])
    ax = plt.gca()
    ax.set_ylim([0., 1.5 * max(population)])
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))  # x轴刻度间隔设为1
    # 在左侧显示图例
    plt.legend(loc="upper left")
    for a, b in zip(x, population):
        plt.text(a, b, round(b, 2), ha='center', va='bottom', fontsize=8)

    # 画折线图
    ax2 = plt.twinx()
    ax2.set_ylabel(right_labels[index])
    # 设置坐标轴范围
    ax2.set_ylim([0., 2 * max(rate)])
    plt.plot(x, rate, marker='.', label='增长率')
    # 显示数字
    for a, b in zip(x, rate):
        plt.text(a, b, round(b, 2), ha='center', va='bottom', fontsize=8)
    # 在右侧显示图例
    plt.legend(loc="upper right")

    plt.title(titles[index])
    plt.legend()
    plt.show()


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
# 数据来自《经济与能源》23-70行
def read_structure_of_consumption(df):
    return np.vsplit(df.values[21:69, 5:16], 8)


# 能耗品种结构图表绘制
# 数据来自《经济与能源》23-70行
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
                                        '天然气消费量及子项变化趋势', '新能源消费量变化趋势']
    energy_consumption_title = ['第一产业（农林）能耗结构变化趋势', '第二产业能耗结构变化趋势',
                                '能源供应部门能耗结构变化趋势',
                                '工业消费部门能耗结构变化趋势', '第三产业能耗结构变化趋势',
                                '交通消费部门能耗结构变化趋势',
                                '建筑消费部门能耗结构变化趋势', '居民生活能耗结构变化趋势']

    population_and_GDP = read_population_and_GDP(df_economy_and_energy)

    # 补充2009年常驻人口7810.27万人
    pre_population = np.insert(population_and_GDP[0][:-1].astype(np.float64), 0, 7810.27)
    plot_population(population_and_GDP[0], (population_and_GDP[0].astype(np.float64) - pre_population) / pre_population,
                    0)

    # 补充2009年DGP总量34471.70亿元

    pre_GDP = np.insert(population_and_GDP[1][:-1].astype(np.float64), 0, 34471.70)
    plot_population(population_and_GDP[1], (population_and_GDP[1].astype(np.float64) - pre_GDP) / pre_GDP, 1)

    GDP_by_person = population_and_GDP[1].astype(np.float64) / population_and_GDP[0].astype(np.float64)
    pre_GDP_by_person = np.insert(GDP_by_person[:-1], 0, 34471.70 / 7810.27)
    plot_population(GDP_by_person, (GDP_by_person - pre_GDP_by_person) / pre_GDP_by_person, 2)

    energy_consumption_variety = read_energy_consumption_variety_structure(df_economy_and_energy)
    for i, consumption in enumerate(energy_consumption_variety):
        plot_energy_consumption_variety_structure(consumption, energy_consumption_variety_title[i])

    energy_consumption_structure = read_structure_of_consumption(df_economy_and_energy)
    for i, consumption in enumerate(energy_consumption_structure):
        plot_structure_of_consumption(consumption, energy_consumption_title[i])
