import pyautogui as pg#天武关 魔云崖            
import time
from multiprocessing import pool


time.sleep(2)
buttonlocate = pg.locateOnScreen('F:\\auto\\head.png',grayscale=False,confidence=0.5)
buttonlocatex,buttonlocatey = pg.center(buttonlocate)

checkcount = 0

def locate_head():
    pg.moveTo(buttonlocatex,buttonlocatey,duration=1)



def tianwuguan():
    time.sleep(0.5)
    pg.moveTo(buttonlocatex,buttonlocatey,duration=1)
    pg.press('tab')
    time.sleep(0.5)
    pg.moveRel(600,200,duration=1)#天武关
    pg.doubleClick()
    time.sleep(0.5)
    pg.press('tab')


def mijingfushi():
    time.sleep(0.5)
    pg.moveTo(buttonlocatex,buttonlocatey,duration=1)
    pg.press('tab')
    time.sleep(0.5)
    pg.moveRel(130,550)#秘境浮石        
    pg.doubleClick()
    pg.press('tab')


def check():
    global checkcount
    while True:
        time.sleep(2)
        buttonlocate = pg.locateOnScreen('F:\\auto\\zi.png',grayscale=False,confidence=0.5)
        if buttonlocate:
            checkcount = 1



def go():
    time.sleep(1.5)
    while True:
        
        tianwuguan()
        time.sleep(8)
        mijingfushi()
        time.sleep(8)


go()



