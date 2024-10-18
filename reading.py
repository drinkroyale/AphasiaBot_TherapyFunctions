import pyttsx3
import speech_recognition as sr

# List of sentences for reading aloud
sentences_to_read = [
    "The cat is on the mat.",
    "I like to eat apples and bananas.",
    "The sky is blue and the grass is green."
]

def reading_therapy():
    for sentence in sentences_to_read:
        # Print the sentence for the user to read
        print(f"Please read aloud: '{sentence}'")
        
        # Capture user's spoken word
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
                user_input = recognizer.recognize_google(audio).lower()
                
                # Check if the user's input matches the sentence
                if user_input == sentence.lower():
                    print("Correct!")
                else:
                    print(f"Incorrect, you said '{user_input}'. Try again!")
        
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

reading_therapy()
