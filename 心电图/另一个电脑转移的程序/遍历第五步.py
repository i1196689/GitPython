#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import codecs
import pywt
import pywt.data
import csv,math,xlwt
import xlsxwriter
import xlrd


file_name = [1,6,7,8,9,12,14,15,16,18,19,22,24,201,203,205,207,208,209,215,220,223,230,0,3,5,11,13,17,21,23,200,202,210,212,213,214,217,219,221,222,228,231,232,233,234]



for num_ter in file_name:


    def import_excel_matrix(path):
        table = xlrd.open_workbook(path).sheets()[0]  # 获取第一个sheet表
        row = table.nrows  # 行数
        data_matrix = []
        for i in range(row):  # 对列进行遍历
            data_matrix.append(table.row_values(i))
        return data_matrix

    def save(data,path):
        if type(data[0]) is int:
            tem =[]
            tem.append(data)
            tem.append(data)
            data = tem  
        f = xlsxwriter.Workbook(path)  # 创建工作簿
        sheet1 = f.add_worksheet('sheet1')  # 创建sheet
        if len(data[-1])!=len(data[0]):
            del data[-1]    
        l = len(data[0])
        h = len(data)  # h为行数，l为列数
    
        for i in range(h):
            for j in range(l):       
                sheet1.write(i, j, data[i][j])
        f.close()
    path_train = r'C:\Users\666\Desktop\mitdb\10%s\训练用数据_10%s.xlsx'%(num_ter, num_ter)
    path_loc = r'C:\Users\666\Desktop\mitdb\10%s\r峰坐标_10%s.xlsx'%(num_ter, num_ter)
    path_s_loc = r'C:\Users\666\Desktop\mitdb\10%s\特殊数据定位_10%s.xlsx'%(num_ter, num_ter)
    path_1 = r'C:\Users\666\Desktop\mitdb\10%s\训练用特殊数据定位_10%s.xlsx'%(num_ter, num_ter)
    path_2 = r'C:\Users\666\Desktop\mitdb\10%s\成熟数据_10%s.xlsx'%(num_ter, num_ter)


    data_1 = import_excel_matrix(path_train)
    data_2 = import_excel_matrix(path_1)

    logal = ['N','S','V','F','U']

    for i in range(len(data_1)):
        data_1[i].append('D')

    for men in data_2:
        if men[-1] < len(data_1):
            if men[1] in ['A','a','J','S']:
                data_1[int(men[-1])][-1] = 'S'
            elif men[1] in ['V','E']:
                data_1[int(men[-1])][-1] = 'V'
            elif men[1] == 'F':
                data_1[int(men[-1])][-1] = 'F'
            elif men[1] in  ['N','L','R','e','j']:
                data_1[int(men[-1])][-1] = 'N'
            elif men[1] in ['/','f','Q']:
                data_1[int(men[-1])][10] = 'U'

    data_3 = []
    for j in data_1:
        if j[-1] in logal:
            data_3.append(j)

    data_1 = data_3

    for i in range(len(data_1)):
        if data_1[i][-1] == 'N':
            data_1[i].extend([1,0,0,0,0])
        if data_1[i][-1] =="S":
            data_1[i].extend([0,1,0,0,0])
        if data_1[i][-1] =="V":
            data_1[i].extend([0,0,1,0,0])
        if data_1[i][-1] =="F":
            data_1[i].extend([0,0,0,1,0])
        if data_1[i][-1] =="U":
            data_1[i].extend([0,0,0,0,1])
    save(data_1,path_2)
    print('第五步处理结束。数据%s'%num_ter)

        
