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



# log_N = [1,0,0,0,0]
# log_S = [0,1,0,0,0]
# log_V = [0,0,1,0,0]
# log_F = [0,0,0,1,0]
# lgo_U = [0,0,0,0,1]

# data_N = ['N']
# data_PB = ['/']
# data_L = ['L']
# data_R = ['R']
# data_PVC = ['V']
# data_APB = ['A']
data_N = []
data_PB = []
data_L = []
data_R = []
data_PVC = []
data_APB = []
for i in file_name:
    path = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\10%s\心拍数据.xlsx'%(i)
    data = import_excel_matrix(path)
    for E_list in data:
        if E_list[261] == 'N':
            data_N.append(E_list[0:260])
        if E_list[261] == '/':
            data_PB.append(E_list[0:260])
        if E_list[261] == 'L':
            data_L.append(E_list[0:260])
        if E_list[261] == 'R':
            data_R.append(E_list[0:260])
        if E_list[261] == 'V':
            data_PVC.append(E_list[0:260])
        if E_list[261] == 'A':
            data_APB.append(E_list[0:260])


path_GABP_N = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\GA_BP\测试数据\data_N.xlsx'
path_GABP_PB = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\GA_BP\测试数据\data_PB.xlsx'
path_GABP_L = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\GA_BP\测试数据\data_L.xlsx'
path_GABP_R = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\GA_BP\测试数据\data_R.xlsx'
path_GABP_PVC = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\GA_BP\测试数据\data_PVC.xlsx'
path_GABP_APB = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\GA_BP\测试数据\data_APB.xlsx'





save(data_N,path_GABP_N)
save(data_PB,path_GABP_PB)
save(data_L,path_GABP_L)
save(data_R,path_GABP_R)
save(data_PVC,path_GABP_PVC)
save(data_APB,path_GABP_APB)        





