'''
a=10
def func():
    global a#定义全局变量
    a=100
    print(a)
print(a)
func()
print(a)
##函数内部可以接着定义函数
def func1(a):
    x=1  #可以用列表  x=[1]
    def func2(b):
        nonlocal x
        x=a+b+1  #x[0]=a+b+1
        return x
    return func2
i=func1(3)(4)
print(i)
#匿名函数
g=lambda x: 2*x+1
print(g(10))

f=lambda x,y:x+y
print(f(4,5))
'''
print(list(filter(None,[1,0,False,True])))
print((list(filter(lambda x:x%2,range(10)))))

ff=list(map(lambda x : x*2 ,range(10)))
print(ff)

