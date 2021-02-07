#speach recnosization package
#pyttsx3 package
#pyaudio package
#pywhatkit module
import speech_recognition as sr
import pyttsx3
import pywhatkit

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say('I am your virtual assistance made by Aryan')
engine.say('I am listning.')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listning...")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)#opens the youtube in your device

run_alexa()