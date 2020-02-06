#有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os

filepath="C:\\Users\\liuju\\GitPython\\python_exercise\\"
filename=os.listdir(filepath)
count_sum=0
count_none=0
count_express=0
express=[]
for i in range(len(filename)):
    with open(filepath+filename[i],encoding="utf-8") as f:
        s=f.readlines()
    count_sum+=len(s)
    for j in s:
        if j=="\n":
            count_none+=1
        if j[0]=="#":
            count_express+=1
            express.append(j)

print("总行数为:%s.\n空行数为:%s.\n注释行数为:%s."%(count_sum,count_none,count_express))
print(express)
