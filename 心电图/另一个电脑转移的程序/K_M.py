import csv
import matplotlib.pyplot as plt



with open(r'C:\Users\666\Desktop\mitdb\100_new.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    y = [row[1]for row in reader] #读取第1列

y = [float(i) for i in y] #将字符串转化为数字


def  K_M(aim,num):
    out = [0]*len(aim)
    for i in range(len(aim)):
        if len(aim)-num>=i:
            if abs(aim[i]-aim[i+1])<0.014:
                out[i] = sum([aim[i+j] for j in range(num)])/num
            else:
                out[i] = aim[i]
        else:
            out[i] = aim[i]
    return out
new = K_M(y,2)

for k in range(10):
    new = K_M(new,2)
plt.figure("new")
plt.plot(new)
plt.figure("y")
plt.plot(y)
plt.show()
