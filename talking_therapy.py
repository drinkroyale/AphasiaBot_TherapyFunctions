import speech_recognition as sr
from gtts import gTTS
import playsound
import random

# Tagalog phrases for common conversation
tagalog_phrases = {
    "Kamusta ka?": ["Mabuti naman ako, ikaw?", "Ayos lang ako, ikaw kamusta?", "Okay lang ako."],
    "Magandang araw!": ["Magandang araw din sa'yo!", "Magandang araw! Kumusta ka?"],
    "Anong ginagawa mo ngayon?": ["Nagluluto ako.", "Nanonood ako ng TV.", "Nag-aaral ako."],
    "Kumain ka na ba?": ["Oo, kumain na ako.", "Hindi pa, ikaw?", "Mamaya pa ako kakain."],
    "Saan ka pupunta?": ["Pupunta ako sa tindahan.", "Pupunta ako sa trabaho.", "Wala akong pupuntahan."],
    "Paalam": ["Paalam! Ingat ka!", "Sige, hanggang sa muli!", "Ingat, hanggang bukas!"]
}

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Magandang umaga! Ako si AphasiaBot! Tayo'y makipagusap!")
        audio = recognizer.listen(source)

    try:
        # Convert spoken words to text (in Tagalog)
        text = recognizer.recognize_google(audio, language='tl-PH')
        print(f"Ito ang iyong sinabi: {text}")
        return text
    except sr.UnknownValueError:
        print("Paumanhin, hindi ko maintindihan. Pakiulit.")
        return None
    except sr.RequestError:
        print("Walang internet connection.")
        return None

# Function to generate speech in Tagalog
def bot_reply(response):
    tts = gTTS(text=response, lang='tl')
    tts.save("response.mp3")
    playsound.playsound("response.mp3")

# Main talking therapy loop
def talking_therapy():
    while True:
        # Recognize what the patient says
        patient_input = recognize_speech()
        
        if patient_input:
            # Exit condition
            if "paalam" in patient_input.lower():
                bot_reply("Paalam! Ingat ka!")
                break
            
            # Check if there is a related response to the user's input
            for key_phrase in tagalog_phrases:
                if key_phrase.lower() in patient_input.lower():
                    bot_response = random.choice(tagalog_phrases[key_phrase])
                    break
            else:
                # If no matching phrase, the bot will respond with a default phrase
                bot_response = "Pakiulit nga?"

            # Display and say the bot's response
            print(f"Bot says: {bot_response}")
            bot_reply(bot_response)

talking_therapy()
