import os
#zip 可以压缩多个迭代对象里面的元素，比如像这样的多个列表：
a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[6,7,8,9,0]
zipped=zip(a,b,c)
print(list(zipped))
print(list(zip(*zip(a,b,c))))
print("--------------------------")
#在一些列表中，可以使用步长比如 [::2] 去获取对应的值，当你使用 -1 的时候会发现，可以直接倒序访问：
s="fwojgwiogwo"
print(s[::2]) #对list也适用
print(s[::2])
print("-----------------")
#容器对象可以随便你拆分，比如这样的元组：
tuples=(1,2,3,4,5,6,7,8,9,0)
q,w,*e,r=tuples
print(q)
print(w)
print(e)
print(r)
print("-------------")
#你可以直接打印模块的名称，从而快速获取到模块所在的具体位置：
print(os)
#当你的列表中的元素都是字符串，你想要把它们转成字符串的时候就可以使用 join，还可以自己定义要连接的字符，比如这样：

#如果你想要获取列表中反过来的元素，可以使用 reversed ，非常方便简洁：
for i in reversed([1,2,3,4,5]):
    print(i)