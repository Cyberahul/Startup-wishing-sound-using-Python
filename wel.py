import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate=engine.getProperty('rate')
volume=engine.getProperty('volume')
engine.setProperty('rate',100)
engine.setProperty('volume', 100)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.stop()
    exit()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Dear Rahul, All set to use your PC")
        #speak("I am your Friend, All set to use your PC")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Dear Rahul, All set to use your PC")
        #speak("I am your Friend, All set to use your PC")
    else:
        speak("Good Evening Dear Rahul, All set to use your PC")
        #speak("I am your Friend, All set to use your PC")

if __name__=="__main__":
    wishme()
