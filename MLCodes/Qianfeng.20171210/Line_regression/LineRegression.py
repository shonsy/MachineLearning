#!/usr/bin/python
# -*- coding:utf-8 -*-

# 人工生成用于测试回归的数据集
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

if __name__ == '__main__':

    plt.figure()
    plt.title('Sample regression problem with one input variable')
    # 每个样本只有一个变量
    X_R1, y_R1 = make_regression(n_samples = 100, n_features=1,
                                n_informative=1, bias = 150.0,
                                noise = 30, random_state=0)
    plt.scatter(X_R1, y_R1, marker= 'o', s=50)
    plt.show()


    X_train, X_test, y_train, y_test = train_test_split(X_R1, y_R1,
                                                   random_state = 0)


    # 调用线型回归模型
    linreg = LinearRegression()

    # 训练模型
    linreg.fit(X_train, y_train)

    # 输出结果
    print('线型模型的系数(w): {}'.format(linreg.coef_))
    print('线型模型的常数项(b): {:.3f}'.format(linreg.intercept_))
    print('训练集中R-squared得分: {:.3f}'.format(linreg.score(X_train, y_train)))
    print('测试集中R-squared得分: {:.3f}'.format(linreg.score(X_test, y_test)))


    X_train, X_test, y_train, y_test = train_test_split(X_R1, y_R1,
                                                   random_state = 0)
    # 调用线型回归模型
    linreg = LinearRegression()

    # 训练模型
    linreg.fit(X_train, y_train)

    # 输出结果
    print('线型模型的系数(w): {}'.format(linreg.coef_))
    print('线型模型的常数项(b): {:.3f}'.format(linreg.intercept_))
    print('训练集中R-squared得分: {:.3f}'.format(linreg.score(X_train, y_train)))
    print('测试集中R-squared得分: {:.3f}'.format(linreg.score(X_test, y_test)))



    # 可视化输出结果

    plt.figure(figsize=(5,4))
    plt.scatter(X_R1, y_R1, marker= 'o', s=50, alpha=0.8)
    plt.plot(X_R1, linreg.coef_ * X_R1 + linreg.intercept_, 'r-')
    plt.title('Least-squares linear regression')
    plt.xlabel('Feature value (x)')
    plt.ylabel('Target value (y)')
    plt.show()