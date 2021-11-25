import pandas as pd

list = ['A','B','C','D','A']

list1 = ['1','2','3','4','5']

dict1 = {}
for i in list:
    dict1[str(i)] = 2

print(dict1)

dic = dict(zip(list,list1))
print(dic)

df = pd.DataFrame(dic, columns=['id', 'age'])
print(df)