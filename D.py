import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

figure_save_path = './output'


# 一次读取一张整表
def read_sheet(file, sheet):
    return pd.read_excel(file, sheet_name=sheet)


# 读取人口和GDP数据
# 数据来自《经济与能源》2-10行
def read_population_and_GDP(df):
    return df.values[:9, 5:16]


# 人口和GDP相关图表绘制
# 数据来自《经济与能源》2-10行
def plot_population(population, qoq, yoy, index):
    qoq *= 100
    yoy *= 100
    x = range(2010, 2021)
    x2 = range(2016, 2021)
    titles = ['常驻人口及增长率', 'GDP及增长率', '人均GDP及增长率', '能源消费量总量及增长率', '碳排放量总量及增长率',
              '人均碳排放量及增长率', '能源消费强度及增长率', '碳排放强度及增长率']
    labels = ['常驻人口', 'GDP', '人均GDP', '能源消费量', '碳排放量', '人均碳排放量', '能源消费强度', '碳排放强度']
    left_labels = ['常驻人口（万人）', 'GDP（亿元）', '人均GDP（万元）', '能源消费量（万tce）', '碳排放量（万tCO2）',
                   '人均碳排放量（tCO2）', '能源消费强度（tce/万元）', '碳排放强度（tCO2/万元）']
    right_labels = ['常驻人口增长率（%）', 'GDP增长率（%）', '人均GDP增长率（%）', '能源消费量增长率（%）', '碳排放量增长率（%）',
                    '人均碳排放量增长率（%）', '能源消费强度增长率（%）', '碳排放强度增长率（%）']

    # 画柱状图
    plt.bar(x, population, label=labels[index], color='pink')
    plt.xlabel('年份')
    plt.ylabel(left_labels[index])
    ax = plt.gca()
    ax.set_ylim(min(0., min(population)), 1.4 * max(population))
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))  # x轴刻度间隔设为1
    # 在左侧显示图例
    plt.legend(loc="upper left")
    for a, b in zip(x, population):
        plt.text(a, b, round(b, 2), ha='center', va='bottom', fontsize=8)

    # 画折线图
    ax2 = plt.twinx()
    ax2.set_ylabel(right_labels[index])
    # 设置坐标轴范围
    mask = np.ma.masked_invalid(qoq)

    ax2.set_ylim(min(0., 1.4 * np.min(mask), 1.4 * np.min(yoy)), max(2 * np.max(mask), 2 * np.max(yoy)))
    plt.plot(x, mask, marker='.', c='r', label='环比增长率')
    plt.plot(x2, yoy, marker='v', c='b', label='同比增长率')

    # 只有环比增长率
    # ax2.set_ylim(min(0., 1.4 * np.min(mask)), 2 * np.max(mask))
    # plt.plot(x, mask, marker='.', c='r', label='增长率')

    # 显示数字
    for a, b in zip(x, qoq):
        plt.text(a, b, round(b, 2), ha='center', va='bottom', fontsize=8)
    for a, b in zip(x2, yoy):
        plt.text(a, b + 0.1, round(b, 2), ha='center', va='bottom', fontsize=8)

    # 在右侧显示图例
    plt.legend(loc="upper right")

    plt.title(titles[index])
    plt.legend()
    plt.savefig(os.path.join(figure_save_path, titles[index]))
    # plt.savefig(os.path.join(figure_save_path, 'qoq only', titles[index]))
    plt.show()


