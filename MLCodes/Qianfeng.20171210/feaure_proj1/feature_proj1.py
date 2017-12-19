# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import validation_curve
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.metrics import confusion_matrix
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


    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    for i in range(4):
        # print('归一化前，训练数据第{}维特征最大值：{:.3f}，最小值：{:.3f}'.format(i + 1,
        #                                        X_train.iloc[:, i].max(),
        #                                        X_train.iloc[:, i].min()))
        # print('归一化后，训练数据第{}维特征最大值：{:.3f}，最小值：{:.3f}'.format(i + 1,
        #                                        X_train_scaled[:, i].max(),
        #                                        X_train_scaled[:, i].min()))
        # print()

#     3. 交叉验证
    k_range = [5, 10, 15, 20]
    cv_scores = []
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn, X_train_scaled, y_train, cv=3)
        cv_score = np.mean(scores)
        print('k={}，验证集上的准确率={:.3f}'.format(k, cv_score))
        cv_scores.append(cv_score)


    best_k = k_range[np.argmax(cv_scores)]
    best_knn = KNeighborsClassifier(n_neighbors=best_k)
    best_knn.fit(X_train_scaled, y_train)
    print('测试集准确率：', best_knn.score(X_test_scaled, y_test))



    c_range = [1e-3, 1e-2, 0.1, 1, 10, 100, 1000, 10000]
    train_scores, test_scores = validation_curve(SVC(), X_train_scaled, y_train,
                                                 param_name='C', param_range=c_range,
                                                 cv=3, scoring='accuracy')
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    plt.figure(figsize=(10, 8))
    plt.title('Validation Curve with SVM')
    plt.xlabel('C')
    plt.ylabel('Score')
    plt.ylim(0.0, 1.1)
    lw = 2
    plt.semilogx(c_range, train_scores_mean, label="Training score",
                 color="darkorange", lw=lw)
    plt.fill_between(c_range, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.2,
                     color="darkorange", lw=lw)
    plt.semilogx(c_range, test_scores_mean, label="Cross-validation score",
                 color="navy", lw=lw)
    plt.fill_between(c_range, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.2,
                     color="navy", lw=lw)
    plt.legend(loc="best")
    plt.show()

    # 从上图可知对SVM，C=10, 100为最优参数
    svm_model = SVC(C=100)
    svm_model.fit(X_train_scaled, y_train)
    print(svm_model.score(X_test_scaled, y_test))



    parameters = {'max_depth':[3, 5, 7, 9], 'min_samples_leaf': [1, 2, 3, 4]}
    clf = GridSearchCV(DecisionTreeClassifier(), parameters, cv=3, scoring='accuracy')
    clf.fit(X_train, y_train)

    print('最优参数：', clf.best_params_)
    print('验证集最高得分：', clf.best_score_)


    # 获取最优模型
    best_model = clf.best_estimator_
    print('测试集上准确率：', best_model.score(X_test, y_test))


    k = 7
    # 转换为二分类问题
    y_train_binary = y_train.copy()
    y_test_binary = y_test.copy()

    y_train_binary[y_train_binary != 1] = 0
    y_test_binary[y_test_binary != 1] = 0

    knn = KNeighborsClassifier(k)
    knn.fit(X_train_scaled, y_train_binary)
    y_pred = knn.predict(X_test_scaled)

    # 准确率
    print('准确率：{:.3f}'.format(accuracy_score(y_test_binary, y_pred)))

    # 精确率
    print('精确率：{:.3f}'.format(precision_score(y_test_binary, y_pred)))

    # 召回率
    print('召回率：{:.3f}'.format(recall_score(y_test_binary, y_pred)))

    # F1值
    print('F1值：{:.3f}'.format(f1_score(y_test_binary, y_pred)))



    # PR 曲线
# PR曲线的绘制


    # fpr, tpr, _ = roc_curve(y_test, y_pred)
    print('AUC值：{:.3f}'.format(roc_auc_score(y_test_binary, y_pred)))

# 混淆矩阵
# 混淆矩阵的绘制

    y_pred = svm_model.predict(X_test_scaled)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    plt.figure()
    plt.grid(False)
    plt.imshow(cm, cmap='jet')
    plt.colorbar()





