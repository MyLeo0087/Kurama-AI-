import requests
from dotenv import load_dotenv
import os
from datetime import datetime
API_KEY="67ddbc19ac10d900e9c9170ee5d4b628"


def get_weather():
    city = "Nepalgunj,NP"
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            return "I couldn't get the weather for Nepalgunj."

        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        return f"The temperature in Nepalgunj is {temp}°C with {condition}."
    
    except Exception as e:
        print("Error:", e)
        return "Something went wrong while checking the weather."
    
def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")  # e.g., 04:35 PM
    return f"It's {current_time}."

def get_current_date():
    now = datetime.now()
    current_date = now.strftime("%A, %B %d, %Y")  # e.g., Tuesday, August 5, 2025
    return f"Today is {current_date}."

