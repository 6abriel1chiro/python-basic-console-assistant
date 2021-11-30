# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:36:15 2021

@author: Gabriel Ichiro
"""

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pymongo
listener = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    try:
        with sr.Microphone() as source:
            print("escuchando... ")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'eva' in command:
                command = command.replace('eva', '')
                #print(command)
    except:
        pass
    return command

def greeting():
    name=request.form.get('name')
    talk('hi ' + name + ' nice to meet you, my name is EVA')

def ListeningToMusic(command):
    song=command.replace('play', '')
    talk('playing' + song)
    pywhatkit.playonyt(song)

def getActualTime(command):
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk('it is ' + time)
    print('it is ' + time)

def WikipediaSummary(command):
    search = command.replace('search', '')
    info = wikipedia.summary(search, 1)
    print(info)
    talk('found: ' + info)

def open_notes():
    talk('these are your notes ')




def runEVA():
    command = listen_command()
    if 'hello' in command:
        greeting()
    elif 'notes' in command:
        open_notes()
    elif 'play' in command:
        ListeningToMusic(command)
    elif 'time' in command:
        getActualTime(command)
    elif 'search' in command:
        WikipediaSummary(command)
    elif 'tell me something' in command:
        talk(pyjokes.get_joke())
    elif 'bye' in command:
        talk('bye then')
        exit(0)
    else:
        talk('I dont know what you are talking about')
while True:
    runEVA()
