# pip install speechrecognition pyttsx3 pyaudio
from datetime import datetime
import requests
import speech_recognition as sr
import pyttsx3
import webbrowser

# if msg == "hi" or msg == "hello" or msg == "hey" or msg == "hii" or msg == "hi there":
#     print("Hello how are you...!!!")
# else:
#     print("I didn't understand that.")

greet_keywords = ["hi", "hello", "hey", "hii", "hi there", "hey there", "hello there"]
date_intent = ["date","what is the date","what's the date","tell me the date","current date"]
time_intent = ["time", "current time", "what is the time", "what's the time", "tell me the time"]
news_intent = ["news", "current news", "what's the news", "tell me the news", "latest news"]
weather_intent = ["weather", "current weather", "what's the weather", "tell me the weather", "weather update"]


# Text to speech
engine = pyttsx3.init()
engine.setProperty("rate",170)
def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_input():
    print("Welcome to Chatbot...!!!")
#     print("""
# Please select your input method:
# 1. Keyboard Input
# 2. Voice Input
# """)
    # choice = int(input("Enter your choice (1 or 2): "))
    # if choice == 1:
    #     msg = input("Enter your message: ").lower()
    # elif choice == 2:
    #     # Speech to text
    #     rec = sr.Recognizer()
    #     with sr.Microphone() as source:
    #         print("Listening...")
    #         audio = rec.listen(source)
    #     try:
    #         query = rec.recognize_google(audio)
    #         print("You :",query)
    #         msg = query.lower()
    #     except:
    #         speak("Can't understand what you said...")
    #         return ""
    
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = rec.listen(source)
    try:
        query = rec.recognize_google(audio)
        print("You :",query)
        return query.lower()
    except:
        speak("Can't understand what you said...")
        return ""


def get_news():
    # API - Application Programming Interface
    url = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=695e07af402f4b119f0703e9b19f4683"
    response = requests.get(url)
    data = response.json()
    total_results = data["totalResults"]
    print("Total news articles found: ", total_results)
    articles = data["articles"]
    for i in range(12):
        print("News Title: ",articles[i]["title"])


def get_weather():
    ip_url = "http://ip-api.com/json/"
    location = requests.get(ip_url).json()
    lat = location['lat']
    lon = location['lon']
    print("Your current location is:",location['city'],location["country"])
    api_key = "83e01e3dce5d28839bb5a177cb51af12"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    print("Current Condition :",data["weather"][0]["description"])
    print("Current Temperature:",data["main"]["temp"])


chat = True

while chat:
    msg = take_input()
    
    if msg in greet_keywords:
        speak("Hello how are you...!!!")
    elif msg in date_intent:
        date = datetime.now().strftime("%d %b, %Y")
        speak(f"Today's date is: {date}")
    elif msg in time_intent:
        time = datetime.now().strftime("%I:%M:%S %p")
        speak(f"Current time is: {time}")
    elif msg in news_intent:
        print("Here are the latest news: ")
        get_news()
    elif msg in weather_intent:
        speak("The current weather is: ")
        get_weather()
    elif msg.startswith("open"):
        website = msg.split()[-1]     # ["open", "google"]
        webbrowser.open(f"https://www.{website}.com")
    elif msg == "exit" or msg == "bye":
        speak("Goodbye!")
        chat = False
    else:
        speak("I didn't understand that.")