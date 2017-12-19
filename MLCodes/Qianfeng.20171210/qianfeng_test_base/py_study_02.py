#!/usr/bin/python
#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np

if __name__ == '__main__':
    countries = ['中国','美国','澳大利亚','None']
    print(pd.Series(countries))

    numbers = [4,5,None]
    print(pd.Series(numbers))

    country_dicts = {"CH":"中国",
                     "US":"美国",
                     "AU":"澳大利亚"}
    country_dicts_s = pd.Series(country_dicts)
    print(country_dicts_s)

    # print("iloc:",country_dicts_s[2])
    # print('loc:',country_dicts_s.loc['US'])
    print('[]:',country_dicts_s.iloc[[0,2]])

    print('========================')

    print('loc:\n',country_dicts_s.loc[["US",'AU']])
































