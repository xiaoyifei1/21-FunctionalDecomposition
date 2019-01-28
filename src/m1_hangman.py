"""
Hangman.

Authors: Yifei Xiao and Jared .
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.
import random

def main():
    run_the_game()
    # test_get_word()
    # test_choice_to_make()
    # test_get_guess()
    # test_compare()

def run_the_game():
    print('Game started !')
    words = construct_the_string()
    answer = get_word(words)
    M = choice_to_make()
    print(answer)
    progress = ''
    for k in range(len(answer)):
        progress += '-'

    run_game_loop(M,progress,answer)




# Functions

def construct_the_string():
    with open('words.txt') as f:
        f.readline()
        string=f.read()
        words=string.split()
    return words

def get_word(words):
    n_string = input('Enter the min word length: ')
    n = int(n_string)
    while True:
        r = random.randrange(0, len(words))
        item = words[r]
        if len(item) > n:
            return item

def choice_to_make():
    print('How many unsuccessful choices you want to')
    string=input('allow yourself? ')
    times=int(string)
    return times

def get_guess():
    letter = input('Guess a Letter: ')
    return letter

def compare(words,letter):
    for k in range(len(words)):
        if words[k]==letter:
            return True
    return False

def run_game_loop(M, progress, answer):
    while M > 0 and answer != progress:
        guess = get_guess()
        if compare(answer, guess):
            progress = add_letter(progress, guess,answer)
            print('You are correct!')
            print()
            print('You currently know: ', progress)
            print()
        else:
            M -= 1
            print('You are wrong! You have', M, 'guesses left.')
            print()
            print('You currently know: ', progress)
            print()
    award(M)

def add_letter(progress, letter,answer):
    returned_progress = ''
    for k in range(len(answer)):
        if answer[k] == letter:
            returned_progress += answer[k]
        else:
            returned_progress += progress[k]
    return returned_progress

def award(M):
    if M==0:
        print('LOSE!')
    else:
        print('You WIN!!!')


# Test Functions

def test_get_word():
    words = construct_the_string()
    answer = get_word(words)
    print(answer)

def test_choice_to_make():
    print(choice_to_make())

def test_get_guess():
    print(get_guess())

def test_compare():
    print(compare('akj','k'))

    print(compare('abc','e'))


main()

####### Do NOT attempt this assignment before class! #######

