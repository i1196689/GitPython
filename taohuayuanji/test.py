import pytesseract

from PIL import Image

def convert_img(img,threshold):
    img = img.convert("L")  # 处理灰度
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return img







image = Image.open('local.png')

b,g,r = image.split()
b.save('b.png')
g.save('g.png')
r.save('r.png')

image = Image.open('b.png')
image=convert_img(image,100)
image = image.convert('L')

image.show()

local_zi = (74,40,25,25)  #'第'字截图
pg.screenshot('zi.png',local_zi)

local_num = (140,43,61,20)# 坐标截图
pg.screenshot('local.png',local_num)



button = pg.locateCenterOnScreen(r'zi.png',grayscale=False,confidence=0.8)

pg.moveTo(button)

text = pytesseract.image_to_string(image)
print(text)