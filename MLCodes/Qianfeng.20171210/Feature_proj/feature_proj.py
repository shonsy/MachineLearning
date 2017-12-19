# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
if __name__ == '__main__':
    # 加载数据集
    fruits_df = pd.read_table('fruit_data_with_colors.txt')
    # print(fruits_df.head())

    # print('样本个数：', len(fruits_df))

    # 创建目标标签和名称的字典
    fruit_name_dict = dict(zip(fruits_df['fruit_label'], fruits_df['fruit_name']))
    # print(fruit_name_dict)

    # 划分数据集
    X = fruits_df[['mass', 'width', 'height', 'color_score']]
    y = fruits_df['fruit_label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/4, random_state=0)

    # print('数据集样本数：{}，训练集样本数：{}，测试集样本数：{}'.format(len(X), len(X_train), len(X_test)))

    # 特征归一化
    # scaler = MinMaxScaler()
    # X_train_scaled = scaler.fit_transform(X_train)
    # X_test_scaled = scaler.transform(X_test)
    #
    # for i in range(4):
    #     print('归一化前，训练数据第{}维特征最大值：{:.3f}，最小值：{:.3f}'.format(i + 1,
    #                                        X_train.iloc[:, i].max(),
    #                                        X_train.iloc[:, i].min()))
    #     print('归一化后，训练数据第{}维特征最大值：{:.3f}，最小值：{:.3f}'.format(i + 1,
    #                                        X_train_scaled[:, i].max(),
    #                                        X_train_scaled[:, i].min()))
    #     print()

    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)



    # label_color_dict = {1: 'red', 2: 'green', 3: 'blue', 4: 'yellow'}
    # colors = list(map(lambda label: label_color_dict[label], y_train))
    #
    # fig = plt.figure(figsize=(10, 5))
    # ax1 = fig.add_subplot(121, projection='3d', aspect='equal')
    # ax1.scatter(X_train['width'], X_train['height'], X_train['color_score'], c=colors, marker='o', s=100)
    # ax1.set_xlabel('width')
    # ax1.set_ylabel('height')
    # ax1.set_zlabel('color_score')
    #
    # ax2 = fig.add_subplot(122, projection='3d', aspect='equal')
    # ax2.scatter(X_train_scaled[:, 1], X_train_scaled[:, 2], X_train_scaled[:, 3], c=colors, marker='o', s=100)
    # ax2.set_xlabel('width')
    # ax2.set_ylabel('height')
    # ax2.set_zlabel('color_score')
    #
    # plt.show()

#     3.归一化对结果的影响

    # knn = KNeighborsClassifier(n_neighbors=5)
    # # 在未归一化的数据上进行训练并测试
    # knn.fit(X_train, y_train)
    # print('未归一化特征，测试准确率：{:.3f}'.format(knn.score(X_test, y_test)))
    #
    # # 在归一化的数据上进行训练并测试
    # knn.fit(X_train_scaled, y_train)
    # print('归一化特征后，测试准确率：{:.3f}'.format(knn.score(X_test_scaled, y_test)))





    # 4 随机生成有序型特征和类别特征作为例子
    # X_train = np.array([['male', 'low'],
    #                   ['female', 'low'],
    #                   ['female', 'middle'],
    #                   ['male', 'low'],
    #                   ['female', 'high'],
    #                   ['male', 'low'],
    #                   ['female', 'low'],
    #                   ['female', 'high'],
    #                   ['male', 'low'],
    #                   ['male', 'high']])
    #
    # X_test = np.array([['male', 'low'],
    #                   ['male', 'low'],
    #                   ['female', 'middle'],
    #                   ['female', 'low'],
    #                   ['female', 'high']])
    #
    # # 在训练集上进行编码操作
    # label_enc1 = LabelEncoder() # 首先将male, female用数字编码
    # one_hot_enc = OneHotEncoder() # 将数字编码转换为独热编码
    # # print(label_)
    # label_enc2 = LabelEncoder() # 将low, middle, high用数字编码
    #
    # tr_feat1_tmp = label_enc1.fit_transform(X_train[:, 0]).reshape(-1, 1) # reshape(-1, 1)保证为一维列向量
    # tr_feat1 = one_hot_enc.fit_transform(tr_feat1_tmp)
    # tr_feat1 = tr_feat1.todense()
    #
    # tr_feat2 = label_enc2.fit_transform(X_train[:, 1]).reshape(-1, 1)
    #
    # X_train_enc = np.hstack((tr_feat1, tr_feat2))
    # print(X_train_enc)
    #
    # # 在测试集上进行编码操作
    #
    # te_feat1_tmp = label_enc1.transform(X_test[:, 0]).reshape(-1, 1) # reshape(-1, 1)保证为一维列向量
    # te_feat1 = one_hot_enc.fit_transform(te_feat1_tmp)
    # te_feat1 = te_feat1.todense()
    #
    # te_feat2 = label_enc2.fit_transform(X_test[:, 1]).reshape(-1, 1)
    #
    # X_test_enc = np.hstack((te_feat1, te_feat2))
    # print(X_test_enc)