# GDP结构图
# 数据来自《经济与能源》2-10行
def plot_economy_structure(economies, name):
    x = range(2010, 2021)
    left_sum = np.zeros((1, len(x))).reshape(-1)
    right_sum = np.zeros((1, len(x))).reshape(-1)
    flags = [0, 0, 0, 1, -1, -1, 1, -1, -1]  # left: -1, both: 0 , right: 1
    labels = ['', '', ['农林消费部门', '第一产业'], '第二产业', '能源供应部门', '工业消费部门', '第三产业',
              '交通消费部门', '建筑消费部门']
    width = 0.3
    # 画子图是为了legend显示完全
    fig, ax = plt.subplots()

    for i in range(8, 1, -1):
        if flags[i] == -1:
            plt.bar(np.array(x) - 0.5 * width, economies[i], width, label=labels[i], bottom=left_sum)
            left_sum += economies[i].astype(np.float64)
        elif flags[i] == 1:
            plt.bar(np.array(x) + 0.5 * width, economies[i], width, label=labels[i], bottom=right_sum)
            right_sum += economies[i].astype(np.float64)
        else:
            plt.bar(np.array(x) - 0.5 * width, economies[i], width, label=labels[i][0], bottom=left_sum)
            left_sum += economies[i].astype(np.float64)
            plt.bar(np.array(x) + 0.5 * width, economies[i], width, label=labels[i][1], bottom=right_sum)
            right_sum += economies[i].astype(np.float64)

    plt.legend(bbox_to_anchor=(1.01, 0.4), loc=3, borderaxespad=0)

    plt.xlabel('年份')
    plt.ylabel('GDP（亿元）')
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))  # x轴刻度间隔设为1
    plt.title(name)

    # 通过画子图的方式，使legend显示完全，如果不用这种方法，legend放在图像外面时，legend显示不全
    fig.subplots_adjust(right=0.75)
    plt.savefig(os.path.join(figure_save_path, name))
    plt.show()


# GDP三产业占比图（碳排放占比图）
# 数据来自《经济与能源》2-10行
def plot_proportion_of_industry(y, index):
    x = range(2010, 2021)
    titles = ['各产业GDP及占比', '各产业碳排放量及占比']
    left_labels = ['各产业GDP（万亿）', '碳排放量（万tCO2）']
    right_labels = ['各产业占比（%）', '各产业占比（%）']

    # 画柱状图
    width = 0.3 if index == 0 else 0.2
    plt.bar(np.array(x) - 1.5 * width, y[0], width, label='第一产业', color='skyblue')
    plt.bar(np.array(x) - 0.5 * width, y[1], width, label='第二产业', color='pink')
    plt.bar(np.array(x) + 0.5 * width, y[2], width, label='第三产业', color='lightgreen')
    if index == 1:
        plt.bar(np.array(x) + 1.5 * width, y[3], width, label='居民生活', color='orange')
    plt.xlabel('年份')
    plt.ylabel(left_labels[index])
    ax = plt.gca()
    ax.set_ylim(min(0., np.min(y)), 1.4 * np.max(y))
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))  # x轴刻度间隔设为1
    # 在左侧显示图例
    plt.legend(loc="upper left")

    # 画折线图
    ax2 = plt.twinx()
    ax2.set_ylabel(right_labels[index])
    proportion = y / y.sum(axis=0)[np.newaxis, :]
    # 设置坐标轴范围
    ax2.set_ylim(min(0., 1.4 * np.min(proportion)), 2 * np.max(proportion))
    plt.plot(x, proportion[0], marker='.', c='b', label='第一产业占比')
    plt.plot(x, proportion[1], marker='v', c='r', label='第二产业占比')
    plt.plot(x, proportion[2], marker='*', c='g', label='第三产业占比')
    if index == 1:
        plt.plot(x, proportion[3], marker='+', c='brown', label='居民生活占比')
    # 在右侧显示图例
    plt.legend(loc="upper right")

    plt.title(titles[index])
    plt.legend()
    plt.savefig(os.path.join(figure_save_path, titles[index]))
    plt.show()


# 读取能源消耗量数据
# 数据来自《经济与能源》11-22行
def read_energy(df):
    return df.values[9:21, 5:16]


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
    plt.savefig(os.path.join(figure_save_path, name))
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
            plt.bar(x, consumption[i], label=labels[i], bottom=pos_sum, width=0.5)
            pos_sum += consumption[i].astype(np.float64)
        else:
            plt.bar(x, consumption[i], label=labels[i], bottom=neg_sum, width=0.5)
            neg_sum += consumption[i].astype(np.float64)

    plt.legend(bbox_to_anchor=(1.01, 0.4), loc=3, borderaxespad=0)

    plt.xlabel('年份')
    plt.ylabel('消耗量（万tce）')
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))  # x轴刻度间隔设为1
    plt.title(name)

    # 通过画子图的方式，使legend显示完全，如果不用这种方法，legend放在图像外面时，legend显示不全
    fig.subplots_adjust(right=0.8)
    plt.savefig(os.path.join(figure_save_path, name))
    plt.show()


