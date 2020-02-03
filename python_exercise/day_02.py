#用python生成200个激活码 1/5为数字，2/5为小写字母，2/5为大写字母
import string
from random import randint
s_low=string.ascii_lowercase
s_up=string.ascii_uppercase
s_num="0123456789"
def key_create(num):
    key=[]
    for i in range(num):
        keys=""
        for j in range(1,17):
            choice=randint(1,5)
            if choice==1:
                s=randint(0,9)
                keys +=s_num[s]
            elif 2<=choice<4:
                s=randint(0,25)
                keys +=s_low[s]
            else:
                s=randint(0,25)
                keys +=s_up[s]
            if j%4==0 and j!=16:
                keys +="-"
        key.append(keys)
    return key
Key=key_create(200)
print(Key)
print("共有激活码%s个。已经存入key.txt文件。" % (len(Key)))
for s in Key:
    f=open("key.txt","a")#'a'，代表追加模式'a',可以实现多次写入。即每次执行都会在上一行的基础上，换行写入
    f.write(str(s)+"\n")
    f.close()