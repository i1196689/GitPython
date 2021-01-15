import numpy as np
import matplotlib.pyplot as plt
import codecs
import pywt
import pywt.data
import csv,math,xlwt
import xlsxwriter
import xlrd


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


path_train = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\整理数据\train已处理.xlsx'
path =r'C:\Users\liuju\Desktop\PNN_python-master\N.xlsx'
data = import_excel_matrix(path_train)
num_n = 0
num_L = 0
num_r = 0
num_e = 0
num_j = 0
out = []
for e_list in data:
    if e_list[261] == 'N' and num_n < 401:
        out.append(e_list)
        num_n = num_n + 1
    if e_list[261] == 'L' and num_L < 401:
        out.append(e_list)
        num_L = num_L + 1
    if e_list[261] == 'R' and num_r < 401:
        out.append(e_list)
        num_r = num_r + 1
    if e_list[261] == 'e' and num_e < 201:
        out.append(e_list)
        num_e = num_e + 1
    if e_list[261] == 'j' and num_j < 201:
        out.append(e_list)
        num_j = num_j + 1   

save(out,path)