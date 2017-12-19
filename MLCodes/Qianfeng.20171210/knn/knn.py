# -*- coding: utf-8 -*-
# 导入必要的包
import matplotlib.pyplot as plt
# 绘制图，数据可视化
import pandas as pd
# 文本数据，转换成table表格数据（数组）
from sklearn.model_selection import train_test_split
# 切割数据集

# 一、加载数据集
fruit_df = pd.read_table('fruit_data_with_colors.txt')
print(fruit_df.head())
# 查看前5行

print("样本个数：",len(fruit_df))

print('==================================================')

"""
创建目标和字典名称，本质上把标签数据（1,2,3,4）和水果（key ，value）映射(zip)
"""

fruit_df_dict = dict(zip(fruit_df['fruit_label'],fruit_df['fruit_name']))
print(fruit_df_dict)

print('=======================================================')

# 二、分割数据集
X = fruit_df[['mass','width','height','color_score']]
# 特征矩阵
y = fruit_df['fruit_label']

X_train ,X_test ,y_train,y_test = train_test_split(X , y ,test_size=1/4 , random_state=0)

print('数据集样本：{}，训练集样本数：{}，测试集样本数：{}'.format(len(X) ,len(X_train),len(X_test)))

print('=======================================================')

from mpl_toolkits.mplot3d import Axes3D
# 3D数据展示图的库

label_color_dict = {1:'red' , 2:'green' ,3:"blue" ,4:"yellow"}
colors = list(map(lambda label:label_color_dict[label],y_train))
# print(colors)
fig = plt.figure()
# 初始化图像
ax = fig.add_subplot(111 , projection = '3d')
# 初始化3D图，将画布分割成1行1列，图像在从左到右，从上到下的第1块

# scatter散点图
ax.scatter(X_train['width'],X_train["height"],X_train['color_score'],c = colors ,marker = 'o',s = 100)
ax.set_xlabel('width')
ax.set_ylabel('height')
ax.set_zlabel('color_score')
# 设置x，y，z三维数据
plt.show()


from sklearn.neighbors import KNeighborsClassifier
# 导入KNN算法包


# 三、选择建立模型
knn = KNeighborsClassifier(n_neighbors=5)
# 初始化模型，调“超参数”，k = 5

# 四、训练模型
knn.fit(X_train , y_train)

# 五、验证模型

y_pred = knn.predict(X_test)
print(y_pred)
"""
当k = 5时，输出标签数据多，knn模型的未知数据就是该标签数据
"""

from ml_visualization import plot_fruit_knn

plot_fruit_knn(X_train ,y_train , 1)
plot_fruit_knn(X_train ,y_train , 5)
plot_fruit_knn(X_train ,y_train , 10)










































