# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

words = ['chicken', 'dog', 'cat', 'mouse', 'frog']


lives_remaining = 14
guessed_letters = ""

# Getting a Random Word
def pick_a_word():
    word_position = random.randint(0, len(words) - 1)
    return words[word_position]


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


