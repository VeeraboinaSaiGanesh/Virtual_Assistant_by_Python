import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime

# This method is for taking the commands and recognizing the command
# from the speech_recognition module we will use the recognizer method for recognizing
def takeCommand():
    r = sr.Recognizer()

    # From the speech_recognition module, we will use the Microphone module for listening to the command
    with sr.Microphone() as source:
        print('Listening')

        # Seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)

        # Now we will be using the try and except block for handling exceptions
        try:
            print("Recognizing")

            # For listening the command in Indian English we can also use 'hi-In' for Hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print("The command is printed =", Query)

        except Exception as e:
            print(e)
            print("Say that again please")
            return "None"

        return Query

def speak(audio):
    engine = pyttsx3.init()
    # Getter method (gets the current value of engine property)
    voices = engine.getProperty('voices')

    # Setter method .[0]=male voice and [1]=female voice in setProperty.
    engine.setProperty('voice', voices[0].id)

    # Method for the speaking of the assistant
    engine.say(audio)

    # Blocks while processing all the currently queued commands
    engine.runAndWait()

def tellDay():
    # This function is for telling the day of the week
    day = datetime.datetime.today().weekday() + 1

    # This line tells us about the number that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def tellTime():
    # This method will give the time
    time = datetime.datetime.now().strftime("%H:%M")
    print("The time is", time)
    speak(f"The time is {time}")

def Hello():
    # This function is for when the assistant is called it will say hello and then take query
    speak("Hello Sir, I am Jack . Tell me how may I help you")

def Take_query():
    # Calling the Hello function for making it more interactive
    Hello()

    # This loop is infinite as it will take our queries continuously until and unless we do not say bye to exit or terminate the program
    while True:
        # Taking the query and making it into lower case so that most of the times query matches and we get the perfect output
        query = takeCommand().lower()
        if "open youtube" in query:
            speak("Opening Youtube ")
            webbrowser.open("https://www.youtube.com")
            continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("https://www.google.com")
            continue

        elif "open github" in query:
            speak("Opening Github ")
            webbrowser.open("https://github.com")
            continue
        elif "open instagram" in query:
            speak("Opening Instagram ")
            webbrowser.open("https://www.instagram.com")
            continue
        elif "open Chat" in query:
            speak("Opening Chat GPT ")
            webbrowser.open("https://chatgpt.com")
            continue


        elif "which day it is" in query:
            tellDay()
            continue

        elif "tell me the time" in query:
            tellTime()
            continue

        # This will exit and terminate the program
        elif "see you soon" in query:
            speak("Bye. Take Care")
            exit()

        elif "tell me your name" in query:
            speak("I am Jack. Your desktop assistant")

if __name__ == '__main__':
    # Main method for executing the functions
    Take_query()
