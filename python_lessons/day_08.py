x={1,2,3}
x.add(123)
print(x)
x.add("abc")
print(x)

x.remove(123)
print(x)
try:
    x.remove("444")
except Exception as e:
    print(e)

#集合之间的运算
x1={1,2,3}
x2={3,4,5}
print(x1|x2)
print(x1.union(x2))
print(x1&x2)
print(x1.intersection(x2))

print(x1.difference(x2))
print(x1^x2)