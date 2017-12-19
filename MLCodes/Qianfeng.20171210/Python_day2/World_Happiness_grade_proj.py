#!/usr/bin/python
#-*- coding:utf-8 -*-
# 引入必要的包
import csv
import os
import numpy as np
import pandas as pd

"""
1.指定数据集路径
"""
dataset_path = 'data'
report_2015_datafile = os.path.join(dataset_path , '2015.csv')
# 数字不能命名变量
report_2016_datafile = os.path.join(dataset_path , '2016.csv')
print(report_2015_datafile)
print(report_2016_datafile)

print('============数据加载=====================')

"""
2.读入数据
技术点1：csv操作
技术点2：for循环操作
"""
def load_data(data_file):
    """
    (1)读取数据文件，加载数据
    （2）返回列表，其中列表中的每个元素为一个元祖，包括
    Country ,Region , Happiness Rank , Happiness Score
    """
    data = []
    with open(data_file,'r') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            #取出每行数据的Country ,Region , Happiness Rank , Happiness Score
            data.append((row['Country'] , row['Region'] ,
                         row['Happiness Rank'] , row['Happiness Score']
                         ))
    return data

report_2015_data = load_data(report_2015_datafile)
report_2016_data = load_data(report_2016_datafile)

"""
数据预览
前10条的数据（Country ,Region , Happiness Rank , Happiness Score）
"""
print('2015年，前10条记录预览')
print(report_2015_data[:10])
print('2016年，前10条记录预览')
print(report_2016_data[:10])

print('===============2015年~2016年本地数据预览==================')


"""
3.1 查看幸福指数分布情况
技术点：列表推导式
"""
happiness_2015_score = [float(item[3]) for item in report_2015_data]
happiness_2016_score = [float(item[3]) for item in report_2016_data]

print("2015年报告，前10条记录幸福预览",happiness_2015_score[:10])
print("2016年报告，前10条记录幸福预览",happiness_2016_score[:10])


print('==============2015年~2016年幸福预览==================')

# 查看数据用直方图分布

hist_2015 ,hist_edge_2015 = np.histogram(happiness_2015_score)
hist_2016 ,hist_edge_2016 = np.histogram(happiness_2016_score)

print('2015年报告，幸福指数直方图数据分布：{}；直方图边界：{}。'.format(hist_2015,hist_edge_2015))
print('2016年报告，幸福指数直方图数据分布：{}；直方图边界：{}。'.format(hist_2016,hist_edge_2016))

print('============以上是2015~2016年直方图数据展示===================')


def get_region_happinss_score(report_data):

    """
    3.3 统计分析区域的幸福指数
    """
    region_score_dict = {}
    for item in report_data:
        region = item[1]
        score = float(item[3])
        if region in region_score_dict:
            region_score_dict[region].append(score)

        else:
            region_score_dict[region] = [score]

    return region_score_dict

report_2015_score_dict = get_region_happinss_score(report_2015_data)
report_2016_score_dict = get_region_happinss_score(report_2016_data)
print(report_2015_score_dict)

print('2015年报告')
for region , scores in report_2015_score_dict.items():
    print('{}:最大值{}，最小值{} ， 平均值{} ， 中间值{}'.format(region ,
          np.max(scores) , np.min(scores) , np.mean(scores),np.median(scores)
                                                  ))

print('=============2015~2016上下区域幸福分布========================')


print('2016年报告')
for region , scores in report_2016_score_dict.items():
    print('{}:最大值{}，最小值{} ， 平均值{} ， 中间值{}'.format(region ,
          np.max(scores) , np.min(scores) , np.mean(scores),np.median(scores)
                                                  ))

    print('==========================以上是前2个需求===========================')



"""
3.3 比较2年间的排名变化情况
技巧：讲数据构成dict ， key:国家， value：Happiness Rank
字典推导式
"""

country_2015_score_dict = {item[0]:int(item[2]) for item in report_2015_data}
country_2016_score_dict = {item[0]:int(item[2]) for item in report_2016_data}

print(country_2015_score_dict)

# 将数据转换为Series

ser_2015 = pd.Series(country_2015_score_dict)
ser_2016 = pd.Series(country_2016_score_dict)

print('2015年，数据预览 ')
print(ser_2015)
print('2016年数据预览')
print(ser_2016)

print('=================2015~2016年国家的分析指数========================')


"""
（1）将2年的记录相减，即得排名变化情况
（2）注意Series在计算中，是按照index的顺序计算的，
    所以不用担心顺序问题
"""

ser_change = ser_2016 - ser_2015
print('2015~2016年变化情况')
print(ser_change)


print('================变化情况==============')


"""
(1)查看上升最快的国家
（2）查看下降的国家
"""


print('2015年~2016年幸福指数上升最快的国家',ser_change.argmin())
print('2015年~2016年幸福指数下降最快的国家',ser_change.argmax())


"""
今天的项目通过分析世界幸福指数报告实践了Python数据分析的常用技巧
包括：
1.csv操作
2.字典的构造
3.Numpy
4.列表推导式
5.Series的构造计算
"""







































































