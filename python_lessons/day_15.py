import re
'''
m=re.search("(\d{3})-(\d{7,})-(\d{3,})","我的公司的座机是：024-12345678-5432")
if  m is not None:
    print(m.groups())
    print(m.groups()[0])

###
s="我的Email是abcd@163.com,你的是xyz@112.com,还是ccc@125.org"
prefix="[0-9a-zA-Z]+@[0-9a-zA-Z]+\."
result=re.findall(prefix+"com|"+prefix+"net",s,re.I)
print(result)
'''
#浮点数表示方法：
def fun(matched):
    return format(float(matched.group()),"0.2f")
result=re.subn("-?\d+(\.\d+)?",fun,"PI is 3.1415926,e is 2.71656. -0.2+1.3=1.1")
print(result)