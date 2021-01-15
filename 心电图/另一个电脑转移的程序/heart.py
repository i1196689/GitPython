import wfdb
from wfdb import processing
import numpy as np
import matplotlib.pyplot as plt

import pywt
import pywt.data
import csv,math,xlwt
import xlsxwriter
import xlrd

#file_name = [1,6,7,8,9,12,14,15,16,18,19,22,24,201,203,205,207,208,209,215,220,223,230,0,3,5,11,13,17,21,23,200,202,210,212,213,214,217,219,221,222,228,231,232,233,234]

file_name = [0]
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

for num_iter in file_name:
    with open(r'C:\Users\666\Documents\MATLAB\MIT_HIT\10%s\10%s.csv'%(num_iter,num_iter),'r') as csvfile:
        reader = csv.reader(csvfile)
        y = [row[0]for row in reader] #读取第1列

    record =np.array([float(i) for i in y])  #将字符串转化为数字
    min_bpm = 20
    max_bpm = 230
    search_rad = int(360*60/max_bpm)
    qrs_inds=processing.gqrs_detect(sig=record, fs=360)
    corrected_peak_inds=list(processing.correct_peaks(record, peak_inds=qrs_inds, search_radius=search_rad, smooth_window_size=150))

    
    while corrected_peak_inds[0] < 95:
        del corrected_peak_inds[0]
    while corrected_peak_inds[-1]+165 > len(record):
        del corrected_peak_inds[-1]

    h_mtx = []


    for num in corrected_peak_inds:
        h_mtx.append(list(record[num-95:num+165]))
        h_mtx[-1].append(num)
    
    

    path = r'C:\Users\666\Documents\MATLAB\MIT_HIT\10%s\心拍数据.xlsx'%(num_iter)
    save(h_mtx,path)
    print('数据10%s处理结束...'%(num_iter))