import xlwt,re

filePath="D:\\test\\"
with open(filePath+"city.txt",encoding="utf-8")as f:
    data=f.read()
print(data)
data=re.split(r"[\s\:\,\{\}\'\"]",data)
data=[x for x in data if x!=""]
wk=xlwt.Workbook(encoding="utf-8")
ws=wk.add_sheet("city",cell_overwrite_ok=True)
def ww(x,y,st):
    return ws.write(x,y,st)
ww(0,0,data[0])
ww(0,1,data[1])
ww(1,0,data[2])
ww(1,1,data[3])
ww(2,0,data[4])
ww(2,1,data[5])
wk.save(filePath+"city.xls")