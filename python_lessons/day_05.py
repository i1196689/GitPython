s1="abcde"
s2=""
for c in s1:
    s2=c+s2
print(s2)
print(s1[::-1])


#格式化整数
n=1234
print(format(n,"10d"))
print(format(n,"0>10d"))
print(format(n,"0<10d"))

#格式化浮点数
x1=1234.5678
x2=30.1
print(format(x1,"0.2f"))
print(format(x2,"0.2f"))

#描述format函数
print(format(x2,"*>15.4f"))
print(format(x2,"*<15.4f"))
print(format(x2,"*^15.4f"))
print(format(123456789,","))
print(format(123456.1245876,",.2f"))
print(format(x1,"e"))
print(format(x1,"0.2e"))