import pymongo
import datetime
import pandas as pd
from pymongo import MongoClient
import numpy as np

def _connect_mongo(host, port, username, password, db):
    """ A util for making a connection to mongo """

    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)


    return conn[db]


def read_mongo(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
    """ Read from Mongo and Store into DataFrame """

    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)

    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))

    # Delete the _id
    if no_id and not(df.empty):
        del df['_id']

    return df

def get_StockList(db, collection,query={}, host='localhost', port=27017, username=None, password=None, no_id=True):

    df = read_mongo(db, collection, query, host, port, username, password, no_id)

    return df[['number','name']]
#_connect_mongo('localhost', 27017,None,None,'gupiaoDB')
# sql=None
# # sql ={"author": "Mike1"}
# df = read_mongo('gupiaoDB','testDocs',sql)
# df.head(3)
#
# print(df.head(3))


# client = MongoClient('localhost', 27017)
#
# print(client.database_names())
# db = client['gupiaoDB']
#
# aDoc = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#          "date": datetime.datetime.utcnow()}
#
# testDocs = db.testDocs
# testDocs.insert_one(aDoc)
# # db.collection_names(include_system_collections=False)['testDoc']

if __name__ == '__main__':
    df = get_StockList('StocksCodes','stocks_codes',None)
    print(df.head(10))
    print(df.columns.values.tolist())
    # print(df.axes)
    # data = pd.DataFrame( np.arange( 1, 31, 2 ).reshape( 3, 5 ),
    # index=['one', 'two', 'three'], columns=['a', 'b', 'c', 'd', 'e'] )
    # data.columns.values.tolist()
    # data.__dict__.keys()
    # list = data._info_axis[:]
    # # str = data.columns
    # # str.split('[')[1].split[0]
    # print(list.values)

