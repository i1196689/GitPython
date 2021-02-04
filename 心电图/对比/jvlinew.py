import numpy as np
import math
import copy
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt

from bayes_opt import BayesianOptimization

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


# def save(data,path):
#     f = xlsxwriter.Workbook(path)  # 创建工作簿
#     sheet1 = f.add_worksheet('sheet1')  # 创建sheet
#     l = len(data[0])
#     h = len(data)  # h为行数，l为列数
#     for i in range(h):
#         for j in range(l):
#             sheet1.write(i, j, data[i][j])
#     f.close()


path_v = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\均值标准差\V.xlsx'
path_s = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\均值标准差\S.xlsx'
path_n = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\均值标准差\N.xlsx'
path_u = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\均值标准差\U.xlsx'
path_f = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\均值标准差\F.xlsx'


data_v = import_excel_matrix(path_v)
data_s = import_excel_matrix(path_s)
data_n = import_excel_matrix(path_n)
data_u = import_excel_matrix(path_u)
data_f = import_excel_matrix(path_f)

path = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\test\归一化\F.xlsx'

data = import_excel_matrix(path)

print('数据导入结束。开始计算...')
def get_num(s):    
    out_v = []
    out_s = []
    out_n = []
    out_u = []
    out_f = []
    for j in range(260):
        out_v.append(abs(s[j] - data_v[j][0])/data_v[j][1]) 
        out_s.append(abs(s[j] - data_s[j][0])/data_s[j][1])
        out_n.append(abs(s[j] - data_n[j][0])/data_n[j][1])
        out_u.append(abs(s[j] - data_u[j][0])/data_u[j][1])
        out_f.append(abs(s[j] - data_f[j][0])/data_f[j][1])
    
    out_v = [abs(i-np.mean(out_v)) for i in out_v]
    out_s = [abs(i-np.mean(out_s)) for i in out_s]
    out_n = [abs(i-np.mean(out_n)) for i in out_n]
    out_u = [abs(i-np.mean(out_u)) for i in out_u]
    out_f = [abs(i-np.mean(out_f)) for i in out_f]

    s = [sum(out_v),sum(out_s),sum(out_n),sum(out_u),sum(out_f)]  
    return s
num = 0
for e_list in data:
    s = get_num(e_list)
    if s[3] == min(s):
        num = num + 1
    
print(num/len(data))

