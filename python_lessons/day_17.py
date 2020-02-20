#将字典转换为xml文档
'''
import dicttoxml
import os
from xml.dom.minidom import parseString
d=[20,"names",{"name":"Bill","age":30,"salary":2000},
            {"name":"Mike","age":40,"salary":3000},
            {"name":"John","age":20,"salary":1000}]
bxml=dicttoxml.dicttoxml(d,custom_root="persons")
xml=bxml.decode("utf-8")
print(xml)
dom=parseString(xml)
preetyxml=dom.toprettyxml(indent=" ")
print(preetyxml)
f=open("day_17.xml","w",encoding="utf-8")
f.write(preetyxml)
f.close()
'''

#将xml文档装换为字典
import xmltodict
f=open("day_16.xml","rt",encoding="utf-8")
xml=f.read()
import pprint
d=xmltodict.parse(xml)
print(d)
pp=pprint.PrettyPrinter(indent=4)
pp.pprint(d)