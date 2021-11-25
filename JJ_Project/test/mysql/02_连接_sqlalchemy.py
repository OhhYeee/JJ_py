from sqlalchemy import create_engine
from sqlalchemy.sql import text

dbname = 'JJ_Test'

engine = create_engine('mysql+mysqlconnector://root:12345678@localhost:3306/{}'.format(dbname))
conn = engine.connect()
res = text(
    '''
    select * from borrowOrders 
    '''
)
result = conn.execute(res)

rows = result.fetchone()
# tem_dict = convert_engine_result_to_dict(rows)
# print(tem_dict)

result.close()

