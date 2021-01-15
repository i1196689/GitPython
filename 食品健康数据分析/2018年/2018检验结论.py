import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei']
xls_file = pd.read_excel(r'C:\Users\liuju\Desktop\2017-2019食品抽检数据汇总\2018年食品数据\2018年农产品直报系统.xls')

group = xls_file.loc[:,'检验结论'].value_counts()
group.to_excel(r'C:\Users\liuju\Desktop\2017.xlsx')
group.name = ''
'''
xls_file['检验结论'].plot.pie()
plt.show()
'''
group.plot.pie(autopct='%.0f%%')
plt.title('检验结论')
plt.show()


