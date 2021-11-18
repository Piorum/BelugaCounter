import os
import time
import math
import random
import keyboard
import pyautogui
import cv2 as cv
from PIL import Image
import win32api, win32con
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

output = '1'
outputL = '1'
def checknumber():
    global output
    img = pyautogui.screenshot(region=(380, 927, 60, 20))
    new_size=tuple(4*x for x in img.size)
    img = img.resize(new_size)
    img.save('ScreenshotRaw.png')
    img = cv.imread('ScreenshotRaw.png',0)
    ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
    blur = cv.GaussianBlur(thresh2,(5,5),0)
    ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    cv.imwrite('ScreenshotProccesed.png', th3)
    output = pytesseract.image_to_string(th3)
    symbols = ['i', 'l', '|', '!', 'I', ')', '(', ':', ';', ']', '[', '{', '}']
    for x in symbols:
        output = output.replace(x,'1')
    numeric_filter = filter(str.isdigit, output)
    output = "".join(numeric_filter)

while True:
    firstsleep = random.randint(2, 4)
    time.sleep(firstsleep)
    checknumber()
    if len(output) == 6:
        if int(outputL) != int(output):
            output = int(output) + 1
            outputL = output
            keyboard.write(str(output))
            time.sleep(1.2)
            checknumber()
            output = int(output) + 1
            if int(output) == int(outputL):
                keyboard.press_and_release('enter')
                time.sleep(11)
            else:
                if len(str(output)) == 6:
                    keyboard.press_and_release('ctrl+a')
                    keyboard.write(str(output))
                    keyboard.press_and_release('enter')
                    outputL = output
                    time.sleep(11)
                
