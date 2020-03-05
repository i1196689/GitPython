import time

'''
def log(test):
    def decorate(func):
        def wrapper(*args,**kwargs):
            f=func(*args,**kwargs)
            print('这个函数名字是%s'%func.__name__,'。','备注:',test)
            return f
        return wrapper
    return decorate

@log('来测试')
def test():
    return print('1111')
test()
'''
def log(test):
    def decorate(func):
        def wrapper(*args,**kwargs):
            time_start=time.time()
            f=func(*args,**kwargs)
            time_cost=time.time()-time_start
            print('函数%s运行时间为:%s.'%(func.__name__,time_cost),':',test)
            return func
        return wrapper
    return decorate

@log('测试函数')
def recursion(n):
    s=0
    for i in range(n):
        s+=i
    return print(i)


recursion(10000)

