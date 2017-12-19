# -*- coding:UTF-8 -*-
from datetime import datetime
import requests
from lxml import etree
from pymongo import MongoClient

client = MongoClient()
db = client.gupiaoDB
my_set = db.fulldata

db_number = client.StocksList
my_number = db_number.StockCodes

cursor = my_number.find()
my_number_list = []
my_number_list_new = []
def get_gupiao_number():
    for i in cursor:
        my_number_list.append(i['number'])
    print("获取股票编号成功")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S\n'))

def get_data():
    id_duan = '300285'
    my_number_list_new = my_number_list[my_number_list.index(id_duan) + 1:]

    for i in my_number_list_new:
        try:
            full_data_list = dict()
            url = 'http://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/' \
                  'stockid/{}/ctrl/2017/displaytype/4.phtml'.format(i)
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            s = etree.HTML(r.text)

            year_list = s.xpath('//*[@id="con02-1"]/table/td/a/text()')[1:]

            print("爬取进程：{:.2%}\n".format((my_number_list_new.index(i)+1) / len(my_number_list_new)))
            print("本次运行已经保存{}支股票\n".format(my_number_list_new.index(i)+1))
            print("剩余{}支股票\n".format(len(my_number_list_new)-my_number_list_new.index(i)))
            print("正在爬取{}号股票\n".format(i))

            dict_2017 = get_2017_data(i, 2017, s)
            if dict_2017:
                full_data_list.update(dict_2017)
            else:
                continue

            for j in year_list:
                try:
                    dict_usua = get_usual_data(i, j)
                    full_data_list.update(dict_usua)
                except Exception as e:
                    print("异常：{}".format(e))
                    continue

            my_set.insert(dict(full_data_list))
            print("{}号股票所有数据保存成功\t".format(i))
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S\n'))

        except Exception as e:
            print("异常：{}".format(e))
            continue


def get_2017_data(gupiao_number, year, s):

    data_1 = s.xpath('//*[@id="con02-1"]/table[2]//tr/td[1]/a/text()')
    data_2 = s.xpath('//*[@id="con02-1"]/table[2]//tr/td[2]/text()')[1:]
    data_3 = s.xpath('//*[@id="con02-1"]/table[2]//tr/td[3]/text()')[1:]
    data_4 = s.xpath('//*[@id="con02-1"]/table[2]//tr/td[4]/text()')[1:]
    my_gupiao_name = s.xpath('//*[@id="toolbar"]/div[1]/h1/a/text()')

    res_1 = dict(zip(data_1, data_2))  # 月份组合数据
    res_2 = dict(zip(data_1, data_3))
    res_3 = dict(zip(data_1, data_4))
    time = dict()
    if my_gupiao_name:
        time['id'] = gupiao_number
        time['name'] =my_gupiao_name[0]

        time['{}-12-31'.format(year)] = res_1
        time['{}-9-30'.format(year)] = res_2
        time['{}-6-30'.format(year)] = res_3
    if my_gupiao_name:
        if not data_2:
            print('{}号股票2017-12-31数据不存在'.format(gupiao_number))
            del time['{}-12-31'.format(year)]
        if not data_3:
            print('{}号股票2017-9-30数据不存在'.format(gupiao_number))
            del time['{}-9-30'.format(year)]
        if not data_4:
            print('{}号股票2017-6-30数据不存在'.format(gupiao_number))
            del time['{}-6-30'.format(year)]

        print("\t{}号股票2017年数据返回成功\t".format(gupiao_number))
        print(datetime.now().strftime('\t%Y-%m-%d %H:%M:%S\n'))
        return time
    else:
        print("\t{}号股票2017年数据为空\t".format(gupiao_number))
        print(datetime.now().strftime('\t%Y-%m-%d %H:%M:%S\n'))

def get_usual_data(gupiao_number, year):

    url = 'http://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/' \
          'stockid/{}/ctrl/{}/displaytype/4.phtml'.format(gupiao_number,year)

    r = requests.get(url)
    r.encoding = r.apparent_encoding
    s = etree.HTML(r.text)
    data_1 = s.xpath('//*[@id="con02-1"]/table[2]//tr/td[1]/a/text()')
    data_2 = s.xpath('//*[@id="con02-1"]/table[2]//tr/td[2]/text()')[1:]
    data_3 = s.xpath('//*[@id="con02-1"]/table[2]//tr/td[3]/text()')[1:]
    data_4 = s.xpath('//*[@id="con02-1"]/table[2]//tr/td[4]/text()')[1:]
    data_5 = s.xpath('//*[@id="con02-1"]/table[2]//tr/td[5]/text()')[1:]
    my_gupiao_name = s.xpath('//*[@id="toolbar"]/div[1]/h1/a/text()')

    res_1 = dict(zip(data_1, data_2))  # 月份组合数据
    res_2 = dict(zip(data_1, data_3))
    res_3 = dict(zip(data_1, data_4))
    res_4 = dict(zip(data_1, data_5))
    time = dict()
    if my_gupiao_name:
        time['id'] = gupiao_number

        time['name'] = my_gupiao_name[0]
        time['{}-12-31'.format(year)] = res_1
        time['{}-9-30'.format(year)] = res_2
        time['{}-6-30'.format(year)] = res_3
        time['{}-3-31'.format(year)] = res_4

    if my_gupiao_name:
        print("\t{}号股票{}年数据返回成功\t".format(gupiao_number, year))
        print(datetime.now().strftime('\t%Y-%m-%d %H:%M:%S\n'))
        if not data_2:
            print("\t{}号股票{}-12-31数据为空\t".format(gupiao_number, year))
            del time['{}-12-31'.format(year)]
        if not data_3:
            print("\t{}号股票{}-9-30数据为空\t".format(gupiao_number, year))
            del time['{}-9-30'.format(year)]
        if not data_4:
            print("\t{}号股票{}-6-30数据为空\t".format(gupiao_number, year))
            del time['{}-6-30'.format(year)]
        if not data_5:
            print("\t{}号股票{}-3-31数据为空\t".format(gupiao_number, year))
            del time['{}-3-31'.format(year)]

        print("\t{}号股票{}年数据返回成功\t".format(gupiao_number, year))
        print(datetime.now().strftime('\t%Y-%m-%d %H:%M:%S\n'))
        return time
    else:
        print("\t{}号股票{}年数据为空\t".format(gupiao_number, year))
        print(datetime.now().strftime('\t%Y-%m-%d %H:%M:%S\n'))

if __name__ == '__main__':
    get_gupiao_number()
    get_data()
