import pymysql

def _connect_MYSQL(_host, _port, _username, _password, _db):
# A util for making a connection to MYSQL
    if _username and _password:
        connection = pymysql.connect(host=_host,
                                user=_username,
                                password=_password,
                                db=_db,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor
                                )
    return connection


def creat_table(_host, _port, _username, _password, _db,_sql,table_name):

    connection = _connect_MYSQL( _host, _port, _username, _password, _db )

    try:
        with connection.cursor() as cursor:
            cursor.execute(_sql.format(table_name))
            print("创建{}表成功".format(table_name))
    finally:
        connection.close()

def insert_data(_host, _port, _username, _password, _db,_sql,table_name, values):
    connection = _connect_MYSQL( _host, _port, _username, _password, _db )
    try:
        with connection.cursor() as cursor:
            sql = _sql.format(table_name)
            cursor.execute(sql, values)
            connection.commit()
    finally:
        connection.close()


if __name__ == '__main__':
    # !/usr/bin/python
    # -*- coding: utf-8 -*-
    import DataPreparation.getStocksFeature as dp

    df_stocks = dp.getDetailInforForAllStocks()


    print(list)
