import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests
import pyjokes
import random
import time
from dotenv import load_dotenv


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('234harshsingh@gmail.com', 'ifkl sqvf qopp raec')  # Use your email and App Password here
        server.sendmail('234harshsingh@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")
        speak("I'm sorry, I couldn't send the email. Please try again later.")

# Email list
email_list = {
    "Avkesh": "singhavkesh363@gmail.com",
    "Harsh": "john@example.com",
    "Sonu": "jane@example.com"
}

def emailToRecipient():
    speak("Which email address would you like to send an email to?")
    for name in email_list.keys():
        speak(name)

    recipient_name = takeCommand().lower()
    if recipient_name in email_list:
        to = email_list[recipient_name]
        speak("What should I say?")
        content = takeCommand()
        try:
            sendEmail(to, content)
        except Exception as e:
            print(f"Error: {e}")
            speak("I'm sorry, there was an error sending the email.")
    else:
        speak("Sorry, I couldn't find that email address.")

# Weather Feature
def getWeather(city):
    api_key = "your_actual_openweathermap_api_key"  # Replace with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    
    print(data)  # Inspect the response
    
    if data.get("cod") != 404:
        weather = data.get("main", {})
        if weather:
            temperature = weather.get("temp")
            description = data["weather"][0].get("description", "no description available")
            speak(f"The temperature in {city} is {temperature} degrees Celsius with {description}.")
        else:
            speak("Weather information is not available.")
    else:
        speak("City not found, please try again.")

def getNews():
    api_key = "8f9286a641ba45a190089005a38b9c7a"
    print(f"Loaded API Key: {api_key}")
    news_url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    
    try:
        response = requests.get(news_url)
        response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)
        
        response_json = response.json()
        print(response_json)  # Inspect the response

        if "articles" in response_json and response_json["articles"]:
            articles = response_json["articles"]
            speak("Here are the top headlines.")
            for article in articles[:5]:
                speak(article["title"])
        else:
            print("No articles found.")
            speak("I'm sorry, I couldn't find any news articles at the moment.")
    except Exception as e:
        print(f"Error fetching news: {e}")
        speak("I'm sorry, I couldn't fetch the news at the moment.")

# Task Management
tasks = []

def addTask():
    speak("What task would you like to add?")
    task = takeCommand()
    tasks.append(task)
    speak(f"Task '{task}' added to your list.")

def showTasks():
    if tasks:
        speak("Here are your tasks.")
        for task in tasks:
            speak(task)
    else:
        speak("You have no tasks.")

# Fun Feature: Jokes and Facts
def tellJoke():
    joke = pyjokes.get_joke()
    speak(joke)

def funFact():
    facts = ["Honey never spoils.", "Bananas are berries, but strawberries are not.", "A day on Venus is longer than a year."]
    speak(random.choice(facts))

# System Control
def systemControl(command):
    if 'shutdown' in command:
        os.system("shutdown /s /t 1")
    elif 'restart' in command:
        os.system("shutdown /r /t 1")
    elif 'log off' in command:
        os.system("shutdown -l")

# Browser Search
def searchGoogle(query):
    speak('Searching Google...')
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Alarms
def setAlarm(alarm_time):
    speak(f"Alarm set for {alarm_time}.")
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            speak("Time to wake up!")
            break

# Calculator
def calculator(command):
    try:
        command = command.replace("calculate", "").strip()
        result = eval(command)
        speak(f"The result is {result}.")
    except:
        speak("Sorry, I couldn't calculate that.")

# Main Loop
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'open wikipedia' in query:                # not working properly
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:               #working
            webbrowser.open("youtube.com")

        elif 'open google' in query:               #working
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:              #working
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:                         #working
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'Jarvis What was the Current time' in query:        #not working
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'Jarvis Open VScode' in query:           #working
            codePath = "C:\\Users\\234ha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'Jarvis Send Email' in query:                      #working
            emailToRecipient()

        elif 'Jarvis give me Weather Report' in query:                   #not working
            speak("Which city's weather would you like to know?")
            city = takeCommand()
            getWeather(city)

        elif 'news' in query:                         #not working
            getNews()

        elif 'Jarvis Add task' in query:                   #working
            addTask()

        elif 'Jarvis Show tasks' in query:                #working
            showTasks()

        elif 'Jarvis tell me a joke' in query:                    #working
            tellJoke()

        elif 'fun fact' in query:      #working
            funFact()

        elif 'shutdown' in query or 'restart' in query or 'log off' in query:               #
            systemControl(query)

        elif 'search google' in query:
            query = query.replace("search google for", "")
            searchGoogle(query)

        elif 'Jarvis set alarm' in query:                          #not working
            speak("What time should I set the alarm for?")
            alarm_time = takeCommand()
            setAlarm(alarm_time)

        elif 'Jarvis calculate' in query:             #not working
            calculator(query)
