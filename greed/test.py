def max_list(each_list):
    d={}
    for each in each_list:
        if each in d:
            d[each]+=1
        else:
            d[each]=1
    d=sorted(d.items(),key=lambda item:item[1],reverse=True)
    return d
a=[1,24,5,61,2,3,2,2,2,1,1,1]
d=dict(max_list(a))
print(d)