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


def import_excel_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]  # 获取第一个sheet表
    row = table.nrows  # 行数
    data_matrix = []
    for i in range(row):  # 对列进行遍历
        data_matrix.append(table.row_values(i))
    data_matrix = np.mat(data_matrix)
    return data_matrix

def save(data,path):

    f = xlsxwriter.Workbook(path)  # 创建工作簿
    sheet1 = f.add_worksheet('sheet1')  # 创建sheet
    # l = len(data[0])
    # h = len(data)  # h为行数，l为列数
    [h,l] = data.shape
    for i in range(h):
        for j in range(l):
            # sheet1.write(i, j, data[i][j])
            sheet1.write(i, j, data[i,j])
    f.close()


path_0 = r'C:\Users\liuju\Desktop\PNN_python-master\数据\分类\testdata_0.xlsx'
path_1 = r'C:\Users\liuju\Desktop\PNN_python-master\数据\分类\testdata_1.xlsx'
path_2 = r'C:\Users\liuju\Desktop\PNN_python-master\数据\分类\testdata_2.xlsx'
path_3 = r'C:\Users\liuju\Desktop\PNN_python-master\数据\分类\testdata_3.xlsx'
path_4 = r'C:\Users\liuju\Desktop\PNN_python-master\数据\分类\testdata_4.xlsx'
path = r'C:\Users\liuju\Desktop\PNN_python-master\数据\分类\testdata.xlsx'

data_0 = import_excel_matrix(path_0)
data_1 = import_excel_matrix(path_1)
data_2 = import_excel_matrix(path_2)
data_3 = import_excel_matrix(path_3)
data_4 = import_excel_matrix(path_4)
data = np.zeros((1,260))
data = np.mat(data)
label = []
for i in range(1000):
    if i < len(data_0):
        data = np.row_stack((data,data_0[i,:]))
        label.append(0)
    if i < len(data_1):
        data = np.row_stack((data,data_1[i,:]))
        label.append(1)
    if i < len(data_2):
        data = np.row_stack((data,data_2[i,:]))
        label.append(2)
    if i < len(data_3):
        data = np.row_stack((data,data_3[i,:]))
        label.append(3)
    if i < len(data_4):
        data = np.row_stack((data,data_4[i,:]))
        label.append(4)    
data = np.delete(data,0,axis=0)
label = np.mat(label)
label = label.T
save(data,path)
save(label,r'C:\Users\liuju\Desktop\PNN_python-master\数据\分类\testlabel_data.xlsx')