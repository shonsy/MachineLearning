#!/usr/bin/python
#-*- coding:utf-8 -*-
# 引入必要的包
import pandas as pd
import numpy as np

"""
1.二项分布
"""
# 1次试验中，成功的次数
print(np.random.binomial(1,0.5))
print('======================================')
print('1000次试验中，成功的次数,',np.random.binomial(1000,0.5))
# 1000次试验中，成功的概率

print('====================================================')

n_events = 100000
events = np.random.binomial(1,0.5,n_events)

two_in_a_row = 0
for i in range(1,n_events):
    if events[i] ==1 and events[i -1 ] ==1:
        two_in_a_row +=1
#         统计
print('{}次投掷硬币，连续2次都是正面的次数{}'.format(n_events , two_in_a_row))

print('========================================================')


"""
2.正太分布
"""

print(np.random.normal(loc = 0.75))

sample = np.random.normal(loc = 0.75 , size = 1000)
print('期望值：',np.mean(sample))
print('标准差：',np.std(sample))




































