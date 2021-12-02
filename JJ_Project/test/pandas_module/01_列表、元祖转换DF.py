import pandas as pd

a = ((1,2,3),(4,5,6),(7,8,9))
print(a)
b = list(a)
print(b)
# 列表转换成df
df = pd.DataFrame(b,columns=['One','Two','Three'])
print("------df-------")
print(df)

print("------df1-------")
# 元祖转换成df
df1 = pd.DataFrame(a,columns=['One','Two','Three'])
print(df1)