import datetime

import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "12345678",
    database = "JJ_Test"
)

print(mydb)

conn = mydb.cursor()
conn.execute(
    '''
    select * from borrowOrders
    '''
)
res = conn.fetchall()


t = type(res)
print(type(res[0]))

print("-------res-------")
print(res)
df1 = pd.DataFrame(res, columns=['id', 'user_id', 'orderno', 'bankcode', 'createdat'])
print("------df1-------")
print(df1)

df2 = df1.append(df1)
print("------df2-------")
print(df2)


print("------s-------")
s = df1.loc[(df1['id'] == 1), 'createdat']
print(s)

print("-------f--------")
print(min(datetime.datetime(2021-10-10), "2021-10-10"))






