'''#列表的排序
a=[5,4,2,7,6,8,5,3]
a.sort()
print(a)#本身变了
b=[3,5,7,2,8,5,2,1,4]
c=sorted(b)#返回一个排好序的列表副本。
print(c)
print(b)

a.sort(reverse=True)
print(a)

print(sorted(b,reverse=True))
'''
class Myclass():
    def __init__(self):
        self.value=0

my1=Myclass()
my1.value=20

my2=Myclass()
my2.value=30

my3=Myclass()
my3.value=10
a=[my1,my2,my3]
print(a)


