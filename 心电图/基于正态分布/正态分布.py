# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:21:13 2018

@author: lj
"""
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

from scipy import stats





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

#path_train = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\整理数据\\short_train.xlsx'
path_test = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\整理数据\\short_test.xlsx'
# path_trainlab = r'C:\Users\666\Documents\MATLAB\MIT_HIT\整理数据\train_lab-f.xlsx'
# path_testlab = r'C:\Users\666\Documents\MATLAB\MIT_HIT\整理数据\test_lab-f.xlsx'
path_train = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\GA_BP\训练数据\data_N.xlsx'


data_train = import_excel_matrix(path_train)

def t_mean(data):
    for i in data:
        s = sum(data[i])/len(260)
        for j in range(260):
            if s > 0 :
                data[i][j] = data[i][j] - s
            else:
                data[i][j] = data[i][j] + s

    return data





tar_data = [i[0] for i in data_train[0:3000]]

print(tar_data[0:10])
tar_data = np.array(tar_data)
s = stats.kstest(tar_data,mode='norm',args=(tar_data.mean(),tar_data.std()))
print(s)

#args=(tar_data.mean(),tar_data.std())