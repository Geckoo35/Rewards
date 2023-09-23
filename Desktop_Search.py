import time
import pyautogui

def desktop_search ():

    # Cerca i numeri da 1 a 30 su Google
    for i in range(26, 55):

        # Digita il numero da cercare
        
        pyautogui.typewrite(str(i))
        time.sleep(0.5)
        pyautogui.press('enter')

        # Attendi il caricamento dei risultati
        time.sleep(2) # attendi che i risultati si caricano

        # Torna alla pagina di ricerca di Google
        pyautogui.hotkey('ctrl', 'e')

        time.sleep(2) # attendi che i risultati si caricano

    # Cerca i numeri da 1 a 30 su Google
    for i in range(60, 71):

        # Digita il numero da cercare
        pyautogui.typewrite(str(i))
        time.sleep(0.5)
        pyautogui.press('enter')

        # Attendi il caricamento dei risultati
        time.sleep(2) # attendi che i risultati si caricano

        # Torna alla pagina di ricerca di Google
        pyautogui.hotkey('ctrl', 'e')

        time.sleep(2) # attendi che i risultati si caricano

def mobile_search ():

    pyautogui.hotkey('F12')
    time.sleep(5)
    pyautogui.moveTo(x=555, y=335)
    time.sleep(5)
    pyautogui.click()
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'e')
    time.sleep(5)

    # Cerca i numeri da 1 a 30 su Google
    for i in range(2, 25):

        # Digita il numero da cercare
        pyautogui.typewrite(str(i))
        time.sleep(0.5)
        pyautogui.press('enter')

        # Attendi il caricamento dei risultati
        time.sleep(2) # attendi che i risultati si caricano

        # Torna alla pagina di ricerca di Google
        pyautogui.hotkey('ctrl', 'e')

        time.sleep(2) # attendi che i risultati si caricano