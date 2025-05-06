import pyttsx3
import speech_recognition
import datetime
import wikipedia
import webbrowser
import os
import sys

print("Initializing Jarvis")

MASTER = "musa"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to wish the user
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning " + MASTER)
    elif 12 <= hour < 18:
        speak("Good Afternoon " + MASTER)
    else:
        speak("Good Evening " + MASTER)

# Microphone function
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"User said: {query}\n")
        return query.lower()  # Convert query to lowercase for case-insensitive comparison
    except Exception as e:
        print("Say that again, please.")
        return None

# Main code starts here
speak("Ready... Listening!")
wishMe()  # Call wishMe() to greet the user

while True:
    query = takeCommand()

    # Define a dictionary of predefined questions and answers
    qa_pairs = {
        "what is your name": "My name is Jarvis.",
        "how are you": "I'm functioning at full capacity, thank you.",
        "you know me": "Yes, I know who you are, You are my boss! and your name is Samuel Musa Adinata.",
        "do you know me": "Yes, I know who you are, You are my boss! and your name is Samuel Musa Adinata.",
        "jarvis": "Yes sir",
        "therapist": "Yes sir",
        "hello jarvis": "Yes",
        "hello therapist": "Yes",
        "good night": "Good Night sir, Have A nice Dream",
        "what the hell": "Fuck You! Risqi!",
        "hello": "hello sir!, what's going on?",
        "hello hello": "hello sir!, what's going on?",
        "hello hello hello": "hello sir!, what's going on?",
        "nothing": "okey sir, tell me if you have problem!",
        "tell me what you can": "Okay sir. Hello, my name is Jarvis! and Moses is the one who made me! like AI made by tony stark in iron man movie. and I'm still in development",
        "who you are": "my name is Jarvis! and Moses is the one who made me! like AI made by tony stark in iron man movie. and I'm still in development",
        "i dont know": "because is that, and i'am here..",
        "um": "what your problem Sir?",
        "hey": "yes, what's going on"
        
    
    }

    # Logic for tasks based on the query
    if query is not None and "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        print(result)
        speak(result)

    elif "open youtube" in query:
        url = "https://www.youtube.com"
        webbrowser.open(url)

    elif "open whatsapp" in query:
        url = "https://web.whatsapp.com"
        webbrowser.open(url)

    elif "open google" in query:
        url = "https://www.google.com"
        webbrowser.open(url)

    elif "play music" in query:
        music_folder = "C:\\Users\\ACER\\Music"
        music_files = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]

    elif "open chrome" in query:
        folder = "C:\\Users\\ACER\\Music"

        if music_files:
            selected_music = os.path.join(music_folder, music_files[0])
            os.startfile(selected_music)
            speak("Playing music.")
        else:
            speak("No music files found in the specified folder.")

    # Check for predefined questions and provide answers
    elif query in qa_pairs:
        speak(qa_pairs[query])
        
    elif query in ["thank you", "thanks"]:
        speak("You're welcome. Goodbye!")
        sys.exit()  # Exit the program

    # Add more conditions as needed for additional tasks

    # Example: If none of the specific tasks match, provide a generic response
    else:
        speak("I'm sorry, I didn't understand that.")
