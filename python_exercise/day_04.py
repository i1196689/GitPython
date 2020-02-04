#任一个英文的纯文本文件，统计其中的单词出现的个数。
import re

with open("test.txt","r") as f:
    s=re.split(r'[\s\,\.\!\;\?]+',f.read())#正则表达式将内容提取出来。
d={}
for st in s:
    if st in d:
        d[str(st)]+=1
    else:
        d[st]=1
s=sorted(d.items(),key=lambda L:L[1],reverse=True)
print(s)
print (len(s))

for ch in s:
    t=open("test_1.txt","a")
    t.write(str(ch)+"\n")#需用str函数。
    t.close()