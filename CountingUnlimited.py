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

nameoutput = '1'
nonpermitted = ['memow', 'gigi']
def checkname():
    global nameoutput
    img = pyautogui.screenshot(region=(380, 905, 300, 20))
    new_size=tuple(4*x for x in img.size)
    img = img.resize(new_size)
    img.save('NameScreenshotRaw.png')
    img = cv.imread('NameScreenshotRaw.png',0)
    nameoutput = pytesseract.image_to_string(img)
    nameoutput = nameoutput.partition(" ")[0]

output = '1'
outputL = '1'
def checknumber():
    global output
    img = pyautogui.screenshot(region=(380, 927, 60, 20))
    new_size=tuple(4*x for x in img.size)
    img = img.resize(new_size)
    img.save('ScreenshotRaw.png')
    img = cv.imread('ScreenshotRaw.png',0)
    output = pytesseract.image_to_string(img)
    symbols = ['i', 'l', '|', '!', 'I', ')', '(', ':', ';', ']', '[', '{', '}']
    for x in symbols:
        output = output.replace(x,'1')
    numeric_filter = filter(str.isdigit, output)
    output = "".join(numeric_filter)
while True:
    try:
        time.sleep(3)
        permissable = True
        checkname()
        for name in nonpermitted:
            if name == nameoutput:
                permissable = False
        if permissable == True:
            checknumber()
            if len(output) == 6:
                if int(outputL) != int(output):
                    output = int(output) + 1
                    outputL = output
                    keyboard.press_and_release('ctrl+a')
                    keyboard.write(str(output))
                    keyboard.press_and_release('enter')
                    time.sleep(10)
    except:
        print('*ERROR*')
        try:
            keyboard.press_and_release('ctrl+a')
            time.sleep(15)
        except:
            print('***CRITICAL ERROR***')
        
                
