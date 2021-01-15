import numpy as np
import xlrd, xlwt, math


T1 = [-0.05,0,0.05]
T2 = [-0.05,0,0.05]
T3 = [0,0.1,0.2]
T4 = [0,0.025,0.05]
T7 = [-0.05,0,0.05]
T8 = [-0.1,0,0.1]
T9 = [0,0.05,0.1]
T10 = [-0.025,0,0.025]
T11 = [-0.05,0,0.05]
T12 = [-0.1,-0.05,0]



def import_excel_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]  # 获取第一个sheet表
    row = table.nrows  # 行数
    col = table.ncols  # 列数
    data_matrix = np.zeros((row, col))  # 生成一个nrows行*ncols列的初始矩阵
    for i in range(col):  # 对列进行遍历
        cols = np.matrix(table.col_values(i))  # 把list转换为矩阵进行矩阵操作
        data_matrix[:, i] = cols  # 按列把数据存进矩阵中
    return data_matrix





def save(data, path):
    f = xlwt.Workbook()  # 创建工作簿
    sheet1 = f.add_sheet('sheet1',cell_overwrite_ok=True)  # 创建sheet
    l = len(data[0])
    h = len(data)  # h为行数，l为列数
    for i in range(h):
        for j in range(l):
            if i>3 and j>5:
                sheet1.write(i, j, "(%s,%s)"%(round(data[i][j][1],4),round(data[i][j][0],4)))
            else:
                sheet1.write(i, j, round(data[i][j],4))
    f.save(path)

data_file = r'C:\Users\liuju\Desktop\ooout.xls'  # Excel文件存储位置d

data = import_excel_matrix(data_file)
data = data.tolist()

m,n = len(data),len(data[0])

min_T0 = T1[0] + T2[0] + T3[0] + T4[0] + T7[0] + T8[0] + T9[0] +T10[0] + T11[0] + T12[0]
min_C = math.exp(-0.1*T1[2]) + math.exp(-0.1*T2[2]) +math.exp(-0.2*T3[2]) +math.exp(-0.2*T4[2]) +math.exp(-0.3*T7[2]) +math.exp(-0.3*T8[2]) +math.exp(-0.4*T9[2]) +math.exp(-0.4*T10[2])+math.exp(-0.5*T11[2])+math.exp(-0.5*T12[2])
for i in range(m-4):
    for j in range(n-6):
        T0 = data[i+4][0] + data[i+4][1] + data[i+4][2] +data[i+4][3] +data[i+4][4] +data[i+4][5] +data[0][j+6] +data[1][j+6]+data[2][j+6]+data[3][j+6]
        C = math.exp(-0.1*data[i+4][0]) + math.exp(-0.1*data[i+4][1]) +math.exp(-0.2*data[i+4][2]) +math.exp(-0.3*data[i+4][3]) +math.exp(-0.3*data[i+4][4]) +math.exp(-0.5*data[i+4][5])   +math.exp(-0.2*data[0][j+6]) +math.exp(-0.4*data[1][j+6])+math.exp(-0.4*data[2][j+6])+math.exp(-0.5*data[3][j+6])
        data[i+4][j+6] = (T0/min_T0,C/min_C)


path = r'C:\\Users\\liuju\\Desktop\\out.xls'  # Excel文件存储位置
save(data,path)