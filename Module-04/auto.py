import pyautogui as pag
import time

# pag.alert("this is alert")Hello world!
time.sleep(5)
for i in range(1,5):
    time.sleep(3)
    pag.write('print("hello World")', interval=0.25)
    pag.press('enter')

