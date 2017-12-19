#!/usr/bin/python
#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np

"""
1.二项分布
从二项分布中采样
"""
# 1次试验中，成功的次数
print(np.random.binomial(1, 0.5))

# 1000次试验中，成功的次数

print('1000次试验中，成功的次数: ', np.random.binomial(1000, 0.5))

# 1000次试验中，成功的概率
print('1000次试验中，成功的次数: ', np.random.binomial(1000, 0.5) / 1000)

# 模拟100000次试验中，连续两次都是1的次数
n_events = 100000
events = np.random.binomial(1, 0.5, n_events)

two_in_a_row = 0
for i in range(1, n_events - 1):
    if events[i] == 1 and events[i - 1] == 1:
        two_in_a_row += 1
print('{}次投掷硬币，连续两次都是正面的次数{}'.format(n_events, two_in_a_row))

"""
2.正太分布
"""
print(np.random.normal(loc=0.75))

samples = np.random.normal(loc=0.75, size=1000)

print('期望：', np.mean(samples))
print('标准差：', np.std(samples))












