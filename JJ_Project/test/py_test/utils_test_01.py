from sqlalchemy import create_engine
from sqlalchemy.sql import text
from utils.myfunctools import *

dbname = 'JJ_Test'

engine = create_engine('mysql+mysqlconnector://root:12345678@localhost:3306/{}'.format(dbname))
conn = engine.connect()
res = text(
    '''
    select * from borrowOrders limit 1
    '''
)
result = conn.execute(res)
rows = result.fetchall()
tem_dict = {}
for i in rows:
    tem_dict = convert_engine_result_to_dict(i)
print(tem_dict)

result.close()
