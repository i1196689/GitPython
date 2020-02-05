#你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
import os,re
filepath="D:\\text\\"
filename=os.listdir(filepath)
for i in range(len(filename)):
    with open(filepath+"%s"%(filename[i]),"r") as f:
        s=re.split(r"[\s\,\.\?\;\'\"\!\:]+",f.read())
    d={}
    for st in s:
        if st in d:
            d[st]+=1
        else:
            d[st]=1
    t=sorted(d.items(),key=lambda L:L[1],reverse=True)
    print(t[0:5])# 输出使用频率前5的单词。
