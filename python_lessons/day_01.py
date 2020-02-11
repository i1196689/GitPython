#字符串与字符串之间的连接方式有5种。
###1.用 "+"
s1="hello"
s2="word"
s=s1+s2
print(s)
# 2 直接连接
s="hello""word"
print(s)
##3 ","连接
print("hello","word")
##4格式化
s="<%s> <%s>"%(s1,s2)
print(s)
##5 join
s=" ".join([s1,s2])
print(s)
#字符串与非字符串如何连接
#1 “+”
n=20
s=s1+str(n)
print(s)
#2 格式化

