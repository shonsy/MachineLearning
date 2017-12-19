# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# 度量精准度
from sklearn.linear_model import LogisticRegression
from ml_visualization import plot_class_regions_for_classifier
# 自定义的可视化工具

if __name__ == '__main__':
    # 一、加载数据集
    fruit_df = pd.read_table('fruit_data_with_colors.txt')
    X = fruit_df[['width','height']]
    #特征矩阵
    y = fruit_df['fruit_label'].copy()
    #copy()，修改原数据的同时，原数据进行备份

    #将不是apple的标签设置为0（2,3,4）
    y[y != 1] = 0

    #二、分割数据集
    X_train , X_test ,y_train , y_test = train_test_split(X , y , test_size=1/4,random_state=0)

    # 调“超参数”，—不同的C
    c_values = [0.1 , 1 , 100]
    for c_value in c_values:
        #三、选择（建立）模型
        lr_model = LogisticRegression(C = c_value)
        #初始化lR算法

        #四、训练模型
        lr_model.fit(X_train , y_train)

        #五、验证模型
        y_pred = lr_model.predict(X_test)

        acc = accuracy_score(y_test , y_pred)
        # 度量精准度(精准率)
        print('C ={}，准确率：{:.3f}'.format(c_value , acc))

        #可视化
        plot_class_regions_for_classifier(lr_model , X_test.values ,y_test.values ,title='C = {}'.format(c_value))
