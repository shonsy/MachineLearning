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

    fruit_df = pd.read_table('fruit_data_with_colors.txt')
    X = fruit_df[['mass','width','height','color_score']]
    y = fruit_df['fruit_label']
    X_train , X_test , y_train , y_test = train_test_split(X , y , train_size=1/4 , random_state=1)
    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train , y_train)
    y_pred = knn_model.predict(X_test)
    acc = accuracy_score(y_test , y_pred)
    print(acc)




