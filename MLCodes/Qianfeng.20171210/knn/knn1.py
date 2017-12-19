# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
# 数据可视化
import pandas as pd
# 把csv转换成表格数据（数据）
from sklearn.model_selection import train_test_split
# 分割数据
fruit_df = pd.read_table('fruit_data_with_colors.txt')
# 不能用read_csv

print(fruit_df.head())
# 前5行

print('样本个数：',len(fruit_df))
# 创建目标标签和名称的字典，本质上把标签数据（1，2，3，4）和水果（key ，value）映射（zip）

frutt_name_dict = dict(zip(fruit_df['fruit_label'] , fruit_df['fruit_name']))
print(frutt_name_dict)

print('========================================================')
X = fruit_df[['mass','width','height','color_score']]
# 4个特征的矩阵

y = fruit_df['fruit_label']
# 标签矩阵

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=1/4 , random_state=0)
print('数据集样本：{} , 训练集样本数：{} , 测试集样本数：{}'.format(len(X) , len(
                                               X_train ),len(X_test)))

from mpl_toolkits.mplot3d import Axes3D

label_color_dict = {1:'red',2:'green',3:'blue',4:'yellow'}
colors = list(map(lambda label:label_color_dict[label] , y_train))
fig = plt.figure()

ax = fig.add_subplot(111 ,projection = '3d')
# 初始化3d图，将画布分割成1行1列，图像画在从左到右从上到下的第1块
# scatter 散点图
ax.scatter(X_train['width'] , X_train['height'] ,X_train['color_score'],c=colors,marker = 'o',s=100)
ax.set_xlabel('width')
ax.set_ylabel('height')
ax.set_zlabel('color_score')
plt.show()

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
# 初始化模型，调‘超参数’，n=5
knn.fit(X_train ,y_train)
y_pred = knn.predict(X_test)
print('===========================================================')
print(y_pred)
# 当n=5时，输出标签数据多，knn模型的未知数据就是该标签数据
from ml_visualization import plot_fruit_knn

plot_fruit_knn(X_train ,y_train ,1)
plot_fruit_knn(X_train ,y_train ,5)
plot_fruit_knn(X_train ,y_train ,10)
