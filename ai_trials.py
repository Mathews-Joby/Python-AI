import webbrowser as wb
import wikipedia
import time
import datetime
import speech_recognition as understand
import pyttsx3
import subprocess
import os
import pynput
import pywhatkit
from pynput.keyboard import Key, Controller

keyboard = Controller()
engine = pyttsx3.init()
while True:
    

    user = input("                                  YOU: ")
    

    if "play" in user:
        song=user.replace("play","")
        pywhatkit.playonyt(song)
    elif "open" in user:
        engine.say("i can open chrome, microsoft edge and websites")
        engine.runAndWait()
        engine.say("you can also ask me to open.exe file by typing it")
        engine.runAndWait()        
        if "chrome" or "google" or "google chrome" in user:
            os.startfile('chrome.exe')
        if "edge" in user:
            os.startfile('msedge.exe')
            time.sleep(0.2)
            keyboard.press(Key.ctrl)
            keyboard.press("w")
            keyboard.release(Key.ctrl)
            keyboard.release("w")
        if "python" in user:
            os.startfile('python.exe')
            time.sleep(0.01)
            keyboard.press(Key.ctrl)
            keyboard.press("w")
            keyboard.release(Key.ctrl)
            keyboard.release("w")
        if "exe" in user:
            try:
                program = user.replace("open ","")
                os.startfile(program)
            except:
                engine.say("file not found! try again")
                engine.runAndWait()
        




    #os.startfile('chrome.exe')
    #os.startfile('Unity Hub.exe')
