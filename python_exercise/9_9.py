def prince(n):
    if n==1:
        return print('%s*%s=1'%(1,1))
    else:
        for i in range(1,n+1):
            if i==n:
                print('%s*%s=%s'%(i,n,i*n))
            else:
                print('%s*%s=%s'%(i,n,i*n),end=',')

    return prince(n-1)

prince(11)