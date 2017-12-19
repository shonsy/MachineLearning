#!/usr/bin/python
#-*- coding:utf-8 -*-
# 引用必要的库
import matplotlib.pyplot as plt
import numpy as np
"""
1.subplots(222)
2行2列第2个子图
y轴是人为造的数据，x轴是matplotlib自动生成的
"""
plt.figure()
plt.subplot(1,2,1)
line_data = np.arange(1,9)
# 数据是1~8
plt.plot(line_data , '-o')
# plt.show()
right_data = line_data **2
plt.subplot(1,2,2)
plt.plot(right_data , '-x')
# plt.show()
# x轴是matplotlib自动生成的

# 保证子图中坐标轴范围一致（Y轴）
plt.figure()
ax1 = plt.subplot(1,2,1)
plt.plot(line_data , '-o')
ax2 = plt.subplot(1,2,2,sharey = ax1)
# sharey是要返回sharey=ax1的对象，本质上就是要使用ax1的y轴坐标
plt.plot(right_data , '-')
# plt.show()

fig , ((ax1 , ax2 , ax3),(ax4 , ax5 , ax6))=plt.subplots(2,3,sharex = True,sharey = True )
# sharex = True,sharey = True:  x轴 和y轴范围都是一样的
ax5.plot(right_data , '-')
# plt.show()

"""
2.直方图
"""
fig , ((ax1 , ax2),(ax3 , ax4))=plt.subplots(2,2,sharex=True)
axs = [ax1 ,ax2 ,ax3 , ax4]
# 4个子图， 0，1，2，3
for n in range(len(axs)):
    sample_size = 10 **(n +1)
#     10^1 ,10^2,10^3,10^4
    sample = np.random.normal(loc = 0 ,scale = 1 ,size = sample_size )
    # sample = np.random.normal(size = sample_size )

    #标准的正太分布  loc 指的是均值，scale 指的是标准差
    # 标准的正太分布Python已经封装好了，可以不写
    axs[n].hist(sample)
    axs[n].set_title('n ={}'.format(sample_size))
plt.show()























































