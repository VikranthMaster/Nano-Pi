from gtts import gTTS
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import datetime
from playsound import playsound
import time

def speak(audio):
	myText = audio
	language = "en"
	gTTS(text=myText,lang=language,slow=False)

def speech():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='en-in')
        print(f"User said: {text}\n")

    except Exception as e:
        print("Say that again please")
        return "None"
    return text

while True:

		text = speech().lower()
    
        WIKIPEDIA = ["wikipedia","who","what"]
        for phrase in WIKIPEDIA:
            if phrase in text:
                    speak('Searching Wikipedia...')
                    text = text.replace("wikipedia", "")
                    results = wikipedia.summary(text, sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

        YOUTUBE = ["open youtube","i want to watch videos","i want to watch movies","open YouTube"]
        for phrase in YOUTUBE:
            if phrase in text:
                    webbrowser.open("https://www.youtube.com/")

        GOOGLE = ["open google","search","open Google"]
        for phrase in GOOGLE:
            if phrase in text:
                webbrowser.open("https://www.google.com/")

        NEVERSKIP = ["open neverskip","neverskip"]
        for phrase in NEVERSKIP:
            if phrase in text:
                webbrowser.open("https://parent.neverskip.com/#/auth/login")

        PLAY_MUSIC = ["play music","start music","music please","music"]
        for phrase in PLAY_MUSIC:
            if phrase in text:
                speak("Playing...")             
                # path="C:/Users/TS/Music/telugu songs/"
                files=os.listdir(path)
                d=random.choice(files)
                os.startfile(path + d)
            
        TIME = ["what is the time","time"]
        for phrase in TIME:
            if phrase in text:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"The time is {strTime}")

        CODE = ["open code","i want to code","open visual studio code","code"]
        for phrase in CODE:
            if phrase in query:
                speak("Opening....")
                subprocess.Popen("")

        # elif 'email to vikranth' in query:
        #     try:
        #         speak("What Should i say?")
        #         takeCommand()
        #         to = "vikrantht32@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry i am not able to send this email")
        
        DATE = ["what is the date","date","what's the date today"]
        for phrase in DATE:
            if phrase in text:
                current_date = datetime.date.today()
                speak(f"Today's date is {current_date}")
                print(f"Today's date is {current_date}")
        
        # NOTE_STRS = ["make a note", "write this down", "remember this"]
        # for phrase in NOTE_STRS:
        #     if phrase in text:
        #         speak("What would you like me to write down?")
        #         note_text = takeCommand()
        #         note(note_text)
        #         speak("I've made a note of that.")

        # PICTURE = ["analyse image","show me picture","picture","image"]
        # for phrase in PICTURE:
        #     if phrase in text:
        #         speak("Analysing..")
        #         show_image()

        # VIDEO = ["open camera","analyse video","video"]
        # for phrase in VIDEO:
        #     if phrase in text:
        #         speak("Analysing..")
        #         video()

        STOP = ["stop","break"]
        for phrase in STOP:
            if phrase in text:
                break
                speak("Shutting....")

        # COMMAND = ["open command prompt","open cmd"]
        # for phrase in COMMAND:
        #     if phrase in text:
        #         subprocess.Popen(["terminator.exe"])

        TIMER = ["set a timer","start the countdown","timer"]
        for phrase in TIMER:
            if phrase in text:
                countdown(int(t))