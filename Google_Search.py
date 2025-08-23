from gtts import gTTS
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
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

def google_search(query):
    if "google" in query :
        if "open google" in query.strip():
             speak("Opening Google...")
             webbrowser.open("https://www.google.com")
        else:
            import wikipedia as googleScrap
            query = query.replace("search google", "").replace("google search", "")
            query = query.replace("search on goole","").replace("torch on google","").replace("open google","")
            speak("Searching...")
            try:
                pywhatkit.search(query)
                result = googleScrap.summary(query,1)
            except:
                print("")

def youtube_search(query):
    if "youtube" in query:
        if "open youtube" in query.strip():
            speak("opening youtube ...")
            webbrowser.open("https://www.youtube.com")

        elif "youtube search" in query.strip() or "seartching on youtube" in query.strip():
            query = query.replace("youtube search","").replace("search on youtube","")
            speak("Searching .... ")
            web = "https://www.youtube.com/results?search_query="+query
            webbrowser.open(web)
        else:
            speak(("playing video .... "))
            query = query.replace("youtube search","").replace("search on youtube","")
            web = "https://www.youtube.com/results?search_query="+query
            webbrowser.open(web)
            pywhatkit.playonyt(query)

def wikipedia_search(query):
    if "wikipedia"in query:
        speak("Searching from wikipedia .... ")
        query = query.replace("wikipedia","").replace("wikipedia search","")
        query = query.replace("search on wikipedia","")
        result = wikipedia.summary(query,sentences = 1)
        speak("According to wikipedia ... ")
        print(result)
        speak(result)
   
                