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
firstsleep = '1'
breaktrigger = random.randint(10,20)
breakcount = 0
delaycheck = 0
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

def breaktime():
    global breaktrigger
    global breakcount
    breakcount += 1
    if breakcount >= breaktrigger:
        sleeptime = random.randint(12600,24200)
        print("Sleeping for " + str(sleeptime) + " seconds.")
        time.sleep(sleeptime)
        breaktrigger = random.randint(250,300)
        breakcount = 0
        print("Sleep is over.")
while True:
    try:
        firstsleep = random.randint(2, 3)
        time.sleep(firstsleep)
        checknumber()
        if len(output) == 6:
            if delaycheck >= 24:
                time.sleep(delaycheck)
                keyboard.press_and_release('ctrl+a')
                keyboard.write(str(output))
                keyboard.press_and_release('enter')
                time.sleep(9)
                breaktime()
                delaycheck = 0
            if int(outputL) != int(output):
                time.sleep(delaycheck)
                output = int(output) + 1
                outputL = output
                keyboard.press_and_release('ctrl+a')
                keyboard.write(str(output))
                time.sleep(2)
                checknumber()
                output = int(output) + 1
                if int(output) == int(outputL):
                    keyboard.press_and_release('enter')
                    time.sleep(9)
                    breaktime()
                    delaycheck = 0
                else:
                    if len(str(output)) == 6:
                        keyboard.press_and_release('ctrl+a')
                        keyboard.write(str(output))
                        keyboard.press_and_release('enter')
                        outputL = output
                        time.sleep(9)
                        breaktime()
                        delaycheck = 0
                    else:
                        delaycheck += random.randint(0,3)
            else:
                delaycheck += random.randint(0,3)
    except:
        print('ERROR')
        print('output: ' + str(output))
        print('outputL: ' + str(outputL))
        print('firstsleep: ' + str(firstsleep))
        print('breaktrigger: ' + str(breaktrigger))
        print('breakcounter: ' + str(breakcount))
        print('delaycheck: ' + str(delaycheck))
        try:
            keyboard.press_and_release('ctrl+a')
            time.sleep(15)
            breaktime()
        except:
            print('***CRITICAL ERROR ABORT ABORT ABORT***')
        
                
