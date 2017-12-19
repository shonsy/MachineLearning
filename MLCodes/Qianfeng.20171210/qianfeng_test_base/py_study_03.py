#!/usr/bin/python
#-*- coding:utf-8 -*-
import pandas as pd

if __name__ == '__main__':
    """
    一、常建Series
    """

    # countries = ['中国','美国','澳大利亚']
    # countries_s = pd.Series(countries)
    # print(type(countries_s))
    # print(countries_s)
    #Series自动创建index，我们只关注 右边数据

    # numbers = [4,5,6]
    # print(pd.Series(numbers))

    # country_dicts = {"CH":"中国",
    #                  "US":"美国",
    #                  "AU":"澳大利亚"}

    # country_dicts_s = pd.Series(country_dicts)
    # print(country_dicts_s)
    # print(country_dicts_s.index)


    """
    二、处理丢失数据
    """
    # countries = ['中国','美国','澳大利亚',None]
    # print(pd.Series(countries))
    # print('=================================')
    # numbers = [4,5,6,None]
    # print(pd.Series(numbers))


    """
    Series索引
    """

    country_dicts = {"CH":'中国',
                     "US":'美国',
                     "AU":'澳大利亚'
    }

    country_dicts_s = pd.Series(country_dicts)
    print(country_dicts_s)

    print('==================================')


    print('iloc:',country_dicts_s.iloc[2])
    #     iloc :行索引

    print('======================================')
    print('loc',country_dicts_s.loc['US'])

    print('====================================')
    print('[]=',country_dicts_s['US'])

    print('==================================')

    print('iloc:\n',country_dicts_s.iloc[[0,2]])


    print('====================================')

    print('loc:\n',country_dicts_s.loc[['US' ,'AU']])





















































































































































































