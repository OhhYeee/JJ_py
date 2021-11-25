import pandas as pd
dict = {'A' : '1', 'B' : '2', 'C' : '3','D': '4'}

list = []
# for i in dict.items():
#     list.append((i))
# print(list)


for i in range(10):
    list.append((i,i+100))

print(list)
print("--------df---------")
df = pd.DataFrame(list,columns=['user_id', 'ts'])
print(df)
