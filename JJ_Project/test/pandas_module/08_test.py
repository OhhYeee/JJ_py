import datetime
import logging

import mysql.connector
import pandas as pd
import numpy as np

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "12345678",
    database = "JJ_Test"
)

print(mydb)
conn = mydb.cursor()
def select_offline(conn):
    conn.execute(
        '''
        select * from offline_user
        '''
    )
    res = conn.fetchall()
    t = type(res)
    print("-------type(res)-------")
    print(t)
    print(type(res[1]))
    df1 = pd.DataFrame(res, columns=['user_id', 'earliest_ts'])
    if 1 != 1:
        return df1
    else:
        return pd.DataFrame(columns=['user_id', 'earliest_ts'])

def select_realtime(conn):
    conn.execute(
        '''
        select * from realtime_user
        '''
    )
    res_real = conn.fetchall()
    t = type(res_real)
    print("-------type(res_real)-------")
    print(t)
    print(type(res_real[1]))
    df2 = pd.DataFrame(columns=['user_id', 'data_ts'])
    if 1 == 1:
        df2 = pd.DataFrame(res_real, columns=['user_id', 'data_ts'])
    return df2


print("-----df1------")
df1 = select_offline(conn)
print(df1['earliest_ts'].dtypes)
print(df1)

print("------df2-------")
df2 = select_realtime(conn)
print(df2['data_ts'].dtypes)
print(df2)

try:
    print("-------df22-------")
    df2 = df2.groupby('user_id')['data_ts'].min()
    print(df2)
except Exception as e:
    logging.ERROR("df22出错了！！！details:" + e)
logging.info("df22 :" + df2)

print("-------df3--------")
if df1.empty and df2.empty:
    print("都是空df！！！")
else:
    df3 = df1.merge(df2,how="outer", on = 'user_id')
    print(df3)

    print("-------df4--------")
    def add_ts(x):
        if x['earliest_ts'] is None and x['data_ts'] is None:
            return None
        elif x['earliest_ts'] is None:
            return x['data_ts']
        elif x['data_ts'] is None:
            return x['earliest_ts']
        else:
            return min(str(x['earliest_ts']), str(x['data_ts']))

    df3.loc[:, "ts"] = df3.apply(add_ts, axis=1)
    print(df3)

    print("--------df5--------")
    # df5 = df3.sort_values(by='ts',ascending=False,inplace=False)
    # df3.sort_values(by='ts',ascending=False,inplace=False)
    # print(df5)
    # print(df5[['user_id','ts']])

    print("-------df6_rank---------")
    df3['rank'] = df3['ts'].rank(method='first', ascending=False)
    print(df3)

    print("-------df6---------")
    df6 = df3[df3['rank'] <= 5]
    print(df6)

    print("-------df7---------")
    df7 = df6.head(3)
    print(df7)

    print("-------list--------")
    list = list(df6['user_id'])
    print(list)
    list = [str(i) for i in list]
    print(list)

