import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei']
xls_file = pd.read_excel(r'C:\Users\liuju\Desktop\2017-2019食品抽检数据汇总\2019年食品数据\2019年直报系统食用农产品.xlsx')

group = xls_file.loc[:,'复检结论'].value_counts()
group.name = ''

group.plot.pie(autopct='%.0f%%')
plt.title('复检结论')
plt.show()