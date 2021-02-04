
import numpy as np

from sklearn.decomposition import PCA
import pywt
import pywt.data
import csv,math,xlwt
import xlsxwriter
import xlrd
import math
import random
import xlrd,xlsxwriter
import copy

import matplotlib.pyplot as plt
def import_excel_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]  # 获取第一个sheet表
    row = table.nrows  # 行数
    data_matrix = []
    for i in range(row):  # 对列进行遍历
        data_matrix.append(table.row_values(i))
    return data_matrix

def save(data,path):
    f = xlsxwriter.Workbook(path)  # 创建工作簿
    sheet1 = f.add_worksheet('sheet1')  # 创建sheet
    l = len(data[0])
    h = len(data)  # h为行数，l为列数
    for i in range(h):
        for j in range(l):
            sheet1.write(i, j, data[i][j])
    f.close()

def t_pac(data,r):
    
    data = np.array(data)
   
    pca = PCA(n_components=r)
    data = pca.fit(data).transform(data)
    print('各主成分贡献度:{}'.format(pca.explained_variance_ratio_))
    
    return data

path_v = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\归一化\V.xlsx'
path_s = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\归一化\S.xlsx'

# path_vv = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\均值标准差\V.xlsx'
# path_ss = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\均值标准差\S.xlsx'

# data_vv = import_excel_matrix(path_vv)
# data_ss = import_excel_matrix(path_ss)


data_v = import_excel_matrix(path_v)
data_s = import_excel_matrix(path_s)

data_v = np.array(data_v)
data_s = np.array(data_s)

# list_s = [i[2] for i in data_ss]
# list_v = [i[2] for i in data_vv]

# list_s = list_s[0:10]
# list_v = list_v[0:10]
# list_s.sort()
# list_v.sort()

# def newdata(data,list_new):
#     data_new = []
#     for i in range(len(data)):
#         list_a = []
#         for k in list_new:
#             list_a.append(data[i][int(k)])
#         data_new.append(list_a)    
#     return data_new

# data_v = newdata(data_v,list_v)
# data_s = newdata(data_s,list_s)


# data_v = t_pac(data_v,2)
# print(data_v)

# data_s = t_pac(data_s,2)

plt.figure()
plt.scatter(data_v[:, 1], data_v[:, 2],c='#00CED1',alpha=.8)#红
plt.scatter(data_s[:, 1], data_s[:, 2],c='#DC143C',alpha=.8)
plt.show()