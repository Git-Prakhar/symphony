import speech_recognition as sr
import os
import pyttsx3 as tts
import pyautogui as pg

def speak(text: str):
    engine = tts.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def listen_for_wake_word():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        while True:
            try:
                print("Listening for wake word...")
                audio = r.listen(source, phrase_time_limit=5)
                recognized_text = r.recognize_google(audio).lower()
                recognizedArr = recognized_text.split()
                print(recognizedArr)
                if "bobo" in recognizedArr or "babu" in recognizedArr:
                    command_index = recognizedArr.index("bobo") if "bobo" in recognizedArr else recognizedArr.index("babu")

                    if command_index > 0 and recognizedArr[command_index - 1] == "hello":
                        speech_command(recognizedArr[command_index + 1:])
                    elif command_index < len(recognizedArr) - 1 and recognizedArr[command_index + 1] == "stop":
                        speak("Goodbye! Have a great day!")
                        break


            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Error: {0}".format(e))


def speech_command(commandArr: list):
    if commandArr == []:
        speak("Hey there! How can I help you today?")
        return
    
    if 'cancel' in commandArr:
        speak("Okay, cancelling the current operation")
        return
    if commandArr[0] == "say":
        speak(" ".join(commandArr[1:]))
        
        
    elif commandArr[0] == "open":
        openArr = commandArr[1:]
        if len(openArr) == 1:
            os.system("start " + openArr[0])
            speak("Opening " + openArr[0])
    elif commandArr[0] == "search":
        searchArr = commandArr[1:]
        if not (searchArr[0] == "url"):
            os.system(
                'start brave "https://www.google.com/search?q='
                + "+".join(searchArr)
                + '"'
            )
            speak("Searching for " + " ".join(searchArr) + " on Google")
    elif commandArr[0] == "url":
        urlArr = commandArr[1:]
        if len(urlArr) == 1:
            os.system(f'start brave "www.{urlArr[0]}.com"')
            speak("Opening url: " + urlArr[0])
        elif len(urlArr) > 1 and urlArr[1] == "at" and len(urlArr) == 3:
            validTLD = ["com", "org", "net", "gov", "edu", "in"]
            if urlArr[2] in validTLD:
                os.system(f'start brave "www.{urlArr[0]}.{urlArr[2]}"')
                speak("Opening url: " + urlArr[0] + "." + urlArr[2])
            else:
                speak("Invalid TLD")
                return
    elif commandArr[0] == "youtube":
        if len(commandArr) == 1:
            os.system("start brave www.youtube.com")
            speak("Opening YouTube")
            return
        youtubeArr = commandArr[1:]
        if youtubeArr[0] == "search":
            os.system(
                'start brave "https://www.youtube.com/results?search_query='
                + "+".join(youtubeArr[1:])
                + '"'
            )
            speak("Searching for " + " ".join(youtubeArr[1:]) + " on YouTube")
    elif commandArr[0] == "monkey":
        os.system("start brave www.moneytype.com")
        speak("Good Luck Typing! Get that 150 WPM!")
    elif commandArr[0] == "continue":
        # Check if brave is opened and the tab is youtube then left click on a specific co-ordinate
        pass
        
if __name__ == "__main__":
    listen_for_wake_word()
