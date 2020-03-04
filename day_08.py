a=[1,2,3]
b=[11,22,33]
dict1={}
dict2=dict1.fromkeys(b,'str')
for key in dict2.keys():
    print(key)
print('11111111111')
for value in dict2.values():
    print(value)
print('22222222222222222')
for itemers in dict2.items():
    print(itemers)
for i in range(6):
    print(dict2.get(i,'索引%s不存在'%i))
dict2.clear()
print(id(a))
print(id(b))
print(a.pop())#删除对象的一个值，默认为最后一个值
print(a)
print(b.pop(1))
print(b)
a=[1,2,3,4,5,6,3,2,5,7,0,0]
a=list(set(a))
print(a)