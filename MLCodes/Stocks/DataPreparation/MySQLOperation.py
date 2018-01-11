# !/usr/bin/python
#_*_ coding: utf-8 _*_

import random
import sys
import requests
from datetime import datetime
from lxml import etree
import pymysql
import pandas as pd
import string


def getConnection(host='localhost', user='root', password='root', db='Stocks', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor):

    connection = pymysql.connect(host= host, user=user, password=password, db=db, charset=charset, cursorclass=cursorclass)
    return connection;

def executeSQL(table_name=None,sql={},host='localhost', user='allan', password='110', db='Stocks', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor):

    try:
        connection = getConnection(host=host, user=user, password=password, db=db, charset=charset,cursorclass=cursorclass)
        with connection.cursor() as cursor:
            if table_name != None:
                sql = sql.format(table_name)
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
    except:
            print("Unexpected error:", sys.exc_info()[0],sys.exc_info()[1])
    finally:
        cursor.close()
        connection.close()


def get_yearly_increase_of_stocks(stocklist,year,tablename='stocks_Transaction'):
    tradingdays = get_first_last_trading_days_of_year(tablename,host= '172.22.213.98')

    for index in range(len(stocklist)):
       for x in range(len(tradingdays)):
           if stocklist[index]== tradingdays[x]['股票号'] and tradingdays[x]['first_day_of_year'].year == int(year):
                firstday_of_trading = tradingdays[x]['first_day_of_year']
                if(firstday_of_trading.month !=1):
                    continue
                lastday_of_trading = tradingdays[x]['last_day_of_year']
                # ,(b.收盘价*b.复权因子-a.开盘价*a.复权因子)/(a.开盘价*a.复权因子) as 涨幅
                sql = r'SELECT DISTINCT a.股票号,a.股票名,a.日期 ,(b.收盘价*b.复权因子-a.开盘价*a.复权因子)/(a.开盘价*a.复权因子) as 涨幅 ' \
                      r'FROM (SELECT * FROM `{0}` where 日期="{1}" and 股票号="{3}")a, ' \
                      r'(SELECT * FROM `{0}` where 日期="{2}"  and 股票号="{3}")b'.format(tablename,firstday_of_trading,lastday_of_trading,stocklist[index])
                # sql =   r'SELECT * FROM `{0}` where 日期="{1}"'.format(tablename,firstday_of_trading)
                rows = executeSQL(sql=sql, host='172.22.213.98')
                print('hi')

def get_first_last_trading_days_of_year(table_name,host='localhost', user='allan', password='110', db='Stocks', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor):
    sql = r'select 股票号,股票名,min(cast(日期 as date)) as first_day_of_year,max(cast(日期 as date)) as last_day_of_year from  `{}`  GROUP BY 股票号,股票名,year(cast(日期 as date))'
    rows = executeSQL('stocks_Transaction', sql, host='172.22.213.98')
    return rows

if __name__ == '__main__':
    # sql = r'select 股票号,股票名,min(cast(日期 as date)) as first_day_of_year,max(cast(日期 as date)) as last_day_of_year from  `{}`  GROUP BY 股票号,股票名,year(cast(日期 as date))'
    # df = pd.DataFrame(executeSQL('stocks_Transaction',sql,host= '172.22.213.98'))
    # print(df.head(10))
    lstStocks = []
    lstStocks.append('600000')
    get_yearly_increase_of_stocks(lstStocks,'2000')
    # sql = 'a {0},{1},{0}'.format('hi','there')
    # test = 'my name is {0} ,age {1},{0}'.format('hoho', 18)
    # print(sql)
    # print(test)