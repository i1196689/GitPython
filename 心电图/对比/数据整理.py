import numpy as np
import matplotlib.pyplot as plt
import codecs
import pywt
import pywt.data
import csv,math,xlwt
import xlsxwriter
import xlrd


#file_name = [1,6,7,8,9,12,14,15,16,18,19,22,24,201,203,205,207,208,209,215,220,223,230]
file_name = [0,3,5,11,13,17,21,23,200,202,210,212,213,214,217,219,221,222,228,231,232,233,234]

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

#path_test = r'C:\Users\666\Documents\MATLAB\MIT_HIT\整理数据\test合集.xlsx'
path_train = r'C:\Users\666\Documents\MATLAB\MIT_HIT\整理数据\train合集.xlsx'
path = r'C:\Users\666\Documents\MATLAB\MIT_HIT\整理数据\train已处理.xlsx'
path_lab = r'C:\Users\666\Documents\MATLAB\MIT_HIT\整理数据\train_lab.xlsx'


data = import_excel_matrix(path_train)
test_lab = []

log_N = [1,0,0,0,0]
log_S = [0,1,0,0,0]
log_V = [0,0,1,0,0]
log_F = [0,0,0,1,0]
lgo_U = [0,0,0,0,1]

data_n = []
data_s = []
data_v = []
data_f = []
data_u = []

for men in data:
    if men[261] in ['A','a','J','S']:
        men.append('S')
        men.extend(log_S)
        data_s.append(men)
        
    elif men[261] in ['V','E']:
        men.append('V')
        men.extend(log_V)
        data_v.append(men)
        
    elif men[261] == 'F':
        men.append('F')
        men.extend(log_F)
        data_f.append(men)
        
    elif men[261] in  ['N','L','R','e','j']:
        men.append('N')
        men.extend(log_N)
        data_n.append(men)
        
    elif men[261] in ['/','f','Q']:
        men.append('U')
        men.extend(lgo_U)
        data_u.append(men)
        
    else:
        data.remove(men)
    



max_nun = max(len(data_f),len(data_u),len(data_n),len(data_v),len(data_s))
mul = []
for i in range(max_nun):
    if i < len(data_n):
        mul.append(data_n[i])
        test_lab.append(log_N)
    if i < len(data_v):
        mul.append(data_v[i])
        test_lab.append(log_V)
    if i < len(data_s):
        mul.append(data_s[i])
        test_lab.append(log_S)
    if i < len(data_f):
        mul.append(data_f[i])
        test_lab.append(log_F)
    if i < len(data_u):
        mul.append(data_u[i])
        test_lab.append(lgo_U)

save(mul,path)
save(test_lab,path_lab)