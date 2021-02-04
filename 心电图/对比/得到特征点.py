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



def save(data,path):
    f = xlsxwriter.Workbook(path)  # 创建工作簿
    sheet1 = f.add_worksheet('sheet1')  # 创建sheet
    l = len(data[0])
    h = len(data)  # h为行数，l为列数
    for i in range(h):
        for j in range(l):
            sheet1.write(i, j, data[i][j])
    f.close()


def import_excel_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]  # 获取第一个sheet表
    row = table.nrows  # 行数
    data_matrix = []
    for i in range(row):  # 对列进行遍历
        data_matrix.append(table.row_values(i))
    return data_matrix


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

list_1 = [i for i in range(260)]


def d_tran(list_1,data_v):
    list_2 = [i[1] for i in data_v]
    d = dict(zip(list_1,list_2))
    d = sorted(d.items(),key = lambda d:d[1])
    k_list = []
    for k in d:
        k_list.append(k[0])
    
    for i in range(260):
        data_v[i].append(k_list[i])
    save(data_v,r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\均值标准差\F.xlsx')
    return k_list

d = d_tran(list_1,data_f)
