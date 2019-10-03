#import pynput as pp
from pynput import mouse
import os
from pynput import keyboard
from pynput.mouse import Button, Controller
import time
import math as ma

log_path = "./logs/"
c_l = "click_log.txt"
if not os.path.exists(log_path):
    os.makedirs(log_path)
pos = 0
key_pos = 0

def log_writer(data, output, c_l):
    file = open(output+c_l, "a")
    file.write(f"{data[0]}, {data[1]} \n")
    file.close()

def on_click(x, y, button, pressed):
    global pos
    if pressed:
        pos = (x, y)
    if not pressed:
        return False

def on_press(key):
    try:
        print(f"alphanumeric key {key.char} pressed")
    except AttributeError:
        print(f"special key {key} pressed")

def on_release(key):
    #print('{0} released'.format(key))
    if key:
        return False

def map_count(ab1, ac1):
    #ab1, ac1 = input().split()
    ab1, ac1 = int(ab1), int(ac1)
    #ab1, ac1 = (-1250+int(ab1)), (-700+int(ac1))
    n = 60
    abb = ab1
    acc = ac1
    while ab1 > n or ac1 > n:
        ab1 /= 2
        ac1 /= 2
    ab1 = ma.fabs(ab1)
    ac1 = ma.fabs(ac1)
    
    if ab1 > ac1:
        ac = (n*ac1)/ab1
        ab = n
    elif ab1 < ac1:
        ab = (n*ab1)/ac1
        ac = n
    elif ab1 == ac1:
        ac, ab = n, n

    if acc < 0:
        ac = -ac
    if abb < 0:
        ab = -ab

    return ab, ac

def shoot(mou, dirY, dirX, range):
    t = 0.1**1.125
    dirX, dirY = map_count(dirX, dirY)
    #dirX/=2
    #dirY/=2
    mou.press(Button.left)
    time.sleep(t)
    mou.move(dirX, dirY)
    time.sleep(t)
    mou.release(Button.left)
    mou.move(-dirX, -dirY)

def nn():
    mou = Controller()
    # разворачивание окна
    mou.position = (460, 1400)
    mou.click(Button.left, 1)

    time.sleep(0.1)
    # начало игры
    an, bn = 1000, 700
    mou.position = (an, bn)
    mou.click(Button.left, 1)

    time.sleep(8.25)
    # боевая позиция
    mou.position = (an+200, bn-50)

    #for i in range(1,4):
    shoot(mou, 0, 200, 50)
    time.sleep(0.5)
    shoot(mou, 100, -100, 50)
    time.sleep(0.5)
    shoot(mou, -200, 0, 50)

    time.sleep(2.5)
    # скиншот
    #mou.position = (1225, 795)
    #mou.click(Button.left, 1)

    # выход из игры
    mou.position = (an-360, bn+10)
    mou.click(Button.left, 1)
    # сворачивание окна
    mou.position = (an+188, bn-680)
    mou.click(Button.left, 1)
    pass

for i in range(1):
    nn()
    #time.sleep(1)

while 0:
    with mouse.Listener(on_move=lambda x, y : None, on_click=on_click, on_scroll=lambda x, y, dx, dy : None) as listener:
        listener.join()
        #log_writer(pos, log_path, c_l)
        print(pos)



    #with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    #    listener.join()