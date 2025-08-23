from gtts import gTTS
import speech_recognition as sr
import webbrowser
import pyautogui
import os
from time import sleep
import random
import playsound
#----------- This function is for speak -------
def speak(text):
    print("Kurama:", text)
    try:
        tts = gTTS(text=text, lang='en')
        filename = f"voice_{random.randint(1,10000)}.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("Error:", e)

disapp = {
    "cmd": "cmd",
    "photoshop": r"D:\Application\Adobe Software\Photoshop 2023\Adobe Photoshop 2023\Photoshop.exe",
    "vs code": "Visual Studio Code",
    "browser": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    "premiere pro": r"D:\Application\Adobe Software\Premiere pro 2023\Adobe Premiere Pro 2023\Adobe Premiere Pro.exe",
    "after effect": r"C:\Program Files\Adobe\Adobe After Effects 2023\Support Files\AfterFX.exe",
    "obs": r"D:\Application\OBS\obs-studio\bin\64bit\obs64.exe"
}


def open_web(query):
    if "open task manager" in query:
        speak("Opening task manager")
        pyautogui.hotkey('ctrl', 'shift', 'esc')

    elif "open task view" in query:
        speak("Opening task view")
        pyautogui.hotkey('win', 'tab')
    
    elif "open setting" in query:
                speak("opening setting .... ")
                pyautogui.hotkey('win', 'i')

    elif "open file manager" in query:
        speak("opening file manager .... ")
        pyautogui.hotkey('win', 'e')

    elif ".com" in query or ".org" in query:
        query = query.replace("open", "").replace("launch", "").replace("%20", "").replace(" ", "")
        speak(f"Opening {query}")
        webbrowser.open(f"https://www.{query}")
    else:
        for app in disapp:
            if app in query.lower():
                path = disapp[app]
                speak(f"Opening {app}")
                os.system(f'start "" "{path}"')


def tab_control(query):
    
    if "forward tab" in query:
        speak("Ok sir")
        pyautogui.hotkey("ctrl", "tab")

    elif "previous tab" in query:
        speak("Ok sir")
        pyautogui.hotkey("ctrl", "shift", "tab")

    elif "reopen tab" in query or "restore tab" in query:
        speak("Ok sir")
        pyautogui.hotkey("ctrl", "shift", "t")

    elif "private tab" in query or "incognito" in query:
        speak("Ok sir")
        pyautogui.hotkey("ctrl", "shift", "n")

    elif "new tab" in query:
        speak("Ok sir")
        pyautogui.hotkey("ctrl", "t")

    elif "close tab" in query:
        speak("Ok sir")
        pyautogui.hotkey("ctrl", "w")


    elif "refresh tab" in query:
        speak("Ok sir")
        pyautogui.hotkey("ctrl", "r")


    elif "switch to tab" in query:
        speak("Ok sir")
        for i in range(1, 9):
            if f"tab {i}" in query:
                pyautogui.hotkey("ctrl", str(i))
                break

    else:
        speak("Sorry, I didn’t understand the tab command.")


def window_control(query):
    if "maximize window" in query:
        speak("Maximizing window")
        pyautogui.hotkey('alt', 'space','n')

    elif "close window" in query or "close app" in query:
        speak("Closing window")
        pyautogui.hotkey('alt', 'f4')

    elif "show window" in query:
        speak("Showing desktop")
        pyautogui.hotkey('win', 'd')

    elif "restore windows" in query:
        speak("Restoring all windows")
        pyautogui.hotkey('win', 'shift', 'm')

    else:
        speak("Sorry, I didn't understand the window command.")


    

    

    

    
    


