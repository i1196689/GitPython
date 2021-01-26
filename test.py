n = 3
i_list = []
j_list = []
k_list = []
i = 0
while i < n :
    i_list.append(i)
    i = i + 1
    j = 0
    while j < i  :
        j = j + 1
        j_list.append(j)
        k = 0
        while k < j  :
            k = k + 1
            k_list.append(k)

print('i:%s'%len(i_list))
print(i_list)
print('j:%s'%len(j_list))
print(j_list)
print('k:%s'%len(k_list))
print(k_list)