import xlrd
import  matplotlib.pyplot as plt

file_name = [100,101,103,105,106,107,108,1012,1013,1014,1015,1016,1017,1018,1019,1021,1022,1023,1024,10200,10201,10202,10203,10205,10207,10208,10209,10210,10212,10213,10214,10215,10219,10220,10221,10222,10223,10228,10230,10233,10234]
file_name_0 = [5,6,7,8,12,13,14,15,16,17,18,19,21,22,23,24,200,201,202,203,205,207,208,209,210,212,213,214,215,219,220,221,222,223,228,230,233,234]

def import_excel_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]  # 获取第一个sheet表
    row = table.nrows  # 行数
    data_matrix = []
    for i in range(row):  # 对列进行遍历
        data_matrix.append(table.row_values(i))
    return data_matrix

def  create(num):
    path = r'C:\Users\666\Desktop\mitdb\%s\心拍数据_%s.xlsx'%(num,num)
    return path

path = [create(num) for num in file_name]
for pat in path:
    matr = import_excel_matrix(pat)
    plt.plot(matr[10])
    plt.show()