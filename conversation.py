from gtts import gTTS
import datetime
import speech_recognition as sr
import os
import random
import playsound

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

#----------- 1. Response for Hello ----------------
def hello_respond():
    def conversation():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            return ("Good Morning, sir")

        elif hour>=12 and hour<=18:
            return ("Sir")

        else:
            return ("Good Evening. sir")

    hello_responses = [
    "Yes sir!",
    "Hello, how can I assist you ?",
    "I’m here ",
    "Greetings! What do you need?",
    "Ready sir",
    "Hello sir",
    "At your service!",
    "Hey! What’s the task?",
    "Online and listening!",
    "Here I am, sir!",
    "Welcome back! What’s next?","Kurama speking sir","system active sir",conversation()]

    response = random.choice(hello_responses)
    speak(response)

#----------- 1. Response for How are you ----------------
def how_are_you():
    how_are_you_responses = [
    "I'm good sir!",
    "Doing great sir!",
    "All systems go sir!",
    "Feeling sharp sir!",
    "Perfectly fine sir!",
    "Ready as ever sir!",
    "No complaints sir!",
    "Running smoothly sir!",
    "Doing just fine sir!",
    "Alive and alert sir!",
    "Operating at full power sir!"]
    response = random.choice(how_are_you_responses)
    speak(response)



def sleep_now():
    sleep_now_responses = [
    "Going offline, sir.",
    "Shutting down.",
    "Okay, going to sleep.",
    "Call me when you need me.",
    "Powering down.",
    "I'll be here if you need me.",
    "Resting now.",
    "Taking a break.",
    "See you soon, sir.",
    "Sleeping now.",
    "Alright, switching off."]
    response = random.choice(sleep_now_responses)
    speak(response)






