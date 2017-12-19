#!/usr/bin/python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# # #1. Subplots
# plt.figure()
# # 表示1行2列，现在在第一个子图上进行操作
# # y轴是人为数据，x轴是matplotlib自动生成的
# plt.subplot(1, 2, 1)
# linear_data = np.arange(1, 9)
# plt.plot(linear_data, '-o')
# plt.show()
#
# exponential_data = linear_data ** 2
# plt.subplot(1, 2, 2)
# plt.plot(exponential_data, '-x')
# # plt.show()
#
# # 保证子图中坐标范围一致
# plt.figure()
# ax1 = plt.subplot(1, 2, 1)
# plt.plot(linear_data, '-o')
# ax2 = plt.subplot(1, 2, 2, sharey=ax1)
# # 返回sharey=ax1的对象，要使用ax1的y轴坐标
# plt.plot(exponential_data, '-x')
# plt.show()
#
# fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex=True, sharey=True)
# ax5.plot(exponential_data, '-')
# plt.show()
# """
# (ax1, ax2, ax3):第一行的数据
# (ax4, ax5, ax6)：第二行的数据
# sharex=True, sharey=True ，x轴和y轴的范围都是一样的
# ax5,只在第5张图中绘制，exponential_data：8^2=64
# """
#
# # 2.直方图
#
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
# axs = [ax1, ax2, ax3, ax4]
# # 4个子图 0 1 2 3
# for n in range(len(axs)):
#     sample_size = 10 ** (n + 1)
#     # 10^1  10^2  10^3 10^4
#     sample = np.random.normal(loc=0., scale=1., size=sample_size)
#     # 正太分布指定loc均值 ， scale标准差 ，size是生成多少个数据点
#     # 默认bin的个数为10
#     axs[n].hist(sample)
#     axs[n].set_title('n={}'.format(sample_size))
# plt.show()


# 使用gridspec和直方图绘制一个复杂分析图
# import matplotlib.gridspec as gridspec
#
# x = np.random.random(size=10000)
# # x轴是标准的随机分布，样本点是10000个点
# y = np.random.normal(loc=0., scale=1., size=10000)
# # y轴也是标准的正太分布，样本点10000个点
# plt.figure()
# gspec = gridspec.GridSpec(3, 3)
# # GridSpec把图像分割，3行3列
# top_hist = plt.subplot(gspec[0, 1:])
# # 第0行，第1列靠后
# side_hist = plt.subplot(gspec[1:, 0])
# # 第2,3行，第0列
# lower_right = plt.subplot(gspec[1:, 1:])
# # 其余的部分4个区域
#
# lower_right.scatter(x, y)
# top_hist.hist(x, bins=100, normed=True)
# side_hist.hist(y, bins=100, orientation='horizontal', normed=True)
# # orientation='horizontal'指定方向，方向 = ‘水平’
#
# side_hist.invert_xaxis()
# # invert_xaxis()坐标轴反转
# plt.show()
"""
x轴是（上）是随机分布的散点图，y轴（左边）是正太分布
1.x轴点2边是均匀分散的，中间是密集的
2.主要看数据在2个维度上的分布情况
"""

# 3.盒型图

import pandas as pd
# 正态分布采样
normal_sample = np.random.normal(loc=0., scale=1., size=10000)
# 随机数采样
random_sample = np.random.random(size=10000)
# gamma分布采样
gamma_sample = np.random.gamma(2, size=10000)

df = pd.DataFrame({'normal': normal_sample,
                  'random': random_sample,
                  'gamma': gamma_sample})
print(df.describe())
plt.figure()
plt.boxplot(df['normal'], whis='range')
# whis='range'是不启用离群值
plt.show()

# plt.figure()
# plt.boxplot([df['normal'], df['random'], df['gamma']], whis='range')
# plt.show()
#
# plt.figure()
# plt.boxplot([df['normal'], df['random'], df['gamma']])
# plt.show()
# # 启用离群值
#
# # 4.热图
# """
# y:正太
# x:随机分布
# """
# plt.figure()
# y = np.random.normal(loc=0., scale=1., size=10000)
# x = np.random.random(size=10000)
# plt.hist2d(x, y, bins=25)
# plt.show()
#
# # 中间的数值是越大的
#
# plt.figure()
# y = np.random.normal(loc=0., scale=1., size=10000)
# x = np.random.random(size=10000)
# plt.hist2d(x, y, bins=100)
# plt.colorbar()
# plt.show()
