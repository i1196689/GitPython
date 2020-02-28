num=input('输入大于等于0的数进行开方:')#牛顿迭代算开方
num.strip('输入大于等于0的数进行开方:')
num=int(num)
def func(x):
    return x*x-num
def func1(x):
    return 2*x
def pp(aim):
    return print('牛顿迭代方法，%s的开根号是%s.'%(num,aim))
if num==0:
    pp(num)
else:
    x1=1
    x2=num+1
    count=0
    while x2*x2-num>0.001:
        count+=1
        x2=x1-(func(x1)/(func1(x1)))
        x1=x2
        print('迭代第%s次,值为%s'%(count,x2))
    pp(x2)
