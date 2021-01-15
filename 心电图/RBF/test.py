import numpy as np
a = np.zeros((3,3))
a = np.mat(a)
print(a)
for c,d in enumerate(a):
    print(c,d)


[m,n] = d[0].shape
e = []
for i in range(n):
    e.append(d[0,i])
print(e)
