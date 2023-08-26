import pandas as pd

translation = pd.read_csv('data/elder_speech.csv')

# Create dict from translation
translation_dict = dict(zip(translation['english'], translation['elder_speech']))

# Ask user for input in jupyer notebook
user_input = input('Enter text to translate: ')

# Translate user input
translation = [translation_dict[word] if word in translation_dict else word for word in user_input.split()]

# Print translation
print(' '.join(translation))