from datetime import datetime

import logger

# 数据库查询结果数据类型转换
def convert_engine_result_to_dict(rows):
    if not rows:
        return {}

    tmp_dict = {}
    for i in rows.iterkeys():
        import decimal
        if isinstance(rows[i], str) or isinstance(rows[i], int):
            tmp_dict[i] = rows[i]
        elif isinstance(rows[i], decimal.Decimal):
            tmp_dict[i] = float(rows[i])
        elif isinstance(rows[i], datetime):
            tmp_dict[i] = datetime.timestamp(rows[i])
        elif isinstance(rows[i], type(None)):
            tmp_dict[i] = None
        else:
            logger.warn("unexpect type!! {type_name}".format(type_name=type(rows[i])))
            tmp_dict[i] = str(rows[i])
    return tmp_dict