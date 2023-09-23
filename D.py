import pandas as pd
import numpy as np
import matplotlib as mpl


# 读取能耗品种结构数据
# 数据来自《经济与能源》71-88行
def read_structure_of_consumables(file):
    sheet = '经济与能源'
    df = pd.read_excel(file, sheet_name=sheet)
    return df.values[69:75, 5:16], df.values[75:81, 5:16], df.values[81:87, 5:16]


# 能耗品种结构图表绘制
# 数据来自《经济与能源》71-88行
def plot_structure_of_consumables():
    pass


if __name__ == '__main__':
    file_path = 'data.xlsx'
    coal_consumables, oil_consumables, natural_gas_consumables = read_structure_of_consumables(file_path)
    plot_structure_of_consumables(coal_consumables)
    plot_structure_of_consumables(oil_consumables)
    plot_structure_of_consumables(natural_gas_consumables)
