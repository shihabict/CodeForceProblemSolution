import pyautogui
import time
pyautogui.FAILSAFE = False

for i in range(50):
    
    time.sleep(3)
    pyautogui.press('j')
    time.sleep(3)
    pyautogui.press('l')
    time.sleep(3)
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.press('enter')