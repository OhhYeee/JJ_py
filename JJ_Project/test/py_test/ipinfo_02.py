import urllib
import requests
import json
import logger


class IPApi():
    def __init__(self, API_IP, YOUR_ACCESS_KEY, SECURITY):
        self.API_IP = API_IP
        # self.USER_NAME = USER_NAME
        # self.PASSWORD = PASSWORD
        self.YOUR_ACCESS_KEY = YOUR_ACCESS_KEY
        self.SECURITY = SECURITY

    # 查询外部第三方ip解析接口
    def ip_api_func(self, user_ip):
        # data = {'username': self.USER_NAME, 'password': self.PASSWORD}
        dd = {'token': self.YOUR_ACCESS_KEY, 'security': self.SECURITY}
        d = urllib.parse.urlencode(dd)  #
        if self.API_IP is not None:
            try:
                url = 'http://' + self.API_IP + '/' + user_ip + '?' + d  # 拼接url地址
                req = requests.get(url, timeout=(10, 20))
                result = json.loads(req.text)
                loc = result['loc']
                long_and_lat = loc.split(',')
                latitude = long_and_lat[0]
                longitude = long_and_lat[1]
                # 将ip解析返回值入表idrisk_ip_parse
                if longitude is None or latitude is None:
                    return ''
                else:
                    return result
            except Exception as err:
                logger.error("调用IP服务出现异常:{}".format(err))
        else:
            return ''



if __name__ == "__main__":
    # 创建IP API实例
    IP_API_URL = 'ipinfo.io'
    # IP_USER_NAME = ''
    # IP_PASSWORD = ''
    IP_YOUR_ACCESS_KEY = '5a78fe99948357'
    IP_SECURITY = 1

    # logger.info('create ip_api ')
    ip_api = IPApi(IP_API_URL, IP_YOUR_ACCESS_KEY, IP_SECURITY)
    result = ip_api.ip_api_func('124.105.106.90')
    assert result == {'ip': '124.105.106.90',
                      'city': 'Lapu-Lapu City',
                      'region': 'Central Visayas',
                      'country': 'PH',
                      'loc': '10.3103,123.9494',
                      'org': 'AS9299 Philippine Long Distance Telephone Company',
                      'postal': '6015',
                      'timezone': 'Asia/Manila'}
    print('===========request success===========')
    print('res: {}'.format(result))
