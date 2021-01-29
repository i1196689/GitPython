import numpy as np
import math
import copy
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt



import pywt.data
import csv,math,xlwt
import xlsxwriter
import xlrd
import math

import xlrd,xlsxwriter



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

path = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\最大最小归一化\V.xlsx'
path_s = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\最大最小归一化\已经处理\V.xlsx'

data = import_excel_matrix(path)

m = len(data)
n = len(data[0])

for i in range(m):
    num_min = min(data[i])
    num_max = max(data[i])
        
    for j in range(n):
        data[i][j] = (data[i][j] - num_min)/(num_max - num_min)
    

    


save(data,path_s)

plt.plot(data[0])
plt.show()
print(data[0][-1])