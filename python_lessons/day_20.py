'''
def log(func):
    def wrapper(*args,**kw):
        print("call%s():"% func.__name__)
        return func(*args,**kw)
    return wrapper

@log #相当与   log(now())
def now():
    print("2020-02-20")
f=now
f()

with open("day_19.txt","r",encoding="utf-8")as f:
    data=f.read()
print(data)
d={}
maxChar=""
for c in data:
    if c.isspace():
        continue
    if d.get(c)is None:
        d[c]=1
        if maxChar=="":
            maxChar=c
    else:
        d[c]+=1
        if d[maxChar]<d[c]:
            maxChar=c
print(maxChar)
print(d[maxChar])
'''
import fire
class Myclass:
    def process(self):
        pass


def process():
    pass
print(type(Myclass().process).__name__=="method")
print(type(process).__name__=="function")
fire.Fire()