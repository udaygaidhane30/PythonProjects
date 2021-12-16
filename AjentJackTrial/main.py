import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def welcome():
    curr_hour = datetime.datetime.now().hour
    if 0 < curr_hour < 12:
        speak("Good Morning Sir")

    elif 12 < curr_hour < 16:
        speak("Good Afternoon Sir")

    else:
        speak("Good evening Sir")

    speak("My name is Agent Jack")
    speak(f"Today is {datetime.datetime.now().strftime('%A')}")


def take_command():
    r = sr.Recognizer
    with sr.Microphone as source:
        print("Listening....")
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        print("Sorry I could not understand")
        return "None"

    return query


welcome()

