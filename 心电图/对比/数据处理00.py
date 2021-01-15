
import xlsxwriter
import xlrd
import numpy as np
def import_excel_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]  # 获取第一个sheet表
    row = table.nrows  # 行数
    data_matrix = []
    for i in range(row):  # 对列进行遍历
        data_matrix.append(table.row_values(i))
    return data_matrix


def save(data,path):
    f = xlsxwriter.Workbook(path)  # 创建工作簿
    sheet1 = f.add_worksheet('sheet1')
    data = np.mat(data)
    [h,l] = data.shape# h为行数，l为列数
    for i in range(h):
        for j in range(l):
            sheet1.write(i, j, data[i,j])
    f.close()

path_train = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\train_lable_bp.xlsx'
path_test = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\test_label_bp.xlsx'

train_label = import_excel_matrix(path_train)
test_label = import_excel_matrix(path_test)

def class_lab(label):
    a = len(label[0])
    b = len(label)
    for i in range(b):
        for j in range(a):
            if label[i][j] == 1:
                label[i] = j
                break
    label = np.mat(label)
    label = label.T
    return label

out_train = class_lab(train_label)
out_test = class_lab(test_label)
path_outtest = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\test_label.xlsx'
path_outtrain = r'C:\Users\liuju\Documents\MATLAB\MIT_HIT\对比\train_label.xlsx'

save(out_train,path_outtrain)
save(out_test,path_outtest)