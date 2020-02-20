'''
f=open("day_19.txt","r",encoding="utf-8")
print(type(f))
print(f.read(3))#读取前n个字符串。
f.seek(6)#移动指针到指定位置。
print(f.read(2))
f.close()
print("--------------------")
f=open("day_19.txt","r",encoding="utf-8")
print(f.readline(4))
f.close()
f=open("day_19.txt","r",encoding="utf-8")
print(f.readlines(3))#如果指定n，那么只会读取行字符串个数大于n的行。
'''
# with语句适用于对语句进行访问的场合，确保不管使用过过程是否发生异常都会执行必要的清理工作。
with open("day_19.txt","r",encoding="utf-8")as f:
    data=f.read()
    print(data)
print("---------------")
#将with语句用于自定义的类。 __enter__    __exit__
class Myclass:
    def __enter__(self):
        print("__enter__() is call")
        return self
    def process1(self):
        print("process1")
    def process2(self):
        x=1/0
        print("process2")
    def __exit__(self,exc_type,exc_value,traceback):
        print("__exit__()is call")
        print(f"type:{exc_type}")
        print(f"value:{exc_value}")
        print(f"trace:{traceback}")
with Myclass()as my:
    my.process1()
    my.process2()
