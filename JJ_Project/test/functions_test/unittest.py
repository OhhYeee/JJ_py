import unittest

import time

# t1 = time.time()
# t2 = time.time()
#
# print(t1)
# print(t2)

start = time.time()
num = 0
j = 10
for i in range(500):
    if j == 10:
        if num != 1:
            num = 1
end = time.time()
print(end - start)


# start = time.time()
# num = 0
# j = 10
# for i in range(500):
#     if j == 10:
#         num = 1
# end = time.time()
# print(end - start)

# apply_ts = datetime.strptime(str_apply_ts,'%Y-%m-%d %H:%M:%S')
print(None + 100)