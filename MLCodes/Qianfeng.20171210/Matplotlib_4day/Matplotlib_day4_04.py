#!/usr/bin/python
#-*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1.Pandas绘图,DataFrame绘图

# np.random.seed(100)
df = pd.DataFrame({'A': np.random.randn(365).cumsum(0),
                  'B': np.random.randn(365).cumsum(0) + 20,
                  'C': np.random.randn(365).cumsum(0) - 20},
                 index=pd.date_range('2017/1/1', periods=365))
print(df.head())
# df.plot()
# plt.show()

# df.plot('A', 'B', kind='scatter')
# plt.show()

# df.plot(kind='box')
# plt.show()

# df.plot(kind='hist', alpha=0.7)
# plt.show()
#
# df.plot(kind='kde')
# plt.show()

# # pandas.tools.plotting
#
# # 2. Seaborn绘图
import seaborn as sns
np.random.seed(100)
v1 = pd.Series(np.random.normal(0, 10, 1000), name='v1')
v2 = pd.Series(2 * v1 + np.random.normal(60, 15, 1000), name='v2')

np.random.seed(100)
v1 = pd.Series(np.random.normal(0, 10, 1000), name='v1')
v2 = pd.Series(2 * v1 + np.random.normal(60, 15, 1000), name='v2')

# # 通过matplotlib绘图
# plt.figure()
# plt.hist(v1, alpha=0.7, bins=np.arange(-50, 150, 5), label='v1')
# plt.hist(v2, alpha=0.7, bins=np.arange(-50, 150, 5), label='v2')
# plt.legend()
# plt.show()


plt.figure()
plt.hist([v1, v2], histtype='barstacked', normed=True)
v3 = np.concatenate((v1, v2))
sns.kdeplot(v3)
plt.show()

# # 使用seaborn绘图
# plt.figure()
# sns.distplot(v3)
# # plt.show()
#
#
# # 使用seaborn绘图
# plt.figure()
# sns.jointplot(v1, v2, alpha=0.4)
# # plt.show()
#
# # 使用seaborn绘图
# plt.figure()
# grid = sns.jointplot(v1, v2, alpha=0.4)
# grid.ax_joint.set_aspect('equal')
# plt.show()
#
# plt.figure()
# sns.jointplot(v1, v2, kind='hex')
# plt.show()
#
# plt.figure()
# sns.jointplot(v1, v2, kind='kde')
#
# iris = pd.read_csv('iris.csv')
# print(iris.head())
#
# sns.pairplot(iris, hue='Name', diag_kind='kde')
#
# plt.figure()
# plt.subplot(121)
# sns.swarmplot('Name', 'PetalLength', data=iris)
# plt.subplot(122)
# sns.violinplot('Name', 'PetalLength', data=iris)
# plt.show()