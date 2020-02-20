import re
#用正则表达式提取网址
'''
s="<a herf='http://geekori.com'>极客起源</a> <a herf='http://www.microsoft.com'>微软</a>"
result=re.findall("<a[^>]*herf='([^>]*)'>",s,re.I)
print(result)
for url in result:
    print(url)

'''
from xml.etree.ElementTree import parse

doc=parse("day_16.xml")
print(type(doc))

for item in doc.iterfind("products/product"):
    id=item.findtext("id")
    name=item.findtext("name")
    price=item.findtext("price")
    uuid=item.get("uuid")
    print("-------------------------")
    print("uuid=",uuid)
    print("name=",name)
    print("price=",price)
    print("id=",id)
    