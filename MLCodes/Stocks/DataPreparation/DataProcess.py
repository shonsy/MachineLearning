import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient
from DBOperation import DBOperation as DBOper
import DataPreparation.getStocks as gtStock

def getDetailInforForAllStocks():
    df = DBOper.read_mongo('gupiaoDB','fulldata',None)

    labels_df = df.columns.values.tolist()
    # print(arr)
    # print(len(arr))

    #df.dropna( axis=1 )
    lstStock = []
    for nRow in range(len(df.index)): # nRow: df中每一行记录
    # for nRow in range( 1000, 1050 ):
        basicInfor = {'id': '{}'.format( df.ix[nRow, 'id'] )}
        basicInfor['name'] = df.ix[nRow, 'name']
        # print(dictInfor)
        labelIndex = 0;
        i = 0
        for nQuarter in range( 0, len( labels_df ) - 2, 1 ):  # nQuarter:每1季度
            basicInfor['date'] = labels_df[labelIndex]
            labelIndex = labelIndex + 1
            featureInfor = df.iat[nRow, nQuarter]  # df.iat[nRow,nQuarter]每1个季度的详细数据
            stockInfor = basicInfor.copy();
            #         if not math.isnan(float(featureInfor)):
            #         if not featureInfor is np.nan:
            if isinstance( featureInfor, dict ):  # 仅当季度数据不为空时添加记录
                stockInfor.update( featureInfor )
                lstStock.append( stockInfor )
            if i < 3 and isinstance( featureInfor, dict ):
                # print(featureInfor)

                #             print(stockInfor.values())
                i = i + 1
    #             print(len(lstStock))

    df_stock = pd.DataFrame( lstStock )
    print(df_stock.head(2))

    # lst = df.axes
    print( df_stock.shape )
    df_stock.to_csv( '9.csv', encoding='utf-8' )
    return df_stock
    # df_stock.iloc[1:10,0:11]
    # print(len(df))
    # df.iloc[:,90]

def getDetailInforForSelectedStocks(lstSelectdStocks):
    df = DBOper.read_mongo('gupiaoDB','fulldata',None)

    labels_df = df.columns.values.tolist()
    # print(arr)
    # print(len(arr))

    #df.dropna( axis=1 )

    lstStock = []
    for nRow in range(len(df.index)): # nRow: df中每一行记录
    # for nRow in range( 1000, 1050 ):
        basicInfor = {'id': '{}'.format( df.ix[nRow, 'id'] )}

        isSelectdStock = False
        for i in range(len(lstSelectdStocks)):
            if basicInfor['id'] == lstSelectdStocks[i]:
                isSelectdStock = True
                break
        #if not selected stock, continue to check the next record
        if not isSelectdStock:
            continue
        basicInfor['name'] = df.ix[nRow, 'name']
        # print(dictInfor)
        labelIndex = 0;
        i = 0
        for nQuarter in range( 0, len( labels_df ) - 2, 1 ):  # nQuarter:每1季度
            basicInfor['date'] = labels_df[labelIndex]
            labelIndex = labelIndex + 1
            featureInfor = df.iat[nRow, nQuarter]  # df.iat[nRow,nQuarter]每1个季度的详细数据
            stockInfor = basicInfor.copy();
            #         if not math.isnan(float(featureInfor)):
            #         if not featureInfor is np.nan:
            if isinstance( featureInfor, dict ):  # 仅当季度数据不为空时添加记录
                stockInfor.update( featureInfor )
                lstStock.append( stockInfor )
            if i < 3 and isinstance( featureInfor, dict ):
                # print(featureInfor)

                #             print(stockInfor.values())
                i = i + 1
    #             print(len(lstStock))

    df_stock = pd.DataFrame( lstStock )
    print(df_stock.head(2))

    # lst = df.axes
    print( df_stock.shape )
    df_stock.to_csv( '9.csv', encoding='utf-8' )
    return df_stock
    # df_stock.iloc[1:10,0:11]
    # print(len(df))
    # df.iloc[:,90]

if __name__ == '__main__':

    # df = getDetailInforForAllStocks()
    df = gtStock.getSZ50_Composite()
    df[1].values.tolist()
    # lstStocks = ['600001','600002']
    # df = getDetailInforForSelectedStocks(df[1].values.tolist())
    # yconnect = create_engine('mysql+mysqldb://root:root@localhost/stocks?charset=utf8')
    pd.io.sql.to_sql(df,'stocks_features', yconnect, schema='stocks', if_exists='append')# df.to_csv( 'sz50features.csv', encoding='UTF-8' )
    print( df.head( 10 ) )
    print( df.shape)




