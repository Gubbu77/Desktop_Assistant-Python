import os
import pyttsx3 as tts
import speech_recognition as sr
from selenium import webdriver
import datetime
import psutil
import pyjokes


dateTime = datetime.datetime.now()
day = dateTime.strftime("%A")
month = dateTime.strftime("%B")
date = dateTime.strftime("%d")
year = dateTime.strftime("%Y")
hour = dateTime.strftime("%H")
min = dateTime.strftime("%M")

engine = tts.init()
def assistant_speak(output) :

    engine.say(output)
    engine.runAndWait()

def greetings():
    h = int(datetime.datetime.now().hour)
    if h >= 0 and h < 12:
        assistant_speak("Good Morning sir.")

    elif h>= 12 and h< 18:
        assistant_speak("Good afternoon sir")

    else:
        assistant_speak("Good night sir")

def get_audio():
    recognizer = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print('Recognizing..')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

        # audio = recognizer.listen(source, phrase_time_limit= 5)
    print('Stop')

    try:
        text = recognizer.recognize_google(audio, language= 'en-US')
        print('You : ', text)
        return text

    except:
        assistant_speak("Sorry sir, Could not recognize your voice")
        get_audio()
        return "None"


# close app

def close_app(app_name) :
    running_apps = psutil.process_iter(['pid', 'name'])  # returns names of running processes
    found = False
    for app in running_apps :
        sys_app = app.info.get('name').split('.')[0].lower()

        if sys_app in app_name.split() or app_name in sys_app :
            pid = app.info.get('pid')  # returns PID of the given app if found running

            try :  # deleting the app if asked app is running.(It raises error for some windows apps)
                app_pid = psutil.Process(pid)
                app_pid.terminate()
                found = True
            except :
                pass

        else :
            pass
    if not found :
        assistant_speak(app_name + "not found running")
    else :
        assistant_speak(app_name + "closed")


def openApp(text):

    text = text.lower()


    if 'open chrome' in str(text) or 'open google' in str(text) or 'google chrome' in str(text):
        assistant_speak('Opening Google Chrome')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        return


    elif 'open file'  in str(text) or 'files'  in str(text).lower() or 'file'  in str(text):
        assistant_speak('Opening file explorer')
        os.startfile("C:\Windows\explorer.exe")
        return

    elif 'open youtube'  in str(text) or 'youtube'  in str(text).lower():
        assistant_speak('Opening Youtube')
        os.startfile("C:\wssistantApps\YouTube.lnk")
        return

    elif 'gmail' in str(text) or 'email' in str(text) or 'my email' in str(text) or 'gmail' in str(text) :
        assistant_speak('Opening Gmail')
        os.startfile("C:\wssistantApps\Gmail.lnk")
        return

    elif 'vscode' in str(text) or 'visual studio' in str(text) or 'visual studio code' in str(text) or 'code' in str(text) :
        assistant_speak('Opening Visual studio code')
        os.startfile("C:\Program Files\Microsoft VS Code\Code.exe")
        return

    elif 'terminal' in str(text) or 'cmd' in str(text) or 'black screen' in str(text) or 'command prompt' in str(text):
        os.startfile("C:\wssistantApps\Command Prompt.lnk")
        assistant_speak('Opening Command Prompt')
        return

    elif 'telegram' in str(text) or 'tele' in str(text) or 'open telegram' in str(text):
        os.startfile("C:\wssistantApps\Telegram.lnk")
        assistant_speak('Opening Telegram')
        return
    else:
        assistant_speak('Cannot find that application')
        return



def closeApp(text):

    text = text.lower()

    if "chrome" in text or "google" in text:
        assistant_speak("Closing Chrome")
        close_app("chrome")
        return

    elif "files" in text or "file" in text or "file explore" in text :
        assistant_speak("Closing File explore")
        close_app("explorer")
        return

    elif "youtube" in text or "tube" in text :
        assistant_speak("Closing Youtube")
        close_app("youtube")
        return

    elif "telegram" in text or "tele" in text :
        assistant_speak("Closing Telegram")
        close_app("telegram")
        return

    elif "terminal" in text or "cmd" in text :
        assistant_speak("Closing command prompt")
        close_app("command prompt")
        return

    elif "pycharm" in text or "pycharm" in text :
        assistant_speak("Closing Pycharm")
        close_app("pycharm")
        return

    elif "vscode" in text or "visual studio" in text :
        assistant_speak("Closing visual studio code")
        close_app("visual studio code")
        return

def jokes():
    jokes = pyjokes.get_joke(language= 'en', category= 'neutral')
    assistant_speak(jokes)

def process_text(text):
    try:
        if 'search' in text or 'play' in text:
            pass
            return

        elif "who are you" in text or "define yourself" in text:
            about = '''Hello i am Jarvis, Iam your personal assistant created by indrajith, 
             I can help you with whatever you ask or to do.'''
            assistant_speak(about)
            return


        elif 'how are you' in text:
            assistant_speak("I am fine, Thank you")
            assistant_speak("How are you, Sir")


        elif 'fine' in text or "good" in text:
            assistant_speak("It's good to know that your fine")


        elif "what's the time" in text or "time" in text:
            assistant_speak(hour + min)
            return

        elif "what's the date today" in text or "date" in text:
            assistant_speak(date + month)
            return

        elif "date and year" in text or "year" in text:
            assistant_speak(day + date + month + year)
            return


        elif "tell me a joke" in text or "jokes" in text or "joke" in text or 'tell joke' in text or "make me laugh" in text:
            assistant_speak("Ok joke coming")
            jokes()
            return


        elif "open" in text:
            openApp(text)
            return

        elif "close" in text or "stop" in text or "kill" in text or "exit" in text:
            closeApp(text)
            return


    except :

        assistant_speak("I don't understand, I can search the web for you, Do you want to continue?")

if __name__ == "__main__" :
    greetings()

    text = get_audio()


    if "hey jarvis" in str(text).lower() or "jarvis" in str(text).lower() or  "hello jarvis" in str(text).lower() or "hello" in text.lower() or "hi" in text.lower() or "hey" in text.lower():
        assistant_speak("yes sir")
        # assistant_speak('''Welcome sir, Iam your personal assistant Jarvis''')

        assistant_speak("What can i do for you?")
        while (1) :


            text = get_audio()

            if text == 0 :
                continue

            if "bye" in str(text).lower() or "sleep" in str(text).lower() :
                assistant_speak("See you later sir, take care.")
                break

            process_text(text)
