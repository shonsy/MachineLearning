#!/usr/bin/python
#-*- coding:utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import numpy as np
# # 1. Matplotlib架构
#
# # 2. 基本图像的绘制
# plt.plot(3, 2,'*')
# plt.show()
# # x = 2 , y = 3
# print('=============数据展示1=============')
#
# # 使用scripting层绘制
# fig = Figure()
# canvas = FigureCanvasAgg(fig)
# # FigureCanvasAgg画布引用进来
# ax = fig.add_subplot(111)
# ax.plot(3,2,'.')
# canvas.print_png('test.png')
# # canvas帆布
# """
# 本地保存图像
# """
#
# # # matplot 会自动用颜色区分不同的数据#  gca ，拿到当前坐标轴
# plt.figure()
# plt.plot(3,2,'o')
# plt.show()
# ax = plt.gca()
# # gca拿到当前坐标轴
# ax.axis([0,6 , 0,10] )
# # axis轴
# plt.show()
# """
# 更改axis坐标轴范围 x , y
# """
#
# """
# matplot会自动用颜色区分不同的数据
# """
# plt.figure()
# plt.plot(1.5, 1.5, 'o')
# plt.plot(2, 2, '*')
# plt.plot(2.5, 2.5, '*')
# plt.show()
#
# # 3. 散点图 scatter
#
# x = np.arange(1,10)
# y = x
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# #设置标题
# ax1.set_title('Scatter Plot')
# # #设置X轴标签
# plt.xlabel('X')
# #设置Y轴标签
# plt.ylabel('Y')
# # #画散点图
# ax1.scatter(x,y,c = 'r',marker = 'o')
# #设置图标
# plt.legend('x1')
# #显示所画的图
# plt.show()
#
#
# # 改变颜色及大小
#
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# y = x
# colors = ['red'] * (len(x) - 1)
# colors.append('green')
# plt.figure()
# plt.scatter(x, y, s=100, c=colors)
# plt.show()
#
# """
# 使用zip合并两个列表为一个新列表
# 新列表中的每个元素为对应位置上的元组
# 使用*进行对元祖列表解包
# """
# l1 = list(range(1, 6))
# l2 = list(range(6, 11))
# zip_generator = zip(l1, l2)
# tuple_list = list(zip_generator)
# print(type(zip_generator))
# print(list(tuple_list))
# print('==============解包================')
# x , y = zip(*tuple_list)
# print(x)
# print(y)
#
# print('==============数据展示===============')
# plt.figure()
# plt.scatter(x[:2], y[:2], c='red', label='samples 1')
# plt.scatter(x[2:], y[2:], c='blue', label='samples2')
# plt.show()
#
#
# """
# 添加坐标标签，标题
# """
#
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title('Scatter Plot Example')
# plt.show()

# 4.线图
linear_data = np.arange(1, 9)
quadratic_data = linear_data ** 2
#注意，这里我们只指定了y轴数据，x轴的都是matplotlib自动生成的
plt.figure()
plt.plot(linear_data, '-o', quadratic_data, '-o')
# plt.show()
plt.show()
plt.plot([22, 44, 66], '--r')
plt.show()


"""
1.添加坐标轴标签及图例
2.填充两个line间的区域
"""

# 添加坐标轴标签及图例
plt.xlabel('x data')
plt.ylabel('y data')
plt.title('Line Chart Title')
plt.legend(['legend1', 'legend2', 'legend3'])
plt.show()

# 填充两个line间的区域
plt.gca().fill_between(range(len(linear_data)),
                      linear_data, quadratic_data,
                      facecolor='green',
                      alpha=0.25)
"""
fill_between是2条线之间的区域
x坐标是len(linear_data) ， y坐标是linear_data, quadratic_data,
facecolor是2条线之间的颜色
alpha = 0.25透明度
"""
plt.show()
# 柱状图

plt.figure()
x_vals = list(range(len(linear_data)))
# x坐标是range(len(linear_data))生成的个数[0~7]
# y轴是np.arange(1, 9)的值
plt.bar(x_vals, linear_data, width=0.3)
# width = 0.5 1：连起来了
plt.show()
# plt.show()

# group bar chart
"""
同一副图中添加新的柱状图
注意，为了不覆盖第一个柱状图，需要对x轴做偏移
"""
x_vals2 = [item + 0.3 for item in x_vals]
plt.bar(x_vals2, quadratic_data, width=0.3)
plt.show()

# stack bar chart
plt.figure()
x_vals = list(range(len(linear_data)))
plt.bar(x_vals, linear_data, width=0.3)
# 横坐标是【0~7】，y轴的数据是matplotlib生成的
plt.bar(x_vals, quadratic_data, width=0.3, bottom=linear_data)
plt.show()

# 横向柱状图
plt.figure()
x_vals = list(range(len(linear_data)))
plt.barh(x_vals, linear_data, height=0.3)
# 水平方向指定宽度，横向方向的话指定高度
plt.barh(x_vals, quadratic_data, height=0.3, left=linear_data)
# 纵向叠加的话，放在左边
plt.show()
