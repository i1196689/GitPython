import numpy as np
import math
import copy
from sklearn.decomposition import PCA





import pywt.data
import csv,math,xlwt
import xlsxwriter
import xlrd
import math

import xlrd,xlsxwriter
from bayes_opt import BayesianOptimization


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

path = r'C:\Users\liuju\Desktop\PNN_python-master\out111.xlsx'
path_out = r'C:\Users\liuju\Desktop\PNN_python-master\outout.xlsx'
data = import_excel_matrix(path)


def cal(i,j):
    i = i
    j = j

    num_w = (max(data[i][1],data[1][j]) - min(data[i][1],data[1][j]))/min(data[i][1],data[1][j])
    num_n = (max(data[i][2],data[2][j]) - min(data[i][2],data[2][j]))/min(data[i][2],data[2][j])
    num_z = max(data[i][3],data[3][j]) - min(data[i][3],data[3][j])
    if num_w <= 0.06 and num_n <= 0.08 :
        if num_z <=6000:
            out_num = 1
        else:
            out_num = 0
    else:
        out_num = 0
    return out_num

for i in range(306):
    for j in range(306):
        if i > 3 and j > 3:
            data[i][j] = cal(i,j)

save(data,path_out)


