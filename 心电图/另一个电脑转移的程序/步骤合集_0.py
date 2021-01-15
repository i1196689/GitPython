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


file_name = [200,201,202,203,205,207,208,209,210,212,213,214,215,219,220,221,222,223,228,230,233,234]

num_ter = 



with open(r'C:\Users\666\Documents\MATLAB\MIT_HIT\10%s\10%s.csv'%(num_ter,num_ter),'r') as csvfile:
    reader = csv.reader(csvfile)
    y = [row[0]for row in reader] #读取第1列

ecg = [float(i) for i in y] #将字符串转化为数字



mode = pywt.Modes.smooth


def plot_signal_decomp(data, w, title):
    """Decompose and plot a signal S.
    S = An + Dn + Dn-1 + ... + D1
    """
    w = pywt.Wavelet(w)#选取小波函数
    a = data
    ca = []#近似分量
    cd = []#细节分量
    for i in range(5):
        (a, d) = pywt.dwt(a, w, mode)#进行5阶离散小波变换
        ca.append(a)
        cd.append(d)

    rec_a = []
    rec_d = []

    for i, coeff in enumerate(ca):
        coeff_list = [coeff, None] + [None] * i
        rec_a.append(pywt.waverec(coeff_list, w))#重构

    for i, coeff in enumerate(cd):
        coeff_list = [None, coeff] + [None] * i
        if i ==3:
            print(len(coeff))
            print(len(coeff_list))
        rec_d.append(pywt.waverec(coeff_list, w))

    fig = plt.figure()
    ax_main = fig.add_subplot(len(rec_a) + 1, 1, 1)
    ax_main.set_title(title)
    ax_main.plot(data)
    ax_main.set_xlim(0, len(data) - 1)


    for i, y in enumerate(rec_a):
        ax = fig.add_subplot(len(rec_a) + 1, 2, 3 + i * 2)
        ax.plot(y, 'r')
        ax.set_xlim(0, len(y) - 1)
        ax.set_ylabel("A%d" % (i + 1))

    for i, y in enumerate(rec_d):
        ax = fig.add_subplot(len(rec_d) + 1, 2, 4 + i * 2)
        ax.plot(y, 'g')
        ax.set_xlim(0, len(y) - 1)
        ax.set_ylabel("D%d" % (i + 1))
    return rec_a[1]


def R_thd(aim,thd,s):#thd：阈值，s：规定的选取r的范围，% 如果两个坐标小于50可以判定只有一个是真正的r波
    n = 0
    out = []
    while n+s<len(aim):
        tem = aim[n:n+s]
        tem = list(tem)
        if max(tem) > thd and n+tem.index(max(tem)) not in out:
            out.append(n+tem.index(max(tem)))
        n = n +10
    las = aim[n-10:-1]
    if max(las) > thd :
        out.append(n-10+tem.index(max(tem)))
    out_m = [aim[i] for i in out]
    return out,out_m

def con(aim,aim_m,thd):#去掉间隔太近的假波峰
    r = []
    num = len(aim)
    if len(aim) > 1:
        for i in range(num - 1):
            if aim[i+1] - aim[i] < thd:
                if aim_m[i+1] > aim_m[i]:
                    r.append(aim[i])
                else:
                    r.append(aim[i+1])


    for j in r:
        if j in aim:
            aim.remove(j)
    return aim

def out_r(aim,new):#获得每个心拍
    out = []
    if aim[0]<=96:
        del aim[0]
    if len(new)-aim[-1]<164:
        del aim[-1]
    for i in aim:
        out.append(new[i-96:i+164])
    return out
    

