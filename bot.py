import time
import math
import keyboard
import pyautogui
import win32api, win32con
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

output = '1'
outputL = '1'

while True:
    time.sleep(2.5)
    try:
        img = pyautogui.screenshot(region=(380, 936, 60, 20))
        new_size=tuple(8*x for x in img.size)
        img = img.resize(new_size)
        output = pytesseract.image_to_string(img)
        numeric_filter = filter(str.isdigit, output)
        output = "".join(numeric_filter)
        if int(outputL) != int(output):
            output = int(output) + 1
            keyboard.write(str(output))
            keyboard.press_and_release('enter')
            outputL = output
            time.sleep(10)
    except:
        print('ERROR: ' + str(output) + ' ' + str(outputL))
