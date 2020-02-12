"""Chapter 5 数据预处理"""
import pandas as pd

"""
# 5.1.1 查看缺失值
df2 = pd.read_excel(r"D:\Vickie\practice\test.xlsx",
                    sheet_name="Sheet2")
print(df2)  # NaN代表空值
print(df2.info())  # 性别      3 non-null object,而其他列是4 ，所以在性别一列有一个空值。
# 还可以用isnull()方法判断，如果是缺失值则返回True
print(df2.isnull())
# 5.1.2 删除缺失值 dropna()方法默认删除含有缺失值的行
print(df2.dropna())  # 如果想删除空白行，则传入参数
print(df2.dropna(how="all"))  # 只删除全为空值的行
# 5.1.3 缺失值填充：一般情况只要缺失数据比例不是过高（不大于30%）尽量不要删除而是选择填充
# fillna()方法
df3 = pd.read_excel(r"D:\Vickie\practice\test.xlsx",
                    sheet_name="Sheet3", sep=",")
print(df3.fillna(0))  # 缺失值按格式补0
print(df3.fillna({"性别": "男", "年龄": "30"}))  # 其余空值显示NaN, NaT可能根据其他列的格式显示


# 5.2 重复值处理
# drop_duplicates()方法，默认对所有值进行重复值判断，切默认保留第一个（行）值。
df4 = pd.read_excel(r"D:\Vickie\practice\test.xlsx",
                    sheet_name="Sheet4", sep=",")
print(df4)
print(df4.drop_duplicates(subset=["客户姓名", "唯一识别码"], keep="last"))  # 保留最后一个值，默认是first
print(df4.drop_duplicates(subset=["客户姓名", "唯一识别码"], keep=False))  # 把重复值全删除


# 5.3 异常值的检测与处理
# replace()方法对特定的值进行替换
# 5.4 数据类型转换
# Pandas主要有6种数据类型：int, float, object(python对象类型，O表示), string_(字符串类型，S10表示长度为10的字符串), unicode_(
# 固定长度的unicode类型，与字符串定义方式一样), datetime64[ns](表示时间格式)
# 在python中也可通过dtype方法获取某一列的数据类型
df4 = pd.read_excel(r"D:\Vickie\practice\test.xlsx",
                    sheet_name="Sheet4", sep=",")
# print(df4)
# print(df4["订单编号"].dtype)
# print(df4["唯一识别码"].dtype)

# 5.4.2 数据类型转换 astype()方法
# print(df4["唯一识别码"].astype("float64"))  # 将唯一识别码从Int类型转换为float类型
# 5.5 索引设置：默认从0开始的自然数作为索引
# df4.columns = ["订单编号", "客户", "识别码", "时间"]
# df4.index = [1, 2, 3, 4, 5, 6]
print(df4.set_index("订单编号"))  # 重新设置索引列，传入多个列名时称为层次化索引（一般在某一列有多个重复值的情况下）
# 5.5.3 重命名索引rename()方法
print(df4.rename(columns={"订单编号": "新订单编号",
                          "客户姓名": "新客户姓名"},
                 index={1: "一",
                        2: "二",
                        3: "三", }))
                        

# 5.5.4 重置索引：主要应用在层次化索引表中，将索引列当做一个columns进行返回
# reset_index(level=None, drop=False, inplace=False)
# level指定将层次化索引的第几级别转化为columns，第一个索引为0级，第二个索引为1级，默认为全部索引
# drop参数用来指定是否将原索引删掉，即不作为一个新的columns，默认不删除
# inplace是否修改原数据表
df5 = pd.read_excel(r"D:\Vickie\practice\test.xlsx",
                    sheet_name="5.5.4", sep=" ")
print(df5)
print(df5.reset_index())  默认将全部index转换为columns
# reset_index()方法常用于数据分组、数据透视表中
"""























