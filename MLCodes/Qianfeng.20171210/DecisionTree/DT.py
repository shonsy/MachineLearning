#!/usr/bin/python
# -*- coding:utf-8 -*-
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from ml_visualization import plot_decision_tree

if __name__ == '__main__':

    iris = load_iris()
    X_train , X_test , y_train , y_test = train_test_split(iris.data , iris.target , random_state=0)
    max_depth_values = [2 ,3 ,4]
    for max_depth_val in max_depth_values:
        dt_model = DecisionTreeClassifier(max_depth = max_depth_val)
        dt_model.fit(X_train , y_train)
        print('max_depth = ',max_depth_val)
        print('训练集样本：{:.3f}'.format(dt_model.score(X_train , y_train)))
        print('测试集样本：{:.3f}'.format(dt_model.score(X_test , y_test)))
        print()

    dt_model = DecisionTreeClassifier(max_depth = 4)
    dt_model.fit(X_train , y_train)
    plot_decision_tree(dt_model , iris.feature_names , iris.target_names)
    print(iris.feature_names)
    print(dt_model.feature_importances_)





















