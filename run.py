# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random


words = ['chicken', 'dog', 'cat', 'mouse', 'frog', 'abruptly', 'absurd']


lives_remaining = 7
guessed_letters = ""


# Getting a Random Word
def pick_a_word():
    word_position = random.randint(0, len(words) - 1)
    return words[word_position]


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Printing the Word
def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            display_word = display_word + letter
        else:
            display_word = display_word + '-'
    print(display_word)


# Getting a Guess
def get_guess(word):
    print_word_with_blanks(word)
    print('Lives Remaining: ' + str(lives_remaining))
    guess = input(' Guess a letter or whole word?')
    return guess


def play():
    word = pick_a_word()
    print('{:*^80}'.format(' WELCOME TO HANGMAN ! '))
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print('You win! Well Done!')
            break
        if (lives_remaining == 6):
            print("\n+---+")
            print("    |")
            print("    |")
            print("    |")
            print("   ===")
        elif lives_remaining == 5: 
            print("\n+---+")
            print("O   |")
            print("    |")
            print("    |")
            print("   ===")
        elif lives_remaining == 4:
            print("\n+---+")
            print("O   |")
            print("|   |")
            print("    |")
            print("   ===")
        elif lives_remaining == 3:
            print("\n+---+")
            print(" O  |")
            print("/|  |")
            print("    |")
            print("   ===")
        elif lives_remaining == 2:
            print("\n+---+")
            print(" O  |")
            print("/|\ |")
            print("    |")
            print("   ===")
        elif lives_remaining == 1:
            print("\n+---+")
            print(" O  |")
            print("/|\ |")
            print("/   |")
            print("   ===")
        elif lives_remaining == 0:
            print("\n+---+")
            print(" O   |")
            print("/|\  |")
            print("/ \  |")
            print("    ===")
            print('You are Hung!')
            print('The word was: ' + word)
            break


# Processing the Guess
def process_guess(guess, word):
    if len(guess) > 1 and len(guess) == len(word):
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)


def whole_word_guess(guess, word):
    if guess.lower() == word.lower():
        return True
    else:
        return False


def single_letter_guess(guess, word):
    global guessed_letters
    global lives_remaining
    if word.find(guess) == -1:
        lives_remaining = lives_remaining - 1
    guessed_letters = guessed_letters + guess.lower()
    if all_letters_guessed(word):
        return True
    return False


def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter.lower()) == -1:
            return False
    return True


play()
