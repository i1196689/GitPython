import numpy as np
from math import e
import matplotlib.pyplot as plt
import csv
with open(r'C:\Users\666\Desktop\mitdb\100_new.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    y = [row[1]for row in reader] #读取第1列

y = [float(i) for i in y] #将字符串转化为数字

a = y
def weigh(aim_0):
    var_1 = np.var(aim_0)
    w =e**(-((aim_0[0]-aim_0[-1])**2)/(2*var_1))
    return w

def G_s(aim,num):
    out=[0]*len(aim)
    for i in range(len(aim)):
        if i >=(num-1)/2 and i <len(aim)-(num-1)/2-1:
            out[i] = aim[i]*weigh([aim[i+j-int((num-1)/2)] for j in range(num)])+aim[i+1]*weigh([aim[i+k+1-int((num-1)/2)] for k in range(num)])
            print(i)
        else:
            out[i] = aim[i]
            print(i)
    return out
out = G_s(a,5)


plt.figure("a")
plt.plot(a)
plt.figure("new")
plt.plot(out)
plt.show()