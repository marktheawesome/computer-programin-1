# Mark, G
#

import random 

def get_puzzle():
    words = ['breitling','jazz','rolex','exist']
    
    return random.choice(words)

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    letter = input("Enter a letter:")
    return letter 

def display_board(solved):
    print(solved) 

def show_result(puzzle,solved):
    if puzzle == solved:
        print("you win! ")
    else:
        print("YOU SUCK!!!!!!!!!!")
    
def play():
    puzzle = get_puzzle()
    guesses = ''
    solved = get_solved(puzzle,guesses)
    strikes = 0
    limit = 6

    display_board(solved)

    while solved != puzzle and strikes < limit:
        letter = get_guess()

        if letter not in puzzle:
            strikes += 1 

    
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)
    show_result(puzzle,solved)
play()
