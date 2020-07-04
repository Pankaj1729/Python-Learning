import pyttsx3
import datetime
import speech_recognition as sr
import p
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Jarvis Sir. How may i help you!")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listen....")
        r.pause_threshold=1#if stop 1 sec
        audio=r.listen(source)

    try:
        print("Recognizing....")
        quary=r.recognize_google(audio,language='en-in')
        print("User said: ",quary)

    except Exception as e:
        #print(e)#for print error
        print("Sorry sir! I can't understand ")
        print("please speak again")
        return "None"
    return quary
if __name__=='__main__':
    speak("Hello Pankaj Sir")
    wishme()
    takecommand()

