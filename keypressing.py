import speech_recognition as sr
from nltk.corpus import stopwords

def extract_keywords(text):
    # Tokenize and remove stop words
    stop_words = set(stopwords.words('english'))
    words = text.split()
    keywords = [word for word in words if word.lower() not in stop_words]
    return keywords

def main():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

        try:
            recognized_text = r.recognize_google(audio)
            print(f"You said: {recognized_text}")

            # Extract keywords
            keywords = extract_keywords(recognized_text)
            print("Extracted keywords:", keywords)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    main()
