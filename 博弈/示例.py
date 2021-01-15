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



def import_excel_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]  # 获取第一个sheet表
    row = table.nrows  # 行数
    col = table.ncols  # 列数
    data_matrix = np.zeros((row, col))  # 生成一个nrows行*ncols列的初始矩阵
    for i in range(col):  # 对列进行遍历
        cols = np.matrix(table.col_values(i))  # 把list转换为矩阵进行矩阵操作
        data_matrix[:, i] = cols  # 按列把数据存进矩阵中
    return data_matrix


def cal(matrix):
    size = matrix.shape
    out = np.zeros(shape=(size[0], size[0]))
    for i in range(size[0]):
        for j in range(size[0]):
            if i == j:
                out[i][j] = 1
            else:
                out[i][j] = 1 - 0.1 * (abs(matrix[i][0] - matrix[j][0]) + abs(matrix[i][1] - matrix[j][1]))
    return out


def data_save(data, path):
    f = xlwt.Workbook()  # 创建工作簿
    sheet1 = f.add_sheet('sheet1',cell_overwrite_ok=True)  # 创建sheet
    [h, l] = data.shape  # h为行数，l为列数
    for i in range(h):
        for j in range(l):
            sheet1.write(i, j, data[i, j])
    f.save(path)


data_file = r'C:\Users\liuju\Desktop\ooout.xls'  # Excel文件存储位置d
#path = r'C:\\Users\\666\\Desktop\\out.xls'  # Excel文件存储位置
#tra = np.array(import_excel_matrix(data_file))
#out = cal(tra)
#save(out, path)
#print(out)
data = import_excel_matrix(data_file)
data = data.tolist()
print(data)