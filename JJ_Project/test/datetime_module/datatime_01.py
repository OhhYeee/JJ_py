import time
import datetime

# datetime常量
print("---------01--------")
print(datetime.MINYEAR)
print(datetime.MAXYEAR)

print("---------02--------")
print(datetime.datetime.min)
print(datetime.datetime.max)
print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.today())
print(datetime.date.fromtimestamp(time.time()))

print("---------03--------")
now = datetime.date(2021, 3, 4)
# 生成新的对象，替换旧的对象中的年月日
# tomorrow = now.replace(2021, 3, 5)
tomorrow = now.replace(day=5)
print(now)
print(tomorrow)

print("---------04--------")
print(now.timetuple())
print(now.toordinal())
print(datetime.date.fromtimestamp(time.time()).weekday())
print(datetime.date.fromtimestamp(time.time()).isoweekday())
print(datetime.date.fromtimestamp(time.time()).isocalendar())
print(datetime.date.fromtimestamp(time.time()).isoformat())

print("---------05--------")
timedelta = tomorrow - now
print(timedelta)




