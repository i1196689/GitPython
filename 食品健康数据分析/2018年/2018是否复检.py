import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei']
xls_file = pd.read_excel(r'C:\Users\liuju\Desktop\2017-2019食品抽检数据汇总\2018年食品数据\2018年农产品直报系统.xls')

group = xls_file.loc[:,'是否复检'].value_counts()
group.to_excel(r'C:\Users\liuju\Desktop\2017.xlsx')
group.name = ''

p1,ax1 = plt.subplots()
bar = ax1.bar(x=['否','是'],height=group['否'])
plt.text(x='否',y=group['否']+500,s='%s'%group['否'],fontsize=15)
ax1.spines['top'].set_visible(False)
ax2 = ax1.twinx()
ax2.bar(x=['否','是'],height=group['是'])
plt.text(x='是',y=group['是']+0.1,s='%s'%group['是'],fontsize=15)
ax2.spines['top'].set_visible(False)
plt.title('是否复检')
plt.show()