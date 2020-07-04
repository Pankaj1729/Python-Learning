import pyttsx3
k=pyttsx3.init()#for initiate the module
def speak(s):
    k.speak(s)
    k.runAndWait()
speak("Hello sir! I am Jarvis write anything you want to liten it") 
str1=("input anything ")
speak(str1)
