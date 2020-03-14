import time
def timers(func):
    def wrapper(*args,**kwargs):
        time_start=time.time()
        f=func(*args,**kwargs)
        time_end=time.time()
        time_cost=time_end-time_start
        print('程序%s运行时间为:%s.'%(func.__name__,time_cost))
        return f
    return wrapper


