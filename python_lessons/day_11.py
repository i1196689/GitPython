'''a=[3,4,5,6]
print(a)
del a[2]
print(a)

print(a.pop(1))
print(a)

a.pop()
print(a)


a=[{"name":"Bill","age":40},{"name":"Mike","age":12},{"name":"JOhb","age":29}]
print(a)

print(sorted(a,key=lambda x :x["age"]))

a.sort(key=lambda x:x["age"],reverse=True)
print(a)'''

d={}
d["name"]="Bill"
d[10]=20
d[True]=False
d[12.3]=20.1
d[(1,2,4)]=[4,5,6]

class Person():
    pass
p1=Person()
p2=Person()
d["p1"]=p1
d["p2"]=p2
print(d)