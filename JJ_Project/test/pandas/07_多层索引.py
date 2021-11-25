import pandas as pd

stocks = pd.read_excel('/Users/jiajun.jiang/PycharmProjects/JJ_test/datas/stocks/互联网公司股票.xlsx')

print(stocks)

# 返回列的唯一值，即去重
# print(stocks['公司'].unique())

# 返回列去重后的count数量
# print(stocks['公司'].nunique())

# 返回索引信息
# print(stocks.index)

# 按照公司分组，求收盘平均数
df1 = stocks.groupby('公司')['收盘'].mean()
print(df1)

# series的分层索引Multiindex
print(stocks.groupby(['公司', '日期'])[['收盘','开盘']].mean())

