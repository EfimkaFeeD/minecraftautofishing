from numpy import array
from time import sleep
from multiprocessing import Process
from ahk import AHK
from PIL import ImageGrab
import pytesseract
import cv2
ahk = AHK()

def fishing_bot():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    while True:
        sleep(0.2)
        fish = ImageGrab.grab(bbox=(1652, 961, 1900, 979))
        fishing_temp = pytesseract.image_to_string(cv2.cvtColor(array(fish), cv2.COLOR_BGR2GRAY), lang='eng')
        fishing = fishing_temp.strip()
        if fishing == 'Fishing Bobber splashes':
            print(fishing)
            sleep(0.3)
            ahk.right_click()
            print('gottem')
            sleep(2)
            ahk.right_click()
            print('less go')

def eating_bot():
    while True:
        sleep(900)
        ahk.send_input('2')
        sleep(0.2)
        ahk.key_down('RButton')
        sleep(2)
        ahk.key_up('RButton')
        sleep(0.2)
        ahk.send_input('1')
        sleep(0.2)
        ahk.right_click()

if __name__ == '__main__':
    fb = Process(target=fishing_bot)
    fb.start()
    eb = Process(target=eating_bot)
    eb.start()
