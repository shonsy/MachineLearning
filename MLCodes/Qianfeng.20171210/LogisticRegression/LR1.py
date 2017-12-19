# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

if __name__ == '__main__':
    # 一、 加载数据集
    fruits_df = pd.read_table('fruit_data_with_colors.txt')
    X = fruits_df[['width' , 'height']]
    y = fruits_df['fruit_label'].copy()
    y[y!=1] =0
    # 2分类问题

    # 二、切分数据集
    X_train , X_test , y_train , y_test = train_test_split(X , y , train_size = 1/4 , random_state=0)

    c_values = [2 ,3 ,4]
    for c_val in c_values:
        # 三、选择模型
        lr_model = LogisticRegression(C = c_val)
        # 四、训练模型
        lr_model.fit(X_train , y_train)
        # 五、测试模型
        y_pred = lr_model.predict(X_test)
        acc = accuracy_score(y_test , y_pred)
        print('C = {} , 准确率:{:.3f}'.format(c_val , acc))