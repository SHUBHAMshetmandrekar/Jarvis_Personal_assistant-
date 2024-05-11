import random
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import turtle
import calendar
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=3)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

# function to allow jarvise to wish....
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning sir")
    elif hour>12 and hour<18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("i am jarvis, tell me how can i help you? ")

#to send email
def sendEmail(to,pm):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mypcaddress13@gmail.com','I AM protected')
    server.sendmail('mypcaddress13@gmail.com',to,pm)
    server.close()

#turtle circle pattern
def tertle():

    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("black")
    t.pencolor("green")
    a = 0
    b = 0
    t.speed(0)
    t.penup()
    t.goto(0,200)
    t.pendown()
    while True:
        t.forward(a)
        t.right(b)
        a+=3
        b+=1
        if b == 210:
            break
        t.hideturtle()
    turtle.done()



if __name__ == "__main__":

    wish()
    while True:
    #if 1:

        query = takecommand().lower()

        #logic building for tarks

        if "open notepad" in query:
            speak("opening notepad")
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "command prompt" in query:
            speak("opening command prompt")
            os.system("start ")

        elif "open camera" in query:
            speak("opening camera")
            #if u want to use external camera use 1 instead of 0.
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            speak("playing music from your pc")
            music_dir = "C:\\Users\\shubham and shivam\\Desktop\\New folder\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
         #   for song in songs:
          #      if song.endswith(',mp3'):
            os.startfile(os.path.join(music_dir, rd))



        #online task....
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")


        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")

        elif "instagram" in query:
            speak("opening instagram")
            webbrowser.open("www.instagram.com")

        elif "stack overflow" in query:
            speak("opening stack overflow")
            webbrowser.open("www.stackoverflow.com")

        elif "google" in query:
            speak("opening google. sir, what should i search on google?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "message" in query:
            shivam = "9673104173"
            daddy = "7083425970"
            siddhi = "7262093868"
            sushmi = "8378977488"
            vaishnavi = "7020629067"
            dhana = "8806145774"
            vinay = "9067789947"
            divyata = "8080860552"
            subodh = "7767037959"
            samidha = "9765599953"
            siddhis = "9168236845"

            speak("sir, to whom should i send message?")
            pm = takecommand().lower()
            speak("sir,what should i send message")
            cm = takecommand().lower()
            speak("message will be delivered")
            kit.sendwhatmsg(f"+91{pm}", f"{cm}",11,25)

        elif "play a song on youtube" in query:
            speak("sir, what song should i play?")
            cm = takecommand().lower()
            speak("playing on youtube.")
            kit.playonyt(f"{cm}")

        elif "play birthday song" in query:
            #speak("playing birthday song")
            cm = takecommand().lower()
            speak("playing birthday song.")
            kit.playonyt(f"https://youtu.be/evTWSWZvtqY")


        elif "who is your developer" in query:
                 speak("my developer is shubham shetmandrekar")

        elif "who developed you" in query:
                speak("my developer is shubham shetmandrekar")

        elif "open soundcloud" in query:
             speak("opening sound cloud")
             webbrowser.open("www.soundcloud.com")

        elif "generate pattern" in query:
            speak("generating pattern")
            tertle()

        elif "calendar" in query:
            speak("enter the current year: ")
            year = int(takecommand().lower())
            speak("enter the current month: ")
            month = takecommand().lower()
            if month == "january" :
                month = 1
            if month == "february" :
                month = 2
            if month == "march":
                month = 3
            if month == "april":
                month = 4
            if month == "may":
                month = 5
            if month == "june":
                month = 6
            if month == "july":
                month = 7
            if month == "august":
                month = 8
            if month == "september":
                month = 9
            if month == "october":
                month = 10
            if month == "november":
                month = 11
            if month == "december":
                month = 12
            else :
                speak("sir something is wrong. please try again ")
                #query = takecommand().lower()
            speak("opening calender")



            print(calendar.month(year, month))



        elif "hi jarvis" in query:
            say = ["hi sir. you seems so in good mood","hello sir,","hi sir"]
            tell = random.choice(say)
            speak(tell)

        elif "aradhya" in query:
            speak("he is very handsome guy and he is very smart. ")

        elif "do you have a girlfriend" in query:
            speak("no sir.")

        elif "how are you jarvis" in query:
            speak("i am good. how are you sir?")
            cm = takecommand().lower()
            if "I am fine" in query :
                speak("good to hear that.")
            if "I am not fine" in query:
                speak("ohh. sad to hear that. i heared that music heals. would you like to hear one?")
                if "yes" in query:
                    speak("sir, what song should i play?")
                    cm = takecommand().lower()
                    speak("playing on youtube.")
                    kit.playonyt(f"{cm}")



        elif "send email" in query:
            try:
                shubham = "shetmandrekarshubham107@gmail.com"
                speak("whom should i send ?")
                cm = takecommand().lower()
                speak("what should i say?")
                pm = takecommand().lower()
                to = cm
                sendEmail(to,pm)
                speak("email has been sent to",f"{cm}")
            except Exception as e:
                print(e)
                speak("sorry sir, due to some problem i am not able to send email")

        elif "thanks" in query:
            speak("thank you sir, have a great day.")
            sys.exit()

        speak("sir, do you have any other work? ")



# takecommand()
    #speak("")







    #somthing new is coming stay tuned........