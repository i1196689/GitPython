#用 Python 写一个爬图片的程序
from urllib import request
from bs4 import BeautifulSoup
from PIL import Image
import os,requests

filePath="D:\\test\\"
#with request.urlopen("http://www.baidu.com")as f:
#data=f.read()
r=requests.get("http://tieba.baidu.com/p/1165861759")
data=r.text
soup=BeautifulSoup(data,"lxml")
count=0
for imag in soup.find_all("img"):
    count+=1
    f=imag.get("src")
    if f[0]!="h":
        f="http:"+f
    #with request.urlopen(ima_url)as ff:
        #data=ff.read()
    r_1=requests.get(f)
    t=open(filePath+"new_%s.png"%count,"wb")
    t.write(r_1.content)
    t.close()
    print("正在下载第%s张图片."%count)

