# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
if __name__ == '__main__':

    fruits_df = pd.read_table('fruit_data_with_colors.txt')
    X = fruits_df[['width', 'height']]
    y = fruits_df['fruit_label'].copy()
    y[y!=1] = 0
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/4, random_state=0)

    c_value = [0.1 ,10 ,10000]
    for c_val in c_value:
        svm_model = SVC(C = c_val)
        svm_model.fit(X_train , y_train)
        y_pred = svm_model.predict(X_test)
        acc = accuracy_score(y_test , y_pred)
        print('C = {} , 准确率：{:.3f}'.format(c_val , acc))



