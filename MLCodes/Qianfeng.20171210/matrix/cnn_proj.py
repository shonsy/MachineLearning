#!/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from ml_visualization import plot_fruit_knn

if __name__ == '__main__':
    # 加载数据集
    fruits_df = pd.read_table('fruit_data_with_colors.txt')
    print(fruits_df.head())
    print('样本个数：',len(fruits_df))
    # 创建目标标签和名称的字典
    fruit_name_dict = dict(zip(fruits_df['fruit_label'], fruits_df['fruit_name']))
    print(fruit_name_dict)
    # 划分数据集
    X = fruits_df[['mass', 'width', 'height', 'color_score']]
    y = fruits_df['fruit_label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/4, random_state=0)
    print('数据集样本数：{}，训练集样本数：{}，测试集样本数：{}'.format(len(X), len(X_train), len(X_test)))
    # 查看数据集
    sns.pairplot(data=fruits_df, hue='fruit_name', vars=['mass', 'width', 'height', 'color_score'])
    label_color_dict = {1: 'red', 2: 'green', 3: 'blue', 4: 'yellow'}
    colors = list(map(lambda label: label_color_dict[label], y_train))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X_train['width'], X_train['height'], X_train['color_score'], c=colors, marker='o', s=100)
    ax.set_xlabel('width')
    ax.set_ylabel('height')
    ax.set_zlabel('color_score')
    plt.show()
    sns.pairplot(data=fruits_df , hue='fruit_name' , vars = ['mass','width','height','color_score'])
    label_color_dict = {1:'red', 2:'green' , 3:'blue' , 4:'yellow'}
    colors = list(map(lambda label: label_color_dict[label] , y_train))
    fig = plt.figure()
    ax = fig.add_subplot(111 , projection = '3d')
    ax.scatter(X_train['width'] , X_train['height'] , X_train['color_score'],c = colors , marker = 'o' , s = 100)
    ax.set_xlabel('width')
    ax.set_ylabel('height')
    ax.set_zlabel('color_score')
    plt.show()
    knn = KNeighborsClassifier(n_neighbors=5)
    # 选择建立模型，初始化代码
    knn.fit(X_train, y_train)
    # 训练模型
    y_pred = knn.predict(X_test)
    print(y_pred)
    # 测试模型
    acc = accuracy_score(y_test, y_pred)
    print('准确率：', acc)
    # 验证模型
    plot_fruit_knn(X_train, y_train, 1)
    plot_fruit_knn(X_train, y_train, 5)
    plot_fruit_knn(X_train, y_train, 10)



