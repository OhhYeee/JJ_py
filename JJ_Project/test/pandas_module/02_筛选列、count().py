import pandas as pd

student = ((1,"张三",20),(2,"李四",22),(3,"王五",24),(4,"赵六",20))
df = pd.DataFrame(student,columns=['ID','姓名','年龄'])
print(df)
print("-----df2------")

df2 = df[df.年龄 == 20 ]
print(df2.count())
# print(df2.count())

print("--------df3---------")
df3 = df.where(df.年龄 > 20)
print(df3.count())

print(df['年龄'].nunique())



# print("-----------")
# print(df.groupby(by=["年龄"]).count())