import os
import pyautogui
from PIL import ImageGrab
from time import sleep
##the window must be precicely positionwd for this to work!!
x=1302#cordinates from top folloing button
y=315
sleep(5)# time to focus on the relevant window

while True:
    px = ImageGrab.grab().load()

    while y<1130: #bottom end cordinate
        color0 = px[x, y]
        if color0== (0, 0, 0):#color black from the folow button?
            i=1
            while i<72:#Segmento de recta d 72pixels que deverá ser preto do botao follow
                color1 = px[x+i, y]       
                colorT = tuple(map(sum, zip(color0,color1)))
                i=i+1
            if colorT== (0, 0, 0):#color black from the folow button ad 70 pixels rigt?
                print(colorT)
                pyautogui.click(x+89, y+17)#click reposition
                y=y+42#abaixo do botao
                sleep(1)
                print("---")
                print(y)
        y=y+4
    pyautogui.press('pagedown')
    y=315

