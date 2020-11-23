from random import choice, shuffle
from urllib import response
from webbrowser import BackgroundBrowser
import pyttsx3
import speech_recognition as sr
from datetime import date, datetime
import webbrowser as web 
import os
from speech_recognition import UnknownValueError
import wikipedia as wiki
import smtplib
from youtube_search import YoutubeSearch as yt_search 
import json
import cts



# register web browser location
web.register('chrome', None, web.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'))

# list of response
greetings_res = ['hello sir, how may I help', 'hi sir, good to hear from you']
talk_res = ['fine sir thanks']

# list of commands
greetings = ['yosh', 'hello', 'hi']
# kill = ['kill', 'die', 'bye', 'quit']
talk = ["what's up"]



engine = pyttsx3.init('sapi5')  #create object 



def init_voice():
#working with narrrator voice 
    voices = engine.getProperty('voices') #getting voice property into 'voices' 
    engine.setProperty('voice', voices[1].id) #setting voice property of 'voices'

    rate = engine.getProperty('rate') #getting the rate/speed of the narrator 
    engine.setProperty('rate', 192) #setting the rate/speed of the narrator


def speak(text):
    engine.say(text)
    engine.runAndWait()







def greeting():
    hour = int(datetime.now().hour)
    # print(hour)
    if hour>=0 and hour<4 :
        speak('Good night sir')
    elif hour >= 4 and hour<12 :
        speak('Good morning sir')
    elif hour>=12 and hour<15 :
        speak('Good Noon sir')
    
    elif hour>=15 and hour<20 :
        speak('Good Afternoon sir')
    else :
        speak('hello sir')
    




# get id and title searched youtube video in a list
def get_yt(search):
    result = yt_search(search, max_results=1).to_json()
    a = json.loads(result)
    yt_id =a['videos'][0]['url_suffix']
    yt_title = a['videos'][0]['title']
    return [yt_id, yt_title]




# text to speech converter
def take_command():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening.....')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try :
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-us')
        print(f'user said - {query}')
        return query
    
    except UnknownValueError as e:
        return (f'unknown error {e}')

    except Exception as e:
        print('Please speak again...')
        #take_command()




# All given command in a function -(not completed)

def all_com():
    while True:
        query = take_command()
        query = query.lower()
        # print(query)
        # query = 'discord bot'

        if 'quit' in query :
            speak('Good bye sir, hope to see ya again')
            try :
                os.remove(__cached__)
            except Exception as e:
                speak(str(e))
            break

        elif query in greetings : 
            shuffle(greetings_res)
            res = choice(greetings_res)
            # print(res)
            speak(res)


        elif 'notepad' in query:
            path = 'C:\\Windows\\system32\\notepad.exe'
            speak('opening notepad')
            os.startfile(path)

        elif 'vs code' in query :
            path = 'C:\\Users\\Rudra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            speak('opening vs code')
            os.startfile(path)
        
        elif 'command' in query :
            path = 'C:\\Windows\\system32\\cmd.exe'
            speak('opening command prompt')
            os.startfile(path)

        elif 'youtube' in query :
            speak('What do you want to search?')
            
            try :
                search = take_command()
                yt = get_yt(search)
                
                web.get('chrome').open('youtube.com' + yt[0])
                speak('opening '+ yt[1])
                # a.clear()


            except Exception as e:
                speak(str(e))

        elif 'facebook' in query:
            try:
                web.get('chrome').open('fb.com')
                speak('opening facebook')
            except Exception as e:
                speak(str(e))


        elif 'stack overflow' in query:
            try:
                web.get('chrome').open('stackoverflow.com')
                speak('opening stack overflow')
            except Exception as e:
                speak(str(e))

        elif 'codeforces' in query:
            try :
                web.get('chrome').open('codeforces.com')
                speak('opening codeforces')
            except Exception as e:
                speak(str(e))

        elif 'fast' in query:
            try:
                web.get('chrome').open('fast.com')
                speak('opening speed test')
            except Exception as e:
                speak(str(e))
        
        elif 'discord bot' in query and not cts.activeDiscord:
            speak('starting bot, please wait')
            cts.client.run(cts.token)
            speak('im back to my local server now')


