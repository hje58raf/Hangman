# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import os

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


# Getting a Guess
def get_guess(word):
    print_word_with_blanks(word)
    print('Lives Remaining: ' + str(lives_remaining))
    guess = input(' Guess a letter or whole word?')
    return guess


def play():
    word = pick_a_word()
    clear_terminal()
    print('{:*^80}'.format(' WELCOME TO HANGMAN ! '))
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print('You win! Well Done!')
            break
        if lives_remaining == 0:
            print('You are Hung!')
            print('The word was: ' + word)
            break


# Printing the Word
def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            display_word = display_word + letter
        else:
            display_word = display_word + '-'
    print(display_word)


# Processing the Guess
def process_guess(guess, word):
    if len(guess) > 1 and len(guess) == len(word):
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)
