import xlrd,xlsxwriter
from xlutils.copy import copy
s = []
for n in range(303):
    if n>4:
        st = ['=IF(AND((MAX(E2,$B$%s)-MIN(E2,$B$%s))/MIN(E2,$B$%s)<=0.06,(MAX(E3,$C$%s)-MIN(E3,$C$%s))/MIN(E3,$C$%s)<=0.06,MAX(E4,$D$%s)-MIN(E4,$D$%s)<=6000),1,0)'%(n,n,n,n,n,n,n,n)]
        s.append(st)



def save(data,path):
    f = xlsxwriter.Workbook(path)  # 创建工作簿
    sheet1 = f.add_worksheet('sheet1')  # 创建sheet
    l = len(data[0])
    h = len(data)  # h为行数，l为列数
    for i in range(h):
        for j in range(l):
            sheet1.write(i+4, j+4, data[i][j])
    f.close()

path = r'C:\Users\liuju\Desktop\PNN_python-master\out111.xlsx'
save(s,path)