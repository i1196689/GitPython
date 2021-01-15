import pandas as pd
import matplotlib.pyplot as plt
import copy


plt.rcParams['font.sans-serif']=['SimHei']
xls_file = pd.read_excel(r'C:\Users\liuju\Desktop\2017-2019食品抽检数据汇总\2018年食品数据\2018年农产品直报系统.xls')

group = xls_file.loc[:,'抽样数量'].value_counts()
'''
group.name = ''
group.plot.pie()
plt.title('抽样数量')
plt.show()

group = group.drop(index=250)
a=pd.Series(250,index=['other'])
group = group.append(a)
print(group)
'''
num = 0
g_index = group.index
group_1 = group.copy()
for index in g_index:
    if group[index] < 300 :
        num += group[index]
        group = group.drop(index=index)
    else:
        group_1 = group_1.drop(index=index)
g_other = pd.Series(num,index=['other'])
group = group.append(g_other)
group.name = ''
group.plot.pie(autopct='%.0f%%')
plt.title('抽样数量')
plt.show()

'''
group_1.name = ''
group_1.plot.pie(autopct='%.0f%%')
plt.title('抽样数量')
plt.show()
'''


