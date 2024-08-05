import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
#import requests
#from bs4 import BeautifulSoup #play first link
import pyjokes as pj
import pyautogui
import psutil #read documentation
import os

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%H :%M :%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)


def wish():
    speak("Welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 5 and hour < 12 :
        speak("Good morning sir!")
    elif hour >= 12 and hour < 17 :
        speak("Good Afternoon sir!")
    elif hour >=17 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("It's getting late sir.You should sleep. However if you need me.")
    speak("Stark at your service. How can I help you today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # wait 1 second and start listening
        audio = r.listen(source) # listen to microphone

    try:
        print("Recognizing...")
        query = r.recognize_google (audio, language = 'en-in' )
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say that again please...")
        
        return "None"

    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/KIIT/Desktop/Python Projects/Stark/Screenshot/ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("The CPU usage is at" + usage)

def battery():
    battery = psutil.sensors_battery()
    speak("The battery is at")
    speak(battery.percent)

def jokes():
    speak(pj.get_joke())

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com:587')  #gmail account , gmail port
    server.ehlo()
    server.starttls()
    server.login('#youremail ', '#email password')
    server.sendmail('#youremail', to, content)
    server.close()

def removeSpaces(string):
    return string.replace(" ", "")

def play_youtube_song(song_name):
    query = song_name.replace(' ', '+')
    url = f"https://www.youtube.com/results?search_query={query}"
    wb.open_new_tab(url)
    #play first link
    #response = requests.get(url)
    #soup = BeautifulSoup(response.text, 'html.parser')
    #
    ## Finding the first video link in the search results
    #first_video = soup.find('a', {'class': 'yt-uix-tile-link'})
    #if first_video:
    #    video_url = 'https://www.youtube.com' + first_video['href']
    #    webbrowser.open(video_url)
    #else:
    #    print("No videos found for the given query.")



if __name__ == "__main__":
    wish()
    while True:
        query = takeCommand().lower() #lower for easy comparison

        if 'time' in query:
            time()
        
        elif 'date' in query:
            date()
        
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result=wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'email' in query:
            try:
                speak("What should I write?")
                content = takeCommand()
                to = ("receiver email")
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email!")

        elif 'screenshot' in query:
            screenshot()
            speak("Screenshot has been taken and saved sir")

        elif 'search in chrome'  in query:
            try:
                speak("What should I search for?")
                chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                search = takeCommand().lower()
                wb.get(chromepath).open_new_tab(search)
            except Exception as e:
                print(e)
                speak("Unable to search!")

        elif 'play songs' in query:
            speak("Play online or stored song sir?")
            takeCommand()

        elif 'online song' in query:
            speak("What song should I play?")
            search = takeCommand().lower()
            play_youtube_song(search)

        elif 'stored song' in query:
            songs_dir = 'C:/Users/KIIT/Desktop/Python Projects/Stark/Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
 
        elif 'remember' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You told me to remember that" + data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'remind' in query:
            remind = open('data.txt','r')
            speak("Yes sir you told me to remind you that" + remind.read())        

        elif 'joke' in query:
            jokes()

        elif 'cpu' in query:
            cpu()

        elif 'battery' in query:
            battery()

        elif 'logout' in query:
            os.system("shutdown -l")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")    

        
        
        elif 'offline' in query:
            print("Going Offline")
            speak("Going Offline! Good Bye Sir!")
            quit()

        



takeCommand()        