f = codecs.open(r'C:\Users\666\Desktop\mitdb\10%s\10%s.txt'%(num_ter,num_ter), mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
line = f.readline()   # 以行的形式进行读取文件
list1 = []
while line:
    a = line.split()
    b = a[1:3]   # 这是选取需要读取的位数
    
    list1.append(b)  # 将其添加在列表之中
    line = f.readline()
f.close()

del list1[0:2] #各类心律失常的坐标

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
    print('文件处理结束。')

new = plot_signal_decomp(ecg, 'sym5', "DWT: Ecg sample - Symmlets5")



out,out_m = R_thd(new,0.3,60)

out = con(out,out_m,200)#波波峰对应的坐标

out_m = [new[i] for i in out]#r波波峰

r_loc = out_r(out,new)

#plt.show()
file_name = r'C:\Users\666\Desktop\mitdb\10%s\心拍数据_10%s.xlsx'%(num_ter, num_ter)
file_name_t = r'C:\Users\666\Desktop\mitdb\10%s\特殊数据_10%s.xlsx'%(num_ter, num_ter)
file_name_loc = r'C:\Users\666\Desktop\mitdb\10%s\r峰坐标_10%s.xlsx'%(num_ter, num_ter)
save(r_loc,file_name)
save(list1,file_name_t)
save(out,file_name_loc)
print('第一步结束。数据%s'%(num_ter))



######################################
######################################
######################################

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
path_loc = r'C:\Users\666\Desktop\mitdb\10%s\r峰坐标_10%s.xlsx'%(num_ter, num_ter)
path_p = r'C:\Users\666\Desktop\mitdb\10%s\心拍数据_10%s.xlsx'%(num_ter, num_ter)
path_t = r'C:\Users\666\Desktop\mitdb\10%s\特殊数据_10%s.xlsx'%(num_ter, num_ter)

path_s_loc = r'C:\Users\666\Desktop\mitdb\10%s\特殊数据定位_10%s.xlsx'%(num_ter, num_ter)



loc_100 = import_excel_matrix(path_loc)
t_100 = import_excel_matrix(path_t)


for e in loc_100[0]:
    for t in range(len(t_100)):
        if e-95<=int(t_100[t][0])<=e+165:
            t_100[t].append(e)
            while len(t_100[t])>3:
                del t_100[t][-1]
                
            break
t_100 = [g for g in t_100 if len(g)==3]
    
save(t_100,path_s_loc)
print('第二步结束。数据%s'%(num_ter))


##########################################
##########################################
##########################################


def pearson(vector1, vector2):
    n = len(vector1)
    #simple sums
    sum1 = sum(float(vector1[i]) for i in range(n))
    sum2 = sum(float(vector2[i]) for i in range(n))
    #sum up the squares
    sum1_pow = sum([pow(v, 2.0) for v in vector1])
    sum2_pow = sum([pow(v, 2.0) for v in vector2])
    #sum up the products
    p_sum = sum([vector1[i]*vector2[i] for i in range(n)])
    #分子num，分母den
    num = p_sum - (sum1*sum2/n)

    den = math.sqrt(abs((sum1_pow-pow(sum1, 2)/n)*(sum2_pow-pow(sum2, 2)/n)))
    if den == 0:
        return 0.0
    return num/den



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



path_p = r'C:\Users\666\Desktop\mitdb\10%s\心拍数据_10%s.xlsx'%(num_ter, num_ter)
path_train = r'C:\Users\666\Desktop\mitdb\10%s\训练用数据_10%s.xlsx'%(num_ter, num_ter)
loc_100 = import_excel_matrix(path_p)

name = ['name_%s'%i for i in range(10)]

con = [i for i in range(26)]
out = []
for j in range(len(loc_100)):
    for i in range(10):
        name[i] = loc_100[j][i*26:(i+1)*26]
    per = [pearson(name[i],con) for i in range(10)]
    out.append(per)

save(out,path_train)
print('第三步结束。数据%s'%(num_ter))



############################################
################################################
##################################################




path_train = r'C:\Users\666\Desktop\mitdb\10%s\训练用数据_10%s.xlsx'%(num_ter, num_ter)
path_loc = r'C:\Users\666\Desktop\mitdb\10%s\r峰坐标_10%s.xlsx'%(num_ter, num_ter)
path_s_loc = r'C:\Users\666\Desktop\mitdb\10%s\特殊数据定位_10%s.xlsx'%(num_ter, num_ter)
path_1 = r'C:\Users\666\Desktop\mitdb\10%s\训练用特殊数据定位_10%s.xlsx'%(num_ter, num_ter)
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
    print('文件处理结束。')

data_1 = import_excel_matrix(path_s_loc)
data_2 = import_excel_matrix(path_loc)
data_2 = data_2[0]
for men in data_1:
    num = data_2.index(men[2])

    men.append(num)
save(data_1,path_1)
print('第四步结束。数据%s'%num_ter)


###########################################
#############################################
#############################################







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
        if men[1] == 'S':
            data_1[int(men[-1])][-1] = 'S'
        elif men[1] == 'V':
            data_1[int(men[-1])][-1] = 'V'
        elif men[1] == 'F':
            data_1[int(men[-1])][-1] = 'F'
        elif men[1] == 'N':
            data_1[int(men[-1])][-1] = 'N'
        else:
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

    
