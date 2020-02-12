"""Chapter 4 获取数据源"""
import pandas as pd

import pymysql

# df = pd.read_excel(r"D:\Vickie\practice\test.xlsx",
#                    sheet_name="Sheet1")  # sheet_name= 0,传入Sheet顺序
from pandas.io import sql

df = pd.read_excel(r"D:\Vickie\practice\test.xlsx",
                   sheet_name=0, index_col=0)  # index_col表示用.xlsx文件中的第几列做索引，从0开始计数

# print(df)
# 指定列索引，将本地文件导入DataFrame时，默认使用源数据表的第一行作为列索引，也可通过设置header参数设置列索引。header参数值默认为
# 0，即用第一行作为列索引；也可以是其他行，只需传入具体的那一行即可；也可使用默认从0开始的数作为列索引
df = pd.read_excel(r"D:\Vickie\practice\test.xlsx",
                   sheet_name=0, header=None)

# print(df)

# 指定导入列
df = pd.read_excel(r"D:\Vickie\practice\test.xlsx",
                   # usecols=0)  # Passing an integer for `usecols` is no longer supported.  Please pass in a list of
                   # int from 0 to `usecols` inclusive instead.
                   usecols=[0])  # 表示导入第几列，从0开始计数，也可传入多个
# print(df)
df = pd.read_excel(r"D:\Vickie\practice\test.xlsx",
                   usecols=[0, 2])
# print(df)

# 4.1.2 导入.csv文件
df = pd.read_csv(r"D:\Vickie\practice\test.csv", sep=" ", nrows=2)
print(df)
# 如果是CSV UTF -8（逗号分隔）（*.csv）格式的文件，导入时就要加encoding参数
# 如果是CSV（逗号分隔）（*.csv）格式的文件，导入时需要把编码格式改为gbk。
# engine指定：当文件路径或文件名中包含中文时。
# 调用read_csv()方法时，默认使用C语言作为解析语言，只需把默认的改为python即可。如果文件格式是CSV UTF -8（逗号分隔）（*.csv），
# 对应编码格式应为utf-8-sig；如果是CSV（逗号分隔）（*.csv）格式的文件，对应编码格式为gbk。

# 4.1.3 导入.txt文件
# 利用read_table()导入.txt文件
df1 = pd.read_table(r"D:\Vickie\practice\test.txt", sep=" ")
print(df1)

# 与read_csv()【逗号分隔，可以不写】不同的是，read_table()即使是逗号分隔的文件也需要用sep指明分隔符号。
# read_table()函数其他参数的用法与read_csv()基本一致
df2 = pd.read_table(r"D:\Vickie\practice\test.csv", sep=" ")
print(df2)
"""
# 4.1.4 导入sql文件
eng = pymysql.connect(host='localhost',
                      user='root',
                      password='root',
                      db='test',
                      charset='utf8')

df = pd.read_sql(sql, eng)
print(df)
"""

"""4.2 新建数据"""
"""4.3 熟悉数据"""
# 4.3.1 head()预览前几行，默认显示前五行
df3 = pd.read_excel(r"D:\Vickie\practice\test.xlsx")
print(df3.head())
print(df3.head(3))
# 4.3.2 shape()获取数据表的大小

# print(df3.shape)  # (8, 4)有8行4列数据（不会把行索引、列索引计算进去）

# 4.3.3 info()方法查看数据表中的数据类型
# print(df3.info())
# 4.3.4 describe()方法获取数值分布情况
print(df3.describe())






















