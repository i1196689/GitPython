print("aa","bb",sep=",;")
print("hello",end=" ")
print("word")

#格式化 占位符
s="road"
x=len(s)
print("the length of %s is %d"%(s,x))

a=[1,2,3,4,5,1,2]
print(type(a))

b=(1,23,4,5)
print(type(b))

c={1,2,4,5,6}
print(type(c))
#区别  集合没有重复的元素，列表可以有重复的元素
#去掉重复的元素
a_result=list(set(a))
print(a_result)
m=["a","b","a"]
print(list(set(m)))