# 读取碳排放量数据
# 数据来自《碳排放》2-8行
def read_carbon_emission(df):
    return df.values[:7, 5:16]


f_yoy = lambda x: (x[6:] - x[1:6]) / x[1:6]

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['FangSong']
    plt.rcParams['axes.unicode_minus'] = False
    file_path = 'data.xlsx'
    df_economy_and_energy = read_sheet(file_path, '经济与能源')  # 表《经济与能源》中的数据
    df_carbon_emission = read_sheet(file_path, '碳排放')  # 表《碳排放》中的数据

    population_and_GDP = read_population_and_GDP(df_economy_and_energy).astype(np.float64)
    # 补充2009年常驻人口7810.27万人
    pre_population = np.insert(population_and_GDP[0][:-1], 0, 7810.27)
    plot_population(population_and_GDP[0], (population_and_GDP[0] - pre_population) / pre_population,
                    f_yoy(population_and_GDP[0]), 0)

    # 补充2009年DGP总量34471.70亿元
    pre_GDP = np.insert(population_and_GDP[1][:-1], 0, 34471.70)
    plot_population(population_and_GDP[1], (population_and_GDP[1] - pre_GDP) / pre_GDP,
                    f_yoy(population_and_GDP[1]), 1)

    GDP_by_person = population_and_GDP[1].astype(np.float64) / population_and_GDP[0].astype(np.float64)
    pre_GDP_by_person = np.insert(GDP_by_person[:-1], 0, 34471.70 / 7810.27)
    plot_population(GDP_by_person, (GDP_by_person - pre_GDP_by_person) / pre_GDP_by_person,
                    f_yoy(GDP_by_person), 2)

    # 各产业占比

    energy = read_energy(df_economy_and_energy).astype(np.float64)
    # 补充2009年能源消费量？？？
    pre_energy = np.insert(energy[0][:-1], 0, 0)
    plot_population(energy[0], (energy[0] - pre_energy) / pre_energy, f_yoy(energy[0]), 3)

    plot_economy_structure(population_and_GDP, '地区生产总值结构变化趋势')

    energy_consumption_variety_title = ['煤炭消费量及子项变化趋势', '油品消费量及子项变化趋势',
                                        '天然气消费量及子项变化趋势', '新能源消费量变化趋势']
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

    carbon_emission = read_carbon_emission(df_carbon_emission).astype(np.float64)
    # 补充2009年碳排放量？？？
    pre_carbon_emission = np.insert(carbon_emission[0][:-1], 0, 0)

    plot_population(carbon_emission[0], (carbon_emission[0] - pre_carbon_emission) / pre_carbon_emission,
                    f_yoy(carbon_emission[0]), 4)

    carbon_emission_by_person = carbon_emission[0] / population_and_GDP[0]
    pre_carbon_emission_by_person = np.insert(carbon_emission_by_person[:-1], 0, 0 / 7810.27)
    plot_population(carbon_emission_by_person, (carbon_emission_by_person - pre_carbon_emission_by_person)
                    / pre_carbon_emission_by_person, f_yoy(carbon_emission_by_person), 5)

    # 能源消费强度=能源消费量/GDP
    energy_intensity = energy[0] / population_and_GDP[1]
    pre_energy_intensity = np.insert(energy_intensity[:-1], 0, 0 / 34471.70)
    plot_population(energy_intensity, (energy_intensity - pre_energy_intensity) / pre_energy_intensity,
                    f_yoy(energy_intensity), 6)

    # 碳排放强度=碳排放量/GDP
    carbon_intensity = carbon_emission[0] / population_and_GDP[1]
    pre_carbon_intensity = np.insert(carbon_intensity[:-1], 0, 0 / 34471.70)
    plot_population(carbon_intensity, (carbon_intensity - pre_carbon_intensity) / pre_carbon_intensity,
                    f_yoy(carbon_intensity), 7)

    plot_proportion_of_industry(np.array([population_and_GDP[2], population_and_GDP[3], population_and_GDP[6]]), 0)
    plot_proportion_of_industry(
        np.array([carbon_emission[1], carbon_emission[2], carbon_emission[3], carbon_emission[6]]), 1)
