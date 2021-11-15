import os
import time
import math
import keyboard
import pyautogui
import cv2 as cv
from PIL import Image
import win32api, win32con
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

output = '1'
outputL = '1'

while True:
    time.sleep(2)
    try:
        img = pyautogui.screenshot(region=(380, 936, 60, 20))
        new_size=tuple(4*x for x in img.size)
        img = img.resize(new_size)
        img.save('ScreenshotRaw.png')
        img = cv.imread('ScreenshotRaw.png',0)
        ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
        blur = cv.GaussianBlur(thresh2,(5,5),0)
        ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
        cv.imwrite('ScreenshotProccesed.png', th3)
        output = pytesseract.image_to_string(th3)
        symbols = ['i', 'l', '|', '!', 'I']
        for x in symbols:
            output = output.replace(x,'1')
        numeric_filter = filter(str.isdigit, output)
        output = "".join(numeric_filter)
        if len(output) == 6:
            if int(outputL) != int(output):
                output = int(output) + 1
                keyboard.write(str(output))
                keyboard.press_and_release('enter')
                outputL = output
                time.sleep(11)
    except:
        print("ERROR: '" + str(output) + "' '" + str(outputL) + "'")
