import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei']
xls_file = pd.read_excel(r'C:\Users\liuju\Desktop\2017-2019食品抽检数据汇总\2019年食品数据\2019年直报系统食用农产品.xlsx')

group = xls_file.loc[:,'抽样时间'].value_counts()
group.to_excel(r'C:\Users\liuju\Desktop\2019.xlsx')