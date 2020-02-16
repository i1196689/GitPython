'''
d={"a":123,"b":456,"c":"xyz"}
print(d)

import json
json_str=json.dumps(d)
print(json_str)
print(type(json_str))

d1=json.loads(json_str)
print(d1)
print(type(d1))

from string import Template

template=Template('$s是我最喜欢的编程语言，$s非常容易学习，而且功能强大。')
print(template.substitute(s="python"))


template3=Template("${h}hello word")
template2=Template("$dollar$$相当于多少$pounds英镑")
print(template2.substitute(dollar=20,pounds=123))

data={}
data["dollar"]=30
data["pounds"]=25

print(template2.substitute(data))
'''
name="Bill"
age=20

def getAge():
    pass

s=f"我是{name},我今年{age}岁,明年{getAge()}"
print(s)

class Person:
    def __init__(self):
        self.name="Mike"
        self.age=40
       
    def getAge(self):
        return 41
person=Person()
s1=f"我是{person.name},我今年{person.age}岁,明年{person.getAge()}"
print(s1)
