import requests
from pandas import DataFrame
from lxml import etree
from pymongo import MongoClient
import re
from datetime import datetime

# get Shanghai 50 Composite Index stocks list
def getSZ50_Composite():
    url = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/' \
          'JS.aspx?type=CT&cmd=C.BK06111&sty=FCOIATA&sortType=C' \
          '&pageSize=50&token=7bc05d0d4c3c22ef9fca8c2a912d779c'
    r = requests.get( url, )
    r.encoding = r.apparent_encoding
    print( r.status_code )
    s = r.text[3:-3].split( '","' )
    data = list()
    for i in s:
        # print( i )
        data.append( i.split( ',' ) )
    # print( data )
    df = DataFrame( data )
    # df.to_csv( 'sz50.csv', encoding='UTF-8' )
    return df

# //get all the stocks(codes and name)
def getAllStocksCodes():
    client = MongoClient()
    client.drop_database('StocksCodes')
    db = client.StocksCodes

    my_set = db.stocks_codes
    url = 'http://quote.eastmoney.com/stocklist.html#sz'
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    s = etree.HTML( r.text )
    number_list = s.xpath( '//*[@id="quotesearch"]//a[@target]/text()' )
    count = 1
    for i in number_list:
        name = re.split( '\(|\)', i )[0:2]
        if name[1].find('0')==0 or name[1].find('6')==0 or name[1].find('3')==0:
            print( "正在插入第{}条数据".format( count ) )
            my_set.insert( dict( name=name[0], number=name[1], ) )
            count += 1
        # if count ==4000:
        #     print(my_set)
    # print(number_list.len)
    # gupiao = re.match(r'(.*)(\d)',number_list[2])
    # df = DataFrame(number_list)
    # df.to_csv('number_list.csv', encoding='utf-8-sig')

# get stocks detail features
def getStocksFeature():
    client = MongoClient()
    # client.drop_database( 'StocksFeatures' )
    db = client.StocksFeatures
    my_set = db.Features

    db_stocks = client.StocksCodes
    my_number = db_stocks.stocks_codes

    cursor = my_number.find()
    my_number_list = []
    my_number_list_new = []

    def get_gupiao_number():
        for i in cursor:
            my_number_list.append( i['number'] )
        print( "获取股票编号成功" )
        print( datetime.now().strftime( '%Y-%m-%d %H:%M:%S\n' ) )

    def get_data():
        # id_duan = '300285'
        # my_number_list_new = my_number_list[my_number_list.index(id_duan) + 1:]
        my_number_list_new = my_number_list[my_number_list.index('002861')+1:]

        for i in my_number_list_new:
            try:
                full_data_list = dict()
                url = 'http://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/' \
                      'stockid/{}/ctrl/2017/displaytype/4.phtml'.format( i )
                r = requests.get( url )
                r.encoding = r.apparent_encoding
                s = etree.HTML( r.text )

                year_list = s.xpath( '//*[@id="con02-1"]/table/td/a/text()' )[:]

                print( "爬取进程：{:.2%}\n".format( (my_number_list_new.index( i ) + 1) / len( my_number_list_new ) ) )
                print( "本次运行已经保存{}支股票\n".format( my_number_list_new.index( i ) + 1 ) )
                print( "剩余{}支股票\n".format( len( my_number_list_new ) - my_number_list_new.index( i ) ) )
                print( "正在爬取{}号股票\n".format( i ) )

                # dict_2017 = get_2017_data( i, 2017, s )
                # if dict_2017:
                #     full_data_list.update( dict_2017 )
                # else:
                #     continue

                for j in year_list:
                    try:
                        dict_usua = get_usual_data( i, j )
                        full_data_list.update(dict_usua)
                    except Exception as e:
                        print( "异常：{}".format( e ) )
                        continue

                my_set.insert( dict( full_data_list ) )
                print( "{}号股票所有数据保存成功\t".format( i ) )
                print( datetime.now().strftime( '%Y-%m-%d %H:%M:%S\n' ) )

            except Exception as e:
                print( "异常：{}".format( e ) )
                continue

    def get_usual_data(gupiao_number, year):

        url = 'http://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/' \
              'stockid/{}/ctrl/{}/displaytype/4.phtml'.format( gupiao_number, year )

        r = requests.get( url )
        r.encoding = r.apparent_encoding
        s = etree.HTML( r.text )
        date_quarter = s.xpath( '//*[@id="BalanceSheetNewTable0"]/tbody/tr[1]//td/text()' )

        data_1 = s.xpath( '//*[@id="con02-1"]/table[2]//tr/td[1]/a/text()' )
        data_2 = s.xpath( '//*[@id="con02-1"]/table[2]//tr/td[2]/text()' )[1:]
        data_3 = s.xpath( '//*[@id="con02-1"]/table[2]//tr/td[3]/text()' )[1:]
        data_4 = s.xpath( '//*[@id="con02-1"]/table[2]//tr/td[4]/text()' )[1:]
        data_5 = s.xpath( '//*[@id="con02-1"]/table[2]//tr/td[5]/text()' )[1:]
        my_gupiao_name = s.xpath( '//*[@id="toolbar"]/div[1]/h1/a/text()' )

        listRes = []
        res_1 = dict( zip( data_1, data_2 ) )  # 月份组合数据
        res_2 = dict( zip( data_1, data_3 ) )
        res_3 = dict( zip( data_1, data_4 ) )
        res_4 = dict( zip( data_1, data_5 ) )

        listRes.append(res_1)
        listRes.append(res_2)
        listRes.append(res_3)
        listRes.append(res_4)
        time = dict()
        if my_gupiao_name:
            time['id'] = gupiao_number

            # 保存月份组合数据到time List中
            time['name'] = my_gupiao_name[0]
            for i in range(len(date_quarter)):
                time['{}'.format(date_quarter[i])]=listRes[i]
            # time['{}-12-31'.format( year )] = listRes
            # time['{}-9-30'.format( year )] = res_2
            # time['{}-6-30'.format( year )] = res_3
            # time['{}-3-31'.format( year )] = res_4

        if my_gupiao_name:
            print( "\t{}号股票{}年数据返回成功\t".format( gupiao_number, year))
            print( datetime.now().strftime( '\t%Y-%m-%d %H:%M:%S\n' ) )

            for i in range(len(listRes)):
                quarterDate = listRes[i]  ##quarterDate,单一季度数据
                if not quarterDate:
                    print( "\t{0}号股票{1}年单一季度数据为空\t".format( gupiao_number,year) )
                    # del time['{}'.format(date_quarter[i])]
            # if not data_3:
            #     print( "\t{}号股票{}-9-30数据为空\t".format( gupiao_number, year ) )
            #     del time['{}-9-30'.format( year )]
            # if not data_4:
            #     print( "\t{}号股票{}-6-30数据为空\t".format( gupiao_number, year ) )
            #     del time['{}-6-30'.format( year )]
            # if not data_5:
            #     print( "\t{}号股票{}-3-31数据为空\t".format( gupiao_number, year ) )
            #     del time['{}-3-31'.format( year )]

            print( "\t{}号股票{}年数据返回成功\t".format( gupiao_number, year ) )
            print( datetime.now().strftime( '\t%Y-%m-%d %H:%M:%S\n' ) )
            return time
        else:
            print( "\t{}号股票{}年数据为空\t".format( gupiao_number, year ) )
            print( datetime.now().strftime( '\t%Y-%m-%d %H:%M:%S\n' ) )

    get_gupiao_number()
    get_data()

if __name__ == '__main__':
    getStocksFeature()
    list = [1,2,3]
    print(list[0])

