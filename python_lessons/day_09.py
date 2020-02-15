#如何快速调换字典中的Kye 和value
'''d={"a":1,"b":2}
print({v:k for k,v in d.items()})

a=[i for i in range(101)]
print(a)
'''
#将两个列表合并成一个字典。
a=["a","b"]
b=[1,2]
print(dict(zip(a,b)))

filds=("id","name","age")
records=[["01","Bill","20"],["02","Mike","30"]]

result=[]
for record in records:
    result.append(dict(zip(filds,record)))
print(result)


#列表与元组的差异

'''
1 语法差异 
元组用()  列表用[]
2 元组是只读的，列表是可读写的
'''
#3
e=(1,2)
f=[1,2]
copy_e=tuple(e)
print(copy_e is e) #True, 列表为False

#4 所占空间大小不同
print(e.__sizeof__())
print(f.__sizeof__()) #当元素多时 用元组速度更快。



