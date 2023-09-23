import time
import pyautogui
from Desktop_Search import *

# Apri Edge
pyautogui.hotkey('win', 'r')
pyautogui.typewrite('msedge')
pyautogui.press('enter')
time.sleep(5) # attendi che Edge si apra

desktop_search()

mobile_search()

#Chiudi Edge
pyautogui.hotkey('alt', 'f4')