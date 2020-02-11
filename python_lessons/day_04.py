#检测字符串是否为数字
s1="1234"
print("是数字：",s1.isdigit())
s2="12345aa"
print("12345aa是数字:",s2.isdigit())
try:
    print(int(s2))
except Exception as e:
    print(e)

try:
    print(int("334r"))
except Exception as e:
    print(e)
