#!/usr/bin/python
#-*- coding:utf-8 -*-
import math
import csv
# 一、python面向对象编程
class Person:
    def __init__(self, name, company='自由职业'):
        # 构造函数
        self.name = name
        self.company = company

    def set_name(self, name):
        self.name = name

    def set_company(self, company):
        self.company= company

p = Person('小王')
print('{}的职业是{}'.format(p.name, p.company))

p.set_company('数据分析师')
p.set_name('王工')
print('{}的职业是{}'.format(p.name, p.company))


# 二、Python map() 函数
print('示例1，获取两个列表对应位置上的最小值：')
l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]
mins = map(min, l1, l2)
print(mins)
# (func , List) 最小的

# map()函数操作时，直到访问数据时才会执行
for item in mins:
    print(item)

print('示例2，对列表中的元素进行平方根操作：')
squared = map(math.sqrt, l2)
print(squared)
print(list(squared))

# # 三、匿名函数 lambda
my_func = lambda a, b, c: a * b
# 前面是参数， 后面是方法体
print(my_func)
print(my_func(1, 2, 3))

# 结合map
print('lambda结合map')
l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]
result = map(lambda x, y: x * 2 + y, l1, l2)
print(list(result))

# 四、列表推导式
print('找出1000内的偶数(for循环)：')
l1 = []
for i in range(1000):
    if i % 2 == 0:
        l1.append(i)
print(l1)

print('找出1000内的偶数（列表推导式）')
L2 = [i for i in range(1000) if i %2 ==0]
print(L2)

# 五、Python操作csv数据文件
with open('grades.csv') as csvfile:
    grades_data = list(csv.DictReader(csvfile))
print('记录个数：', len(grades_data))
print('前2条记录：', grades_data[:2])
print('列名：', list(grades_data[0].keys()))
avg_assign1 = sum(float(row['assignment1_grade']) for row in grades_data) / len(grades_data)
print('assignment1平均分数：', avg_assign1)
assign1_sub_month = set(row['assignment1_submission'][:7] for row in grades_data)
print(assign1_sub_month)







