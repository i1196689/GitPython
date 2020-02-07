#敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
# -*- coding: UTF-8 -*-
# coding=utf-8
import os
s=input("intput:")
filePath="D:\\test\\"
fileName=os.listdir(filePath)
with open(filePath+fileName[0],encoding="utf-8")as f:
    context=f.readlines()
if s.replace("intput:","")+"\n" in context:  
    print("Freedom")
else :
    print("Human Rights")