import csv
import matplotlib.pyplot as plt



with open(r'C:\Users\666\Desktop\mitdb\101_new.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    y = [row[1]for row in reader] #读取第1列

y = [float(i) for i in y] #将字符串转化为数字

out = []
for i in range(len(y)):
    if i<len(y)-1:
        if y[i]-y[i+1]>0:
            out.append(y[i]-y[i+1])
        else:
            out.append(y[i+1]-y[i])

#for k in range(3):
#    new = K_M(new,2)
out.sort()
print(out)
print(sum(out)/len(out))

