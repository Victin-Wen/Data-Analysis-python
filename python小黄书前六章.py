'''
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')

too_expensive =  'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
print("The first motorcycle I owned was a " + first_owned.title() + ".")
# 3-4嘉宾名单
dinner = ['viclie wen', 'felix xue', 'star cao', 'diana ning']
message = "Hi " + dinner[0].title() + ", " + "can I invite you have dinner together?"
dinner.append('robert')
new_message = "Hi " + dinner[4].title() + ", " + "can I invite you have dinner together?"
dinner.insert(0, 'alisa li')
dinner.append('crystal')
dinner.insert(2, 'haili ding')
message0 = "Hi " + dinner[0].title() + ", " + "can I invite you have dinner together?"
message1 = "Hi " + dinner[1].title() + ", " + "can I invite you have dinner together?"
message2 = "Hi " + dinner[2].title() + ", " + "can I invite you have dinner together?"
message3 = "Hi " + dinner[3].title() + ", " + "can I invite you have dinner together?"
message4 = "Hi " + dinner[4].title() + ", " + "can I invite you have dinner together?"
message5= "Hi " + dinner[5].title() + ", " + "can I invite you have dinner together?"
message6 = "Hi " + dinner[6].title() + ", " + "can I invite you have dinner together?"
print(message0 + '\n' + message1 + '\n' + message2 + '\n' + message3 + '\n' + message4 + '\n' + message5 + '\n' +
message6)
print('sorry, I have to invite two person to have dinner only')
dinner.pop(6)
print(dinner)

# 3.3 组织列表
# 3.3.1 sort()对列表永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()            # 永久性修改了列表元素的顺序（按字母的排列顺序）
print(cars)
#按与字母顺序相反的顺序排列元素只需向 sort 方法传递参数 reverse = True
cars.sort(reverse = True)
print(cars)

# 3.3.2 sorted()临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))   # 保留元素原来的顺序，同时以特定的顺序呈现它们

print("\nHere is the original list again:")
print(cars)         # 使用sorted()后列表元素的排列顺序没有变
#若要按与字母顺序相反的顺序显示列表，也可向函数sorted()传递参数reverse = Ture
#Note: 在并非所有的值都是小写时，按字母顺序排列列表要复杂些。大多数排序方式都可以使用此节知识。

# 3.3.3 倒着打印列表 反转使用方法reverse()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()   # 只是反转列表元素的排列顺序，而不是按字母顺序相反的顺序排列
print(cars)   # 方法reverse()永久的修改列表元素的排列顺序，可随时恢复，再次调用reverse()即可

# 3.3.4 确定列表长度len()
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
print(len(cars))    # python计算列表元素数时从1开始
# 3-8
places = ["japan", "korea", "australia", "italy", "brazil", "england"]
print("This is the original list:")
print(places)
print("This is the sorted list:")
print(sorted(places))
print("This is the original list again:")
print(places)
places.sorted(reverse = True)
print("This is the sort1 list:")
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)

# 3.4 使用列表时避免索引错误
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])   # 索引是从0开始的，因此报错：IndexError: list index out of range
print(motorcycles[-1])
# 发生索引错误找不到解决办法时尝试打印列表长度
# 第四章 操作列表

# 4.1 遍历整个列表 magicians.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    #print(magician)
# 4.1.2 在for循环中执行更多操作
    print(magician.title() + ", that was a great trick!")
#    print("I can't wait to see your next trick, " + magician.title() + ".\n")
# 使用for循环对每个元素执行钟多不同的操作很有用
# 4.1.3 在for循环结束后执行一些操作：在for循环之后，通常需要提供总结性输出或者执行程序必须完成的其他操作。
# 在for循环后面，没有缩进的代码都只执行一次，而不会重复执行。
print("Thank you, everyone. That was a great magic show!")
# 使用for循环处理数据是一种对数据集执行整体操作的不错的方式。例如，初始化游戏——遍历角色列表；再在循环后添加一个不缩进的代码块，
   Play Now按钮。
# 4.2 避免缩进错误: 忘记缩进；忘记缩进额外的代码行；不必要的缩进；循环后不必要的缩进；for后遗漏了冒号

# 4.3 创建数值列表
# 4.3.1 range():生成一列数字，使用若不达预期，尝试将指定的值加一减一 numbers.py
for value in range(1,6):
    print(value)
# 4.3.2 创建数字列表 list()将range()的结果直接转换为列表
numbers = list(range(1,6))
print(numbers)

# 还可指定步长
even_numbers = list(range(2,11,2))
print(even_numbers)

# 创建一个列表，其中包含前十个整数的平方 squares()
squares =  []
for value in range(1,11):
    square = value **2
    squares.append(square)
print(squares)

# 为使代码简洁，可不使用临时变量square,直接将每个计算得到的值附加到列表末尾
squares =  []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# 4.3.3 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)
print(min(digits),max(digits),sum(digits))

# 4.3.4 列表解析
squares = [value**2 for value in range(1,11)]  # 注意结尾没有冒号
print(squares)

# 4-3 数列20
for numbers in range(1,21):
    print(numbers)

# 数列一百万
squares = []
for value in range(1,1000000):
#    print(value)

squares = [value for value in range(1, 1000001)]
# print(min(squares))
# print(max(squares))
print(sum(squares))

# 4-6 奇数
odd_numbers = list(range(1,20,2))
for odd_number in odd_numbers:
    print(odd_number)

# 4-7 3的倍数
#squares = [value**2 for value in range(1,11)]  # 注意结尾没有冒号
divide = [value % 3 ==0  for value in list(range(1,31))]
print(divide)

# 4-8 立方
squares =  []
for value in range(1,11):
    squares.append(value**3)
print(squares)

# 4-9 立方解析
squares = [value**3 for value in range(1,11)]
print(squares)

# 4.4 使用列表的一部分
# 4.4.1 切片 players.py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3 : ])

# 4.4.2 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team: ")
for player in players[ :3]:    #只遍历前三名
    print(player.title())

# 4.4.3 复制列表 foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[ : ]

my_foods.append('cannoli')    # cannoli包含在我喜欢的食物列表而不在朋友的列表
friend_foods.append('ice cream')
print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

# 不使用切片的i情况下复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
# 这行不通，因为只是将my_foods赋给my_foods，而不是将其副本存储
# friend_foods = my_foods

# 4-10 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("The middle three items in the list are: ")
#for player in players[ :3]:
#    print(player.title())
for player in players[1:4]:
    print(player.title())

# 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[ : ]

my_foods.append('cannoli')    # cannoli包含在我喜欢的食物列表而不在朋友的列表
friend_foods.append('ice cream')
print("My favorite foods are: ")
for my_food in my_foods[ : ]:
    print(my_food)

print("My friend favorite foods are: ")
for friend_food in friend_foods[ : ]:
    print(friend_food)

# 4.5 元组：python将不能修改的值成为不可变的，而不可变的列表被称为元组
# 4.5.1 定义元组 dimensions.py
dimensions = (200, 50)    # 使用圆括号定义元组
# dimensions[0] = 250  TypeError: 'tuple' object does not support item assignment
print(dimensions[0])

# 4.5.2 遍历元组中的所有值
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# 4.5.3 修改元组变量：虽不能修改元组的元素，但是可以给存储元组的变量赋值
dimensions = (200, 50)    # 要修改前面的元组，可重新定义整个元组
print("Original dimensions: ")    # 首先定义一个元组，将其存储的尺寸打印，
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)       # 将一个新的元组存储到变量，
print("\nModified dimensions: ")    # 打印新的尺寸
for dimension in dimensions:    # 给元组变量赋值是合法的
    print(dimension)    # 相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不变，可使用元组。
# 4.6 设置代码格式：PEP8建议每级缩进都使用四个空格。行长为竖线
# 将程序的不同部分分开可使用空行。不能滥用。
# 第五章 if语句

# 5.2 条件测试
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 5.2.1 检查是否相等
# car = 'bmw'
# car == 'bmw'
# True
# 5.2.2 检查是否相等时不考虑大小写(如下)如果大小写无关紧要，只想检查变量的值，将值转换为小写再比较
# car = 'Audi'
# car == 'audi'
# False
# 5.2.3 检查是否不相等 toppings.py  有时候检查两个值是否不等的效率更高
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# 5.2.4 比较数字
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")
# 5.2.5 检查多个条件 and, or


# 5.2.6 检查特定值是否包含在列表中 in
# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# 'mushrooms' in requested_toppings
# True
# 5.2.7 检查特定值是否不包含在列表中 not in    banned_users.py
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
# 5.2.8 布尔表达式【布尔值通常用于记录条件，如游戏是否正在运行，或用户是否可以编辑网站的特定内容】
# game_active =True    【在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方法】
# can_edit = False

# 5.3 If语句 voting.py
age =19
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')

# if-else
age = 17
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('Sorry, you are too young to vote.')
    print('Please register to vote as soon as you turn 18!')

# if- elif -else amusement_park.py
age =12

if age <4:
    print('Your admission cost is $0.')
elif age <18:
    print('Your admission cost is $5.')
else:
    print('Your admission cost is $10')

# 修订: 效率更高，容易修改
age =12
if age <4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print('Your admission cost is $' + str(price) + '.')

# 5.3.4 使用多个elif代码块
age =12
if age <4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print('Your admission cost is $' + str(price) + '.')

# 5.3.5 省略else 代码块
age =12
if age <4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print('Your admission cost is $' + str(price) + '.')

# 5.3.6 测试多个条件 toppings.py
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:    # 不能使用 elif ,因为有一个测试通过它就会跳过余下的测试
    print('Adding pepperoni.')    # 如果想执行一个代码块就用 if-elif-else, 运行多个代码块，就使用一系列独立的if语句。
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')
print("\nFinished making your pizza!")

# 5.4 使用if语句处理列表 toppings.py
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':    # 如果比萨店的青椒用完了
        print('Sorry, we are out of green peppers right now.')  # 告知顾客
    else:
        print('Adding ' + requested_topping + '.')

print('\nFinished making your pizza!')

# 5.4.2 确定列表不是空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')   # result: Are you sure you want a plain pizza?

# 5.4.3 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:    # result
    if requested_topping in available_toppings:     # Adding mushrooms.
        print('Adding ' + requested_topping + '.')      # Sorry, we don't have french fries.
    else:
        print("Sorry, we don't have " + requested_topping + '.')    # Adding extra cheese.
print("\nFinished making your pizza!")      # Finished making your pizza!
'''
# 第六章 字典
# 6.1 一个简单的字典 alien.py
alien_0 = {'color': 'green', 'points' : 5}

print(alien_0['color'])
print(alien_0['points'])




