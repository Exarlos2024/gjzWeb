import random
import pandas as pd

def generate_random_color():
    """生成随机颜色"""
    return f'#{random.randint(0, 0xFFFFFF):06x}'

def highlight_rows(row, colors):
    """为每一行设置背景色"""
    return [f'background-color: {colors[row["重复组"]]}' for _ in row]

# class DataSorter:
#     def __init__(self, dataframe):
#         self.dataframe = dataframe

#     def sort_by_columns(self, columns):
#         """根据指定的列对数据进行排序"""
#         return self.dataframe.sort_values(by=columns).reset_index(drop=True)
