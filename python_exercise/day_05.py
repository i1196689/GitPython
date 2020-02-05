#你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
import os
from PIL import Image
filepath="D:\\photo\\"
filename=os.listdir(filepath)
for i in range(len(filename)):
    ima=Image.open(filepath+"%s"%(filename[i]))
    ima_new=ima.resize((640,480))
    ima_new.save(filepath+"new_%s.png" % (i))#生成图片保存到原有路径



