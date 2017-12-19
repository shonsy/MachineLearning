#!/usr/bin/python
#-*- coding:utf-8 -*-
# 引用必要的库
import  matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# 4.线图
"""
注意，这里我们只指定了y轴数据，x轴的都是matplotlib自动生成的
"""
linear_data = np.arange(1, 9)
quadratic_data = linear_data ** 2
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