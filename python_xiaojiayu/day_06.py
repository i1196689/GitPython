#函数实现阶乘
'''
def func(n):   
    result=n
    for i in range(1,n):
        result*=i
    return result

#print(func(5))
'''
##递归实现阶乘
def recursion(n):
    if n==1:
        return 1
    else:
        return n*recursion(n-1)
print(recursion(5))