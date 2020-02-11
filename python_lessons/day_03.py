s1="hello"
print(s1)
print(s1.capitalize())

s1=s1[0:1]+s1[1].upper()+s1[2:]
print(s1)
s2="Hello"
s=s2[0].lower()+s2[1:]
s3="hello word"
arr=s3.split(" ")
print(arr)
def str_upper(st):
    return st.capitalize()
arr=list(map(str_upper,arr))
print(arr)