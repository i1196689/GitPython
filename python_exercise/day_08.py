#一个HTML文件，找出里面的正文。
import os
from bs4 import BeautifulSoup
filepath="D:\\test\\" #从D盘test文件夹读取。
filename=os.listdir(filepath)
with open(filepath+filename[0],encoding="utf-8") as f:
    s=f.read()
soup=BeautifulSoup(s,"lxml")
for link in soup.find_all("a"):
    print(link.get("href"))#a标签后面跟的网址。
print(soup.get_text())#获取网页内容。