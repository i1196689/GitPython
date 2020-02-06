#使用 Python 生成类似于下图中的字母验证码图片
from PIL import Image,ImageDraw,ImageFont,ImageFilter
from random import randint

#随机字母
def rndChar():
    return chr(randint(65,90))
#随机颜色1
def rndColor():
    return (randint(64,255),randint(64,255),randint(64,255))
#随机颜色2
def rndColor2():
    return (randint(32,127),randint(32,127),randint(32,127))
#240*60
width=60*4
height=60
image=Image.new("RGB",(width,height),(255,255,255))
#创建FONT对象：
font=ImageFont.truetype("arial.ttf",36)
#创建Draw对象：
draw=ImageDraw.Draw(image)
#填充每个像素：
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
for t in range(4):
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
#模糊：
image=image.filter(ImageFilter.BLUR)
image.save("code.jpg","jpeg")
