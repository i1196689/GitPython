import pandas as pd
import numpy as np
'''
series1=pd.Series([2.8,3.01,8.99,8.58,5.18])
print(series1)
series2=pd.Series([2.8,3.01,8.99,8.58,5.18],index=["a",'b','c','d','e'],name="这是一个序列")
print(series2)
series3=pd.Series({"北京":2.8,"上海":3.01,'广东':8.99,'江苏':8.58,'浙江':5.18})
print(series3[0:3])
print(series3['北京':'江苏'])

print(series1.values)
print(series3.index)
print(series1)
'''

list1=[['张三',23,'男'],['李四',27,'女'],['王二',26,'女']]
df1=pd.DataFrame(list1,columns=['姓名','年龄','性别'])
with open('day_03.txt','w',encoding='utf-8')as f:
    f.write(str(df1))#可以转换为str进行存贮

df2=pd.DataFrame({'姓名':['张三','李四','王二'],'年龄':[23,27,26],'性别':['男','女','女']})
print(df2)
print('---------------------')

arr1=np.array([['张三',23,'男'],['李四',27,'女'],['王二',26,'女']])

df3=pd.DataFrame(arr1,columns=['姓名','年龄','性别'],index=['a','b','c'])
print(df3)

print('------------')
print(df3.values)
print('------------')
print(df3.index)
print('------------')
print(df3.columns.tolist())
print('------------')
print(df3.ndim)