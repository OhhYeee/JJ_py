import pandas as pd


print("-----df1------")
student = ((1,"张三",20),(2,"李四",22),(3,"王五",24),(4,"赵六",20))
df1 = pd.DataFrame(student,columns=['ID','姓名','年龄'])
print(df1)

print("-----df2------")
score = ((1,"王五",100), (2, "张三", 90), (3, "李四", 80), (4, "李四", 80))
df2 = pd.DataFrame(score, columns=['ID', '姓名', '分数'])
print(df2)


print("-----df3------")
def select_data(df):
    return (df["分数"] > 80) & (df["姓名"] != "张三")

df3 = df2.loc[select_data, :]
print(df3)

print("-----df4------")
df4 = df2.loc[(df2["分数"] > 80) & (df2["姓名"] != "张三"), :]
print(df4)



