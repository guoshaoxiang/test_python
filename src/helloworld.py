# print("hello world")
# a = b = c = 1
# c = c + 1
# print(a, b, c)

# tinydict = {'name': 'john', 'code': 6734, 2: 'sales'}
# print(tinydict[2], tinydict['name'])

# str = "sdf44fdda()"
# print(repr(str))

# a = 10
# b = 20
# list = [1, 2, 3, 4, 5];
#
# if (a in list):
#     print("1 - 变量 a 在给定的列表中 list 中")
# else:
#     print("1 - 变量 a 不在给定的列表中 list 中")

# for s in "python":
#     print(s)

# for index in range(len("python")):
#     if (index == 2):
#         continue
#     print("python"[index])
#
# else:
#     print("hhhh")

# import math
# import cmath
# a = 1.2
# print(math.ceil(a))
# print("cmath.sin:", cmath.sin(30))

# import random
# for index in range(1, 10):
#     print(random.random())

# print( "My name is %s and weight is %d kg!" % ('Zara', 21))

# import calendar
# cal = calendar.month(2019, 5)
# print(cal)

# import test_module
# print(test_module.sum(3, 5))

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         class_name = self.__class__.__name__
#         print
#         class_name, "销毁"
#
#
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print(id(pt1), id(pt2), id(pt3))  # 打印对象的id
#
# del pt1
# del pt2
# del pt3

# a = str(input('a = '))
# print("sssssss", len(a))

# for x in range(1, 101, 2):
#     print(x)

# row = int(input('请输入行数: '))
# for i in range(row):
#     for _ in range(i + 1):
#         print('*', end='')
#     print()
#
#
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()
#
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()

m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fmn = 1
for num in range(1, m - n + 1):
    fmn *= num
print(fm // fn // fmn)