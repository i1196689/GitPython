#用python生成200个激活码 1/5为数字，2/5为小写字母，2/5为大写字母
#ASCII码：其中48～57为0到9十个阿拉伯数字。
#65～90为26个大写英文字母，97～122号为26个小写英文字母
from random import randint

#创建随机数字：
def rndNum():
    return chr(randint(48, 57))
#创建随机小写字母：
def rndWord_low():
    return chr(randint(97,122))
#创建随机大写字母：
def rndWord_up():
    return chr(randint(65,90))
s=[]
for i in range(4):
    st=""
    for j in range(4):
        choice=randint(1,5)
        if choice==1:
            tem=rndNum()
        if 2<=choice<=3:
            tem=rndWord_low()
        if 4<=choice<=5:
            tem=rndWord_up()
        st+=tem
    s.append(st)
    aims="-".join(s)
else:
    print(aims)
