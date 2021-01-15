import pandas as pd
import matplotlib.pyplot as plt
'''
plt.rcParams['font.sans-serif']=['SimHei']
'''
plt.rcParams['font.family'] = ['Arial Unicode MS'] 
xls_file = pd.read_excel('2017年农产品直报系统.xls')
count = xls_file.loc[:,'检验结论'].value_counts()
print(count)
'''
xls_file['检验结论'].plot.pie()
plt.show()
'''
print(count)
'''
count.plot.pie(autopct='%.0f%%')
plt.show()
'''

