import numpy as np
import xlrd, xlwt

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

data = []
for t3 in T3:
    for t9 in T9:
        for t10 in T10:
            for t12 in T12:
                data.append([t3,t9,t10,t12])





def save(data, path):
    f = xlwt.Workbook()  # 创建工作簿
    sheet1 = f.add_sheet('sheet1',cell_overwrite_ok=True)  # 创建sheet
    l = len(data[0])
    h = len(data)  # h为行数，l为列数
    for i in range(h):
        for j in range(l):
            sheet1.write(i, j, data[i][j])
    f.save(path)



path = r'C:\\Users\\liuju\\Desktop\\lie.xls'  # Excel文件存储位置

save(data,path)