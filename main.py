import speech_recognition as sr
import webbrowser
import musiclibrary
import pyttsx3
import difflib


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("What do you want to search for?")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print("You said:", query)
            return query
        except sr.UnknownValueError:
            speak("Sorry, I could not understand your voice.")
            return None
        except sr.RequestError:
            speak("Speech service is unavailable.")
            return None

def search_and_open(query):
    try:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            speak("Opening the best result for your question.")
            webbrowser.open(url)
            
    except Exception as e:
        print(" Error:", e)
        speak("Sorry, something went wrong while searching.")

def main():
    query = listen()
    if query:
        search_and_open(query)



def processcommand(c):
    if "open google" in c.lower():
        speak("ya offcourse")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c.lower():
        speak("ya offcourse")
        webbrowser.open("https://www.youtube.com")

    elif "open spotify" in c.lower():
        speak("ya offcourse")
        webbrowser.open("https://www.spotify.com")
        
    elif "open chrome" in c.lower():
        speak("ya offcourse")
        webbrowser.open("https://www.google.com/chrome/")
        
    elif c.lower().startswith("play"):
        song = c.lower().split("play")[1]
        matches = difflib.get_close_matches(song, musiclibrary.music.keys(), n=1, cutoff=0.6)

        if matches:
            best_match = matches[0]
            link = musiclibrary.music[best_match]
            speak(f"Playing {best_match}")
            webbrowser.open(link)
        else:
            speak(f"Playing {song} on YouTube")
            url = f"https://www.youtube.com/results?search_query={song.replace(' ', '+')}"
            webbrowser.open(url)

    else:
        search_and_open(c)
            

if __name__ == "__main__":
    speak("Initializing MACAVA...")
    while True:
        r = sr.Recognizer()
        
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            print("Heard:", word)
            if word.lower() in "hello":
                speak("yes, how can I help you")
                

                
                with sr.Microphone() as source:
                    print("MACAVA IS ACTIVE...")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processcommand(command)
                    
                    

        except Exception as e:
            print("Error; {0}".format(e))
                

                