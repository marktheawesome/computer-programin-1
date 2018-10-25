# Mark, G
#10/23/2018

import random 
playing = True

def start_screen():
    print(
        '''
        888                                                           
        888                                                           
        888                                                           
        88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
        888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
        888  888.d888888888  888888  888888  888  888.d888888888  888 
        888  888888  888888  888Y88b 888888  888  888888  888888  888 
        888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                                    888                              
                                Y8b d88P                              
                                "Y88P"                               

        '''
    )
def get_puzzle():
    words = ['breitling','jazz','rolex','exist','garmin','trek','apple','polo','python','hangman','six','chromebook']
    
    return random.choice(words)
    
def get_solved(puzzle, guesses):
    solved = ""
    guesses = guesses + ' 1234567890-=!@#$%^&*()_+[]{}/|;:<>,.?'
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
def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
def end_screen():
    print(
        '''
            | | | |               | |                     
            | |_| |__   __ _ _ __ | | ___   _  ___  _   _ 
            | __| '_ \ / _` | '_ \| |/ / | | |/ _ \| | | |
            | |_| | | | (_| | | | |   <| |_| | (_) | |_| |
            \__|_| |_|\__,_|_| |_|_|\_\\__, |\___/ \__,_|
                                        __/ |            
                                        |___/             
        '''
    )
    print("his was made by Mark Gyomory on 10/23/2018")

start_screen()


while playing:
    play()
    playing = play_again()

end_screen()