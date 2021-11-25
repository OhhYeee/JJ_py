import pandas as pd


print("-----df1------")
student = ((1,"张三",20),(2,"李四",22),(3,"王五",24),(4,"赵六",20))
df1 = pd.DataFrame(student,columns=['ID','姓名','年龄'])
print(df1)

print("-----df2------")
score = ((1,"张三",100), (2, "张三", 90), (3, "李四", 80), (4, "李四", 80))
df2 = pd.DataFrame(score, columns=['ID', '姓名', '分数'])
print(df2)


print("-----df3------")
df3 = df1.merge(df2, how= 'inner', left_on= '姓名', right_on= '姓名')
print(df3)

print("-----df4------")
df4 = df3.groupby('姓名')['年龄'].count()
print(df4['张三'])


print("-----df5------")
df5 = df3['年龄'].value_counts()
print(df5)


print("-----df6------")
df6 = df3.where(df3.年龄 == 20 )
print(df6.count()['年龄'])


print("-----df7------")
df7 = df3.where(df3.年龄 == 20 )
print(df7)
print(df7.describe())


print("-----df8------")
df8 = df3[(df3['姓名'] == '张三') & (df3['年龄'] == 20)]
print(df8)
# df4.where(df4.)

print("---------------")
cnt = df3.count()['姓名']
print(cnt)