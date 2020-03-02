import time
from random import randint
'''
def test():
    time_s=time.time()
    for i in range(10):
        print(i,end=',')
    time_z=time.time()-time_s
    return print(time_z)

def time_test(func):
    def wrapper(*args,**kwargs):
        time_start=time.time()
        f=func(*args,**kwargs)
        time_waste=time.time()-time_start
        print(time_waste)
        return f
    return wrapper


def test_1():
    for i in range(10):
        print(i,end=',')

f=time_test(test_1)

test()
print('------------')
f()
def time_55(func):
    def warpper(*args,**kwargs):
        time_ss=time.time()
        f=func(*args,**kwargs)
        time_zz=time.time()-time_ss
        print(time_zz)
        return f
    return warpper
'''

def output(num):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print('第%s个输出结果是'%num,end=':')
            f=func(*args,**kwargs)
            return f
        return wrapper
    return decorator

def   Rnd():
    res=randint(1,10)
    return print(res)


def   Rnd_1():
    res=randint(1,10)
    return print(res)
Rnd()
print('-------------')

for i in range(10):
    f=output(i)(Rnd_1)
    f()
ff=Rnd
print(ff.__name__)