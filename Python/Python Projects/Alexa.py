import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
  engine.say(text)
  engine.runAndWait()
   
def take_command():
   try:
      with sr.Microphone() as source:
          print("listening...")
          voice = listner.listen(source)
          command = listner.recognize_google(voice)
          command = command.lower()
          if 'alexa' in command:
            command = command.replace('alexa', '')
            talk(command)
   except:
       pass
   return command

def run_alexa():
   command = take_command()
   print(command)
   if 'play' in command:
      song = command.replace('play', '')
      talk("playing" + song)
      pywhatkit.playonyt(song)

   elif 'time' in command:
      time = datetime.datetime.now().strftime('%I:%M %p')
      print('The current time is ' + time)
      talk("The current time is " + time) 

   elif 'who the heck is' in command:
      person = command.replace('who the heck is', '')
      info = wikipedia.summary(person, 1)
      print(info)
      talk(info)

   elif 'date' in command:
      talk('sorry, I have a headache')
   
   elif 'do you have in a relationship' in command:
      talk("yes, i am in relationship with your network aur wifi")

   elif 'joke' in command:
      joke = command.replace('joke', '')
      talk("Searching" + joke)
      voice_joke = pyjokes.get_joke()
      print(voice_joke)
      talk(voice_joke)

   else:
      error_message = "Sorry, I cant Understand Please Try Again"
      talk(error_message)


while True:
   run_alexa()