import os
import pyautogui
from PIL import ImageGrab
from time import sleep
##the window must be precicely positionwd for this to work!!
x=1402#cordinates from top folloing button
y=347
sleep(5)# time to focus on the relevant window

while True:

    px = ImageGrab.grab().load()


    while y<1320: #bottom end cordinate
        color = px[x, y]
        print (y)
        if color== (0, 0, 0):#color black from the folow button?
            pyautogui.click(x, y)

            sleep(1)
            print("---")
            print(y)
            y=y+15
        y=y+15


    pyautogui.press('pagedown')
    y=347
