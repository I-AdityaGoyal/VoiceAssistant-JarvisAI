import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
from Body import Speak

def OpenExe(Query):
    Query = str(Query).lower()
    
    if "visit" in Query:
        Nameofweb = Query.replace("visit ", "")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True
    
    elif "launch" in Query:
        Nameofweb = Query.replace("launch ", "")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True
    
    elif "open" in Query:
        Nameoftheapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    
    elif "start" in Query:
        Nameoftheapp = Query.replace("start ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    
    elif "show" in Query:
        Nameoftheapp = Query.replace("show ","")
        keyboard.press('win')
        # sleep(1)
        # keyboard.write(Nameoftheapp)
        # sleep(1)
        keyboard.press('d')
        sleep(0.5)
        return True
    
    
