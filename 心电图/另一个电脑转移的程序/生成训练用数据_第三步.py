import math
import xlsxwriter,xlrd
import numpy as np

num_ter = 200
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