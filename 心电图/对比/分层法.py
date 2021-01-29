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


path = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\最大最小归一化\已经处理\V.xlsx'


data = import_excel_matrix(path)
data = np.mat(data)

def cla_lay(data):
    out_list = []
    [m,n] = data.shape
    num_ind = int(m/9)
    for i in range(n):
        tem_list =data[:,i]
        tem_list = tem_list.tolist()
        tem_list.sort()
        stor_list = []
        for j in range(9):
            llist = []
            llist.extend(tem_list[j*num_ind])
            llist.extend(tem_list[(j+1)*num_ind])
            stor_list.append(llist)
        stor_list[-1][-1] = tem_list[-1][0]
        out_list.append(stor_list)
    
    return out_list


data = cla_lay(data)
for i in range(9):
    print(data[0][i][1]-data[0][i][0])

