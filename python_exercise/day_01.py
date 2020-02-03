#将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
from PIL import Image,ImageDraw,ImageFont
import os

len=200#字体大小
myfont=ImageFont.truetype("arial.ttf",len) #选择字体和大小。
photo=Image.open("wechat.jpg") #选择图片
add_num=ImageDraw.Draw(photo)
fillcolor="red"#字体颜色
(width,height)=photo.size
add_num.text((width-len/2,0),u"4",font=myfont,fill=fillcolor)#第一个参数为添加文字的坐标
photo.save("new.jpg","jpeg")

