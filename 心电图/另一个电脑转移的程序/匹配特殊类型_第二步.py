import xlsxwriter,xlrd
import numpy as np

num_ter = 234

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




