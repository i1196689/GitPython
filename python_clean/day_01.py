import numpy as np
arr1=np.array([-9,7,4,3],dtype="int")
print(type(arr1))
print(arr1)

arr3=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr3)
for i in range(1,10):
    print(i)

arr2=np.arange(1,10,0.5)
print(arr2)
arr4=np.linspace(1,10,20,endpoint=True)#20个元素
print(arr4)

arr5=np.zeros([4,5])
print(arr5)
arr6=arr5+1
print(arr6)
print(arr6.ndim)

data2=((8.5,6,4,1.2,0.7),(1,2,5,4,7))
data3=np.array(data2)
print(data3)
print(data3[0:1])#python 左闭右开

