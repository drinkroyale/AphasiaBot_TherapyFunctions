import pyttsx3
import speech_recognition as sr

# Initialize TTS engine
engine = pyttsx3.init()

# Speech recognition setup
recognizer = sr.Recognizer()

# Word list for repetition therapy
words_to_repeat = ["apple", "banana", "cat", "dog", "elephant"]

def repeat_therapy():
    for word in words_to_repeat:
        # Say the word using TTS
        print(f"Please repeat the word: {word}")
        engine.say(word)
        engine.runAndWait()
        
        # Capture user's spoken word
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
                user_input = recognizer.recognize_google(audio).lower()
                
                # Check if the user's input matches the word
                if user_input == word:
                    print("Correct!")
                else:
                    print(f"Incorrect, you said '{user_input}'. Try again!")
        
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        
repeat_therapy()
