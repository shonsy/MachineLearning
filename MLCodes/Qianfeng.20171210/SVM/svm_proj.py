# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from ml_visualization import plot_class_regions_for_classifier
if __name__ == '__main__':
    # 加载数据集
    fruits_df = pd.read_table('fruit_data_with_colors.txt')

    X = fruits_df[['width', 'height']]
    y = fruits_df['fruit_label'].copy()

# 将不是apple的标签设为0
    y[y != 1] = 0
# 分割数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/4, random_state=0)

# 不同的C值
    c_values = [0.0001, 1, 100000]

    for c_value in c_values:
    # 建立模型
        svm_model = SVC(C=c_value)

        # 训练模型
        svm_model.fit(X_train, y_train)

        # 验证模型
        y_pred = svm_model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        print('C={}，准确率：{:.3f}'.format(c_value, acc))

     # 可视化
        plot_class_regions_for_classifier(svm_model, X_test.values, y_test.values, title='C={}'.format(c_value))