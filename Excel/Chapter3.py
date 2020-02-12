"""Chapter 3 Pandas数据结构"""
import pandas as pd
import numpy as np

# import matplotlib.pyplot as plt
from pandas import RangeIndex

"""3.1 Series数据结构"""
S1 = pd.Series(["a", "b", "c", "d"])
print(S1)  # 默认从0开始做数据标签，即0、1、2、3
S2 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
print(S2)  # 通过index自定义索引为a,b,c,d
# 传入一个字典
S3 = pd.Series({"a": 1, "b": 2, "c": 3, "d": 4})
print(S3)
# 获取Series的索引：index()方法
S1.index
RangeIndex(start=0, stop=4, step=1)
print(S2.index)  # Index(['a', 'b', 'c', 'd'], dtype='object')
# 获取Series的值：values()方法
S1.values
np.array(['a', 'b', 'c', 'd'], dtype=object)
print(S2.values)  # [1 2 3 4]
"""3.2 DataFrame表格型数据结构"""
# DataFrame由一组数据与一对索引（行、列）组成的表格型数据结构
# 只传入一个单一列表，该列表的值会显示成一列，且行和列都是从0开始的默认索引
df1 = pd.DataFrame(["a", "b", "c", "d"])
print(df1)
# 传入一个嵌套列表：列表里嵌套的列表也可以换成元组
df2 = pd.DataFrame([["a", "A"], ["b", "B"], ["c", "C"], ["d", "D"]])
print(df2)
# 若只给DataFrame()方法传入列表，则行、列索引都是默认值，可通过columns参数自定义列索引，index参数自定义行索引
# 设置列索引
df31 = pd.DataFrame([["a", "A"], ["b", "B"], ["c", "C"], ["d", "D"]],
                    columns=["小写", "大写"])
print(df31)
# 设置行索引
df32 = pd.DataFrame([["a", "A"], ["b", "B"], ["c", "C"], ["d", "D"]],
                    index=["一", "二", "三", "四"])
print("df32 = ")
print(df32)
# 同时设置
df33 = pd.DataFrame([["a", "A"], ["b", "B"], ["c", "C"], ["d", "D"]],
                    columns=["小写", "大写"],
                    index=["一", "二", "三", "四"])
print(df33)

# 传入一个字典
data = {"小写": ["a", "b", "c", "d"], "大写": ["A", "B", "C", "D"]}
df41 = pd.DataFrame(data, index=["一", "二", "三", "四"])
print(df41)  # key值相当于列索引，同样可以使用index定义行索引

# 3.2.3 获取DataFrame的行、列索引
df2.columns
RangeIndex(start=0, stop=2, step=1)
print(df33.columns)  # Index(['小写', '大写'], dtype='object')

df2.index
RangeIndex(start=0, stop=2, step=1)
print(df33.index)  # Index(['一', '二', '三', '四'], dtype='object')

# 3.2.4 获取DataFrame的值：就是获取DataFrame中的某些行或列，将在第六章讲解


























