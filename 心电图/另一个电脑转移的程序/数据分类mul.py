import numpy as np
import xlsxwriter,xlrd


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



path_train = r'C:\Users\666\Desktop\mitdb\整理数据\训练数据集_mul.xlsx'
path_test = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集_mul.xlsx'

path_tn = r'C:\Users\666\Desktop\mitdb\整理数据\训练数据集_tn.xlsx'
path_tf = r'C:\Users\666\Desktop\mitdb\整理数据\训练数据集_tf.xlsx'
path_tv = r'C:\Users\666\Desktop\mitdb\整理数据\训练数据集_tv.xlsx'
path_tu = r'C:\Users\666\Desktop\mitdb\整理数据\训练数据集_tu.xlsx'
path_ts = r'C:\Users\666\Desktop\mitdb\整理数据\训练数据集_ts.xlsx'

path_cn = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集_cn.xlsx'
path_cf = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集_cf.xlsx'
path_cv = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集_cv.xlsx'
path_cu = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集_cu.xlsx'
path_cs = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集_cs.xlsx'



data_tn = import_excel_matrix(path_tn)
data_tf = import_excel_matrix(path_tf)
data_tv = import_excel_matrix(path_tv)
data_tu = import_excel_matrix(path_tu)
data_ts = import_excel_matrix(path_ts)


data_cn = import_excel_matrix(path_cn)
data_cf = import_excel_matrix(path_cf)
data_cv = import_excel_matrix(path_cv)
data_cu = import_excel_matrix(path_cu)
data_cs = import_excel_matrix(path_cs)


def mul(data_N,data_U,data_F,data_V,data_S):
    train_mul = []
    for i in range(len(data_N)):
        if i<len(data_N):
            train_mul.append(data_N[i])
        if i<len(data_U):
            train_mul.append(data_U[i])
        if i<len(data_F):
            train_mul.append(data_F[i])
        if i<len(data_V):
            train_mul.append(data_V[i])
        if i<len(data_S):
            train_mul.append(data_S[i])
    return train_mul

train_mul = mul(data_tn,data_tf,data_tv,data_tu,data_ts)
test_mul = mul(data_cn,data_cf,data_cv,data_cu,data_cs)

save(train_mul,path_train)
save(test_mul,path_test)