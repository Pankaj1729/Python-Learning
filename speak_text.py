import speech_recognition as sr
import speak

r=sr.Recognizer()
with sr.Microphone() as source:
    print("speak something")
    audio = r.listen(source)

try:
    text=r.recognize_google(audio)
    print("you said that :"+text)
    lang = 'en'

#speak.tts(text,lang)
except Exception as e:
    print(e)
