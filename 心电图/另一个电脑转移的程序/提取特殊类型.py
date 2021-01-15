import codecs

f = codecs.open(r'C:\Users\666\Desktop\mitdb\100.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
line = f.readline()   # 以行的形式进行读取文件
list1 = []
while line:
    a = line.split()
    b = a[1:3]   # 这是选取需要读取的位数
    if a[2] != 'N':
        list1.append(b)  # 将其添加在列表之中
    line = f.readline()
f.close()

del list1[0:2]

