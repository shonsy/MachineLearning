#!/usr/bin/python
#-*- coding:utf-8 -*-
import pandas as pd
if __name__ == '__main__':
    # 一、Pandas进阶及技巧
    country1 = pd.Series({'Name': '中国',
                    'Language': 'Chinese',
                    'Area': '9.597M km2',
                     'Happiness Rank': 79})

    country2 = pd.Series({'Name': '美国',
                    'Language': 'English (US)',
                    'Area': '9.834M km2',
                     'Happiness Rank': 14})

    country3 = pd.Series({'Name': '澳大利亚',
                    'Language': 'English (AU)',
                    'Area': '7.692M km2',
                     'Happiness Rank': 9})

    df = pd.DataFrame([country1, country2, country3], index=['CH', 'US', 'AU'])
    print(df)


    print('====================上下文======================')

    # 添加数据
# 如果个数小于要求的个数，会自动进行“广播”操作
# 如果大于要求的个数，会报错
    df['Location'] = '地球'
    print(df)

    df['Region'] = ['亚洲', '北美洲', '大洋洲']
    print(df)


#     二、Pandas索引
    # 行索引
    print('loc:')
    print(df.loc['CH'])
    """
    按行排序，列名作为index ，行向量作为数据
    """
    print(type(df.loc['CH']))
    print('iloc:')
    print(df.iloc[1])
    """
    按行排序，列名作为index ，行向量作为数据
    """

    # 列索引
    print(df['Area'])
    print(type(df['Area']))
    """
    Area这一列，的rows
    """

    # 获取不连续的列数据
    print(df[['Name', 'Area']])

    # 混合索引
# 注意写法上的区别
    print('先取出列，再取行：')
    print(df['Area']['CH'])
    print(df['Area'].loc['CH'])
    print(df['Area'].iloc[0])
    """
    结果都是一样的， 先取出列， 再取出行
    """

    print('先取出行，再取列：')
    print(df.loc['CH']['Area'])
    print(df.iloc[0]['Area'])
    """
    结果都是一样， 先取行，再取列
    """

    # 转换行和列
    print(df.T)

#     三、删除数据
    print(df.drop(['CH']))
#  注意drop操作只是将修改后的数据copy一份，而不会对原始数据进行修改
    print(df)

    print(df.drop(['CH'], inplace=True))
# #     # 如果使用了inplace=True，会在原始数据上进行修改，同时不会返回一个copy
    print(df)

    # 也可直接使用del关键字
    del df['Name']
    print(df)

#     四、DataFrame的操作与加载
    # 加载csv文件数据
    reprot_2015_df = pd.read_csv('2015.csv')
    print('2015年数据预览：')
    print(reprot_2015_df.head())
    print(reprot_2015_df.info())
    # 信息

    # 使用index_col指定索引列
# 使用usecols指定需要读取的列
    reprot_2016_df = pd.read_csv('2016.csv',
                                 index_col='Country',
                                 usecols=['Country', 'Happiness Rank', 'Happiness Score', 'Region'])


    print(reprot_2016_df.head())
    print('列名(column)：', reprot_2016_df.columns)
    print('行名(index)：', reprot_2016_df.index)


# 重置index
# 注意inplace加与不加的区别
    print(reprot_2016_df.reset_index().head())
    reprot_2016_df.rename(columns={'Region': '地区', 'Hapiness Rank': '排名', 'Hapiness Score': '幸福指数'})
    print(reprot_2016_df.head())
# 重命名列名，注意inplace的使用
    reprot_2016_df.rename(columns={'Region': '地区', 'Happiness Rank': '排名', 'Happiness Score': '幸福指数'},
                     inplace=True)
    print(reprot_2016_df.head())

    print('======================================第五==============================')


    # 五 、 Boolean Mask
    # 过滤 Western Europe 地区的国家
    only_western_europe = reprot_2016_df['地区'] == 'Western Europe'
    print(only_western_europe)

    print('===================================分开=====================================')
    # 过滤 Western Europe 地区的国家
    # 并且排名在10之外
    only_western_europe_10 = (reprot_2016_df['地区'] == 'Western Europe') & (reprot_2016_df['排名'] > 10)
    print(only_western_europe_10)

#      六、数据清洗

    log_data = pd.read_csv('log.csv')
    print(log_data.head())
    log_data.set_index(['time', 'user'], inplace=True)
    log_data.sort_index(inplace=True)
    print(log_data)
    print(log_data.fillna(0))
    print(log_data.dropna())
    print(log_data.ffill())
    print(log_data.bfill())



