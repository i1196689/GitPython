import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei']
xls_file = pd.read_excel(r'C:\Users\liuju\Desktop\2017-2019食品抽检数据汇总\2018年食品数据\2018年农产品直报系统.xls')

group = xls_file.loc[:,'月份'].value_counts()
group.name = ''
group = pd.DataFrame(group)

group.plot.box(patch_artist=True)
plt.title('抽样月份')
plt.show()

print(group)
