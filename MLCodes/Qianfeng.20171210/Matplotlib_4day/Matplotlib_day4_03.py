#!/usr/bin/python
#-*- coding:utf-8 -*-

# 1.动画及交互式渲染
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

n = 100
x = np.random.randn(n)
# # 有报错
def update(curr_frm):
    if curr_frm == n:
        a.event_source.stop()
    plt.cla()
    bins = np.arange(-4, 4, 0.5)
    plt.hist(x[:curr_frm], bins=bins)
    plt.axis([-4, 4, 0, 30])
    plt.gca().set_title('Sampling the Normal Distribution')
    plt.gca().set_xlabel('Value')
    plt.gca().set_ylabel('Frequency')
    plt.annotate('n={}'.format(curr_frm), [3, 27])
fig = plt.figure()
# 100毫秒1帧
a = animation.FuncAnimation(fig, update, interval=100)
plt.show()


# 2.交互式

plt.figure()
data = np.random.rand(10)
plt.plot(data)

def onclick(event):
    plt.cla()
    plt.plot(data)
    plt.gca().set_title('Pixels x={}, y={},\n data={}, {}'.format(event.x, event.y, event.xdata, event.ydata))

plt.gcf().canvas.mpl_connect('button_press_event', onclick)
plt.show()


from random import shuffle
import pandas as pd

countries = ['China', 'Australia', 'India', 'USA', 'Canada']
shuffle(countries)
df = pd.DataFrame({'height': np.random.rand(5),
                  'weight': np.random.rand(5),
                  'country': countries})
plt.figure()
plt.scatter(df['height'], df['weight'], picker=5)
plt.gca().set_ylabel('Weight')
plt.gca().set_xlabel('Height')
plt.show()









