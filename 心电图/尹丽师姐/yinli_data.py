import scipy.io
import numpy as np
import xlsxwriter
data_org = scipy.io.loadmat(r'C:\Users\liuju\Desktop\PNN_python-master\数据\vali_data1.mat') # 读取mat文件
data_orglab = scipy.io.loadmat(r'C:\Users\liuju\Desktop\PNN_python-master\数据\vali_label1.mat') # 读取mat文件
data = data_org['vali_data1']
label = data_orglab['vali_label1']
label = np.mat(label)
data = np.mat(data)
data = data.T
data_1 = np.zeros((1,260))
data_1 = np.mat(data_1)
data_2 = np.zeros((1,260))
data_2 = np.mat(data_2)
data_3 = np.zeros((1,260))
data_3 = np.mat(data_3)
data_4 = np.zeros((1,260))
data_4 = np.mat(data_4)
data_5 = np.zeros((1,260))
data_5 = np.mat(data_5)
[m,n] = data.shape
for i in range(m):
    if label[i,1] == 1:
        data_1 = np.row_stack((data_1,data[i,:]))
    elif label[i,2] == 1:
        data_2 = np.row_stack((data_2,data[i,:]))
    elif label[i,3] == 1:
        data_3 = np.row_stack((data_3,data[i,:]))
    elif label[i,4] == 1:
        data_4 = np.row_stack((data_4,data[i,:]))
    else:
        data_5 = np.row_stack((data_5,data[i,:]))
data_1 = np.delete(data_1,0,axis=0)
data_2 = np.delete(data_2,0,axis=0)
data_3 = np.delete(data_3,0,axis=0)
data_4 = np.delete(data_4,0,axis=0)
data_5 = np.delete(data_5,0,axis=0)
def save(data,path):
    data = np.mat(data)
    f = xlsxwriter.Workbook(path)  # 创建工作簿
    sheet1 = f.add_worksheet('sheet1')  # 创建sheet
    # l = len(data[0])
    # h = len(data)  # h为行数，l为列数
    [h,l] = data.shape
    for i in range(h):
        for j in range(l):
            # sheet1.write(i, j, data[i][j])
            sheet1.write(i, j, data[i,j])
    f.close()

save(data_1,r'C:\Users\liuju\Desktop\PNN_python-master\数据\分类\testdata_1.xlsx')
save(data_2,r'C:\Users\liuju\Desktop\PNN_python-master\数据\分类\testdata_2.xlsx')
save(data_3,r'C:\Users\liuju\Desktop\PNN_python-master\数据\分类\testdata_3.xlsx')
save(data_4,r'C:\Users\liuju\Desktop\PNN_python-master\数据\分类\testdata_4.xlsx')
save(data_5,r'C:\Users\liuju\Desktop\PNN_python-master\数据\分类\testdata_5.xlsx')

