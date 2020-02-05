import os
from PIL import Image
filepath="D:\\photo\\"
filename=os.listdir(filepath)
for i in range(len(filename)):
    ima=Image.open(filepath+"%s"%(filename[i]))
    ima_new=ima.resize((640,480))
    ima_new.save(filepath+"new_%s.png" % (i))#生成图片保存到原有路径



