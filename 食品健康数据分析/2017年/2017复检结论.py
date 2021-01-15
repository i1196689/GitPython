import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei']
xls_file = pd.read_excel(r'C:\Users\liuju\Desktop\2017-2019食品抽检数据汇总\2017年食品数据\2017年农产品直报系统.xls')

group = xls_file.loc[:,'复检结论'].value_counts()
group.name = ''

group.plot.pie(autopct='%.0f%%')
plt.title('复检结论')
plt.show()