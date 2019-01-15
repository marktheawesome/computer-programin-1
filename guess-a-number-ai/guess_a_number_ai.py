import math

if math.sqrt(20) == 20**0.5:
    print("True")
'''
Guess a number Ai
Mark,G

'''

import random
import math

# config
low = 1
high = 1000
tries_taken = 1
spread = high - low
limit = math.ceil(math.log(spread,2))

# helper functions
def show_start_screen():
    print (R'''

                                                           _                  ___  _____ 
                                                          | |                / _ \|_   _|
  __ _ _   _  ___  ___ ___    __ _   _ __  _   _ _ __ ___ | |__   ___ _ __  / /_\ \ | |  
 / _` | | | |/ _ \/ __/ __|  / _` | | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__| |  _  | | |  
| (_| | |_| |  __/\__ \__ \ | (_| | | | | | |_| | | | | | | |_) |  __/ |    | | | |_| |_ 
 \__, |\__,_|\___||___/___/  \__,_| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|    \_| |_/\___/ 
  __/ |                                                                                  
 |___/                                                                                   




    ''')

def player_name():
    print ("What is your name?")
    name = input()
    return name 

def show_credits():
    print("This Game was made by Mark.")
    
def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """
    current_added = current_high + current_low 
    average = current_added//2
    return average

def pick_number(name,limit):
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    print (name + " pick a number between 1 and 1000. I'm willing to bet I'll get it in " + str(limit) + " or less.")
    input ()


def check_guess(guess,name,tries_taken):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """

    print(str(name) +" I guess " + str(guess) + (". ") + ("This is try number ") + str(tries_taken))
    print("Was I too high or too low or correct? (h/l/c)")
    put = input()
    if put == "h":
        return 1

    elif put == "l":
        return -1

    elif put == "c":
        return 0

    else:
        print ("invalid input.") 

def show_result(name):
    """
    Says the result of the game. (The computer might always win.)
    """
    print(name + " Guess what. I won!!!!!!! ")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play(name,tries_taken,limit):
    
    current_low = low
    current_high = high
    check = -1 

    pick_number(name,limit)
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess,name, tries_taken)
        tries_taken = tries_taken + 1 
        if limit == tries_taken:
            print("You must have done something wrong. I've gessed the most logical wa possible. It impossible that I've lost.")
            return
        elif check == -1:
            # adjust current_low
            current_low = guess + 1
        elif check == 1:
            # adjust current_high
            current_high = guess - 1 
        if limit == tries_taken:
            print("You must have done something wrong. I've gessed the most logical wa possible. It impossible i lost.")

    show_result(name)


# Game starts running here
show_start_screen()
name = player_name ()

playing = True

while playing:
    play(name,tries_taken,limit)
    playing = play_again()

show_credits()