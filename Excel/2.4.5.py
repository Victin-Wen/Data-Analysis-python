# 2.4.5 输出与输出格式设置
print('我正在学习：{}'.format('python基础知识'))  # 一对一填充
print('我正在学习：{}中的{}'.format('python数据分析', 'python基础知识'))  # 多对多填充
print("{}约{}亿".format("2018年中国单身人数", 2))
print("{}约{:.2f}亿".format("2018年中国单身人数", 2))  # 浮点数设置
print("中国男性占总人口的比例：{:.2%}".format(0.519))  # 百分数设置

# 2.5.3 字符串的复制
var = "python is good! " * 3
print(var)  # 对字符串重复三遍

# 2.5.5 字符串查找
var1 = "测试" in "新产品上线测试号"
print(var1)  # True

var2 = "测试" in "我是一个正常用户"
print(var2)  # False

var3 = "测试" not in "新产品上线测试号"
print(var3)  # False

var4 = "测试" not in "我是一个正常用户"
print(var4)  # True

# 查找c在字符串中的位置
print("Abc".find("c"))  # 2,即第二位

# 查找d是否在字符串中
print("Abc".find("d"))  # -1,即不存在

# 2.5.7 字符串的分隔
# 将字符串“a,b,c”用逗号分隔
print("a,b,c".split(","))  # ['a', 'b', 'c']
# 将字符串“a|b|c”用|分隔
print("a|b|c".split("|"))  # ['a', 'b', 'c']

# 2.5.8 移除字符
# 移除空格
print(" a ".strip())  # a
# 移除换行符
print("\t\n a \t".strip())  # a
# 移除指定字符A
print("AaAAaaA".strip("A"))  # aAAaa,移除首尾的A

"""2.6 数据结构——列表"""
null_list = []
int_list = [1, 2, 3]
str_list = ["a", "b", "c"]

print(int_list * 2)  # [1, 2, 3, 1, 2, 3],列表的复制
print(str_list * 2)  # ['a', 'b', 'c', 'a', 'b', 'c'],列表的合并
print(int_list + str_list)  # [1, 2, 3, 'a', 'b', 'c'],列表的合并
# int_list.extend(str_list)
# print(int_list)  # [1, 2, 3, 'a', 'b', 'c'],列表的合并
# str_list.extend(int_list)
# print(str_list)   # ['a', 'b', 'c', 1, 2, 3],列表的合并
int_str_list = [1, 2, "a", "b"]

# 2.6.5 插入新元素append(), insert()
int_list.append(4)
print(int_list)  # [1, 2, 3, 4],在末尾插入新的元素
str_list.append("d")
print(str_list)  # ['a', 'b', 'c', 'd']

int_list.insert(3, 8)  # [1, 2, 3, 8, 4],在下标3的位置插入元素8
print(int_list)
# 2.6.6 获取列表中值出现的次数 count()
score_list = [3, 4, 9, 4, 7, 9, 3, 6, 4, 3, 7, 9]
print(score_list.count(9))  # 3
# 2.6.7 获取列表中值的位置 index()
sale_list = ["Vickie", "Felix", "Alice", "Marry", "Tony", "Max"]
print(sale_list.index("Tony"))  # 4

# 2.6.8 获取列表中指定位置的值
v = ["a", "b", "c", "d", "e"]
print(v[0])  # a,普通索引
print(v[3])  # d,普通索引
print(v[1:3])  # ['b', 'c'],切片索引，前闭后开区间
print(v[0:3])  # ['a', 'b', 'c'],切片索引，前闭后开区间
print(v[3:])  # ['d', 'e'],从第四位到最后一位的数

# 2.6.9 删除列表中的值pop(), remove()
# str_list.pop(1)
# print(str_list)  # ['a', 'c', 'd'],删除第二位的值
# str_list.remove("c")
# print(str_list)  # ['a', 'b', 'd'],删除元素c

# 2.6.10 对列表中的值进行排序 sort()
s = [1, 3, 4, 6, 2]
s.sort()
print(s)  # [1, 2, 3, 4, 6]

