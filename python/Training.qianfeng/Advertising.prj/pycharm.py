#!/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
# 科学计算库
import matplotlib as mpl
# 制图
import matplotlib.pyplot as plt
# 数据可视化
import pandas as pd
# 把csv格式，转换成数组
from sklearn.model_selection import train_test_split
# 数据一分为二（训练集 ， 测试集）
from sklearn.linear_model import LinearRegression
# sklearn线性回归算法库

# 一、加载数据集
path = 'Advertising.csv'
"""
利用pandas把数据集中的3个列表
读入进来，封装成数组
"""
data = pd.read_csv(path)
x = data[['TV','Radio','Newspaper']]
# 特征矩阵中的3个列表（特征）
y = data['Sales']
print '以下是原数据的特征矩阵为\n',x
print '以下是原数据的标签矩阵为\n',y
print '==========================================================='

mpl.rcParams['font.sans-serif'] = [u'simHei']
# 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
# 解决保存图像是负号‘-’，显示为方块

# 数据可视化1
plt.figure(facecolor='w')
# 背景色为白色
plt.plot(data['TV'] , y , 'ro' ,label = 'TV')
plt.plot(data['Radio'] , y , 'g^' ,label = 'Radio')
plt.plot(data['Newspaper'] , y , 'mv' ,label = 'Newspaper')
plt.legend(loc = "lower right")
plt.xlabel(u'广告花费',fontsize = 16)
plt.ylabel(u'销售额度',fontsize = 16)
plt.title(u'广告花费与销售额度的数据对比',fontsize = 20)
plt.grid()
# 使用面向对象的方式显示网格
plt.show()

# 数据可视化2
plt.figure(facecolor='w',figsize=(9,10))
plt.subplot(311)
plt.plot(data['TV'] , y ,'ro')
plt.title('TV')
plt.grid()
# 使用面向对象的方式显示网格

plt.subplot(312)
plt.plot(data['Radio'] , y ,'g^')
plt.title('Radio')
plt.grid()

plt.subplot(313)
plt.plot(data['Newspaper'] , y ,'b*')
plt.title('Newspaper')
plt.grid()

plt.tight_layout()
# 紧凑显示图片，居中显示
plt.show()


# 二、分割数据集
x_train , x_test , y_train , y_test = train_test_split(x , y , train_size=0.8 , random_state=1)
print type(x_test)
print x_train.shape , y_train.shape
print '====================================================='

# 三、选择（建立）模型
linreg = LinearRegression()
# 初始化模型

# 四、训练模型

model = linreg.fit(x_train , y_train)

print '训练的模型参数为\n',model

print '以下是训练模型的参数系数和截距'

print linreg.coef_ , linreg.intercept_
# coef_参数系数 ， intercept_截距

print '=================================================================='

# 建字典（index）
ordel = y_test.argsort(axis = 0)
# argsort函数返回的是数组值从小到大的索引值，axis = 0 代表列， axis =1 代表行
y_test = y_test.values[ordel]
# 拿到Sales的所有值，index
x_test = x_test.values[ordel,:]
# 拿到TV ， Radio ， Newspaper ，所有值，index

# 五、验证数据

y_hat = linreg.predict(x_test)
mse = np.average((y_hat - np.array(y_test))**2)
# 平方
rmse = np.sqrt(mse)
# 开平方
print 'MSE = ',mse
print 'RMSE = ',rmse

print 'R2 = ',linreg.score(x_train , y_train)
# 模型的得分
print 'R2 = ',linreg.score(x_test , y_test)

print '=================================模型完毕======================='


# 数据可视化3
plt.figure(facecolor='w')
t = np.arange(len(x_test))
# x个数就是索引
plt.plot(t , y_test ,'r-',linewidth = 2 , label = u'真实数据')
plt.plot(t , y_hat ,'g-',linewidth = 2 , label = u'测试数据')
plt.legend(loc = 'upper left')
plt.title(u'多元线性回归销量',fontsize = 18)
plt.grid()
# 网格输出
plt.show()