import math
import collections
from typing import Counter
import xlsxwriter

name_id = [27,18,13,8,24,15,25,3,6,17,11,2,12,1,23,5,16,19,4,28,26,14,20,7,10,21,9,22]
num = [276460,275880,275840,275140,275080,274100,273760,276260,276120,275760,275300,274780,274300,273380,276460,276100,275760,275180,275040,274120,273580,276180,276120,275660,275420,274840,274960,272860]
dict_0 = dict(zip(name_id,num))
dict_1 = dict(zip(num,name_id))
num.sort(reverse=True)

part_0 = []
part_1 = []
part_2 = []
part_3 = []

for i in range(7):
    part_0.append(num[4*i])
    part_1.append(num[4*i+1])
    part_2.append(num[4*i+2])
    part_3.append(num[4*i+3])

tol = []
part_0.reverse()
tol.extend(part_0)
part_3.reverse()
tol.extend(part_3)
part_1.reverse()
tol.extend(part_1)
part_2.reverse()
tol.extend(part_2)
print(tol)
h_num = [2*math.pi*i/28 for i in range(28)]

mul_0 = 0
mul_1 = 0
for j in range(28):
    mul_0 = mul_0 + math.cos(h_num[j])*tol[j]
    mul_1 = mul_1 + math.sin(h_num[j])*tol[j]

out = (mul_0**2 + mul_1**2)**0.5
print(out)

def save(data,path):
    f = xlsxwriter.Workbook(path)  # 创建工作簿
    sheet1 = f.add_worksheet('sheet1')  # 创建sheet
    l = 1
    h = len(data)  # h为行数，l为列数
    for i in range(h):
        
            sheet1.write(i, 1, data[i])
    f.close()

# c = Counter(dict_0).most_common()

# a = [list(i) for i in c]
path = r'C:\Users\liuju\Documents\MATLAB\叶片排序.xlsx'
save(tol,path)