"""2.7 数据结构——字典"""
test_dict = {}
test_dict["Felix"] = 16624921456
test_dict["Vickie"] = 17982331562
# print(test_dict)  # {'Felix': 16624921456, 'Vickie': 17982331562}

# 将键值以列表的形式存放在元组中，然后用dict进行转换
contact = (["Felix", 16624921456], ["Vickie", 17982331562])
test_dict = dict(contact)
# print(test_dict)  # {'Felix': 16624921456, 'Vickie': 17982331562}

# 2.7.3 字典的keys()、values()、items()方法

# test_dict.keys()
print(test_dict.keys())  # dict_keys(['Felix', 'Vickie'])
print(test_dict.values())  # dict_values([16624921456, 17982331562])
print(test_dict.items())  # dict_items([('Felix', 16624921456), ('Vickie', 17982331562)])

"""2.8 数据结构——元组"""
tup1 = (1, 2, 3)

tup2 = ("a", "b", "c")
print(tup1)  # (1, 2, 3)
print(tup2)  # ('a', 'b', 'c')
# 打印长度
print(len(tup1), len(tup2))  # 3 3
# 2.8.4 获取元组内的元素
# 普通索引
print(tup1[2])  # 3
print(tup2[1])  # b
# 切片索引
print(tup1[1:3])  # (2, 3)
print(tup1[:3])  # (1, 2, 3)
print(tup2[1:])  # ('b', 'c')
# 2.8.5 元组与列表相互转换
print(list(tup1))  # [1, 2, 3]
print(tuple(s))  # (1, 2, 3, 4, 6)
# 2.8.6 zip()函数
# zip()函数将可迭代的对象（列表、元组）作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# 通常与for循环一起搭配使用
list_a = [1, 2, 3, 4]
list_b = ["a", "b", "c", "d"]
for i in zip(list_a, list_b):
    print(i)
"""2.10 循环语句"""
# 2.10.1 for循环
subject = ["Excel", "SQL", "Python", "统计学"]
for sub in subject:
    print("我目前正在学习：{}".format(sub))
# 2.10.2 while循环
week = 0
while week <= 7:
    print("我已经学习数据分析{}周了".format(week))
    week += 1
print("我已经学习数据分析{}周了，我可以去找工作啦".format(week - 1))
"""2.12 函数"""


# 2.12.1 普通函数


def learn_python(location):
    doing = ("我正在{}上学Python".format(location))
    # print("我正在{}上学Python".format(location))
    return doing


learn_python("subway")
learn_python("bus")
learn_python("taxi")


# 定义两个参数
def learn_python(location, people):
    doing = ("我正在{}上学Python,人{}".format(location, people))
    return doing


ref = learn_python("地铁", "很多")
print(ref)

# 2.12.2 匿名函数：省略了def定义函数的过程
# lambda arg1, arg2, arg3: expression
f = lambda x, y: x + y
print(f(1, 2))  # 3

"""2.13 高级特性"""
# 2.13.1 列表生成式
num = [1, 2, 3, 4, 5]
print([i ** 2 for i in num])  # [1, 4, 9, 16, 25]
# 如果数据量大for循环嵌套太多程序运行就会变得很慢
list1 = ["A", "B", "C"]
list2 = ["a", "b", "c"]
print([m + n for m in list1 for n in list2])
# 2.13.2 map()函数：表现形式map(function,args)表示对序列args中的每个值进行function操作最终得到一个结果序列
a = map(lambda x, y: x + y, [1, 2, 3], [3, 2, 1])
print(a)  # <map object at 0x000001709B4E51F0>,map()函数生成的结果序列不会直接把全部结果显示出来
# 要想获取到结果需要for循环遍历取出来，也可以使用list方法将结果生成一个列表
for i in a:
    print(i)

b = list(map(lambda x, y: x + y, [1, 2, 3], [3, 2, 1]))
print(b)  # [4, 4, 4]

"""2.14 模块"""
# 数据分析领域用得较多的三个模块分别是Numpy, Pandas, matplotlib.
# import module_name  # 直接import具体的模块名
# from module1 import module2 # 从module1中import module2

