import numpy as np

s=np.array([1,2,3,4,5,6,7,8,2,3,2,5,2,3,1,2,4,5,6,7])
'''
print(np.sort(s))
print(np.argsort(s))#返回由小到大的索引
print(np.array(sorted(s,reverse=True)))
arr1=np.array([[0,1,3],[4,2,9],[4,5,9],[1,-3,4]])
print(arr1)
print("-------------------")
print(np.sort(arr1,axis=0))

print(np.where(s>3,1,-1))
print(np.where(s>3,s,-1))
'''

print(np.extract(s>3,s))