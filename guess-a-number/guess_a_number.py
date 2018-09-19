import random

#variables 
low = 1
high = 100
limit = 5

#helper functions
def play_again():
    again = input("Would you like to play again? (y/n)")

    if again == "y":
        return True
    elif again == 'n':
        return False
    else:
        print("Invalid guess Pleases enter y or n .")   


def get_guess ():
    while True:
        num = input('take a guess:')

        if num.isnumeric():
            num = int(num)
            return num
        else:
            print("Invalid guess Pleases enter a number.")

def play():
    rand = random.randint (low,high)
    print ("I'm think of a number between" + str(low) + " and " + str(high) + ".")

    got_it = False
    tries = 0 
    while got_it == False and tries < limit:
        guess = get_guess()
        if guess == rand:
            got_it = True
        elif guess > rand:
            print ('you guessed too high.')
        elif guess < rand:
            print('you guessed too low')
        tries += 1

    if got_it == True:
        print("You got it!")
    else:
        print("you are such a LOSER!!!!!!!!!!!!!!")

def start_screen():
    print('///////////////////////////////////////////')
    print('/////////////Guess a number////////////////')
    print('///////////////////////////////////////////')
    print()

    input("press 'Enter' to begin")
    print()
    
def end_screen():
    print("bye.")


start_screen()
playing = True
while playing == True:
    play()
    playing = play_again()

end_screen