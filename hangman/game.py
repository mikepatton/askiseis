import string
import random
import hangman
from hangman.pics import gallows

def get_input(correct, wrong):
    all_letters = list(string.ascii_lowercase)
    while True:
        letter = input('What is your guess? \n').lower()
        if letter not in all_letters:
            print(f'{letter.upper()} is not a letter')
        elif letter in correct or letter in wrong:
            print('you already guessed that')
        else:
            return letter




def random_word(n):
    with open ('words.txt') as file:
        all_words = file.read().split('\n')

    word = ''
    while len(word) < n:
        word = random.choice(all_words)

    return word



def mask_word(word, correct):
    word = word
    kryfa = set(word) - set(correct)
    for letter in kryfa:
        word = word.replace(letter, '_')

    return word.upper()

def play():
    correct_letters = []
    wrong_letters = []
    lives = 6
    word = random_word(5)

    while lives > 0:
        print('the word is : ', mask_word(word, correct_letters))
        print(gallows(lives))
        print(wrong_letters)
        guess = get_input(correct_letters, wrong_letters)

        if guess in word:
            correct_letters += guess
            if set(word) == set(correct_letters):
                print('You won')
                break
            print('Nice')
        else:
            wrong_letters += guess
            lives -= 1
            print('wrong')

    else:
        print('You lost')
    print(f'the word was{word.upper()}')

play()

