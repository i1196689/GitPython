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

path_0 = r'C:\Users\666\Desktop\mitdb\整理数据\训练数据集.xlsx'
path_1 = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集.xlsx'

# path_train = r'C:\Users\666\Desktop\mitdb\整理数据\训练数据集_mul.xlsx'
# path_test = r'C:\Users\666\Desktop\mitdb\整理数据\测试数据集_mul.xlsx'

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

data_0 = import_excel_matrix(path_0)
data_1 = import_excel_matrix(path_1)

def clas(data_0):
    data_N = []
    data_F = []
    data_U = []
    data_V = []
    data_S = []

    for num_0 in data_0:
        if num_0[10] == 'N':
            data_N.append(num_0)
        if num_0[10] == 'F':
            data_F.append(num_0)
        if num_0[10] == 'U':
            data_U.append(num_0)
        if num_0[10] == 'V':
            data_V.append(num_0) 
        if num_0[10] == 'S':
            data_S.append(num_0)

    # train_mul = []
    # for i in range(len(data_N)):
    #     if i<len(data_N):
    #         train_mul.append(data_N[i])
    #     if i<len(data_U):
    #         train_mul.append(data_U[i])
    #     if i<len(data_F):
    #         train_mul.append(data_F[i])
    #     if i<len(data_V):
    #         train_mul.append(data_V[i])
    # return train_mul
    return data_N, data_F, data_U, data_V,data_S

data_N, data_F, data_U, data_V,data_S = clas(data_0)

save(data_N,path_tn)
save(data_F,path_tf)
save(data_V,path_tv)
save(data_U,path_tu)
save(data_S,path_ts)

data_cN, data_cF, data_cU, data_cV,data_cS = clas(data_1)


save(data_cN,path_cn)
save(data_cF,path_cf)
save(data_cU,path_cu)
save(data_cV,path_cv)
save(data_cS,path_cs)