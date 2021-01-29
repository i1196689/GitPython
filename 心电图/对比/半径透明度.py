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


path_v = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\最大最小归一化\已经处理\V.xlsx'
path_s = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\最大最小归一化\已经处理\S.xlsx'

data_v = import_excel_matrix(path_v)
data_s = import_excel_matrix(path_s)


def get_num(data,s,r = 0.05):
    data = np.mat(data)    
    [m,n] = data.shape
    lev = int(m/(1/(2*r)))
    
    out = []
    for i in range(n):
        num_down = s[i] - 0.05
        num_up = s[i] + 0.05

        dia = [num_down,num_up]
        if num_down <= 0 :
            num_down = 0
        if num_up >= 1:
            num_up = 1
        if num_down == 0:
            dia = [0,0.1]
        if num_up == 1:
            dia = [0.9,1]
        num = 0
        for j in range(m):
            meta = data[j,i]
            if dia[0] <= meta <=  dia[1] :
                num = num + 1
        out.append(num)
    for t in range(len(out)):
        # if out[t] >= lev:
        #     out[t] = 1
        # else:
        #     out[t] = 0     
        out[t] = out[t]/lev  
    return sum(out)
# s_v = data_v[0]


rate = 0
for i in range(len(data_s)):
    s_s = data_s[i]
    out_1 = get_num(data_s,s_s)
    out_2 = get_num(data_v,s_s)
    if out_1 > out_2:
        rate = rate + 1

print(rate/len(data_s))

