#纯文本文件 student.txt为学生信息, 将其读取到.xsl文件中。
import xlwt,re



filePath="D:\\test\\"
with open(filePath+"sutdent.txt",encoding="utf-8")as f:
    s=f.read()

data=re.split(r"[\s\{\}\[\]\'\"\:\,]+",s)
#data_1=filter(None,data)
data=[x for x in data if x!=""]
print(data)
wk=xlwt.Workbook(encoding="utf-8")
ws=wk.add_sheet("student",cell_overwrite_ok=True)
def ww(x,y,num):
    ws.write(x,y,num)
    return None
    
for i in range(len(data)):
    if i<=4:
        ww(0,i,data[i])
    if 5<=i<=9:
        ww(1,i-5,data[i])
    if i>9:
        ww(2,i-10,data[i])
wk.save(filePath+"student.xls")