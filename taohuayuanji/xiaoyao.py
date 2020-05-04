import pyautogui  as pg
import time
import random


time.sleep(5)
while True:
    pg.press('f7')
    time.sleep(1)
    pg.click(random.randint(213,230),random.randint(259,263))
    time.sleep(random.random())
    pg.moveTo(random.randint(327,355),random.randint(316,369),duration=random.random())
    time.sleep(random.randint(1,2))
    if random.random() > 0.5:
        pg.click()
    else:
        pg.doubleClick()
    time.sleep(random.random())
    pg.moveTo(random.randint(256,313),random.randint(521,528),duration=random.random())
    if random.random() > 0.5:
        pg.click()
    else:
        pg.doubleClick()
    time.sleep(random.random())
    pg.moveTo(random.randint(774,819),random.randint(353,360),duration=random.random())
    if random.random() > 0.5:
        pg.click()
    else:
        pg.doubleClick()
    time.sleep(20)
    



    
    




