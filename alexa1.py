#part1: Take user voice and convert it to text
#part2: Process the text and give some results-->
#part3: Convert results(text) into voice

import speech_recognition as sr    #For recognizing user voice and convert it to text
import pyttsx3			#convert the text to audio
import pywhatkit	#For accessing whatsapp and youtube
import wikipedia	#For wikipedia information
from datetime import datetime	#For date and time accessing
import pyjokes		#For jokes (All are programming jokes)


def talk(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)	#Here 1 is female voice, you can change it to 0 for male voice
    engine.say(answer)
    engine.runAndWait()

def processQuestion(question):			#For processing question
    if 'what are you doing' in question:
        print('Iam waiting for your question')
        talk("Iam waiting for your question")
        return True
    elif 'Who are you' in question:
        print("Iam a hero with zero cinemas")
        talk('Iam a hero with zero cinemas')
        return True
    elif 'eat' in question:
        print("no i eat grass")
        talk('no i eat grass')
        return True
        return True
    elif 'love me' in question:
        print("Yes of course i'll love you")
        talk('Yes of course i will love you')
        return True
    elif 'how are you' in question:
        print('Iam good, thank you. How can I help you')
        talk('Iam good, thank you. How can I help you')
        return True
    elif 'play' in question:
        question = question.replace('play', '')
        pywhatkit.playonyt(question)
        return True
    elif 'who is' in question:
        question = question.replace('who is', '')
        print(wikipedia.summary(question, 1))
        talk(wikipedia.summary(question, 1))
        return True
    elif "time" in question:
        time = datetime.today().time().strftime("%I:%M %p")
        print(time)
        talk(time)
        return True
    elif "joke" in question:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
        return True
    elif "love you" in question:
        talk("get your work done first")
        return True
    elif "bye" in question:
        talk("bye bye, please take care. will meet you again later")
        return False
    else:
        talk("I can't process your question, can you say that again")
        return True

def getQuestion():				#To get the question from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:		#sr is instance
        print("say something")
        audio = r.listen(source)		
        try:
            print(r.recognize_google(audio))
            question = r.recognize_google(audio)
            if 'Alexa' in question:		#You can change it to any name
                question = question.replace('Alexa','')
                print(question)
                return question
            else:
                print('you are not talking to me, please carry on')
                talk('you are not talking to me, please carry on')
                return "notwithme"
        except sr.UnknownValueError:
            print("Sorry, I can't get your Question")

canAskQuestion = True
while canAskQuestion:				#Loop to answer again and again
    question = getQuestion()
    if(question=="notwithme"):
        talk("ok carry on with your friends, bye!")
        canAskQuestion = False
    else:
        canAskQuestion = processQuestion(question)
