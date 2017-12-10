# -*- coding: utf-8 -*-
import csv
import os
import numpy as np
import pandas as pd

# 指定数据集路径
dataset_path = '../data'
report_2015_datafile = os.path.join(dataset_path, '2015.csv')
report_2016_datafile = os.path.join(dataset_path, '2016.csv')


def load_data(data_file):
    """
        读取数据文件，加载数据。
        返回列表，其中列表中的每个元素为一个元组，包括Country, Region, Happiness Rank和Happiness Score
    """
    data = []
    with open(data_file, 'r') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            # 取出每行数据的Country, Region, Happiness Rank和Happiness Score，组合为一个元组放入数据列表中
            # 注意csv模块读入的数据全部为字符串类型
            data.append((row['Country'], row['Region'],
                         row['Happiness Rank'], row['Happiness Score']))
    return data


def get_region_happiness_scores(report_data):
    """
        获取区域包含国家的幸福指数
    """
    region_score_dict = {}
    for item in report_data:
        region = item[1]
        score = float(item[3])
        if region in region_score_dict:
            # 如果region_score_dict已经记录了该区域，则添加该区域的幸福指数到列表中
            region_score_dict[region].append(score)
        else:
            # 如果region_score_dict未记录该区域，则为该区域初始化一个空列表
            region_score_dict[region] = []
    return region_score_dict


def main():
    """
        主函数
    """
    # 读入数据
    report_2015_data = load_data(report_2015_datafile)
    report_2016_data = load_data(report_2016_datafile)

    # 数据预览
    print('2015年报告，前10条记录预览：')
    print(report_2015_data[:10])

    print('2016年报告，前10条记录预览：')
    print(report_2016_data[:10])

    # 任务1. 查看幸福指数分布情况
    print('\n===================== 任务1. 查看幸福指数分布情况 =====================')
    # 注意列表推导式的使用
    happiness_2015_scores = [float(item[3]) for item in report_2015_data]
    happiness_2016_scores = [float(item[3]) for item in report_2016_data]

    # 查看数据
    print('2015年报告，前10条记录幸福指数：', happiness_2015_scores[:10])
    print('2016年报告，前10条记录幸福指数：', happiness_2016_scores[:10])

    # 使用numpy.histogram查看数据的直方图分布
    hist_2015, hist_edge_2015 = np.histogram(happiness_2015_scores)
    hist_2016, hist_edge_2016 = np.histogram(happiness_2016_scores)

    print('2015年报告，幸福指数直方图分布：{}；直方图边界：{}。'.format(hist_2015, hist_edge_2015))
    print('2016年报告，幸福指数直方图分布：{}；直方图边界：{}。'.format(hist_2016, hist_edge_2016))

    # 任务2. 统计分析区域的幸福指数
    print('\n===================== 任务2. 统计分析区域的幸福指数 =====================')
    region_2015_score_dict = get_region_happiness_scores(report_2015_data)
    region_2016_score_dict = get_region_happiness_scores(report_2015_data)

    # 遍历数据字典，以2015年为例
    print('2015报告：')
    for region, scores in region_2015_score_dict.items():
        print('{}：最大值{}，最小值{}，平均值{}，中间值{}'
              .format(region, np.max(scores), np.min(scores),
                      np.mean(scores), np.median(scores)))

    # 任务3. 比较两年间的排名变化情况
    print('\n===================== 任务3. 比较两年间的排名变化情况 =====================')
    # 将数据构建成字典，key是国家，value是其排名
    # 扩展：字典推导式
    country_2015_score_dict = {item[0]: int(item[2]) for item in report_2015_data}
    country_2016_score_dict = {item[0]: int(item[2]) for item in report_2016_data}

    # 2015年数据预览
    print(country_2015_score_dict)

    # 将数据转换为Series
    ser_2015 = pd.Series(country_2015_score_dict)
    ser_2016 = pd.Series(country_2016_score_dict)

    print('2015年，数据预览：')
    print(ser_2015.head())

    print('2016年，数据预览：')
    print(ser_2016.head())

    # 将两年的记录相减，即得出排名变化情况
    # 注意Series在进行计算时，是按照index的顺序进行计算的，所以不需要担心顺序问题
    # NaN表示某一年的记录缺失，无法计算
    ser_change = ser_2016 - ser_2015
    print('2015-2016排名变化：')
    print(ser_change)

    # 可查看某个国家的排名变化
    print('中国的排名变化：')
    print(ser_change['China'])

    # 查看上升最快的国家
    print('2015-2016幸福指数上升最快的国家', ser_change.argmax())
    # 查看下降最快的国家
    print('2015-2016幸福指数下降最快的国家', ser_change.argmin())

if __name__ == '__main__':
    main()
