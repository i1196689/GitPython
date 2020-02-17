'''
s1="TodayL is {}, the temperature is {} degrees."
print(s1.format("Saturday",24))

s2="TodayL is {day}, the temperature is {degree} degrees."
print(s2.format(degree=30,day="Monday"))

s3="TodayL is {week}, the {} is  {degrees}."

print("<"+"hello".center(30)+">")
print("<"+"hello".center(30,"#")+">")

print("<{:^30}>".format("hello"))
print("<{:#^30}>".format("hello"))

print("<"+"hello word".center(50)+">")

a=["a","b","c","d","e"]
s=""
print(s.join(a))

dirs="","user","local","nginx",""
print(dirs)
windowsPath="\\".join(dirs)
print(windowsPath)

import re

print(re.match(".*hello","ahello"))

s="Today is 2013-12-12."
m=re.match(".*\d{4}-\d{2}-\d{2}.*",s)
if m is not None:
    print(m.group())
'''
import re
m1=re.match(".*python","I love python")
print(m1)

m2=re.search("python","I love python")
print(m2.group())

m=re.search("1\d{10}","我的手及好是：1865265552555")
if m is not None:
    print(m.group())
    print(m.start())
    print(m.end())