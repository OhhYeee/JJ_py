import ipinfo
import logger


class IPApi():
    def __init__(self, access_token):
        self.ACCESS_TOKEN = access_token

    # 查询外部第三方ip解析接口
    def ip_api_func(self, user_ip):
        if user_ip is not None:
            try:
                handler = ipinfo.getHandler(self.ACCESS_TOKEN)
                details = handler.getDetails(user_ip, timeout=(10, 20))
                result = details.details
                latitude = result['latitude']
                longitude = result['longitude']
                # 将ip解析返回值入表idrisk_ip_parse
                if longitude is None or latitude is None:
                    return ''
                else:
                    return result
            except Exception as err:
                logger.error("调用IP服务出现异常:{}".format(err))
        else:
            return ''


ipApi = IPApi('5a78fe99948357')
result = ipApi.ip_api_func('216.239.36.21')
print(result)

a = None
b = a.split(',')
print(b[0])
print('b[1]:' + b[1])
if b[1] == '':
    print('--------')