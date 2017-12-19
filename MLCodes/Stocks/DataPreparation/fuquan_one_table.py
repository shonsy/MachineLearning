import random

import requests
from datetime import datetime
from lxml import etree
import pymysql
import pandas as pd


def get_gupiao_list():
    df_number = pd.read_csv(r'../sz50.csv',
                            encoding='utf-8', usecols=[2])

    df_name = pd.read_csv(r'../sz50.csv',
                          encoding='utf-8', usecols=[3])
    df_number_list = list()
    for i in df_number.values:
        df_number_list.extend(list(i))
    df_name_list = list()
    for i in df_name.values:
        df_name_list.extend(list(i))
    gupiao_full_data = dict(zip(df_number_list, df_name_list))
    return gupiao_full_data, df_number_list


def get_data(gupiao_full_data, df_number_list, table_name):
    ua_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ',
        '(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)'
    ]
    ua = {'User-Agent': str(random.choices(ua_list))}
    creat_table(table_name)  # 创建表
    for i in gupiao_full_data.keys():
        # i = 601818
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S\n'))
        print("正在爬取第{}只股票".format(df_number_list.index(i) + 1))
        print("进度{:.2%}".format((df_number_list.index(i) + 1) / len(df_number_list)))
        url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/stockid/{}.phtml?year=2017&jidu=4'
        r = requests.get(url.format(i), headers=ua)
        r.encoding = r.apparent_encoding
        s = etree.HTML(r.text)
        year = s.xpath('//*[@id="con02-4"]/table[1]/tr/td/form/select[@name="year"]/option/text()')
        jidu = s.xpath('//*[@id="con02-4"]/table[1]/tr/td/form/select[@name="jidu"]/option/text()')
        jidu = [x + 1 for x in range(len(jidu))]
        for j in year:
            for k in jidu:
                print("\t正在爬取{}股票{}年第{}季度数据".format(i, j, k))
                tar_data(i, j, k, table_name)
                # time.sleep(0.1)


def tar_data(gupiao_number, year, jidu, table_name):
    ua_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ',
        '(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)'
    ]
    ua = {'User-Agent': str(random.choices(ua_list))}
    url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/' \
          'stockid/{}.phtml?year={}&jidu={}'
    r = requests.get(url.format(gupiao_number, year, jidu), headers=ua)
    r.encoding = r.apparent_encoding
    s = etree.HTML(r.text)
    # title = s.xpath('//*[@id="FundHoldSharesTable"]/tr[1]/td//div/strong/text()') #表头
    data = s.xpath('//*[@id="FundHoldSharesTable"]/tr[1]/following-sibling::*/td/div/text()')  # 表格数据
    date = s.xpath('//*[@id="FundHoldSharesTable"]/tr[1]/following-sibling::*/td/div/a/text()')  # 日期
    date = [x.strip() for x in date]  # 日期处理
    if len(date) == 0:
        # data = s.xpath('//*[@id="FundHoldSharesTable"]/tr[1]/following-sibling::*/td/div/text()')
        size = int(len(data) / 8)  # 表格数据格式处理
        full_data = []  # 整合后的最终数据列表
        for i in range(size):
            start = i * 8
            end = start + 8
            full_data.append(data[start: end])

        for i in full_data:
            i[0] = i[0].strip()
        for i in range(len(full_data)):
            full_data[i].insert(0, str(gupiao_number))  # 整合股票号
            full_data[i].append(gupiao_full_data[gupiao_number])
            insert_data(table_name, full_data[i])  # 插入数据

    else:
        size = int(len(data) / 9)  # 表格数据格式处理
        full_data = []  # 整合后的最终数据列表
        for i in range(size):
            start = i * 9
            end = start + 9
            full_data.append(data[start: end][2:])
        if len(date) != size:
            print("\t{}号股票{}年数据第{}季度跳过成功".format(gupiao_number,year,jidu))
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S\n'))
            return
        for i in range(len(full_data)):
            # full_data[i].append(date[i])  # 整合日期
            full_data[i].insert(0, date[i])  # 整合日期
            full_data[i].insert(0, str(gupiao_number))  # 整合股票号
            full_data[i].append(gupiao_full_data[gupiao_number])
            insert_data(table_name, full_data[i])  # 插入数据
    print("\t数据插入成功")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S\n'))


def creat_table(table_name):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='Stocks',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
    try:
        with connection.cursor() as cursor:
            sql = r'CREATE TABLE `{}` (' \
                  '`股票号`  varchar(255) NOT NULL ,' \
                  '`日期`  date NOT NULL ,' \
                  '`开盘价`  float NULL ,' \
                  '`最高价`  float NULL ,' \
                  '`收盘价`  float NULL ,' \
                  '`最低价`  float NULL ,' \
                  '`交易量（股）`  float NULL ,' \
                  '`交易金额（元）`  float NULL ,' \
                  '`复权因子`  float NULL ,' \
                  '`股票名`  varchar(255) NULL ,PRIMARY KEY (`股票号`, `日期`));'.format(table_name)
            cursor.execute(sql)
            print("创建{}表成功".format(table_name))
    finally:
        connection.close()


def insert_data(table_name, values):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='Stocks',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO `{}` (`股票号`,`日期`, `开盘价`, `最高价`, `收盘价`,`最低价`, `交易量（股）`, `交易金额（元）`, `复权因子`,`股票名`) ' \
                  'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'.format(table_name)
            cursor.execute(sql, values)
            connection.commit()
    finally:
        connection.close()


if __name__ == '__main__':
    table_name = 'stocks_Transaction'
    gupiao_full_data, df_number_list = get_gupiao_list()
    get_data(gupiao_full_data, df_number_list, table_name)
