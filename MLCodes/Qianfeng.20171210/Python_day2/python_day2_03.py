#!/usr/bin/python
#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
if __name__ == '__main__':
#     一、常建Series

    countries = ['中国', '美国', '澳大利亚']
    countries_s = pd.Series(countries)
    print(type(countries_s))
    print(countries_s)

    numbers = [4, 5, 6]
    print(pd.Series(numbers))


    country_dicts = {'CH': '中国',
                'US': '美国',
                'AU': '澳大利亚'}

    country_dict_s = pd.Series(country_dicts)
    print(country_dict_s) 
    print(country_dict_s.index)


# 二、处理缺失数据

    countries = ['中国', '美国', '澳大利亚', None]
    print(pd.Series(countries))
    numbers = [4, 5, 6, None]
    print(pd.Series(numbers))


#     三、Series 索引

    country_dicts = {'CH': '中国',
                'US': '美国',
                'AU': '澳大利亚'}

    country_dict_s = pd.Series(country_dicts)
    print(country_dict_s)


    print('iloc:', country_dict_s.iloc[2])
    print('loc:', country_dict_s.loc['US'])
    print('[]:', country_dict_s['US'])
    print('iloc:\n', country_dict_s.iloc[[0, 2]])
    print()
    print('loc:\n', country_dict_s.loc[['US', 'AU']])






