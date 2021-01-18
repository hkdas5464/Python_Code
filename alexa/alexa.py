import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
listiner=sr.Recognizer()
engine= pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def takecommand():
    try:
        with sr.Microphone() as source:
            talk("hii i am Sailesh how can i help you")
            print("hii i am Sailesh how can i help you")
            print("listening.....")
            voice = listiner.listen(source)
            command = listiner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')


    except:
        pass
    return command



def run_alexa():
    command= takecommand()



    if 'play' in command:
        command=command.replace('play','')
        talk("playing"+command)
        pywhatkit.playonyt(command)
    elif 'time' in command:
        time= datetime.datetime.now().strftime('%I:%M %p')
        talk(f"current time is{time}")
        print(time)
    elif 'who' in command:
        person=command.replace('who','')
        info =  wikipedia.summary(person,1)
        print(info)
        talk(info)




run_alexa()


