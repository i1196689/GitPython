
import xlsxwriter,xlrd
import numpy as np

def import_excel_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]  # 获取第一个sheet表
    row = table.nrows  # 行数
    col = table.ncols  # 列数
    data_matrix = np.zeros((row, col))  # 生成一个nrows行*ncols列的初始矩阵
    for i in range(col):  # 对列进行遍历
        cols = np.matrix(table.col_values(i))  # 把list转换为矩阵进行矩阵操作
        data_matrix[:, i] = cols  # 按列把数据存进矩阵中
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



data = [[1,2,3],[4,5,6]]
file_name = r'C:\Users\666\Desktop\mitdb\100_00.xlsx'

save(data,file_name)
