
import pyautogui as pg         
import time
import random
time.sleep(5)
'''
pg.moveTo(732,530)
[168,147],[839,146]
[165,673],[840,675]
x:[170,830]
y:[150,650]


[1078,85],[1850,656]
x:[1078,1850]
y:[85,656]

[334,825],[1258,1001]
x:[334,1258]
y:[825,1001]
''' 
while True:
    time.sleep(3    )
    time.sleep(random.random())
    if random.random() > 0.5:
        pg.moveTo(random.randint(170,830),random.randint(150,650),duration=random.random())
        time.sleep(random.random())
        pg.click(clicks=random.randint(1,4),interval=random.random())
    else:
        
        time.sleep(random.random())
        pg.moveTo(random.randint(170,830),random.randint(150,650),duration=random.random())
        pg.press('tab')
        pg.click()
        time.sleep(random.random())
        pg.click(clicks=random.randint(5,7),interval=random.random())
        pg.press('tab')
    if random.random() > 0.3:
        time.sleep(random.random())
    if random.random() > 0.5:
        pg.click(random.randint(1078,1850),random.randint(85,656))
    else:
        pg.moveTo(random.randint(334,1258),random.randint(825,1001),duration=random.random())



