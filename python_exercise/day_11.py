#敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
import os
s=input("intput:")
filePath="D:\\test\\"
fileName=os.listdir(filePath)
with open(filePath+fileName[0],encoding="utf-8")as f:
    context=f.readlines()
#去掉空格
def Rep(st):
    return st.replace("\n","")
#代替*的数量
def Rep_num(num):
    a=""
    for ss in range(num):
        a+="*"
    return a
context_new=list(map(Rep,context))
ss=s.replace("input:","")
for i in range(len(context_new)) :
    sss=ss.replace(context_new[i-1],Rep_num(len(context_new[i-1])))
    aims=sss
    ss=aims
print(sss)
    

