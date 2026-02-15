from datetime import datetime
import requests
import webbrowser

greet_keywords = ["hi", "hello", "hey", "hii", "hi there", "hey there", "hello there"]
date_intent = ["date","what is the date","what's the date","tell me the date","current date"]
time_intent = ["time", "current time", "what is the time", "what's the time", "tell me the time"]
news_intent = ["news", "current news", "what's the news", "tell me the news", "latest news"]
weather_intent = ["weather", "current weather", "what's the weather", "tell me the weather", "weather update"]



def get_news():
    # API - Application Programming Interface
    url = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=695e07af402f4b119f0703e9b19f4683"
    response = requests.get(url)    # will make HTTPRequest to the url and get response
    data = response.json()  # in response we have json type of data
    # In Python JSON gets converted into Python dictionary object {key:value}
    articles = data["articles"]
    news_articles = []
    for i in range(12):
        news_articles.append(articles[i]["title"])
    return news_articles


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
    # print("Current Condition :",data["weather"][0]["description"])
    # print("Current Temperature:",data["main"]["temp"])
    return data["main"]["temp"]


def main(msg):
    msg = msg.lower()
    if msg in greet_keywords:
        response = "Hello how are you...!!!"
    elif msg in date_intent:
        date = datetime.now().strftime("%d %b, %Y")
        response = f"Today's date is: {date}"
    elif msg in time_intent:
        time = datetime.now().strftime("%I:%M:%S %p")
        response = f"Current time is: {time}"
    elif msg in news_intent:
        response = get_news()
    elif msg in weather_intent:
        response = get_weather()
    elif msg.startswith("open"):
        website = msg.split()[-1]     # ["open", "google"]
        webbrowser.open(f"https://www.{website}.com")
    elif msg == "exit" or msg == "bye":
        response = "Goodbye!"
    else:
        response = "I didn't understand that."
    return response