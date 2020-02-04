import re

with open("test.txt","r") as f:
    s=re.split(r'[\s\,\.\!\;\?]+',f.read())
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
    t.write(str(ch)+"\n")#用str函数
    t.close()