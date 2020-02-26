'''
list1=[1,2,3,4,['not','di','bu'],4,5,2,1,2,1,1]
print('not' in list1)#False

print('not' in list1[4])#True
print(list1[4][1])#di
print(dir(list))
print(list1.count(1))

print(list1.index(4,0,7))

print(list1)
list2=list1[:]
print(list2)
for i in range(10):
    if i>6:
        break
    print(i,end=',')
    if i==4:
        continue
    print(i+100,end=',')
'''
temp=(1)
print(type(temp)) #int
temp2=2,3,4,5,6
print(type(temp2))# tuple

temp3=(1,)
print(type(temp3))#tuple
tmp1=1,
print(type(tmp1))#tuple
print(8*(8,))

temp4=(1,2,4,5)
temp4=temp4[:2]+(3,)+temp4[2:]
print(temp4)