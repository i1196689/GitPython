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


def pro(s):
    path_r = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\均值标准差\%s.xlsx'%(s)
    path_g = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\test\归一化\%s.xlsx'%(s)
    path_w = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\五种类别\train\均值标准差\主要特征提取\90特征点\%s.xlsx'%(s)
    data_r = import_excel_matrix(path_r)
    data_g = import_excel_matrix(path_g)
    new = [i[2] for i in data_r]
    new = new[0:80]
    data_w = []
    for i in range(len(data_g)):
        list_w = []
        for j in range(260):
            if j in new:
                list_w.append(data_g[i][j])
        data_w.append(list_w)
    save(data_w,path_w)
s = ['U','F','V','S','N']
for i in s:
    pro(i)
    print(i)
