def plus(num):
    return num + 100

def handler(func):
    res = func(100)
    print("执行func,并获取到结果为：{}".format(res))

# 执行handler函数，将plus作为参数传递给handler的形式参数func
handler(plus)