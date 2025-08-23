from gtts import gTTS
import speech_recognition as sr
import  pyautogui
import os
import random
import playsound
import time

class KuramaAssistant:
    def __init__(self):
        self.running = False

    def run(self):
        self.running = True
        print("Kurama is listening...")

        while self.running:
            print("Listening...")
            time.sleep(2)  # Simulate listening every 2 seconds

    def stop(self):
        print("Kurama is stopped.")
        self.running = False


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

# ------------ This function is for listen and understand command -------
def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening.....")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source, timeout="", phrase_time_limit=4)

    try:
        print("Recognition ....\n ")
        query = r.recognize_google(audio, language='en-in')
        print(f"User : {query}")
    except Exception as e:
        print("Listening .....")
        return None
    return query

# Kurama.py

# Kurama.py


#--------------Main program -----------
speak("Hello sir")
if __name__ == "__main__":
    while True: 
        command = takecommand()
        if command:
            command = command.lower()
#<---- Normal conversation ---->
            if "wake up" in command:
                from conversation import hello_respond
                hello_respond()

            elif "how are you" in command or "how r u" in command or "are you ok " in command:
                from conversation import how_are_you 
                how_are_you()

            elif "sleep" in command or "deactive system" in command or "system deactive" in command or "stop" in command:
                from conversation import sleep_now
                sleep_now()
                break
#<---- Web browser ---->
            elif "search google" in command or "google search" in command or "search on google" in command or "open google" in command :
                from Google_Search import google_search
                google_search(command)

            elif "youtube" in command or "open youtube" in command or "play on youtube" in command or "open google" in command :
                from Google_Search import youtube_search
                youtube_search(command)

            elif "wikipedia" in command or "wikipedia search" in command or "search on wikipedia" in command or "open google" in command :
                from Google_Search import wikipedia_search
                wikipedia_search(command)
            
#<---- Weather and Time ---->
                
            elif "weather" in command or "temperature" in command:
                from Weather_time import get_weather
                weather_info = get_weather()
                speak(weather_info)

            elif "time" in command:
                from Weather_time import get_current_time
                speak(get_current_time())

            elif "date" in command or "day" in command:
                 from Weather_time import get_current_date
                 speak(get_current_date())

#<---- Web browser ---->
            elif "open" in command:
                from open_close_app import open_web
                open_web(command)

            elif "tab" in command:
                from open_close_app import tab_control
                tab_control(command)

            elif "window" in command or "minimize" in command or "maximize" in command or "close app" in command:
                from open_close_app import window_control
                window_control(command)

#<---- Laptop task ---->
            elif "snap left" in command:
                speak("Snapping window to the left")
                pyautogui.hotkey('win', 'left')

            elif "snap right" in command:
                speak("Snapping window to the right")
                pyautogui.hotkey('win', 'right')

#---- Youtube task ---->

            elif "pause" in command:
                speak("pause video .. ")
                pyautogui.hotkey('k')

            elif "forward" in command:
                speak("pause video .. ")
                pyautogui.hotkey('l')

            elif "backward" in command:
                speak("pause video .. ")
                pyautogui.hotkey('j')

        
  
                    
          

                            