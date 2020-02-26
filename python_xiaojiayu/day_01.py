#三元操作符
x,y=4,5
small=x if x<y else y
print(x)
#  assert 3>4 
a=[1,2,4]
a.append(3)
print(a)
a.extend([4,5])
print(a)
print('------------')
temp=input()
if isinstance(temp,str):
    print('输入不合法')
else:
    print('you are right!')