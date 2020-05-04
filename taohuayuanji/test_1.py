import pyautogui as pg
from PIL import Image
import math,random

import time
'''
人站在地图中央[646,461]
左上角坐标[135,35,43,63,20]
左上角‘第’[74,40,25,25]
'''
time.sleep(5)
def create_circle(coordinate,radius):
    list_coor = []
    sita = [i*20*2*math.pi/360 for i in range(18)]
    coor_x = [int(radius*math.cos(i)) for i in sita]
    coor_y = [int(radius*math.sin(i)) for i in sita]
    for i in range(18):
        list_temp = []
        x = coordinate[0] + coor_x[i]
        y = coordinate[1] + coor_y[i]
        list_temp.append(x)
        list_temp.append(y)
        list_coor.extend([list_temp])

    return list_coor
coor = [645,445]
list_coor = create_circle(coor,75)
list_coor_1 = list_coor[:9]
list_coor_re = list_coor[9:18]
list_coor_re.extend(list_coor_1)

for i in range(18):
    pg.moveTo(random.randint(list_coor[i][0]-5,list_coor[i][0]+5),random.randint(list_coor[i][1]-5,list_coor[i][1]+5))
    pg.click()
    pg.moveTo(random.randint(list_coor_re[i][0]-5,list_coor_re[i][0]+5),random.randint(list_coor_re[i][1]-5,list_coor_re[i][1]+5))
    pg.click()
    time.sleep(0.2)










