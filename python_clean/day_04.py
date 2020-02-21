import numpy as np
import pandas as pd
'''
df2=pd.DataFrame({'姓名':['张三','李四','王二'],'年龄':[23,27,26],'性别':['男','女','女']})
print(df2)
print('-------------')
df2.to_csv('day_04.csv',encoding='gbk',index=False)#将索引去掉
orde=pd.read_csv('day_04.csv',encoding='gbk')
print(orde)
print('------------------')
print(orde.姓名)
print(orde.年龄)
'''
df1=pd.read_excel('2020_subject.xlsx',encoding='utf-8',sheet_name=0)
print(df1.head(10))
df1.to_excel('2020_subject.xlsx',encoding='utf-8',sheet_name='one')