import os
try:
    import pyttsx3
except:
    print("pyttsx3 module is not installed")
    in2 = input(
        "This program needs pyttsx3 module, do you want to install (y or n): ")
    if (in2 == "y"):
        os.system("pip install pyttsx3")
    elif (in2 == "n"):
        print("You can install menually by:")
        print("pip install pyttsx3")
        exit()
    else:
        exit()

from time import sleep
from pyttsx3 import speak


def ps(msg):
    print(msg)
    speak(msg)
    print()


ps("Welcome")
ps("Hello coder")
ps("I am bot")

while (True):
    ps("Enter what do you want: ")
    inp = input("Enter: ")

    if (("exit" in inp) or ("close" in inp)):
        ps("Have a nice day :)")
        exit()
    elif (("launch" in inp) or ("open" in inp) or ("start" in inp)):
        if (("notepad" in inp) or ('text-editor' in inp) or ("text editor" in inp)):
            speak("opening notepad")
            sleep(5)
            os.system("notepad")
        elif (("chrome" in inp) or ("browser" in inp)):
            speak("opening chrome")
            sleep(5)
            os.system("start chrome")
        elif ("firefox" in inp):
            speak("opening firefox")
            sleep(5)
            os.system("start firefox")
        elif (("video player" in inp) or ("music player" in inp) or ("media player" in inp)):
            speak("opening media player")
            sleep(5)
            os.system("start wmplayer")
        elif (("file explorer" in inp) or ("explorer" in inp)):
            speak("opening explorer")
            sleep(5)
            os.system("explorer")
        else:
            ps("Sorry! but this not supported")
