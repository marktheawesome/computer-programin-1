#imports
import random

#vars
limit = 5

# helper functions
def start_screen():
    print("***********************************")
    print("******    Guess A Number!    ******")
    print("***********************************")
    print()
    
    input("Press 'Enter' to begin")
    print()
    
def end_screen():
    print("Bye.")
    print("This awesome game was made by Mark Gyomory")

def pick_range ():
    high = random.randint(0,1000)
    low = random.randint(0,1000)

    if high < low:
       low, high = high, low 

    print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".")
    return (low,high)
'''
def get_guess is picking new piramiters to choese form.
need to get lo and high form the play func, to keep them the same.
'''
def get_guess (low,high):

    while True:
        num = input('take a guess:')

        if num.isnumeric() and low <= int(num)<= high:
            num = int(num)
            return num
        else:
            print("Invalid guess Pleases enter a number.")

def pick_number(low,high):
    rand = random.randint(low, high)
    return rand

def play():
    low, high = pick_range()       
    rand =  pick_number(low, high)
    got_it = False
    tries = 0
    
    while got_it == False and tries < limit:
        guess = get_guess(low,high)
        got_it = check_guess(rand, guess)
        tries += 1
    
    show_result(got_it)


def play_again():
    while True:
        again = input("Would you like to play again? (y/n) ")

        if again == 'y':
            return True
        elif again == 'n':
            return False
        else:
            print("Invalid guess. Please enter y or n.")

def check_guess(rand, guess):
        if guess > rand:
            print("You guessed too high.")
        elif guess < rand:
            print("You guessed to low.")

        if guess == rand:
            return True
        else:
            return False

def show_result(got_it):
    if got_it == True:
        print("You got it!")
    else:
        print('888')                                
        print('888')                                
        print('888')                                
        print('888 .d88b. .d8888b  .d88b. 888d888') 
        print('888d88""88b88K     d8P  Y8b888P')   
        print('888888  888"Y8888b.88888888888')     
        print('888Y88..88P     X88Y8b.    888')   
        print('888 "Y88P"  88888P" "Y8888 888')


def apple():
    print(
    '''
                            .8 
                        .888
                        .8888'
                    .8888'
                    888'
                    8'
        .88888888888. .88888888888.
    .8888888888888888888888888888888.
    .8888888888888888888888888888888888.
    .&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
    `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
    `00000000000000000000000000000000000'
    `000000000000000000000000000000000'
    `0000000000000000000000000000000'
        `###########################'
    jgs    `#######################'
            `#########''########'
            `""""""'  `"""""'
    '''
    )

# Game starts running here
start_screen()

playing = True

while playing == True:
    play()
    playing = play_again()

end_screen()