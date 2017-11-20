import hangman
from string import ascii_lowercase
import random
from hangman.pics import gallows


def get_letter(correct, wrong):
    letters = list(ascii_lowercase)
    while True:
        letter = input('What is your guess ? \n').lower()
        if letter not in letters:
            print(f"{letter} is not a letter")
        elif letter in correct or letter in wrong:
            print("You already guessed that")
        else:
            return letter


def mask_word(word, correct):
    for letter in set(word) - set(correct):
        word = word.replace(letter, '_')
    return word


def random_word(n):
    with open('words.txt', 'r') as file:
        words = file.read().split('\n')
    word = ''
    while len(word) < n:
        word = random.choice(words)
    return word


def play():
    correct_guesses = []
    wrong_guesses = []
    lives = 6
    word = random_word(5)

    while lives > 0:
        print('The word is : ', mask_word(word, correct_guesses).upper())
        print(gallows(lives))
        print(wrong_guesses)
        print(f"You have {lives} lives left")
        guess = get_letter(correct_guesses, wrong_guesses)
        if guess in word:
            correct_guesses += guess
            if len(set(word) - set(correct_guesses)) == 0:
                print('You WON!!!!')
                print(f"The word was {word.upper()}")
                break
            print('NICE!')
        else:
            print(f"{guess.upper()} is not in the word")
            wrong_guesses += guess
            lives -= 1
    else:
        print("You LOST :(")
        print(f"The word was {word.upper()}")

play()
