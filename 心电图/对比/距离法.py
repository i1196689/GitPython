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


def save(data,path):
    f = xlsxwriter.Workbook(path)  # 创建工作簿
    sheet1 = f.add_worksheet('sheet1')  # 创建sheet
    l = len(data[0])
    h = len(data)  # h为行数，l为列数
    for i in range(h):
        for j in range(l):
            sheet1.write(i, j, data[i][j])
    f.close()


path_v = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\归一化\V.xlsx'
path_s = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\归一化\S.xlsx'
path_n = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\归一化\N.xlsx'
path_u = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\归一化\U.xlsx'
path_f = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\归一化\F.xlsx'


path_ts = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\test\归一化\S.xlsx'

data_v = import_excel_matrix(path_v)
data_s = import_excel_matrix(path_s)
data_n = import_excel_matrix(path_n)
data_u = import_excel_matrix(path_u)
data_f = import_excel_matrix(path_f)

data_ts = import_excel_matrix(path_ts)

print('数据导入结束。开始计算...')
def get_num(data,s):
    data = np.mat(data)    
    [m,n] = data.shape
    
    out = []
    for i in range(n):
        tem_m = data[:,i]
        num = tem_m - s[i]
        num = list(map(abs,num))
        num = sum(num)/m       
        out.append(num)

    return sum(out),out


# def start_train():
#     rate = 0
#     data_sect = data_ts
#     for i in range(len(data_sect)):
#         s_s = data_sect[i]
#         out_1 = get_num(data_s,s_s)
#         out_2 = get_num(data_v,s_s)
#         out_3 = get_num(data_n,s_s)
#         out_4 = get_num(data_u,s_s)
#         out_5 = get_num(data_f,s_s)

#         if out_1 == min([out_1,out_2,out_3,out_4,out_5]):
#             rate = rate + 1
#     print(rate/len(data_sect))

#     return rate/len(data_sect)
# s = start_train()
# print(s)



data_sect = data_ts

s_s = data_sect[0]
out_1,list_1 = get_num(data_s,s_s)
out_2,list_2 = get_num(data_v,s_s)
out_3,list_3 = get_num(data_n,s_s)
out_4,list_4 = get_num(data_u,s_s)
out_5,list_5 = get_num(data_f,s_s)

out = [out_1,out_2,out_3,out_4,out_5]
print(out)

    # if out_1 == min([out_1,out_2,out_3,out_4,out_5]):
    #     rate = rate + 1
    # print('已经计算%s'%(i/len(data_sect)))
# print(rate/len(data_sect))
path_1 = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\list_1.xlsx'
path_2 = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\list_2.xlsx'
path_3 = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\list_3.xlsx'
path_4 = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\list_4.xlsx'
path_5 = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\list_5.xlsx'
save(list_1,path_1)
save(list_2,path_2)
save(list_3,path_3)
save(list_4,path_4)
save(list_5,path_5)