import xlsxwriter,xlrd

num_ter = 234

path_train = r'C:\Users\666\Desktop\mitdb\10%s\训练用数据_10%s.xlsx'%(num_ter, num_ter)
path_loc = r'C:\Users\666\Desktop\mitdb\10%s\r峰坐标_10%s.xlsx'%(num_ter, num_ter)
path_s_loc = r'C:\Users\666\Desktop\mitdb\10%s\特殊数据定位_10%s.xlsx'%(num_ter, num_ter)
path_1 = r'C:\Users\666\Desktop\mitdb\10%s\训练用特殊数据定位_10%s.xlsx'%(num_ter, num_ter)
def import_excel_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]  # 获取第一个sheet表
    row = table.nrows  # 行数
    data_matrix = []
    for i in range(row):  # 对列进行遍历
        data_matrix.append(table.row_values(i))
    return data_matrix

def save(data,path):
    if type(data[0]) is int:
      tem =[]
      tem.append(data)
      tem.append(data)
      data = tem  
    f = xlsxwriter.Workbook(path)  # 创建工作簿
    sheet1 = f.add_worksheet('sheet1')  # 创建sheet
    if len(data[-1])!=len(data[0]):
      del data[-1]    
    l = len(data[0])
    h = len(data)  # h为行数，l为列数
  
    for i in range(h):
      for j in range(l):       
        sheet1.write(i, j, data[i][j])
    f.close()
    print('文件处理结束。')

data_1 = import_excel_matrix(path_s_loc)
data_2 = import_excel_matrix(path_loc)
data_2 = data_2[0]
for men in data_1:
    num = data_2.index(men[2])

    men.append(num)
save(data_1,path_1)
print('第四步结束。数据%s'%num_ter)