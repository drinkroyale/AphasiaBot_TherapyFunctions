import pygame
import random

# Initialize Pygame
pygame.mixer.init()

# Load audio files for words
def load_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Define words, correct object, and foils
word_bank = [
    {'word': 'apple', 'audio': 'apple.mp3', 'correct': 'apple_image.png', 'foils': ['orange_image.png', 'pear_image.png']},
    {'word': 'cat', 'audio': 'cat.mp3', 'correct': 'cat_image.png', 'foils': ['bat_image.png', 'hat_image.png']}
]

# Select a random word therapy session
def random_word_session():
    word_info = random.choice(word_bank)
    all_options = word_info['foils'] + [word_info['correct']]
    random.shuffle(all_options)  # Shuffle the options to make it challenging
    return word_info['word'], word_info['audio'], word_info['correct'], all_options

# Simulate word therapy
def word_therapy():
    word, audio_file, correct_image, options = random_word_session()

    # Play the word audio
    print(f"Listen to the word: {word}")
    load_audio(audio_file)

    # Show options to the user (replace with your actual GUI code)
    print(f"Identify the correct object. Options: {options}")
    
    # Get user response
    user_input = input("Type the image name: ")
    
    # Check if the user selected the correct image
    if user_input == correct_image:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer was {correct_image}.")

# Start the therapy session
if __name__ == "__main__":
    word_therapy()
