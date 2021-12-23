import ipinfo

access_token = '5a78fe99948357'
handler = ipinfo.getHandler(access_token)
ip_address = '216.239.36.21'
details = handler.getDetails(ip_address)    # 访问结果
print('details:{}'.format(details.details))

loc = details.loc   # 获取经纬度
locarr = loc.split(',')
latitude = locarr[0]
longitude = locarr[1]
print('loc:{}'.format(loc))
print('latitude:{}'.format(latitude))
print('longitude:{}'.format(longitude))

